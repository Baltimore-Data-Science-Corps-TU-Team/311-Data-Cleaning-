sr_types = []

with open('311_CSR_2021.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        sr_type = line[5]  # Accessing the SRType column (index 5)
        sr_types.append(sr_type)
        print(sr_type)