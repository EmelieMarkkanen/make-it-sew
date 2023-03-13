from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.utils.text import slugify
import textwrap
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField

STATUS = ((0, "Draft"), (1, "Published"))

DIFFICULTY = (
    (0, 'Beginner'),
    (1, 'Intermediate'),
    (2, 'Expert'),
)

SUGGESTED_FABRICS = (
    ('stretch', 'Stretch'),
    ('non_stretch', 'Non-stretch'),
    ('wool', 'Wool'),
    ('denim', 'Denim'),
    ('silk', 'Silk'),
    ('cotton', 'Cotton'),
    ('lace', 'Lace'),
    ('canvas', 'Canvas'),
    ('chiffon', 'Chiffon'),
    ('jersey', 'Jersey'),
    ('gingham', 'Gingham'),
    ('spandex', 'Spandex'),
    ('organza', 'Organza'),
)


class PostPattern(models.Model):
    """
    Model for posting patterns
    Assigns fields and method for model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_patterns")
    file = CloudinaryField('pdf')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    featured_pattern = models.BooleanField(default=False)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    suggested_fabrics = MultiSelectField(choices=SUGGESTED_FABRICS, null=True)
    likes = models.ManyToManyField(User, related_name='pattern_like', blank=True)

    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def excerpt_slice(self):
        if not self.excerpt:
            # Get the first 25 characters of the description
            excerpt_of_description = textwrap.wrap(strip_tags(self.description), width=25)[:2]
            # Join the characters back together to create the excerpt
            self.excerpt = ' '.join(excerpt_of_description) + '...'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt_slice()
        super().save(*args, **kwargs)


class PostComment(models.Model):
    """
    Model for posting comments
    Assigns fields and method for model
    """
    post = models.ForeignKey(PostPattern, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
