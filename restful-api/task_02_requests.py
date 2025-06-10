#!/user/bin/env python3
"""Module for making HTTP requests to a RESTful API.
"""
import requests
import json
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder.
    """
    method = 'GET'
    url = 'https://jsonplaceholder.typicode.com/posts'
    if method == 'GET':
        response = requests.get(url)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}")
    else:
        print(f"Status code: {response.status_code}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a file.
    """
    method = 'GET'
    url = 'https://jsonplaceholder.typicode.com/posts'
    if method == 'GET':
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            with open('posts.csv', 'w', newline="", encoding="utf-8") as file:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for post in posts:
                    writer.writerow({'id': post['id'], 'title': post['title'],
                                     'body': post['body']})
        else:
            print(f"Status code: {response.status_code}")
