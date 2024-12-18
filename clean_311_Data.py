import pandas as pd

# Define maximum number of columns
max_cols = 25

# Read the CSV file into a DataFrame
df = pd.read_csv('311_Customer_Service_Requests.csv', skipinitialspace=True, na_values=[""], usecols=range(max_cols))

# Drop rows with all NaN values to remove completely empty rows
df.dropna(how='all', inplace=True)

# Group by 'SRType' column
grouped = df.groupby('SRType')
# Concatenate all data frames into one
result = pd.concat([df])
# Define categories
categories = {
    'waste': [
        'SW- City Trash Can or Recycling Cart Concern',
        "SW-Bulk Scheduled (FOR SATURDAY'S ONLY)",
        'SW-Trash Can/Recycling Container Complaint',
        'SW-Public (Corner) Trash Can Request/Removal',
        'SW-Mechanical Street Sweeping',
        'SW-Mechanical Alley Sweeping',
        'SW-Rat Rubout Follow-up',
        'SW-Rat Rubout Alley Concern',
        'SW-Rat Rubout Proactive',
        'SW-Rat Rubout',
        'SW-SIU Clean Up',
        'SW-Bulk Special',
        'SW-Fire Debris Removal',
        'SW-Dumpster Collection',
        'SW-RP Bulk Pickup',
        'SW-Bulk Scheduled-Saturday',
        'SW-Bulk Scheduled',
        'SW-Recycling',
        'SW-Leaf Collection Scheduling',
        'SW-Leaf Removal',
        'SW-Graffiti Removal-Owner\'s Request',
        'SW-Graffiti Removal Proactive',
        'SW-Graffiti Removal',
        'SW-City Trash Can or Recycling Cart Concern',
        'SW-City Trash Can or Recycling Cart Lost or Stolen',
        'SW-Bag Pickup',
        'HCD-Illegal Dumping',
        'WW-Waterway Pollution Investigation',
        'WW-Sediment or Erosion Problem',
        'WW-Water Odor/Bad Taste',
        'WW-Hydrant Damaged',
        'WW-Sewer Overflow',
        'WW-Sewer Water In Basement',
        'WW-Water Leak (Exterior)',
        'WW-Storm Damaged Inlet',
        'WW-Storm Flooded Street',
        'WW-Water No Water',
        'WW-Hydrant Leaking',
        'WW-Water Low Pressure',
        'SW-Dirty Alley',
        'SW-Dirty Street',
        'SW-Dirty Street Proactive',
        'SW-Mixed Refuse',
        'TRM-Debris Hanging From Wires or Poles',
        'TRM-Debris In Roadway'
        'SW-Appliance'],

    'vehicle': [
        'FCPF-Trial Request-Parking',
        'FCPF-Stolen Vehicle/Tags',
        'TRS-Parking Away Notification',
        'TRS-Parking Complaint',
        'TRS-48 Hour Parking/Abandoned Vehicle',
        'TRT-Crosswalks',
        'TRT-New Traffic Sign',
        'TRT-Signal Timing',
        'TRT-Traffic Calming',
        'TRT-Traffic Signal Repairs',
        'TRM-Illegal Sign Removal',
        'TRM-(ADA) Sidewalk Ramp Concern (Repair)',
        'TRM-Bridge Concern',
        'TRM-Curb Repair',
        'TRM-Footways Repair',
        'TRM-Street Repairs',
        'TRM-Steel Plate Repair',
        'TRM-Street and Crosswalk Markings',
        'TRM-Guardrail Concern (Repair)',
        'TRM-Sign Damaged/Sign Structure',
        'TRM-StLight Pole Access Cover/Plate Missing',
        'TRM-StLight Pole Missing',
        'TRM-StLight Damaged/Knocked Down/Rusted',
        'TRM-StLighting Inadequate/Too Bright',
        'TRM-StLighting Cable Faults',
        'TRM-Pickup Pothole',
        'TRM-Potholes',
        'TRM-Snow/Icy Conditions',
        'TRM-Street Cut Notification',
        'TRM-WO Sign Installation',
        'TRM-WO Sign Removal',
        'TRM-Steel Plate Complaint',
        'TRM-Street Lighting Repairs',
        'TRM-Sandbag Pick Up',
        'TRM-StLight Pole Pickup',
        'TRM-Debris In Roadway',
        'TRM-Conduit Repair',
        'TRM-Conduit Restoration',
        'TRM-Street Cut Notification',
        'TTR-Abandoned Vehicle Turn-in Program',
        'TTR-Vehicle Relocation',
        'TTR-Vehicle Removal',
        'PABC-Pay by License Plate Meter Complaints',
        'PABC-Parking Regulation Review',
        'PABC-Electric Vehicle Charging Station Request',
        'PABC-Single Space Meter Complaints',
        'PABC-Driveway Signage Request',
        'PABC-Parking Investigations',
        'SW-Trash Can/Recycling Container Complaint',
        'SW-Public (Corner) Trash Can Request/Removal',
        'SW-Municipal Trash Can Concern',
        'SW-Recycling',
        'SW-Residential Recycling Carts',
        'SW-Bulk Scheduled',
        'SW-Bulk Scheduled-Saturday',
        'SW-Bulk Scheduled',
        'SW-Bulk Special',
        'SW-Bag Pickup',
        'SW-Mixed Refuse',
        'SW-Dumpster Collection',
        'SW-Fire Debris Removal',
        'SW-Dirty Street',
        'SW-Dirty Street Proactive',
        'SW-Dirty Alley',
        'SW-Dirty Alley Proactive',
        'SW-Municipal Trash Can Stolen/Lost',
        'SW-City Trash Can or Recycling Cart Concern',
        'SW-City Trash Can or Recycling Cart Lost or Stolen',
        'SW-Public (Corner) Trash Can Issue',
        'SW-BCPSS Graffiti Removal',
        'SW-Graffiti Removal - Rec and Parks',
        'SW-Graffiti Removal',
        'SW-Graffiti Removal Proactive',
        'SW-Graffiti Removal-Owner\'s Request',
        'SW-Leaf Collection Scheduling',
        'SW-Leaf Removal',
        'SW-Water Way Cleaning',
        'SW-Mechanical Alley Sweeping',
        'SW-Mechanical Street Sweeping',
        'SW-SIU Clean Up',
        'SW-Volunteer Clean-Up Event',
        "SW-Clean Up (Mayor’s Fall Cleanup)",
    ],
    'infrastructure': [
        'Food Facility Complaint'
        'WW-Water Water In Basement',
        'FIR-Fire Smoke Alarm Installation Request',
        'BGE-StLight(s) Out Rear',
        'FIR-Fire Smoke Alarm Installation Request',
        'WW-Water Meter Cover Missing or Damaged',
        'TRT-Traffic Sign Request',
        'WW-Water Meter Leak',
        'BGE-StLight Pole Installation',
        'BGE-No Feed',
        'BGE-Fixture-Arm',
        'BGE-Extend Feed',
        'BGE-Duplex',
        'BGE-Conduit Observation',
        'BGE-Duct Obstruction',
        'BGE-Cable Replacement',
        'BGE-C-Order Damage',
        'BGE-C-Order Non-Damage',
        'BGE-StLight(s) Out',
        'TEC-Street Repair (Misc)',
        'TRM-Street Repairs',
        'TRM-Snow/Icy Conditions',
        'TRM-Potholes',
        'TRM-Pickup Pothole',
        'TRM-Street Cut Notification',
        'TRM-Street and Crosswalk Markings',
        'TRM-Sign Damaged/Sign Structure',
        'TRM-Steel Plate Repair',
        'TRM-Steel Plate Complaint',
        'TRM-StLight Pole Access Cover/Plate Missing',
        'TRM-StLight Pole Missing',
        'TRM-StLight Damaged/Knocked Down/Rusted',
        'TRM-StLighting Inadequate/Too Bright',
        'TRM-StLighting Cable Faults',
        'TRM-Debris Hanging From Wires or Poles',
        'TRM-Conduit Repair',
        'TRM-Conduit Restoration',
        'TEC-Footways Contract/Reconstruction',
        'TEC-Footways Complaint',
        'TEC-Alley Contract/Reconstruction',
        'TEC-Alley Reconstruction Complaint',
        'TRT-Crosswalks',
        'TRT-New Traffic Sign',
        'TRT-Signal Timing',
        'TRT-Traffic Calming',
        'TRT-Traffic Signal Repairs',
        'WW-Water Leak (Exterior)',
        'WW-Sewer Overflow',
        'WW-Sewer Water In Basement',
        'WW-Water No Water',
        'WW-Water Low Pressure',
        'WW-Waterway Pollution Investigation',
        'WW-Water Odor/Bad Taste',
        'WW-Hydrant Leaking',
        'WW-Hydrant Damaged',
        'WW-Storm Damaged Inlet',
        'WW-Storm Flooded Street',
        'WW-Sediment or Erosion Problem',
        'WW-Water Noise In Pipe',
        'RP-Park Maintenance',
        'RP-Building Maintenance',
        'RP-Custodial Services',
        'TRS-Parking Away Notification',
        'TTR-Abandoned Vehicle Turn-in Program',
        'TTR-Vehicle Relocation',
        'TTR-Vehicle Removal',
        'BGE-Construction/New Development',
        'BGE-StLighting Cable Faults',
        'BGE-StLighting Out',
        'BGE-StLighting Pole Installation',
        'BGE-StLighting Pole Pickup',
        'BGE-StLighting Pole Missing',
        'BGE-StLighting Pole Repair',
        'BGE-StLighting Pole Out Rear',
        'BGE-Manhole Work',
        'BGE-Red Tag',
        'BGE-Electric Vehicle Charging Station Request',
        'BGE-Construction/New Development',
        'FOR-Tree Inspection',
        'FOR-Down Tree',
        'FOR-Fallen Limb',
        'FOR-Broken Branch in Tree',
        'FIR-Fire Code Violation',
        'HCD-Vacant Building',
        'HCD-Maintenance Structure',
        'HCD-CCE Building Inspections',
        'HCD-CCE Demolition',
        'HCD-Illegal Flyers',
        'HCD-Illegal Signs on Public Property',
        'HCD-Sanitation Property',
        'HCD-Abandoned Vehicle',
        'HCD-Animals',
        'HCD-Bed Bugs',
        'HCD-Fire Protection',
        'HCD-Insects',
        'HCD-Rodents',
        'HCD-Snow and Ice on Sidewalks',
        'WW-Surface Repair',
        'TRM-Curb Repair',
        'TRM-Street and Crosswalk Markings',
        'TRM-Steel Plate Complaint',
        'RP-Street Lighting Repairs',
        'BGE-Manhole Work',
        'PABC-Driveway Signage Request',
        'SW-Mechanical Alley Sweeping',
        'RP-Grass Cutting',
        'TRM-Footways Repair',
        'TRM-Street Repairs',
        'TRM-Potholes',
        'TRM-Sign Damaged/Sign Structure',
        'TRM-StLight Damaged/Knocked Down/Rusted',
        'TRM-Illegal Sign Removal',
        'TRM-Street Light Out',
        'TRM-Guardrail Concern (Repair)',
        'TRM-StLight Pole Access Cover/Plate Missing',
        'TRM-StLight Pole Missing',
        'TRM-Fence Concern (Repair)',
        'TRM-Steel Plate Repair',
        'TRM-StLight Pole Pickup',
        'TRM-Debris In Roadway',
        'TRM-Street Cut Notification'
    ],
    'animal': [
        'HLTH-Animal Dead Animal Pickup-Wildlife or Stray',
        'HLTH-Animal Attack Against Human',
        'HLTH-Animal Attack Against Animal',
        'HLTH-Animal Bite Pickup',
        'HLTH-Animal Domestic Animal Trap or Capture Request',
        'HLTH-Animal Failure to Restrain Animal, Known Owner/Known Address',
        'HLTH-Animal In Danger/Injured/Abused/Neglected',
        'HLTH-Animal Inspection/Follow-up',
        'HLTH-Animal Aggressive Animal',
        'HLTH-Animal Barking Dog',
        'HLTH-Animal Stray Held',
        'HLTH-Animal Trapped In Vacant Building',
        'HLTH-Animal Unsanitary Conditions',
        'HLTH-Animal Wildlife Complaint',
        'MOHS-Homeless Outreach',
        'SW-Rat Rubout',
        'SW-Rat Rubout Alley Concern',
        'SW-Rat Rubout Follow-up',
        'SW-Rat Rubout Proactive',
        'SW-Dirty Alley Proactive',
        'SW-Leaf Collection Scheduling',
        'SW-Leaf Removal',
        'SW-Water Way Cleaning',
        'SW-Mechanical Alley Sweeping',
        'SW-Mechanical Street Sweeping'
    ],
    'nature': [
        'ECC-Grass Mowing',
        'HCD-Snow and Ice on Sidewalks',
        'FOR-Tree Inspection',
        'HCD-Trees and Shrubs',
        'FOR-Down Tree',
        'FOR-Fallen Limb',
        'SW-Leaf Collection Scheduling',
        'TRM-Snow/Icy Conditions',
        'TRM-Grass Mowing',
        'FOR-Broken Branch in Tree',
        'SW-Leaf Removal',
        'WW-Sediment or Erosion Problem'
    ],
    'vandalism': [
        'HCD-Graffiti',
        'RP-Graffiti Removal',
        'SW-Graffiti Removal-Owner\'s Request',
        'SW-Graffiti Removal Proactive',
        'SW-Graffiti Removal',
        'TRM-Graffiti Referral',
        'ECC-Graffiti Complaint',
        'TRM-Debris Hanging From Wires or Poles',
        'SW-BCPSS Graffiti Removal',
        'SW-Graffiti Removal - Rec and Parks',
        'WW-Hydrant Damaged',
        'HCD-Illegal Flyers'     
    ],
    'finance': ['FIN-City Motor Vehicle Accident'],

    'safety': [
        'MOHS-Homeless Outreach',
        'FCPF-Ombudsman Review',
        'HLTH-EV Waste Hauler',
        'HLTH-EV Noise',
        'HLTH-EV Odor',
        'HLTH-EV Plastic Bag Ban Violation',
        'HLTH-Animal Police/Fire/Sheriff/City Work Crew Standby'
    ]
}

