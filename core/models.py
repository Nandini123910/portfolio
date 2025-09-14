from django.db import models

# -----------------------------
# About Section
# -----------------------------
class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, blank=True, null=True)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    freelance = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.name

# -----------------------------
# Skills Section
# -----------------------------
class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# -----------------------------
# Resume Section: Education & Experience
# -----------------------------
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.CharField(max_length=20, default="Present")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.CharField(max_length=20, default="Present")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

# -----------------------------
# Services Section
# -----------------------------
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Bootstrap icon class, e.g., bi bi-briefcase")

    def __str__(self):
        return self.title

# -----------------------------
# Contact Section: Messages
# -----------------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
