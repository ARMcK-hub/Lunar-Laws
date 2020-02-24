# Lunar-Laws
This repository houses Extract-Transform-Load (ETL) transactions for an ad-hoc lunar and crime analysis.

This project seeks to source data for determining if lunar metrics, such as illumination and phase, impact crime in St. Louis.

The ETL script, Moon_Soup.py, consumes data by webscraping from an online source. The script takes in a pre-merged CSV dataset of another origin, and merges on a date field.
Munged data is then injected into a SQL table using SQLAlchemy.

# Data Sources:
1. Lunar Phase Data: https://lunaf.com/lunar-calendar/
* Web-Scraped using Beautiful Soup 4
2. St. Louis Crime Data: https://www.slmpd.org/crime_stats.shtml
* ad-hoc download as CSV

# Technologies:
1. Python
3. SQL
4. SQLAlchemy
5. Beatiful Soup 4
6. Pandas
7. Jupyter Notebook