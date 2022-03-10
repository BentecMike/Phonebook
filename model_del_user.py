from csv import reader, writer
import csv

# a = []
list = []


def init_del_user(list_data):
    global a
    global b
    a = [str(input('введите фамилию: '))]
    b = list
    print(f'{a}, init ')


path = '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb.csv'


def do_it(list):
    with open(path, 'r', encoding='utf-8') as f_object:
        writer_object = reader(f_object)
        for x in writer_object:
            list.append(x)
    f_object.close()
    return list

result = ['']

def print_list(list):
    w = int(1)
    z = int(0)
    e = int(0)
    r = int(5)
    print(round(len(list)/5))
    for x in range(round(len(list)/5)):
        list_str = ":".join(map(str, list[e:r]))  # ",".join(list)
        result.append(list_str)
        z += 1
        print("Строка гласных:", list_str)
        if z == w:
            e = e + 5
            r = r + 5
            z = 0
            #print("\n")
    print(result)
    return result

a = 'Телефон_2'
def delete(result):
    print(len(result))
    for d in result:
        if a in d:
            result.remove(d)
    print(result)
    return result




def write_pn(result):
    path1 =  '/Users/mikhail.silonov/Desktop/Geekbrains/REPO/Phonebook/pb1.csv'
    with open(path1, 'w', encoding='utf-8') as f_object:  
        writer_object = writer(f_object)
        for x in result:
            f_object.write('\n')
            f_object.write(x)
    f_object.close()



# init_del_user(a)
do_it(list)
print_list(list)
delete(result)
write_pn(result)




# with open(path, 'r', encoding='utf-8') as f_object:
#     writer_object = reader(f_object)
#     for x in writer_object:
#         list.append(x)
# f_object.close()


# # vowels = ["a", "e", "i", "o", "wer", "u", "d", "a", "e", "i", "o", "wer", "u", "d", "a", "e", "i", "o", "wer", "u", "d", "a", "e", "i", "o", "wer", "u", "d"]
# print(len(list))

# print(list[w])
# vowels_str = " ".join(list[0:2])


# # print("Строка гласных:", vowels_str)

# # Строка гласных: a,e,i,o,u
