import unittest
from app.models import User, Post, Comment

class ModelsTestCase(unittest.TestCase):
    def test_user_repr(self):
        user = User(username='testuser', email='test@example.com')
        self.assertEqual(str(user), '<User testuser>')

    def test_post_repr(self):
        post = Post(title='Test Post', content='This is a test post')
        self.assertEqual(str(post), '<Post Test Post>')

    def test_comment_repr(self):
        comment = Comment(text='Test comment')
        self.assertEqual(str(comment), '<Comment Test comment>')

if __name__ == '__main__':
    unittest.main()