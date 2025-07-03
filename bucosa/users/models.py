from django.db import models
from django.contrib.auth.models import User, Group  # Use Django's built-in Group
from .models_group_message import GroupMessage
from .models_group_reaction import GroupMessageReaction
from .models_private_message import PrivateMessage
# Create your models here.

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # removed blank=True, null=True
    email = models.EmailField(('email address'), unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='profile_covers/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
class user_following(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following_user'], name='unique_followers')
        ]
        ordering = ['-created_at']

class GroupProfile(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='profile')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    admins = models.ManyToManyField(User, related_name='admin_groups', blank=True)
    description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='group_pics/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.creator_id:
            raise ValueError('A group must have a creator!')
        super().save(*args, **kwargs)
        # Ensure creator is always an admin
        if self.creator and self.pk and not self.admins.filter(pk=self.creator.pk).exists():
            self.admins.add(self.creator)

    def __str__(self):
        return self.group.name