from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostDetail, BlogPosts, PostCreate, PostUpdate, PostDelete, CategoryList, PostLike, CommentLike, CommentDislike, CommentReply, CommentDelete

class TestBlogUrls(SimpleTestCase):
    """ Test the URLS """

    def test_blog_post_url_resolves(self):
        """
        Test that the url for the blog post detail view is correct.
        """
        url = reverse('post-detail', args=['My-Great-First-Blog-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_blog_url_resolves(self):
        """
        Test that the url for the blog view is correct.
        """
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BlogPosts)

    def test_create_post_url_resolves(self):
        """
        Test that the url for the blog view is correct.
        """
        url = reverse('post-creation')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreate)

    def test_update_post_url_resolves(self):
        """
        Test that the url for updating a post view is correct.
        """
        url = reverse('post-update', args=['My-Great-First-Blog-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdate)

    def test_delete_post_url_resolves(self):
        """
        Test that the url for the deleting a post view is correct.
        """
        url = reverse('post-delete', args=['My-Great-First-Blog-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDelete)

    def test_category_url_resolves(self):
        """
        Test that the url for the category view is correct.
        """
        url = reverse('category', args=['uncategorised'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CategoryList)

    def test_post_like_url_resolves(self):
        """
        Test that the url for liking a post is correct.
        """
        url = reverse('like', args=['My-Great-First-Blog-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_comment_like_url_resolves(self):
        """
        Test that the url for liking a comment is correct.
        """
        url = reverse('comment-like', args=['My-Great-First-Blog-slug', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CommentLike)

    def test_comment_dislike_url_resolves(self):
        """
        Test that the url for disliking a comment is correct.
        """
        url = reverse('comment-dislike', args=['My-Great-First-Blog-slug', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CommentDislike)

    def test_comment_replies_url_resolves(self):
        """
        Test that the url for comment replies is correct.
        """
        url = reverse('comment-reply', args=['My-Great-First-Blog-slug', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CommentReply)

    def test_comment_delete_url_resolves(self):
        """
        Test that the url for deleting a comment is correct.
        """
        url = reverse('comment-delete', args=['My-Great-First-Blog-slug', '1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CommentDelete)
