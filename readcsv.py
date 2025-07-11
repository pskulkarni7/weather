import csv
# Read the CSV file and print its contents

with open('temperatures.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    for line in data:   
            # Assuming the CSV format is: City, Condition, Temperature
            try:
                print(f"It is currently {line[2]}\u00b0C and {line[1]} in {line[0]} city.")
            except IndexError:  
                print("No City data found.")
        
