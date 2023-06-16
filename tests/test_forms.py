from app.forms import RegistrationForm, LoginForm, PostForm, CommentForm

def test_registration_form():
    form = RegistrationForm(username='testuser', email='test@example.com', password='password', confirm_password='password')
    assert form.username.data == 'testuser'
    assert form.email.data == 'test@example.com'
    assert form.password.data == 'password'
    assert form.confirm_password.data == 'password'
    assert form.validate() == True

def test_login_form():
    form = LoginForm(email='test@example.com', password='password', remember=True)
    assert form.email.data == 'test@example.com'
    assert form.password.data == 'password'
    assert form.remember.data == True
    assert form.validate() == True

def test_post_form():
    form = PostForm(title='Test Post', content='This is a test post')
    assert form.title.data == 'Test Post'
    assert form.content.data == 'This is a test post'
    assert form.validate() == True

def test_comment_form():
    form = CommentForm(text='This is a test comment')
    assert form.text.data == 'This is a test comment'
    assert form.validate() == True