from django.db import models

# Create your models here.
class SwiperImg(models.Model):
    class Meta:
        verbose_name = 'Фотографии для Карусели'
    img = models.ImageField(upload_to="gallery")
    description = models.TextField(max_length=100,default='')
    title = models.CharField("Название",max_length=20,default='')
    def __str__(self):
        return self.title
    

class MainNewsPost(models.Model):
    class Meta:
        verbose_name = 'Пост на главной странице'

    img = models.ImageField(upload_to="gallery")
    description = models.TextField(max_length=100,default='')
    title = models.CharField("Название",max_length=20,default='')
    def __str__(self):
        return self.title
    
class NavbarDropdownSpeciality(models.Model):
    class Meta:
        verbose_name = 'Мамандык'
        verbose_name_plural ='Мамандык'
        
    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание специальности",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class NavbarDropdownParents(models.Model):
    class Meta:
        verbose_name = 'Ата-аналарга меню'
        verbose_name_plural ='Ата-аналарга меню' 
    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class NavbarDropdownStudents(models.Model):
    class Meta:
        verbose_name = 'Студенттерге'
        verbose_name_plural ='Студенттерге'
    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class NavbarDropdownAccept(models.Model):
    class Meta:
        verbose_name = 'Кабылдау'
        verbose_name_plural ='Кабылдау'

    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class NavbarDropdownColledge(models.Model):
    class Meta:
        verbose_name = 'Колледж'
        verbose_name_plural ='Колледж'

    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class NavbarDropdownDigitarium(models.Model):
    class Meta:
        verbose_name = 'Digitarium'
        verbose_name_plural ='Digitarium'

    title = models.CharField("Название",max_length=20,default='')
    description = models.TextField("Описание",max_length=100)
    img = models.ImageField("Картинки",upload_to="gallery")
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.title
class MainTable(models.Model):
    title = models.CharField(max_length=20,default='')
    number = models.IntegerField(max_length=10)
    class Meta:
        verbose_name = 'Таблица с цифрами на главной странице'
    def __str__(self):
        return self.title

class MainPost(models.Model):
    class Meta:
        verbose_name = 'Информация на главной странице'

    img = models.ImageField("Картинки",upload_to="gallery")
    description = models.TextField("Описание", max_length=100,default='')
    title = models.CharField("Название",max_length=20,default='')
    def __str__(self):
        return self.title
class MainPostSecond(models.Model):
    class Meta:
        verbose_name = 'Информация на главной странице'

    img = models.ImageField("Картинки",upload_to="gallery")
    description = models.TextField("Описание", max_length=100,default='')
    title = models.CharField("Название",max_length=20,default='')
    def __str__(self):
        return self.title

class Aboutuniverse(models.Model):
    class Meta:
        verbose_name = 'Про колледж'
        verbose_name_plural = 'Про колледж'

    title = models.CharField(max_length=50,default='')
    description = models.TextField("Описание",max_length=300)
    def __str__(self):
        return self.title


class ForParents(models.Model):
    class Meta:
        verbose_name = 'Ата аналарга'
        verbose_name_plural ='Ата-аналарга бет'


    title = models.CharField(max_length=50,default='')
    description = models.TextField("Описание",max_length=300)
    def __str__(self):
        return self.title
