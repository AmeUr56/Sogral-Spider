import scrapy

from ..items import CityItem 

class SogralDataSpider(scrapy.Spider):
    name = "sogral_data"
    allowed_domains = ["www.sogral.dz"]
    start_urls = ["https://www.sogral.dz/index.php/fr/nos-agences"]

    def parse(self, response):
        cities = response.css('a.bt-title')
        for city in cities:
            city_url = city.css('::attr(href)').get()
            yield response.follow(city_url,self.parse_city)
    
    def parse_city(self, response):
        city_item = CityItem()

        
        # Basic information
        bref0 = lambda title: response.xpath(f"//p/strong[contains(text(), '{title}')]/following-sibling::text()").get()
        bref01 = lambda title: response.xpath(f"//p/strong[contains(text(), '{title}')]/following-sibling::text()").re_first(r'\d+')
        
        
        station_name = response.xpath("//p/strong[contains(text(), 'Nom de la gare')]/following-sibling::text()").get()
        if isinstance(station_name,str):
            station_name = station_name.strip()
        if not station_name:
            station_name = response.xpath("//strong[contains(text(), 'Nom de la gare')]/following-sibling::strong/text()").get()
        
        city_item['city'] = response.xpath("//h2[@itemprop='headline']/text()").get().strip() 
        city_item['station_name'] = station_name
        city_item['address'] = bref0('Adresse')
        city_item['total_surface_area_m2'] = bref01('Surface totale de l’infrastructure')
        city_item['built_surface_area_m2'] = bref01('Bâti')
        city_item['parking_spaces'] = bref01('Parking')
        city_item['number_of_platforms'] = bref01('Nombre de quais :')
        
        # Route lines
        def safe_get(lst, index, default=None):
            try:
                return lst[index]
            except IndexError:
                return default

        destination_list = response.xpath("//p/strong[contains(text(), 'La liste de tête de ligne')]/following-sibling::text()").getall()

        city_item['long_distance_line'] = bref01('Grande ligne :')
        city_item['long_distance_destinations'] = safe_get(destination_list,0)
        city_item['medium_distance_line'] = bref01('Moyenne ligne')
        city_item['medium_distance_destinations'] = safe_get(destination_list,1)
        city_item['short_distance_line'] = bref01('Petite ligne :')
        city_item['short_distance_destinations'] = safe_get(destination_list,2)
        
        
        # Transportation details
        bref1 = lambda title: response.css(f"p:contains('{title}')::text").re_first(r'\d+')
        
        city_item['urban_taxi_count'] = bref1('Nombre taxi urbain')
        city_item['inter_willaya_taxi_count'] = bref1('Nombre taxi inter willaya')
        city_item['urban_shuttle_count'] = bref1('Nombre de navettes urbains')
        city_item['daily_passenger_count'] = bref1('Nombre de voyageurs')
        city_item['commercial_units_count'] = bref1('Nombre de locaux commerciaux')

        # Departure details
        city_item['long_distance_departures_per_day'] = bref1('Nombre des départs grands')
        city_item['medium_distance_departures_per_day'] = bref1('Nombre des départs moyens')
        city_item['short_distance_rotations'] = bref1('Nombre des rotations petites ligne')

        # Operational details
        city_item['convention_signature_date'] = response.xpath("normalize-space(//p[contains(text(), 'Date de signature de la convention')]/text())").re_first(r'\d{2}/\d{2}/\d{4}')
        city_item['exploitation_start_date'] = response.xpath("normalize-space(//strong[contains(text(), 'Date de mise en exploitation')]/following::strong[1]/text())").get()
        city_item['concession_authority'] = str(response.xpath("//p[contains(text(),'Autorité Consédente')]/text()").get()).split(':')[-1]

        # Services
        services =[val.strip() for val in response.xpath(
            '//p[strong[contains(text(), "Nos services")]]'
            '/following-sibling::p[preceding-sibling::p[strong[contains(text(), "Nos services")]] '
            'and following-sibling::p[strong[contains(text(), "Contacts importants")]]]'
            '/text()'
        ).getall() ] 
        
        city_item['wifi_available'] = 'Wifi' in services
        city_item['baggage_storage'] = 'Consignes bagages' in services
        city_item['nursing_room'] = 'Salle d’allaitement' in services
        city_item['surveillance'] = 'Télé surveillances' in services
        city_item['prayer_room'] = "Salle de prière" in services  
        
        city_item['additional_services'] = response.xpath("normalize-space(//p[contains(text(), 'Autres services')]/text())").get().split(':')[-1]

        # Contact info
        contacts = response.xpath('//p[strong[contains(text(), "Contacts importants")]]/following-sibling::p/text()').getall()
        contacts = {item[0].strip(): ' '.join(item[1:]).strip() for item in  [contact.split(':') for contact in contacts] if len(item) > 1}
        
        def safe_pairing(key:str) -> str:
            try:
                return contacts[key]
            except KeyError:
                return None
          
        city_item['hospitals'] = safe_pairing('Hôpitaux')
        city_item['hotels'] = safe_pairing('Hôtels')
        city_item['hostels'] = safe_pairing('Auberges')
        city_item['police_security'] = safe_pairing('Sécurité de wilaya')
        city_item['civil_protection'] = safe_pairing('Protection civile')
        city_item['financial_institutions'] = safe_pairing('Etablissements financières')
        city_item['local_administration'] = safe_pairing('administration locale')
        city_item['tourist_sites'] = safe_pairing('- Site touristique')
        city_item['public_garden'] = safe_pairing('- Jardin public')

        yield city_item