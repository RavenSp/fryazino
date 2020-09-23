from django import template
from banners.models import bigBanner, mBanner
import random

register = template.Library()


def all_banners(count=0):

	banners = mBanner.objects.filter(active=True)

	if count>0:

		banners = random.sample(list(banners), count)


	return banners



@register.inclusion_tag('sidebar_small.html')
def all_small_banners(count=0):

	if count > 6:
		count = 6
	

	banners = all_banners(count)


	return {'banners':banners}

@register.inclusion_tag('big_banner_news.html')
def big_banner_news():

	allBanners = bigBanner.objects.filter(active=True)

	banner = random.sample(list(allBanners), 1)

	return {'banner': banner[0]}


@register.simple_tag()
def big_banners_index():

	banners = random.sample(list(bigBanner.objects.filter(active=True)), 2)

	return banners