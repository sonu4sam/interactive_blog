from flask import url_for
from app.models import User, Post

def test_home_page(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200
    assert b'Welcome to the Interactive Blog Website' in response.data

def test_register_page(client):
    response = client.get(url_for('register'))
    assert response.status_code == 200
    assert b'Register' in response.data

def test_login_page(client):
    response = client.get(url_for('login'))
    assert response.status_code == 200
    assert b'Login' in response.data

def test_new_post_page(client, authenticated_user):
    response = client.get(url_for('new_post'))
    assert response.status_code == 200
    assert b'New Post' in response.data

def test_post_page(client, post):
    response = client.get(url_for('post', post_id=post.id))
    assert response.status_code == 200
    assert bytes(post.title, 'utf-8') in response.data
    assert bytes(post.content, 'utf-8') in response.data

def test_update_post_page(client, authenticated_user, post):
    response = client.get(url_for('update_post', post_id=post.id))
    assert response.status_code == 200
    assert bytes(post.title, 'utf-8') in response.data
    assert bytes(post.content, 'utf-8') in response.data

def test_delete_post_page(client, authenticated_user, post):
    response = client.post(url_for('delete_post', post_id=post.id))
    assert response.status_code == 302
    assert response.location == url_for('home', _external=True).encode('utf-8')