from django.db import models

from PIL import Image
import os

from django.conf import settings

import uuid

def get_uuid():
	return str(uuid.uuid4().fields[0])


class Good(models.Model):

	name 				= models.CharField(max_length = 150, verbose_name='Наименование')
	description 		= models.TextField(max_length=1024, verbose_name='Описание', blank=True)

	meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)

	price 				= models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=0, blank=True, null=True)
	old_price			= models.DecimalField(verbose_name='Старая цена', max_digits=15, decimal_places=0, blank=True, null=True)

	quantity			= models.DecimalField(verbose_name='Остаток', max_digits=15, decimal_places=0, blank=True, null=True)

	vendor_code 		= models.CharField(max_length=20, verbose_name='Артикул', blank=True, null=True)
	good_code 			= models.CharField(max_length=20, verbose_name='Код', blank=True, null=True)
	slug 				= models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)

	def __str__(self):

		return self.name

	def save(self, *args, **kwargs):

		if self.slug == "":
			self.slug = get_uuid()	

		super(Good, self).save(*args, **kwargs)
			
	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'



def get_image_name_270(instance, filename):
		
	
	return get_picture_file_name(instance, filename, '270')

def get_image_name_420(instance, filename):
		
	
	return get_image_name(instance, filename, '420')

def get_image_name_1000(instance, filename):
		
	
	return get_picture_file_name(instance, filename, '1000')

def get_image_name_174(instance, filename):
		
	
	return get_image_name(instance, filename, '174')		


def get_image_name(instance, filename, param):
		
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.slug
	return new_name

def get_picture_file_name(instance, filename, param):
    ext 		= filename.split('.')[-1]
    filename 	= ('%s' + '_' + param + '.' + ext) % instance.slug
    return os.path.join('images/', filename)


def picture_thumb_name(instance, filename):
    original_image_path = str(instance.image1000.path).split('/')[-2]
    return os.path.join(original_image_path, filename)

class Picture(models.Model):

	title 					= models.CharField(max_length=150, verbose_name='Наименование', blank=True)
	slug 					= models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
	good 					= models.ForeignKey('Good', verbose_name='Товар', on_delete=models.CASCADE)

	image270				= models.ImageField(upload_to=get_image_name_270, verbose_name='Изображение 270x320', default=None, null=True, blank=True)
	image1000				= models.ImageField(upload_to=get_image_name_1000, verbose_name='Изображение 1000x1000', default=None, null=True, blank=True)
	
	image420 				= models.CharField('420 image', max_length=255, blank=True, default=None, null=True)
	image174 				= models.CharField('174 image', max_length=255, blank=True, default=None, null=True)
	
	main_image				= models.BooleanField(verbose_name='Основная картинка', default=False)

	def __init__(self, *args, **kwargs):

		super(Picture, self).__init__(*args, **kwargs)
		self.__original_image = self.image1000

	def get_420_image_url(self):
		return settings.MEDIA_URL + self.image420

	def get_174_image_url(self):
		return settings.MEDIA_URL + self.image174


	def save(self, *args, **kwargs):
		
		if self.slug == "":
			self.slug = get_uuid()
			self.title = self.slug

		if self.image1000 != self.__original_image:

			size420 	= {'height': 420, 'width': 420}
			size174 	= {'height': 174, 'width': 165}
			super(Picture, self).save(*args, **kwargs)
			extension 	= str(self.image1000.path).rsplit('.', 1)[1]
			filename 	= str(self.image1000.path).rsplit(os.sep,1)[1].rsplit('.',1 )[0]
			fullpath 	= str(self.image1000.path).rsplit(os.sep, 1)[0]

			if extension in ['jpg', 'jpeg', 'png']:

				im 				= Image.open(str(self.image1000.path))
				im.thumbnail((size420['width'], size420['height']))
				thumbname 		= filename + "_" + str(size420['width']) + "x" + str(size420['height']) + '.' + extension
				im.save(fullpath + os.sep + thumbname)
				self.image420 	= picture_thumb_name(self, thumbname)

				im.thumbnail((size174['width'], size174['height']))
				thumbname 		= filename + "_" + str(size174['width']) + "x" + str(size174['height']) + '.' + extension
				im.save(fullpath + os.sep + thumbname)
				self.image174 	= picture_thumb_name(self, thumbname)

				super(Picture, self).save(*args, **kwargs)
		else:	
			super(Picture, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'		