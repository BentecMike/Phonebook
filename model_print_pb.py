import csv
from queue import Empty

def print_pb():
    path = '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = "\n")
        count = 0    
        for row in file_reader:
            print(f' {count}.    {row}')
            count += 1
        print(f'Всего в файле {count} строк.')


