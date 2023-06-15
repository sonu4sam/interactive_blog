import unittest
from app.forms import RegistrationForm, LoginForm, PostForm, CommentForm

class FormsTestCase(unittest.TestCase):
    def test_registration_form(self):
        form = RegistrationForm()
        self.assertFalse(form.validate())

    def test_login_form(self):
        form = LoginForm()
        self.assertFalse(form.validate())

    def test_post_form(self):
        form = PostForm()
        self.assertFalse(form.validate())

    def test_comment_form(self):
        form = CommentForm()
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()