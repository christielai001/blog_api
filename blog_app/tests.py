from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from  .models import Post

# Create your tests here.
class PostAPITest(APITestCase):

    # setup test data that will run before each test
    # create two users and have a user create a post test
    def setUp(self):
        self.user1 = User.objects.create_user(username = "user1", password = "password123")
        self.user2 = User.objects.create_user(username = "user2", password = "password123")

        self.post = Post.objects.create(
            title = "Test Post", 
            content = "Test content texts",
            author = self.user1
        )
    
    # Create token to get authorization
    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    # create a test post
    def test_case_post(self):
        # simulate logged-in user
        token = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # simulate sending a POST request that tests the serializer, view, and database save logic
        response = self.client.post("/post/", {
            "title": "New Post", 
            "content": "New content"
        })

        # 201 = created
        self.assertEqual(response.status_code, 201)

    # create a test for permissions
    # - created a test to see if second user can edit first user's post
    def test_cannot_edit_other_post(self):
        token = self.get_token(self.user2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.patch(f"/post/{self.post.id}/", {
            "title" : "User2 edits", 
            "content" : "change content"
        })

        # set the permissions to denied
        self.assertEqual(response.status_code, 403)

    def test_search_post(self):
        # GET request to retrieve result of the searched word
        # test SearchFilter
        token = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get("/post/?search=Test")

        # 200 = success
        self.assertEqual(response.status_code, 200)    

    def test_filtering_post(self):
        # GET request to retrieve what user wants to see from a certian user  
        # test DjangoFilterBackend
        token = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(f"/post/?author={self.user1.id}")

        # 200 = success
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        # GET request to retrieve to see if the number of post per page is correct  
        token = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get("/post/")

         # 200 = success
        self.assertEqual(response.status_code, 200)

        # check results confirms pagination is active
        self.assertIn("results", response.data)