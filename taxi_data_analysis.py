import csv
import requests
from collections import Counter

# Download the dataset
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)
with open("taxi_zone_lookup.csv", "wb") as file:
    file.write(response.content)

# Reading the CSV file
records = []
with open("taxi_zone_lookup.csv", "r") as file:
    csvreader = csv.reader(file)
    headers = next(csvreader)  # Skip the header row
    for row in csvreader:
        records.append(row)

# a. Total number of records sorted in ascending order
sorted_records = sorted(records, key=lambda x: x[0])  # Sort by the first column (ID)
total_records = len(sorted_records)

# b. Find unique Borough
boroughs = [row[1] for row in records]  # Assuming Borough is in the second column
unique_boroughs = set(boroughs)

# c. Number of records for Brooklyn borough
brooklyn_count = Counter(boroughs)["Brooklyn"]

# d. Save the facts to a text file
output_text = f"Total Records: {total_records}\n" \
              f"Unique Boroughs: {', '.join(unique_boroughs)}\n" \
              f"Brooklyn Borough Records: {brooklyn_count}\n"

# Update the file path for Windows
with open("c:/Users/Siddhant/c400Python/taxi_zone_output.txt", "w") as output_file:
    output_file.write(output_text)

print("Facts saved to c:/Users/Siddhant/c400Python/taxi_zone_output.txt")