# List of strings to remove from SRType
strings_to_remove = ['TRM-Barricades-Install','TRC-Conduit Observation','TRA-Ombudsman Review',
'MOIT-Address Validation Issue','FCPF-VR119-Mail','TRM-Slow Street','Supervisor Follow-Up', 'FCCS-Other', 
'ECC-Language Line', 'FCCS-Refund Check Issues', 'FCCS-Personal Property Tax', 'Information Request','TR-Escalation', 'FCPF-Makes Differ',
'FCPF-Other', 'FCPF-Payments', 'SW-HGW', 'SW-Boarding', 'SW-Appliance (Saturday White Goods)', 'PABC-Residential Reserved Disabled Parking Request',
'ECC-Miscellaneous Request', 'SW-Cleaning', 'ECC-Vehicle Look Up','ECC-Escalation', 'HCD-CCE Building Permit Complaint', 'FCPF-Trial Request-Red Light',
'ECC-Citizen Complaint or Concern', 'HCD-Zoning Investigation', 'TRC-Conduit Investigation', 'HCD-CCE Building Permit Complaint', 'ECC-Citizen Complaint or Concern', 
'TRM-Saltbox Concern','FIR-Fire Code Inspection Request', 'HCD-Systems', 'FCCS-Refunds', 'WW-Storm Inlet Choke', 'FCPF-Trial Request-Speed Citation', 'WW-Sewer Misc Investigation',
'SW-Park Cans', 'TR-Right-Of-Way Permit', 'FCCS-Paid Wrong Account/Misapplied Payment', 'WW-Water Turn Off (Request)', 'SW-Community Pitch-In', 'FCPF-Transfer of Liability', 
'Parking Fines Refunds', 'Alleys', 'New Stop Sign', 'Metered Water', 'Sewer Misc Investigation', 'BCLB-Liquor License Complaint', 'PABC-Residential Parking Permit Inquiries']

