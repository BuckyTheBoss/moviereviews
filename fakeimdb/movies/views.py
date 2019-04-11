from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q



# Create your views here.

def index(request):
	movies = Movie.objects.all()
	return render(request, 'index.html',{'movies': movies})

def movie(request, movie_id):
	movie = Movie.objects.get(pk=movie_id)
	rating = 0
	for review in movie.moviereview_set.all():
		rating += review.rating
	if movie.moviereview_set.count() != 0:
		rating = rating/movie.moviereview_set.count()

	return render(request, 'movie.html', {'movie' : movie, 'rating' : rating})

def review(request,review_id):
	review = MovieReview.objects.get(pk=review_id)
	return render(request,'review.html', {'review' : review})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.first_name = request.POST.get('first_name')
			user.last_name = request.POST.get('last_name')
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form' : form})


@login_required
def add_review(request, movie_id):
	movie = Movie.objects.get(pk=movie_id)
	if request.method == 'POST':
		review_form = MovieReviewForm(request.POST)
		if review_form.is_valid():
			review = review_form.save(commit=False)
			review.user = request.user
			review.movie = movie
			review.save()
			return redirect('movie', movie_id)
	form = MovieReviewForm()
	return render(request, 'addreview.html', {'form' : form, 'movie' : movie })


@login_required
def comment(request, review_id):
	review = MovieReview.objects.get(pk=review_id)
	if request.method == 'POST':
		comment_form = ReviewCommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.user = request.user
			comment.review = review
			comment.save()
			return redirect('review', review_id)
	return redirect('review', review_id)

def upvote(request, review_id):
	review = MovieReview.objects.get(pk=review_id)
	review.votes += 1
	review.save()
	return redirect(request.META['HTTP_REFERER'])

def downvote(request, review_id):
	review = MovieReview.objects.get(pk=review_id)
	review.votes -= 1
	review.save()
	return redirect(request.META['HTTP_REFERER'])

def search(request):
	if request.method != 'POST':
		return redirect('index')

	text = request.POST.get('search', '')
	results = Movie.objects.filter(
		Q(title__icontains=text) |
		Q(desc__icontains=text) )

	return render(request, 'search_results.html', {'results' : results, 'text' : text})