# Blog API

A RESTful API for a blog platform that allows users to create, read, update, and delete posts. This API includes user authentication and authorization to ensure secure access.

## Features
- User registration and login
- JWT authentication
- Create, read, update, and delete blog posts
- Protected routes for authenticated users
- Users can only edit or delete their own posts

## Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite (default Django database)

## Authentication
- User logs in with account credentials
- Server returns an authentication token
- User includes token in requests to access protected routes

## Project Structure
- models.py -> defines database structures
- serializer.py -> converts data to/from JSON
- views.py -> handels requests 
- urls.py -> routes endpoints

## API Endpoints
- Posts
    - GET /post/
    - POST /post/
    - GET /post/{id}
    - DELETE /post/{id}
    - PUT/PATCH /post/{id}

## Installation
- Clone repo
- Create virtual environment
- Install all dependencies in requirement.txt
- Run migrations
- Start server

## Testing
- Postman
- browser (for GET request)

## Future Improvements
- add user registration
- add comments to posts
- add reaction functionality to post


        