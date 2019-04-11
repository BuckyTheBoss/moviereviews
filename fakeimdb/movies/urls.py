from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>', views.movie, name='movie'),
	path('reviews/add/<int:movie_id>', views.add_review, name='add_review'),
	path('reviews/<int:review_id>', views.review, name='review'),
	path('signup/', views.signup, name='signup'),
	path('reviews/<int:review_id>/comment', views.comment, name='comment'),
	path('reviews/<int:review_id>/upvote', views.upvote, name='upvote'),
	path('reviews/<int:review_id>/downvote', views.downvote, name='downvote'),
]
