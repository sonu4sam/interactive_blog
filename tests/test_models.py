from app.models import User, Post, Comment

def test_user_creation():
    user = User(username='testuser', email='test@example.com', password='password')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.password != 'password'

def test_post_creation():
    user = User(username='testuser', email='test@example.com', password='password')
    post = Post(title='Test Post', content='This is a test post', author=user)
    assert post.title == 'Test Post'
    assert post.content == 'This is a test post'
    assert post.author == user

def test_comment_creation():
    user = User(username='testuser', email='test@example.com', password='password')
    post = Post(title='Test Post', content='This is a test post', author=user)
    comment = Comment(text='This is a test comment', commenter=user, post=post)
    assert comment.text == 'This is a test comment'
    assert comment.commenter == user
    assert comment.post == post