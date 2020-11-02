import pandas as pd
import glob

path = r'/Users/maahd/coding/creditShelf/files/modified'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
#frame = frame.drop_duplicates(subset=['start station id'])
frame.to_csv("files/modified/combined/2019-citibike-tripdata-modified-combined-wrong.csv", index=False)
