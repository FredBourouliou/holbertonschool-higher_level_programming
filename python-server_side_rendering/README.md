# Python Server-Side Rendering

Server-side rendering (SSR) is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data. Through this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.

## Learning Objectives

- Understand the concepts of server-side rendering and how it differs from client-side rendering
- Learn the benefits of using server-side rendering in web development
- Implement SSR in Python using the Flask framework
- Utilize Jinja templating engine to dynamically generate HTML pages
- Read and display data from various sources including JSON, CSV, and SQLite databases
- Handle dynamic content and user inputs in web applications

## Project Structure

- **Task 0**: Creating a Simple Templating Program (`task_00_intro.py`)
  - Implementation of a simple templating system that generates personalized invitation files
  
- **Task 1**: Creating a Basic HTML Template in Flask (`task_01_jinja.py`)
  - Basic Flask application with routes for home, about, and contact pages
  - Reusable templates for header and footer

- **Task 2**: Creating a Dynamic Template with Loops and Conditions (`task_02_logic.py`)
  - Integration of Jinja's loop and conditional constructs
  - Reading and displaying data from a JSON file

- **Task 3**: Displaying Data from JSON or CSV Files (`task_03_files.py`)
  - Reading and displaying product data from multiple file formats
  - Implementing query parameter filtering

- **Task 4**: Extending Dynamic Data Display to Include SQLite (`task_04_db.py`)
  - Integration with SQLite database
  - Unified data display across multiple sources

## Setup and Installation

### Dependencies

This project requires the following dependencies:
- Python 3.x
- Flask
- Jinja2 (included with Flask)
- SQLite3 (included with Python)

Install Flask using pip:
```
pip install Flask
```

### Running the Applications

To run any of the Flask applications:
```
python task_01_jinja.py  # For Task 1
python task_02_logic.py  # For Task 2
python task_03_files.py  # For Task 3
python task_04_db.py     # For Task 4
```

For Task 0, you need to create a main script to call the `generate_invitations` function.

### Database Setup

For Task 4, you need to set up the SQLite database:
```
python create_db.py
```

## Resources

- [MDN Web Docs on Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
- [Client-side vs. Server-side vs. Pre-rendering for Web Apps](https://www.toptal.com/front-end/client-side-vs-server-side-pre-rendering)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
