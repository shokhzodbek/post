from django import test
from django.test import TestCase
from .models import Post
class PostTest(TestCase):
      def setUp(self):
            Post.objects.create(post="Just test")
      def test_text_content(self):
            post = Post.objects.get(id="1")
            expected_object_name=f'{post.post}'
            self.assertEqual(expected_object_name,'Just test')

# Create your tests here.
