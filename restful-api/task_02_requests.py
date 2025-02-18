#!/usr/bin/python3
"""Module for fetching and processing posts from JSONPlaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.
    """
    # Make GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Print status code
    print(f"Status Code: {response.status_code}")

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    # Make GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        posts = response.json()

        # Create list of dictionaries with selected fields
        formatted_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define fieldnames for CSV
            fieldnames = ['id', 'title', 'body']

            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write all posts
            writer.writerows(formatted_posts)
