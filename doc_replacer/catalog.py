import os

# создаем мультиплатформенность и пишем создание каталога в разных операционных системах

def create_catalog():
	homedir = os.path.expanduser("~")
	homedir_full = homedir + '/Documents'
	if not os.path.isdir == homedir + '/Документы/Doc Replacer':
		os.mkdir(homedir + '/Документы/Doc Replacer')
		
create_catalog()
	
