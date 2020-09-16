from django import template
from news.models import News, Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('similar_news.html')
def similar_news(obj, conut=3):

	obj_news = obj.tags.similar_objects()

	news = []

	for new in reversed(obj_news):

		if type(new) == News:
			
			if new.publish and new.publisdDate < timezone.now():

				news.append(new)

				if len(news) == conut:

					break

	return {'news':news}

@register.inclusion_tag('last_news.html')
def last_news(conut=2):

	news = News.objects.filter(publish=True, publisdDate__lte=timezone.now()).order_by('-publisdDate')

	return {'news':news[:conut]}