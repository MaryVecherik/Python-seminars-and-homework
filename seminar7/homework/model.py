
def search_data(data, base):
    """ Поиск """
    base = base.split('\n')
    list =[]
    flag =  True
    for i in base:
        if data in i:
            list.append(i)
            flag = False
    if flag:
        list.append('Контакт не найден')
    return list


def search_data_CSV():
    """ Поиск """
    