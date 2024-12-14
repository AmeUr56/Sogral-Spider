# Sogral Crawler

This is a simple Scrapy-based web crawler designed to scrape information about the transport from sogral website and store them in a csv file.

## Features
- Scrapes each wilaya details such as station_name,address,parking_spaces,number_of_platforms, short, medium and long lines and destinations and moore.
- Stores scraped data in an csv file.

## Installation

#### 1. Clone the repository:
```
git clone https://github.com/AmeUr56/Sogral-Spider
```
#### 2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Crawler

#### 1. Run the Scrapy spider:
```
scrapy crawl sogral_data
```
#### 2. The data will be inserted into an CSV file.

## CSV File
The csv table includes the following columns:
- **Basic Information**
  - `city`
  - `station_name`
  - `address`
  - `total_surface_area_m2`
  - `built_surface_area_m2`
  - `parking_spaces`
  - `number_of_platforms`

- **Route Lines**
  - `long_distance_line`
  - `long_distance_destinations`
  - `medium_distance_line`
  - `medium_distance_destinations`
  - `short_distance_line`
  - `short_distance_destinations`

- **Transportation Details**
  - `urban_taxi_count`
  - `inter_willaya_taxi_count`
  - `urban_shuttle_count`
  - `daily_passenger_count`
  - `commercial_units_count`

- **Departure Details**
  - `long_distance_departures_per_day`
  - `medium_distance_departures_per_day`
  - `short_distance_rotations`

- **Operational Details**
  - `exploitation_start_date`
  - `convention_signature_date`
  - `concession_authority`

- **Services**
  - `wifi_available`
  - `baggage_storage`
  - `nursing_room`
  - `surveillance`
  - `additional_services`
  - `prayer_room`

- **Contact Info**
  - `hospitals`
  - `hotels`
  - `hostels`
  - `police_security`
  - `civil_protection`
  - `financial_institutions`
  - `local_administration`
  - `tourist_sites`
  - `public_garden`

## Note:
This spider and similar projects are intended for learning purposes only. Please ensure you comply with the website’s terms of service and robots.txt when using the spider.

## License
This project is licensed under the MIT License.
