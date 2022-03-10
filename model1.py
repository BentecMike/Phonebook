
import xml

path = '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb1.xml'
with open(path, encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = xml.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        print(f'    {row}')
        count += 1
    print(f'Всего в файле {count} строк.')

