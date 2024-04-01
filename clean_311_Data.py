# import pandas as pd
# import csv

# # df = pd.read.csv('311_CSR_2021.csv')
# with open ('311_CSR_2021.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     print()
#     for line in csv_reader:
#         print(line[5])
import pandas as pd
import csv

# Function to return a cleaned version of the data
def clean_data():

    # Function to load the data
    def load_data():
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


        df = pd.read_csv("311_CSR_2021.csv.csv")
        return df

    # Function to focus on the columns of interest
    def focused_data(df):
        focused_data = df.iloc[0:,[4,6,8,10,11,12,18,19,21]]
        return focused_data

    # Function to clean the 'Weapon' column
    def clean_weapon_column(data):
        # Fill NaN values with 'No weapon'
        cleaned_data = data.fillna('No weapon')
        return cleaned_data

    # Function to clean the 'Gender' column
    def clean_gender_column(data):
        # Get unique values in the 'Gender' column
        unique_values = ['B', 'Transgende', 'N', ',', 'FB', 'O', '160', 'FW', 'FU', 'D', '60', '120', '8', 'MB', 'A', '77', '17', 'FF', '165', 'FM', '042819', 'S', 'T', '50']
        
        # Create a dictionary to map unique values to 'U' except for 'M' and 'F'
        replace_dict = {value: 'U' for value in unique_values if value not in ['Male', 'Female', 'W', 'M\\']}
        
        # Replace 'Male' with 'M', 'Female' with 'F', 'W' with 'F', and 'M\' with 'M'
        replace_dict['Male'] = 'M'
        replace_dict['Female'] = 'F'
        replace_dict['W'] = 'F'
        replace_dict['M\\'] = 'M'

        # Replace the values with the dictionary
        cleaned_data = data.replace(replace_dict)

        # Fill NaN values with 'U'
        cleaned_data = cleaned_data.fillna('U')

        return cleaned_data

    # Function to clean the 'Age' column
    def clean_age_column(data):
        # Custom function to convert values to integers and handle 'U' values
        def convert_to_int(value):
            try:
                return int(value)
            except (ValueError, TypeError):
                return 'U'
            
        # Replace numbers 0 and below + numbers 115 and over with 'U'
        cleaned_data = data.apply(lambda x: 'U' if x <= 0 or x >= 115 else x)

        # Fill NaN values with 'U'
        cleaned_data = cleaned_data.fillna('U')
            
        # Apply the custom function to the 'Age' column
        cleaned_data = cleaned_data.apply(convert_to_int)

        return cleaned_data

    # Function to clean the 'Race' column
    def clean_race_column(data):
        # Fill NaN values with 'UNKNOWN'
        cleaned_data = data.fillna('UNKNOWN')
        return cleaned_data

    # Function to clean the 'PremiseType' column
    def clean_premise_type_column(data):
        # Fill NaN values with 'UNKNOWN'
        cleaned_data = data.fillna('UNKNOWN')
        return cleaned_data

    # Load the data
    df = load_data()
    data = focused_data(df)

    # Clean the 'Weapon' column
    cleaned_weapon_column = clean_weapon_column(data['Weapon'])
    # Clean the 'Gender' column
    cleaned_gender_column = clean_gender_column(data['Gender'])
    # Clean the 'Age' column
    cleaned_age_column = clean_age_column(data['Age'])
    # Clean the 'Race' column
    cleaned_race_column = clean_race_column(data['Race'])
    # Clean the 'PremiseType' column
    cleaned_premise_type_column = clean_premise_type_column(data['PremiseType'])

    # Create a new DataFrame with the cleaned columns
    cleaned_data = pd.DataFrame({
        'CrimeDateTime': data['CrimeDateTime'],
        'Description': data['Description'],
        'Weapon': cleaned_weapon_column, 
        'Gender': cleaned_gender_column, 
        'Age': cleaned_age_column,
        'Race': cleaned_race_column,
        'Longitude': data['Longitude'],
        'Latitude': data['Latitude'],
        'PremiseType': cleaned_premise_type_column
        })
    
    def delete_invalid_location_rows(data):
        # delete rows with NaN values in the 'Longitude' and 'Latitude' column
        cleaned_data = data.dropna(subset=['Longitude', 'Latitude'])
        # delete rows with 0 values in the 'Longitude' and 'Latitude' column
        cleaned_data = cleaned_data[cleaned_data['Longitude'] != 0]
        cleaned_data = cleaned_data[cleaned_data['Latitude'] != 0]
        return cleaned_data
    
    def combine_similar_descriptions(data):
        # change 'LARCENY FROM AUTO' to 'LARCENY'
        cleaned_data = data.replace('LARCENY FROM AUTO', 'LARCENY')
        # change 'ROBBERY - CARJACKING' to 'ROBBERY'
        cleaned_data = cleaned_data.replace('ROBBERY - CARJACKING', 'ROBBERY')
        # change 'ROBBERY - COMMERCIAL' to 'ROBBERY'
        cleaned_data = cleaned_data.replace('ROBBERY - COMMERCIAL', 'ROBBERY')
        return cleaned_data
    
    cleaned_data = delete_invalid_location_rows(cleaned_data)
    cleaned_data = combine_similar_descriptions(cleaned_data)

    return cleaned_data