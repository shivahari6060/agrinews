from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='media')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)




class Post(models.Model):
    title = models.CharField(max_length= 300)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models.ManyToManyField(Author)
    body = models.TextField()
    publish = models.DateTimeField()
    categories = models.CharField(max_length=300, blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =["-publish"]
        
    def get_absolute_url(self):
        return "/blog/%s/" %(self.slug) 
        
        
#   this is the slug for the post      
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_post_reciever(sender, instance, *args ,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
            
pre_save.connect(pre_save_post_reciever, sender=Post)






# this is the comment section 
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name =models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Contact message  {} by {}'.format(self.body, self.first_name)