from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from .models import url_links 

def index(request):
	if request.method=='POST':
		provided_link = request.POST.get('provided_link')
		shorted = ""
		data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
		feed_in_data = url_links.objects.all()
		c=0
		for i in feed_in_data:
			if i.links == provided_link:
				c=1
				shorted = i.short_link
		if c==0:
			for i in range(1,7):
				chrct = random.randint(0,len(data)-1)
				alpha = data[chrct]
				shorted+= alpha
			url = url_links(links=provided_link,short_link=shorted)
			url.save()
		final_short_url = 'http://127.0.0.1:8000/' + shorted 
		return render(request, "urls_link/first.html",{'final_short_url': final_short_url})
	return render(request, "urls_link/first.html")


def get_shorten_link(request, shorted_link):

	datas = url_links.objects.filter(short_link=shorted_link)
	link = ""
	for i in datas:
		link = i.links
	return redirect(link)