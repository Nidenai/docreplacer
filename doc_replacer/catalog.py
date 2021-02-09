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

create_catalog()