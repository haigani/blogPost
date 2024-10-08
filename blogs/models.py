from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    # How top return comments related to a post
    # def __str__(self):
    #     return
