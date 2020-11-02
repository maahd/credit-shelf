# Each fine was one month in the year 2019. It contained info about trips. I removed all the extra info so we are only left with info pertaining to the stations. Obviously we had a lot of duplicates cuz this is info about the trips. So I removed the duplicates so each station occurs only once. I used the station ID for this.

import pandas

filename="../files/original/201912-citibike-tripdata.csv"
resulting_file_name = filename.replace('.csv', '-mofified.csv')
resulting_file_name = resulting_file_name.replace('files/original', 'files/modified')

col_list=["start station id", "start station name", "start station latitude", "start station longitude"]
df = pandas.read_csv(filename, usecols=col_list)
df = df.drop_duplicates(subset=['start station id'])
df.to_csv(resulting_file_name, index=False)
