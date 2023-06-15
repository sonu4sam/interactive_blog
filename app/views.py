from app import app, db
from app.models import User, Post, Comment

@app.route('/')
def index():
    # Logic to retrieve and display blog posts
    return 'Welcome to the Interactive Blog Website!'

# Other route handlers for user registration, login, post creation, comment creation, etc.