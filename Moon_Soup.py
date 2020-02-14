# Dependencies
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from splinter import Browser
from sqlalchemy import create_engine
from datetime import datetime


### DEV TOOLS ###
start_date_less1 = '2018/12/31'
weeks = 53

csv_dump = f'Resources/lunar_ds.csv'

# URL of page to be scraped
url = f'https://lunaf.com/lunar-calendar/{start_date_less1}/#next-7-days-moon-phases'

# creating splinter browser and visint url
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)
print('Visiting URL')
browser.visit(url)

# creating empty dataframe
lunar_df = pd.DataFrame(columns = {
    'time',
    'phase',
    'illumination_percent',
    'sign'
})

print('''
--Starting Scrape--
''')

# creating scrape performance metrics
success = 0
fail = 0


# looping through pages for indicated amount of weeks
for week in np.arange(0, weeks):
    
    try: 
        # activating splinter browser
        html = browser.html

        # Create BeautifulSoup object; parse with 'html.parser'
        soup = BeautifulSoup(html, 'html.parser')

        # html parsing articles on page
        articles = soup.find_all('article')

        # looping through article list
        for article in articles:

            # locating links in articles
            links = article.find_all('a')

            # looping through list of links
            for index, item in enumerate(links):

                # extracting description in link tag
                desc = item['title']

                # parsing out all words in description (appears to use a template to create desc)
                desc_items = desc.split(' ')

                # creating phase item
                phase = desc_items[0] + ' ' + desc_items[1]

                # creating illumination item
                ill = desc_items[3][:-1]

                # creating sign item
                sign = desc_items[8]

                # parsing datetime item from time tag
                time = item.find_all('time')[index]['datetime']
                if len(time) > 10:
                    time = time[:10]
                
                lunar_df = lunar_df.append({'time':time, 'phase':phase, 'illumination_percent':ill, 'sign':sign}, ignore_index=True)

        # outputting query status to terminal
        print(f'Completed Week:{week + 1} of {weeks}')
        success += 1

    except:
        print(f'Failed Week: {week + 1} of {weeks}')
        fail += 1
        
    # navigating to next page of next week
    browser.click_link_by_partial_text('7 days after')


# datadump to local csv (issues with others running the chromedriver.exe on their machine)    
lunar_df.to_csv(csv_dump)


print(f'''
--Scrape Completed--
Succeses: {success}
Fails: {fail}
''')


# reading in SLMP 2019 Crime Data
crime_csv = 'Resources/crimedatacombined.csv'
crime_df = pd.read_csv(crime_csv)

# converting crime_df to datetime
crime_df['time'] = pd.to_datetime(crime_df.time)
crime_df['time'] = crime_df['time'].dt.strftime('%Y-%m-%d')

# Merging DFs
merge_df = crime_df.merge(lunar_df, on='time', how='inner')

# creating SQL connection to localhost Postgres
connection_string = 'postgresql://postgres:postgres@localhost:5432/crime_time'
engine = create_engine(connection_string, echo=False)

# Loading dataset to database (NOTE Database crime_time must already exist)
merge_df.to_sql('lunar_crime', con=engine)

print('Done')