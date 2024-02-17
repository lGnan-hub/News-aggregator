import requests
from bs4 import BeautifulSoup

def scrape_weather_data():
    try:
        # URL of the website to scrape
        url = 'https://weather.com/en-IN/weather/today/l/10cdc3bf6584a4a1574a40024d6ead9e2a618860178cab18e2610b7562781bcb'  # Provided URL
        
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant weather information
        location_elem = soup.find(class_='CurrentConditions--location--1Ayv3')
        if location_elem:
            location = location_elem.get_text()
        else:
            location = "Location not found"
        
        temperature_elem = soup.find(class_='CurrentConditions--tempValue--3KcTQ')
        if temperature_elem:
            temperature = temperature_elem.get_text()
        else:
            temperature = "Temperature not found"
        
        condition_elem = soup.find(class_='CurrentConditions--phraseValue--2xXSr')
        if condition_elem:
            condition = condition_elem.get_text()
        else:
            condition = "Condition not found"
        
        humidity_elem = soup.find(text='Humidity').find_next(class_='WeatherDetailsListItem--wxData--23DP5')
        if humidity_elem:
            humidity = humidity_elem.get_text()
        else:
            humidity = "Humidity not found"
        
        wind_elem = soup.find(text='Wind').find_next(class_='WeatherDetailsListItem--wxData--23DP5')
        if wind_elem:
            wind = wind_elem.get_text()
        else:
            wind = "Wind not found"
        
        # Print the weather data
        print(f"Location: {location}")
        print(f"Temperature: {temperature}")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}")
        print(f"Wind: {wind}")
        
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)

if __name__ == "__main__":
    print("Fetching weather data...")
    scrape_weather_data()
