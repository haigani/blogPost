from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post, Comment


class BlogAPITestCase(APITestCase):

    # no Need to add date because it uses current date automaticly
    def setUp(self):
        self.post = Post.objects.create(
            title="title Test",
            content="content Test"
        )
        # self.comment = Comment.objects.create(
        #     text="Text Test"
        # )
        self.post_url = reverse('post_detail', kwargs={'pk': self.post.id})

    # self.comment_url = reverse('comment_list_create', kwargs={'pk': self.post.id})

    def test_create_post(self):
        url = reverse('post_list_create')
        data = {"title": "New Post", "content": "New Content"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_post(self):
        url = reverse('post_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        data = {"title": "Updated Post", "content": "Updated content"}
        response = self.client.put(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_create_comment(self):
    #     data = {"text": "New text"}
    #     response = self.client.post(self.comment_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
