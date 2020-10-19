from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import csv

HOST = 'http://www.fryazino.org'
URL_BASE = 'http://www.fryazino.org/docum/Reshen/'
PAGES = ['5832', '5023', '4558']

'''
, '4095', '3406', '2985', '2718', '2551', '2331'
'''

def transliterate(string):

    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'Ж': u'Zh',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ц': u'Ts',
                       u'Ч': u'Ch',
                       u'Ш': u'Sh',
                       u'Щ': u'Sch',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',
                       u'Ю': u'Yu',
                       u'Я': u'Ya',}

    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'ё': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ъ': u'',
                       u'ы': u'y',
                       u'ь': u'',
                       u'э': u'e',
                       u'ю': u'yu',
                       u'я': u'ya',}

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    bad_symbols = '. , / ? | " ! ~ ` @  # № $ ; : % ^ & ? * ( ) < > \ { } [ ] '.split()

    for symb in bad_symbols:

    	translit_string.replace(symb, '')

    return translit_string

table = []

for PAGE in PAGES:

	URL = URL_BASE + PAGE

	html = urlopen(URL).read()

	BSobj = BeautifulSoup(html, 'lxml')

	cont = BSobj.find('div', {'id':'page_content'}).findAll('p')


	for doc in cont:

		title = ' '.join(doc.get_text().split())
		url = transliterate(title)
		numb = doc.span.text.split()[1]
		date = doc.findAll('span')[1].text.split()[1]
		time = ' 00:00'
		Author = '2'
		DocCategory = '5'
		TypeDoc = '3'
		file = os.path.join(date.split('.')[2], date.split('.')[1], date.split('.')[0], doc.a['href'].split('/')[-1])

		if not os.path.exists(os.path.dirname(file)):
			os.makedirs(os.path.dirname(file))

		if not os.path.exists(file):
			fl = urlopen(HOST + doc.a['href']).read()

			with open(file, 'wb') as f:
				f.write(fl)

			table.append([title, url, numb, Author, DocCategory, TypeDoc, date, None, date + time, True, file])

with open('docs.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)

	writer.writerows(table)


