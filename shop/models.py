from django.db import models



class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Category Title')
    is_active = models.BooleanField(verbose_name='Active / Unactive')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category List'


# class ProductCategory(models.Model):
#     title = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان')
#     url_title = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان در url')
#     is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
#     is_delete = models.BooleanField(verbose_name='حذف شده/نشده')

#     def __str__(self):
#         return f'({self.title} - {self.url_title})'
    
#     class Meta:
#         verbose_name ='دسته بندی'
#         verbose_name_plural = 'دسته بندی ها'




 

class Product(models.Model):
    title = models.CharField(max_length=300 , verbose_name='Product Title')
    category = models.ManyToManyField(ProductCategory, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=400 , null=True , verbose_name='Short Description')
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(default="" , null=False, blank=True , unique=True , verbose_name='Title in url')
    is_active = models.BooleanField(default=False , verbose_name='Active / Unactive')
    image = models.ImageField(upload_to='product_image', blank=True)
    weight = models.DecimalField(verbose_name='Weight', blank=True , null=True , decimal_places=3 , max_digits=10)
    country_of_Origin = models.CharField(max_length=150 , verbose_name='Country of Origin', blank=True , null=True)
    quality = models.CharField(max_length=100 , verbose_name='Quality', blank=True , null=True)
    min_weight = models.DecimalField(verbose_name='Min Weight', blank=True , null=True, decimal_places=3, max_digits=10)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product List'



# class Product(models.Model):
#     title = models.CharField(max_length=300, verbose_name='عنوان محصول')
#     category = models.ManyToManyField(
#         ProductCategory,
#         related_name='product_categories',
#         verbose_name=' دسته بندی ها')
#     brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
#     price = models.IntegerField(verbose_name='قیمت')
#     short_description = models.CharField(max_length=360 , null=True , verbose_name='توضیحات کوتاه')
#     description = models.TextField(verbose_name='توضیحات اصلی')
#     slug = models.SlugField(default="" , null=False , db_index=True , blank=True, unique=True, verbose_name='عناون در url')
#     is_active = models.BooleanField(default=False , verbose_name='فعال/غیر فعال')
#     is_delete = models.BooleanField(verbose_name='حذف شده/ نشده')

#     def get_absolute_url(self):
#         return reverse('product-detail' , args=[self.slug])
    
#     def save(self, *args, **kwargs):
#         # self.slug = slugify(self.title)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.title} - {self.price}"
    
#     class Meta:
#         verbose_name ='محصول '
#         verbose_name_plural = 'محصولات  '