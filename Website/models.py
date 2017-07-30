from django.db import models
from django.contrib.auth.models import User

#from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Item(models.Model):
	CATEGORIES = (
		('Select category', '-'),
		('Stationary', 'Stationary'),
		('Eatables', 'Eatables'),
	)

	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, choices=CATEGORIES, default='-')
	quantity = models.IntegerField()
	pic = models.FileField(upload_to = 'images/', null=True, blank=True)
	specs = models.TextField()
	unit_price = models.IntegerField()
	item_id = models.IntegerField(primary_key=True)
	xcord = models.IntegerField(null=True)
	ycord = models.IntegerField(null=True)
	QRcode = models.CharField(max_length=20, null=True)
	
	def __str__(self):
		return self.name 

	@property
	def status(self):
		if self.quantity:
			return True
		return False

class Review(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
	review_date = models.DateField(null=True)

	def __str__(self):
		return self.title