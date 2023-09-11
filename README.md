# Airflow ETL Process for Weather Data

## Overview

This Airflow ETL (Extract, Transform, Load) process is designed to retrieve weather data from the OpenWeatherMap API, transform it into a structured format, and load it into a CSV file. Users are required to provide their name and email address to receive automated notifications regarding the data extraction process. The ETL process is split into several functions, each serving a specific purpose.

## Author Information

Name and email address:

- **Name**: Pham The Thinh
- **Email**: thinhphamthe874@gmail.com

## Functions

1. **`check_api_request(api_url)`**

    - This function is responsible for making a GET request to the OpenWeatherMap API to retrieve weather data for a specific city (in this example, London).
    - It checks the response status code to ensure the API request was successful and prints the response content.
    - **Parameters**: `api_url` - The URL of the API endpoint.

2. **`extract_data()`**

    - This function extracts relevant weather data from the API response, including information about the city, temperature, pressure, humidity, and sunrise/sunset times.
    - It transforms this data into a structured dictionary format and creates a Pandas DataFrame from the dictionary.
    - Finally, it saves the DataFrame to a CSV file with a timestamp in the filename to indicate when the data was collected.
    - The extracted data includes:
        - City
        - Description (e.g., cloudy, rainy)
        - Temperature (in Celsius)
        - Maximum Temperature (in Celsius)
        - Minimum Temperature (in Celsius)
        - Pressure (in hPa)
        - Humidity (in %)
        - Sunrise Time (Local Time)
        - Sunset Time (Local Time)
        - Local Record Time (Time of API response)

3. **`move_data_s3()`**

    - This function is a placeholder for moving the generated CSV file to an S3 bucket or any other desired storage location. You can implement this function according to your specific requirements for data storage.

## Flow Diagram

Here is a simplified flow diagram of the Airflow ETL process:

```plaintext
[Start] --> [Retrieve Weather Data] --> [Transform Data] --> [Save to CSV] --> [Move to S3] --> [End]
```

## Usage Instructions

To execute this Airflow ETL process for weather data, follow these steps:

1. Ensure you have the required Python packages installed. You can install them using pip:

    ```
    pip install requests pandas
    ```

2. Set up Airflow with the necessary configurations, such as the DAG (Directed Acyclic Graph) to schedule and automate the ETL process.

3. Create a Python script or Airflow operator that calls the `check_api_request` function to retrieve weather data from the OpenWeatherMap API. You can customize the city and API key as needed.

4. Create another Python script or Airflow operator that calls the `extract_data` function to extract, transform, and save the weather data to a CSV file. Ensure you customize the filename and storage location.

5. If you intend to move the CSV file to an S3 bucket, implement the `move_data_s3` function with the appropriate code to accomplish this task.

6. Schedule the Airflow DAG to run at your desired frequency, such as daily or hourly, to keep the weather data up to date.

7. Monitor the Airflow DAG to ensure it runs successfully and that the weather data is extracted, transformed, and loaded according to your requirements.

Feel free to adapt and extend this ETL process to suit your specific use case and integration with Airflow.
