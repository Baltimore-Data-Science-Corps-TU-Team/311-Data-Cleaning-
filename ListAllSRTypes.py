import pandas as pd
import csv

#### LISTS all SR types and save to new file ####

sr_types = []

with open('311_CSR_2021.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:

        # Accessing the SRType column (index 5)
        sr_type = line[5]  
        sr_types.append(sr_type)
        print(sr_type)

total_sr_types = len(sr_types)
print(f"Total number of SR types: {total_sr_types}")

with open('311_CSR_2021.csv') as file:
     csv_reader = csv.reader(file)
     for line in csv_reader:
         
         # Accessing the SRType column (index 5)
         sr_type = line[5]  
         print(sr_type)

# Save SR types to a new file
with open('filtered_ srTypes.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['SR Type'])
    for sr_type in sr_types:
        csv_writer.writerow([sr_type])

print("SR types saved to filtered_ srTypes.csv")