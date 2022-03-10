import csv

def row_imp(dictionary):
    with open("phonNum.csv", mode = "a", encoding = 'utf-8') as f:
        file_writer = csv.writer(f, delimiter = " ", lineterminator  = "\n")
        file_writer.writerow(dictionary.values())
        
def row_imp1(dictionary):
    with open("phonNum1.csv", mode = "a", encoding = 'utf-8') as f:
        file_writer = csv.writer(f, delimiter = " ", lineterminator  = "\n")
        file_writer.writerows(dictionary.values())
        