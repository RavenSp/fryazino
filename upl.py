from documents.models import Documents
import csv
import os

PATH = '/home/raven/work/fryazino/project/dtd/'

def loadfile(file):

	with open(file) as csvfile:
		rd = csv.reader(csvfile)

		for row in rd:

			doc = Documents()

			doc.title = row[0]
			doc.slug = row[1]
			doc.number = row[2]
			doc.Author_id = row[3]
			doc.DocCategory_id = row[3]
			doc.TypeDoc_id = row[5]

			doc.docDate = ''.join(row[6].split())
			doc.publishDate = row[8]
			doc.publish = True
			doc.file = row[10]

			print(doc)

			doc.save()






def go():

	for file in os.listdir(PATH):

		if os.path.isfile(os.path.join(PATH, file)):

			if file.split('.')[-1] == 'csv':

				if file[:4] != 'DONE':
					print('*'*50)
					print(str(file))
					print('*'*50)

					loadfile(os.path.join(PATH, file))
					os.rename(os.path.join(PATH, file), os.path.join(PATH, 'DONE-'+file))

					print(str(file) + ' DONE \n')


if __name__ == '__main__':

	go()

