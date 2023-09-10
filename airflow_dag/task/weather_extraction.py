from datetime import timedelta, datetime
import pandas as pd
import requests
import datetime
import boto3

# url = "http://api.openweathermap.org/data/2.5/weather?"

# api_key = "8c34946f386e3da68c6ede01e504113e"

# city = 'London'
# weather_url = url + 'appid=' + api_key + '&q=' + city


def convert_temperature(kelvin):
    celsius = (kelvin - 273.15) 
    return(celsius)

def convert_time(time):
    return datetime.datetime.utcfromtimestamp(time)

def check_api_request(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API request was successful!")
            print("Response:")
            print(response.text)  # You can print the response content if needed
        else:
            print(f"API request failed with status code {response.status_code}")
            print("Response:")
            print(response.text)  # You can print the response content if needed
    except Exception as e:
        print(f"API request encountered an error: {str(e)}")




def extract_data(api_url):
    response = requests.get(api_url).json()
    for key in response:
        city = response.get('name')
        temperature       = round(convert_temperature(int(response.get('main').get('temp'))),2)
        temperature_min   = round(convert_temperature(int(response.get('main').get('temp_min'))),2)
        temperature_max   = round(convert_temperature(int(response.get('main').get('temp_max'))),2)
        pressure          = response.get('main').get('pressure')
        humidity          = response.get('main').get('humidity')
        description       = response.get('weather')[0].get('description')
        sunrise           = convert_time(response.get('sys').get('sunrise'))
        sunset            = convert_time(response.get('sys').get('sunset'))
        local_record_time = convert_time(response.get('dt'))
        transformed_data  = {
            "City": city,
            "Description": description,
            "Temperature":temperature,
            "Maximum Temperature (C)": temperature_max,
            "Minimum Temperature (C)": temperature_min,
            "Pressure": pressure,
            "Humidity": humidity,
            "Sunrise (Local Time)":sunrise,
            "Sunset (Local Time)": sunset,
            "Local Record Time": local_record_time
        }
        transformed_data_list = [transformed_data]
        df = pd.DataFrame.from_dict(transformed_data_list)
        now = datetime.datetime.now() 
        time_file_create = now.strftime("%d%m%Y")
        file_name = 'Current_weather_data_' + time_file_create + '.csv'
        print(type(file_name))
        print(f'file containe weather data has been create with name{file_name}')
        return file_name

def move_data_s3(api_url):
    # Initialize the S3 client
    client = boto3.client('s3')
    
    # Specify the S3 bucket name
    bucket_name = 'thinh123'  # Replace with your actual bucket name
    
    # Call the extract_data function to get the file name
    file_name = extract_data(api_url)
    
    # Upload the file to S3
    response = client.upload_file(
        file_name,  # Use the file name returned by extract_data
        bucket_name,
        file_name  # Specify the S3 object key (file name)
    )

