import pandas as pd
import csv


# Below are 3 functions with the description of each starting with #### 
# and ending with a row of #########################

# Function to return a cleaned version of the data
#def clean_data():
   
     # Function to load the data
   # def load_data():
        # Features : Expected Types  
        #0 'X' : float, 
        #1 'Y' : float, 
        #2 'RowID' : int, 
        #3 'SRRecordID' : string, 
        #4 'ServiceRequestNum' : string, 
        #5 'SRType' : string, 
        #6 'MethodReceived' : string, 
        #7 'CreatedDate' : string, 
        #8 'SRStatus' : string, open or closed, 
        #9 'StatusDate' : string, 
        #10 'DueDate' : string,
        #11 'CloseDate' : int, 
        #12 'Agency' : string, 
        #13 'LastActivity' : string,
        #14 'LastActivityDate' : string, 
        #15 'Outcome' : string, 
        #16 'Address' : string, 
        #17 'ZipCode' : int, 
        #18 'Neighborhood' : string, 
        #19 'CouncilDistrict' : int, 
        #20 'PoliceDistrict' : string, 
        #21 'PolicePost' : int, 
        #22 'Latitude' : float
        #23 'Longitude' : float,
        #24 'GeoLocation': string


#### Prints total lines for csv ####

# Initialize count
# count = 0  

# with open('311_CSR_2021.csv') as file:
#     csv_reader = csv.reader(file)
#     for line in csv_reader:

#         # Increment count for each iteration
#         count += 1       

#         # Print the 6th element and count  
#         print(f"Line {count}: {line[5]}")   

#         # Print the total count after the loop
#         print(f"Total lines: {count}")  

#########################


#### List all SR types ####

# sr_types = []

# with open('311_CSR_2021.csv') as file:
#     csv_reader = csv.reader(file)
#     for line in csv_reader:
#         sr_type = line[5]  # Accessing the SRType column (index 5)
#         sr_types.append(sr_type)
#         print(sr_type)

#  # Print the total number of SR types
# total_sr_types = len(sr_types)
# print(f"Total number of SR types: {total_sr_types}")

# with open('311_CSR_2021.csv') as file:
#      csv_reader = csv.reader(file)
#      for line in csv_reader:
#          sr_type = line[5]  # Accessing the SRType column (index 5)
#          print(sr_type)

#########################


#### Total number of unique SRTypes ####

# Set to store unique SR types
# sr_types = set()

# with open('311_CSR_2021.csv') as file:
#     csv_reader = csv.reader(file)
#     for line in csv_reader:
#         sr_type = line[5]  # Accessing the SRType column (index 5)
#         sr_types.add(sr_type)

# # Print the total number of unique SR types
# total_sr_types = len(sr_types)
# print(sr_type)
# print(f"Total number of SR types: {total_sr_types}")

#########################    

   