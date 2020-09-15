from django import template
from banners.models import bigBanner, mBanner

register = template.Library()


def all_banners(count=0):

	banners = mBanner.objects.filter(active=True)

	if count>0:
		import random
		banners = random.sample(list(banners), count)


	return banners



@register.inclusion_tag('sidebar_small.html')
def all_small_banners(count=0):

	banners = all_banners(count)


	return {'banners':banners}