count = 0  

with open('311_CSR_2021.csv') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:

        # Increment count for each iteration
        count += 1       

        # Print the 6th element and count  
        print(f"Line {count}: {line[5]}")   

        # Print the total count after the loop
        print(f"Total lines: {count}")  