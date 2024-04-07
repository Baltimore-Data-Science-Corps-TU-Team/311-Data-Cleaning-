import pandas as pd
import csv

#### TOTAL number of unique SRTypes ####

# Set to store unique SR types
sr_types = set()

with open('311_CSR_2021.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        sr_type = line[5]  # Accessing the SRType column (index 5)
        sr_types.add(sr_type)

# Print the total number of unique SR types
total_sr_types = len(sr_types)
print(sr_type)
print(f"Total number of unique SR types: {total_sr_types}")

#########################    Total number of SR types: 286