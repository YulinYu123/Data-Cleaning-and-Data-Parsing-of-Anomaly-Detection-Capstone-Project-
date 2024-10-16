# Capstone Project Overview
This project focuses on processing operational data from Roborigger, a rotation control device used in lifting operations. The goal of the project is to develop a software platform that aggregates and presents data from Roborigger units, while also identifying anomalies and faults in an intuitive way. This enables internal Roborigger personnel and on-site service agents to diagnose issues and provide initial recommendations more efficiently.

## My Contributions

### 1. Data Cleaning and Parsing
I was responsible for handling the preliminary data cleaning and data parsing. Given the large volume of data generated by even a single Roborigger unit, it was essential to filter out unimportant data before anomaly detection. Using the health check report provided by Roborigger's internal system, I evaluated which columns were essential and which could be removed.

As an example, I used the log file `2023.04.05-13.34.10.csv`. The cleaning and parsing steps include:
- Using the Pandas library in Python to create a new DataFrame that contains only important columns (as identified from the health check report). For example, I grouped related columns such as 'GPS Satellites', 'GPS Latitude', 'GPS Longitude', and 'GPS Altitude' into a single category.
- Removing rows with missing values to ensure data quality.

These operations are implemented in the script **`cleaned_data.py`**.

After cleaning, I reorganized the data into a dictionary structure, which allows the data to be accessed and managed based on categories and column names. This step can be found in **`dataParsing_Cleaning.py`**.

### 2. Fault Code Translation and Merging
I was also responsible for converting fault codes into human-readable information and merging filtered data with fault information. This process involved:
- Reading the input CSV file containing operational data and another CSV file with fault details.
- Filtering out non-empty and non-zero values from the "Sevcon Fault" column and converting decimal fault codes to hexadecimal.
- Performing a left join between the operational data and fault information to associate the Sevcon Fault codes with their corresponding messages, descriptions, and recommended actions.

The resulting data provides Roborigger staff with actionable information for diagnosing and solving issues. These steps are detailed in the script **`Faulty_Code.py`**.
