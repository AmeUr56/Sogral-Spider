# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SogralspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CityItem(scrapy.Item):
    # Basic information
    city = scrapy.Field()
    station_name = scrapy.Field()
    address = scrapy.Field()
    total_surface_area_m2 = scrapy.Field()
    built_surface_area_m2 = scrapy.Field()
    parking_spaces = scrapy.Field()
    number_of_platforms = scrapy.Field()

    # Route lines
    long_distance_line = scrapy.Field()
    long_distance_destinations = scrapy.Field()
    medium_distance_line = scrapy.Field()
    medium_distance_destinations = scrapy.Field()
    short_distance_line = scrapy.Field()
    short_distance_destinations = scrapy.Field()

    # Transportation details
    urban_taxi_count = scrapy.Field()
    inter_willaya_taxi_count = scrapy.Field()
    urban_shuttle_count = scrapy.Field()
    daily_passenger_count = scrapy.Field()
    commercial_units_count = scrapy.Field()

    # Departure details
    long_distance_departures_per_day = scrapy.Field()
    medium_distance_departures_per_day = scrapy.Field()
    short_distance_rotations = scrapy.Field()

    # Operational details
    exploitation_start_date = scrapy.Field()
    convention_signature_date = scrapy.Field()
    concession_authority = scrapy.Field()

    # Services
    wifi_available = scrapy.Field()
    baggage_storage = scrapy.Field()
    nursing_room = scrapy.Field()
    surveillance = scrapy.Field()
    additional_services = scrapy.Field()
    prayer_room = scrapy.Field()
    # Contact info
    hospitals = scrapy.Field()
    hotels = scrapy.Field()
    hostels = scrapy.Field()
    police_security = scrapy.Field()
    civil_protection = scrapy.Field()
    financial_institutions = scrapy.Field()
    local_administration = scrapy.Field()
    tourist_sites = scrapy.Field()
    public_garden = scrapy.Field()