# Filter out rows based on strings to remove
df = df[~df['SRType'].isin(strings_to_remove)]

# Read the grouped data CSV into a DataFrame
grouped_df = pd.read_csv('grouped_311data.csv')

# Merge the original DataFrame with grouped data on 'SRType' column
merged_df = pd.merge(df, grouped_df, on='SRType', how='left')

# Write the merged data to a new CSV file
merged_df.to_csv('merged_311data.csv', index=False)
print("Merged data written to 'merged_311data.csv'")






# # Initialize a dictionary to hold SRTypes grouped by category kind
# grouped_by_kind = {kind: [] for kind in categories.keys()}

# # Iterate over the DataFrame and populate the dictionary
# for index, row in df.iterrows():
#     srtype = row['SRType']
#     for kind, kinds_sr_types in categories.items():
#         if srtype in kinds_sr_types:
#             grouped_by_kind[kind].append(srtype)
#             break

# # Create a list of tuples for the grouped data
# grouped_data = []
# for kind, sr_types in grouped_by_kind.items():
#     for sr_type in sr_types:
#         grouped_data.append((kind, sr_type))

# # Convert the list of tuples to a DataFrame
# grouped_df = pd.DataFrame(grouped_data, columns=['Category', 'SRType'])

# # Remove duplicate SRType entries
# grouped_df.drop_duplicates(subset='SRType', inplace=True)

# # Write the grouped data to a new CSV file
# grouped_df.to_csv('grouped_311data.csv', index=False)
# print("Data grouped by category kind written to 'grouped_311data.csv'")