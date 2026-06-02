from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    # Basic Information
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default='ASH Emran')
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Content
    description = models.TextField(max_length=500, help_text="Short description (max 500 characters)")
    content = RichTextField(help_text="Full blog content with rich text formatting")

    # Images
    image = models.ImageField(upload_to='blog_images/', help_text="Blog cover image (will be used as OG image and thumbnail)")

    # SEO Fields
    meta_title = models.CharField(max_length=60, blank=True, help_text="SEO title (60 characters recommended)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO description (160 characters recommended)")
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags for SEO")

    # Open Graph Fields
    og_title = models.CharField(max_length=100, blank=True, help_text="Open Graph title")
    og_description = models.CharField(max_length=160, blank=True, help_text="Open Graph description")

    # Publishing
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")

    class Meta:
        ordering = ['-publish_date']
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)

        # Auto-fill OG fields from basic fields if empty
        if not self.og_title:
            self.og_title = self.title
        if not self.og_description:
            self.og_description = self.description
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_description:
            self.meta_description = self.description

        super().save(*args, **kwargs)
