from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView , ListView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import TweetModelForm
# Create your views here.

class TweetDetailView(DetailView):
	model = Tweet
	template_name = "tweets/detail_view.html"

class TweetListView(ListView):
	template_name = "tweets/list_view.html"
	def get_queryset(self):
		qs = Tweet.objects.all()
		query = self.request.GET.get("q",None)
		if query is not None:
			qs = qs.filter(Q(content__icontains = query))
		return qs

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['create_form'] = TweetModelForm()
	    context['create_url']= reverse_lazy('tweet:create')
	    return context

class TweetCreateView(CreateView):
	model = Tweet
	form_class = TweetModelForm
	template_name = "tweets/create_view.html"
	def form_valid(self , form):
		form.instance.user = self.request.user
		return super().form_valid(form) 

class TweetUpdateView(UpdateView):
	model = Tweet
	fields = ['content']
	template_name = 'tweets/update_view.html'

class TweetDeleteView(DeleteView):
	model = Tweet
	template_name = 'tweets/delete_confirm.html'
	success_url = reverse_lazy('tweet:list')
