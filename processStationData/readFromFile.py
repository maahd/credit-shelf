# Didn't really use this as I moved to Pandas. It's better for larger data sets.

import csv

with open('../files/201901-citibike-tripdata.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    stations_id = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row["start station id"] in stations_id:
                print("found duplicate")
            else:
                print(f'\tStart Station ID: {row["start station id"]}, Start Station Name: {row["start station name"]}')
                stations_id.append(row["start station id"])
                line_count += 1
    print(f'Processed {line_count} lines.')
