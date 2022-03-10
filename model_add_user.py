from csv import writer
import csv
  
a = []

def init(list_data):
    global a
    a = [ 
    str(input('введите фамилию: ')),
    str(input('введите имя: ')),
    str(input('введите номер телефона: ')),
    str(input('введите описание: '))
    ]
    
path = '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb.csv'

def do_it():
    with open(path, 'a', encoding='utf-8') as f_object:  
        writer_object = writer(f_object)
        for x in a:
            f_object.write('\n')
            f_object.write(x)
    f_object.close()
    return a
