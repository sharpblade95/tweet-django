from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView , ListView

# Create your views here.

class TweetDetailView (DetailView):
	queryset = Tweet.objects.all()
	template_name = "tweets/detail_view.html"
	def get_object(self):
		return Tweet.objects.get(id=1)

class TweetListView(ListView):
	template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()

def tweet_detil_view(request, id=1):
	obj = Tweet.objects.get(id=id)
	context = {
		"object":obj
	}
	return render(request, "tweets/detail_view.html",context)



def tweet_list_view(request):
	objlist = Tweet.objects.all()
	context = {
		"object_list" : objlist
	}
	return render(request, "tweets/list_view.html",context)
	