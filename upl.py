from documents.models import Documents
import csv

with open('docs.csv') as csvfile:
	rd = csv.reader(csvfile)

	for row in rd:

		doc = Documents()

		doc.title = row[0]
		doc.slug = row[1]
		doc.number = row[2]
		doc.Author_id = row[3]
		doc.DocCategory_id = row[4]
		doc.TypeDoc_id = row[5]

		dt = row[6].split('.')
		dt.reverse()
		dt = '-'.join(dt)
		doc.docDate = dt
		doc.publishDate = dt + ' 00:00'
		doc.publish = True
		doc.file = row[10]

		print(doc)

		doc.save()
