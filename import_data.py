def read_csv():
    file = 'Phonebook.csv'
    with open (file, 'r', encoding = 'utf-8') as data:
        data1= data.readlines()
    my_list = []
    for line in data1:
        my_list.append(line.split(';'))
    return my_list


def search_data(data, info):
    my_list_info = []
    for i in data:
        for j in i:
            if j == info:
                my_list_info.append(i)
    return my_list_info
