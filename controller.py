
import model_search_pb_surname as mspbs
import model_search_pb_name as mspbn
import model_search_pb_phonenumber as mspbpn
import model_search_pb_descriptoin as mspbd
import model_print_pb as mppb
import model_add_user as mau
import model_del_user as mdu
import view

dictionary = {}
dictionary = \
    {
        '1': '1 - Поиск по фамилии',
        '2': '2 - Поиск по имени',
        '3': '3 - Поиск по номеру телефона',
        '4': '4 - Поиск по описанию',
        '5': '5 - Добавить абонента',
        '6': '6 - Удалить абонента',
        '7': '7 - Печать справочника'
    }

def button_click():
    print("Что нужно сделать?")
    for k in dictionary.values():
        print(k)
    q = view.get_value()
    list = []
    a = []
    if q == 1:
        mspbs.init_search_sername(list)
        result = mspbs.do_it()
    if q == 2:
        mspbn.init_search_name(list)
        result = mspbn.do_it()
    if q == 3:
        mspbpn.init_search_pn(list)
        result = mspbpn.do_it()
    if q == 4:
        mspbd.init_search_descr(list)
        result = mspbd.do_it()
    if q == 5:
        mau.init(list)
        result = mau.do_it()
        view.view_data_mau(result)
    if q == 6:
        mdu.init_del_user(list, a)
        result = mdu.do_it()
        mdu.print_list(list)
        # view.view_data_mdu(result)
    if q == 7:
        result = mppb.print_pb()
        #view.view_data_mppb(result)




