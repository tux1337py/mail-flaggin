#!/usr/bin/python3
#-*-coding:utf8;-*-

import sys
import time
from urllib import request
import re
import os

banner = '''
		_______________________
		[ CODED BY: Tux1337Py ]
		[ TL: @L33TPy         ]
		[ data: 15/06/2018    ]
		[ Nome: Mail-Flaggin  ]
		=======================
'''

os.system('clear')
print(banner)

op='''
	URL     = 1
	Arquivo = 2
'''

print(op)
choic = int (input('	Opcao 1/2: '))
if choic ==1:
	site = input('\n  [!] Sua URL: ')

	try:
		text = request.urlopen(site).read().decode('utf_8','ignore')
		_capt_m = re.compile(r'[\w.-]+@[\w.-]+')
		regex = re.findall(_capt_m, text)

	except Exception as error:
		os.system('clear')
		print('\n\n  :-[  Erro ao se conectar a: ',site)
		print('\n  [!]  ERROR: ',error)
		sys.exit()

	folder= input('\n  [!] Nome de Saida do Arquivo: ')
	print('\n  [*] Emails...[*]\n')
	double = sorted(set(regex))

	for email in double:
		with open(folder,'a') as f:
			f.write(email+'\n')
			f.close()
			time.sleep(00.1)
			print('\033[1;37m	[+]  '+email+' [+]\033[m')
	print('\n	\033[1;32m[+] TOTAL DE EMAILS  | ',len(regex),' <\033[m')
	print('\n	\033[1;32m[+] EMAILS REPETIDOS | ',len(regex)-len(double),' <\033[m')
	print('\n	\033[1;32m[+] EMAILS FILTRADOS | ',len(double),' <\033[m')


else:
	os.system('clear')
	arquivo = str(input('  [!] arquivo: '))
	output = str(input('\n [!] Nome de saida do arquivo: '))

	file = open(arquivo).read()
	get_defaul = re.compile(r'[\w.-]+@[\w.-]+')
	emails_raw = re.findall(get_defaul, file)
	_rm_dup = sorted(set(emails_raw))
	for email in _rm_dup:
		with open(output,'a')  as out:
			out.write(email+'\n')
			out.close()
			time.sleep(00.1)
			print(' \033[1;37m[+] '+email+' [+]\033[m')
	print('\n\033[1;32m[+] TOTAL DE EMAILS   | ',len(emails_raw),' <')
	print('\n [+] EMAILS REPETIDOS  | ',len(emails_raw)-len(_rm_dup),' <')
	print('\n [+] EMAILS FILTRADOS  | ',len(_rm_dup),' <\033[m\n\n')
