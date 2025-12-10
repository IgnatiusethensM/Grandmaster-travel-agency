from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    hero_image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    hero_image_url = models.URLField(max_length=500, blank=True, help_text="External URL for image (alternative to upload)")

    @property
    def get_image_url(self):
        if self.hero_image:
            return self.hero_image.url
        return self.hero_image_url

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.country}"

class Package(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='packages')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='packages')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    overview = models.TextField()
    itinerary = models.JSONField(default=list, help_text="List of daily activities")
    inclusions = models.JSONField(default=list)
    exclusions = models.JSONField(default=list)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class PackageImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, help_text="External URL for image (alternative to upload)")
    caption = models.CharField(max_length=200, blank=True)

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return self.image_url

    def __str__(self):
        return f"Image for {self.package.title}"
