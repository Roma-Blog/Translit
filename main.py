import re

TRANSLIT_CHAR = {
    'а': 'a','б': 'b','в': 'v','г': 'g','д': 'd',
    'е': 'e','ё': 'yo','ж': 'zh','з': 'z','и': 'i','й': 'y','к': 'k',
    'л': 'l','м':'m','н': 'n','о': 'o','п': 'p',
    'р': 'r','с':'s','т': 't','у': 'u','ф': 'f','х': 'h','ц': 'c',
    'ч': 'ch','ш':'sh','щ':'sch','ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-',
}

def translit_work(sity: str, dt: dict = TRANSLIT_CHAR):
    sity = sity.lower()
    list_char_sity: list = []
    for i in range(len(sity)):
        list_char_sity.append(dt.get(sity[i], sity[i]))
    return ''.join(list_char_sity)

def open_file(name_file: str):
    _list_sity = []
    with open(f'{name_file}.txt', 'r') as f:
        _list_sity = f.read().split('\n')

    for i in range(len(_list_sity)):
        _list_sity[i] = re.sub(r'(,\s+|\s+,)',',', _list_sity[i])
        _list_sity[i] = dict.fromkeys(_list_sity[i].split(','), '')
    
    return _list_sity

def translit_list(ls: list):
    for item in ls:
        for el in item:
            item[el] = translit_work(el)
    return ls

def work_file(name_file: str, ls: list):
    with open(f'{name_file}.txt', 'w') as f:
        for item in ls:
            row: list = []
            for el in item:
                row.append(f"{el} ({item[el]})")
            f.write(f'{", ".join(row)}\n')

list_sity = translit_list(open_file("sity"))

work_file("sity-new", list_sity)


