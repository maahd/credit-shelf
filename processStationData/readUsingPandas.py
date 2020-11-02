import pandas

filename="../files/original/201912-citibike-tripdata.csv"
resulting_file_name = filename.replace('.csv', '-mofified.csv')
resulting_file_name = resulting_file_name.replace('files/original', 'files/modified')

col_list=["start station id", "start station name", "start station latitude", "start station longitude"]
df = pandas.read_csv(filename, usecols=col_list)
df = df.drop_duplicates(subset=['start station id'])
df.to_csv(resulting_file_name, index=False)
