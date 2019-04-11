from imdb import IMDb
from movies.models import *
from faker import Faker
from django.contrib.auth.models import User
import random

ia = IMDb()
fake = Faker()

def seed_top_250(number):
	top = ia.get_top250_movies()
	n = 0
	while n < number:
		m = ia.get_movie(top[n].movieID)
		n += 1
		movie_to_add = Movie(
			title = m['title'],
			desc = m.get('plot outline', None), 
			pub_date = m['year'], 
			small_img = m['cover'],
			big_img = m['full-size cover url']
			)
		movie_to_add.save()

def delete_movies():
	for movie in Movie.objects.all():
		movie.delete()


def gen_fname():
	return fake.first_name()

def gen_lname():
	return fake.last_name()

def gen_password():
	return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def gen_user():
	return random.choice(User.objects.all())

def gen_movie():
	return random.choice(Movie.objects.all())

def gen_title():
	return fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)

def gen_paragraph():
	return fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)

def create_users(number):
	for i in range(0, number):
		fname = gen_fname()
		lname = gen_lname()
		username = fname.lower() + lname.lower()
		user = User.objects.create_user(username=username, password=gen_password(), first_name=fname, last_name=lname)
		user.save()

def create_reviews(number):
	for i in range(0, number):
		review = MovieReview(
			user=gen_user(),
			movie=gen_movie(),
			title=gen_title(),
			content=gen_paragraph(),
			rating=random.choice(MovieReview.RATINGS)[0]
			)
		review.save()


def create_comments(number):
	'''number being passed in is to represent the amount of comments per review
	not the total amount, the total amount will be 2 * amount of reviews'''
	for i in range(0, number):
		for review in MovieReview.objects.all():
			comment = ReviewComment(
				user=gen_user(),
				review=review,
				content=gen_paragraph() 
				)
			comment.save()



