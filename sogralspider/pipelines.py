# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from translate import Translator

class SogralspiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        translator= Translator(to_lang="en")

        # Translate to English
        fields_to_translate = [
        'station_name',
        'address',
        'concession_authority',
        'additional_services',
        'hospitals', 
        'hotels', 
        'hostels', 
        'police_security', 
        'civil_protection', 
        'financial_institutions', 
        'local_administration', 
        'tourist_sites', 
        'public_garden'
        ]
    
        for field in fields_to_translate:
            value = adapter.get(field)
            if value:
                translated_value = translator.translate(value)
                adapter[field] = translated_value
        
        # Cast to Float
        fields_to_cast = [
            'total_surface_area_m2',
            'built_surface_area_m2',
            'parking_spaces',
            'number_of_platforms',
            'long_distance_line',
            'medium_distance_line',
            'short_distance_line',
            'urban_taxi_count',
            'inter_willaya_taxi_count',
            'urban_shuttle_count',
            'daily_passenger_count',
            'commercial_units_count',
            'long_distance_departures_per_day',
            'medium_distance_departures_per_day',
            'short_distance_rotations',
        ]
        for field in fields_to_cast:
            value = adapter.get(field)
            adapter[field] = float(value)
        

        return item
