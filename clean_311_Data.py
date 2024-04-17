import pandas as pd
import os
import csv


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



# # Group by category and export into seperate files

# # Load data from CSV into DataFrame
# df = pd.read_csv('CategorySRType.csv')

# # Group by 'Category' column
# grouped = df.groupby('Category')

# # Iterate over each group and write it to a separate file
# for category, group_df in grouped:
#     # Define the output file name based on the category
#     output_file = f"{category.replace(' ', '_')}_data.csv"
    
#     # Write the group to a CSV file
#     group_df.to_csv(output_file, index=False)

#     print(f"Data for '{category}' written to '{output_file}'")
##################################################################


#Group by categories and exportin into one file

# Load data from CSV into DataFrame
df = pd.read_csv('CategorySRType.csv')

# Group by 'Category' column
grouped = df.groupby('Category')

# Create an empty list to store data frames for each category
dfs = []

# Iterate over each group and append it to the list
for category, group_df in grouped:
    dfs.append(group_df)

# Concatenate all data frames into one
result = pd.concat(dfs)

# Write the concatenated data to a single CSV file
result.to_csv('grouped_data_by_category.csv', index=False)

print("Data grouped by category written to 'grouped_data_by_category.csv'")
