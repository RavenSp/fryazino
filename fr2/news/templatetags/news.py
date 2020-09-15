from django import template
from news.models import News, Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('similar_news.html')
def similar_news(obj, conut=2):

	obj_news = obj.tags.similar_objects()

	news = []

	for new in reversed(obj_news):

		if type(new) == News:
			
			if new.publish and new.publisdDate < timezone.now():

				news.append(new)

				if len(news) == 2:

					break

	return {'news':news}