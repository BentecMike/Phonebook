import csv
from csv import writer

x = []

def init_search_pn(a):
    global x
    x.append(str(input('введите номер телефона: '))) 
    

def do_it():
    path = '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb_2.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",") 
        count = 0
        count1 = 1    
        for row in file_reader:
            print('x' in (row))
            # print(f'{count1}. строка {count}    {row}')
            if row == x:
                print(f'{count1}. строка {count}    {row}')
                count1 += 1
            count += 1

