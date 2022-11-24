import csv
from lib2to3.pgen2.token import NEWLINE

with open('usa_cities.csv', 'r') as file:
    csv_data = csv.reader(file)     
    # print(csv_data)
    # next(csv_data)
    # for row in csv_data:
    #   print(row)
    
    with open('usa_cities_new.csv', 'w') as new_file:
        usa_cities_writer = csv.writer(new_file, delimiter='\t')
        for row in csv_data:
            usa_cities_writer.writerow(row)

## DictWriter Method
# with open('usa_cities.csv', 'r') as file:
    # csv_data = csv.DictReader(file)
    # with open('usa_cities_new.csv', 'w') as new_file:
        # fieldnames = ['LatD','LatM', 'LatS', 'NS', 'LonD','LonM', 'LonS', 'EW', 'City', 'State']
        # usa_cities_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        # usa_cities_writer.writeheader()
# 
        # for row in csv_data:
            # if row:
                # usa_cities_writer.writerow(row)
# 
# 