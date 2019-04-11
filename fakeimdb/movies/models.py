from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField(default='')
	pub_date = models.CharField(max_length=5)
	small_img = models.URLField()
	big_img = models.URLField(default=None, blank=True, null=True)

class MovieReview(models.Model):
	RATINGS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	rating = models.IntegerField(choices=RATINGS)
	votes = models.IntegerField(default=0)

class MovieReviewForm(ModelForm):
	class Meta:
		model = MovieReview
		fields = ['title','content','rating']

class ReviewComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
	content = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

class ReviewCommentForm(ModelForm):
	class Meta:
		model = ReviewComment
		fields = ['content']
