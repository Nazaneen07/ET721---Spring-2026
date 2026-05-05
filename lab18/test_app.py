"""
Nazaneen Baguaei, 
May 5, 2026
Lab 19: unit test for veryfing authentication in FLask-SQlite app
"""

import os
import sqlite3
import pytest 
from app import app

#--------------------
# TEST DATABASE SETUP
#--------------------
TEST_DB = "test_flask_auth.db"

def init_test_db():
    #stimulate a database connection
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # create a template table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
                   )
""")
    conn.commit()
    conn.close()

#create a mock database to run the app.py file
@pytest.fixture
def client(monkeypatch):
    #override database to use test database
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    #match the mock database
    monkeypatch.setattr("app.get_db", test_get_db)
    app.config['SECRET_KEY'] = 'test_secret'

    # call function to run the mock database
    init_test_db()

    # create an instance of the Flask test client
    with app.test_client() as client:
        # yield means return the client and after the test finished the code resumes 
        yield client 

    # clean test database after tests
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

#--------------------
# TEST HOME REDIRECT
#--------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location


#--------------------
# TEST LOGIN SUCCESS
#--------------------
def test_login_success(client):
    # first create a user to test the login later 
    client.post('/signup', data={
        "username": "loginuser",
        "email": "login@example.com",
        "password": "123456"
    })

    # test the login with the user info above 
    response = client.post('/login', data={
        "email": "login@example.com",
        "password": "123456"
    }, follow_redirects=True)

    # assert testing
    assert response.status_code == 200
    # convert the <h1> welcome </h1> in dashboard.html into bytes object 
    assert "Welcome" in response.data.decode()

#--------------------
# TEST LOGIN FAILURE
#--------------------
def test_login_failure(client):
    response = client.post('/login', data={
        "email": "login@example.com",
        "password": "wrong123"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

#--------------------
# TEST SIGNUP
#--------------------
def test_signup(client):
    response = client.post('/signup', data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "123456"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data