from news.models import News
import csv
import os

def upload_news(cnt=5):

	with open('news1.csv') as csvfile:
		rd = csv.reader(csvfile)

		count = 0

		for row in rd:

			new = News.objects.create(title=row[0], category_id=row[4])

			new.slug =  new.slug + row[1][:50]
			new.publisdDate = ' '.join(row[2].split())
			new.news_text = row[3]
			new.keywords = 'Новости,' + row[7]
			new.seo_description = row[5]

			for tag in row[7].split(','):

				new.tags.add(tag)

			if len(row) > 8:

				if os.path.exists('/home/raven/work/fryazino/project/media/' + row[8]):
					
					new.image = row[8]
					new.image_in_body = True
					print('/home/raven/work/fryazino/project/media/' + row[8])

				new.save()

				print(new.title)
				count += 1



			else:

				new.save()
				print(new.title)
				count += 1

			
			#if count > cnt:

			#	break

