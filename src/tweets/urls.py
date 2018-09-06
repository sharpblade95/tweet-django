from django.urls import path 
from .views import tweet_detil_view,tweet_list_view ,TweetDetailView , TweetListView

urlpatterns = [
    #spath('admin/', admin.site.urls),
    path('1/', TweetDetailView.as_view(), name='detail'),
    path('', TweetListView.as_view(), name='list'),

]

