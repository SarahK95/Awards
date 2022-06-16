from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='sarah', password='sara000')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='sarah')
        self.post = Projects.objects.create(id=1, title='test post', photo='https://cdn.pixabay.com/photo/2022/05/12/12/55/sunset-7191546_960_720.jpg', description='HELLO',
                                        user=self.user, url='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Projects))

    def test_save_post(self):
        self.project.save_project()
        post = Projects.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_projects(self):
        self.post.save()
        posts = Projects.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_project(self):
        self.post.save()
        project = Projects.search_project('test')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.post.delete_project()
        project = Projects.search_project('test')
        self.assertTrue(len(project) < 1)
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        Projects.objects.all().delete()
         
        

        