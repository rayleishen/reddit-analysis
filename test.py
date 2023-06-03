import csv

#file = open('test.csv', encoding="utf-8")

# Open file 
with open('test.csv', errors="ignore") as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        print(row)