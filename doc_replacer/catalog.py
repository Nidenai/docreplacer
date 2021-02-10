import os


# создаем мультиплатформенность и пишем создание каталога в разных операционных системах

def create_catalog():
    homedir = os.path.expanduser("~")
    name_os = os.name

    if name_os == 'posix':
        if not os.path.isdir(homedir + '/Документы/Doc Replacer'):
            os.mkdir(homedir + '/Документы/Doc Replacer')
    elif name_os == 'nt':
        if not os.path.isdir(homedir + '\OneDrive\Документы\Doc Replacer'):
            os.mkdir(homedir + '\OneDrive\Документы\Doc Replacer')

# создаем переменную, в которую записываем наименование текущего каталога, в зависимости от оси
name_os = os.name
homedir = os.path.expanduser("~")
working_catalog = ''
if name_os == 'posix':
    working_catalog = (homedir + '/Документы/Doc Replacer')
elif name_os == 'nt':
    working_catalog = (homedir + '\OneDrive\Документы\Doc Replacer')

# записываем в переменную весь список того, что есть в каталоге:

string_of_dir = str(os.listdir(working_catalog))




