# Project Title

ETL (Extract Transform and Load) Using Python and PostgreSQL for Tableau

## Case Study

### US Flights Case Study

### Scenario:
You were provided with a flat file containing data about domestic flights in the United States. You are asked to have the data loaded into a PostgreSQL database and appropriately modeled in a star schema for use in Tableau.

### Data:
The data is provided in a txt flat file (UTF-8 encoded), which is delimited by the pipe character (column headers are provided on the first line). 

### Requirements:
* Load the data into the PostgreSQL database provided (name: db_etl)
* Create and load one Fact table to contain data about the flights.
* Create and load appropriate Dimension table(s).
* Create a view that joins your Fact table to your Dimension table(s) and returns columns for analysis.

### Additional Instructions:
**Fact Table**
* Create an additional column called **distance_group** that bins the distance values into groups in 100 mile increments. Example: 83 miles is 0-100 miles. 255 miles is 201-300 miles.
* Create an additional column that indicates if the departure delay in minutes (**DEPDELAY**) is greater than 15.
* Choose appropriate data types and perform conversions to load the data from the source into these types.
* Fix obviously bad data when encountered, if possible.

**Dimension Table(s)**
* Create at least one dimension table and load it from the source data.
* Clean up the Airline Name column by removing the Airline Code from it.
* Clean up the Airport Name fields by removing the concatenated city and state.
* Fix obviously bad data when encountered, if possible.

## About the Scripts
The module **flights_etl.py** starts the process and will extract, check, fix (when possible), transform and load data from the txt file into the PostgreSQL database (the database part is done by imported module **flights_db**). The script will save a log with missing entries on **missing_data.tx**, and a log with obviously erroneous entries (not fixed by the script) on **bad_data.txt**, both logs created on the same directory where the script is run from. The logs can be used later to refine the script.

### Scripts Author
Jamil Said Jr. -- Copyright (C) 2018 Jamil Said Jr
