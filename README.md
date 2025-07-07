# Netflix Titles Data Cleaner

This is a Python script that cleans and organizes the Netflix Movies and TV Shows dataset. It separates movies and TV shows, handles missing values, formats columns, and saves cleaned CSV files into an output directory for further analysis.

## Project Structure

netflix/
├── raw/               # Contains the original CSV file
│   └── netflix_titles.csv
├── output/            # Output folder for cleaned CSV files
│   ├── movies_clean.csv
│   └── series_clean.csv
└── script/            # Contains the Python script
    └── clean_data.py

## Features

- Reads the raw dataset from the raw/ folder
- Separates Movies and TV Shows into separate DataFrames
- Removes rows with missing title or type
- Fills missing values for key columns like director, cast, country, date_added, etc.
- Converts the date_added column to proper datetime format
- Extracts numeric duration values (in minutes for movies, seasons for TV shows)
- Validates and standardizes rating values
- Saves two clean CSV files into the output/ folder:
  - movies_clean.csv
  - series_clean.csv

## Requirements

- Python 3.7 or higher
- pandas library

Install the required library using pip:

