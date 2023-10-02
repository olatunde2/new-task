

This project is a Django-based application that allows you to upload video chunks, combine them into complete videos, and retrieve the complete videos. It can be used to handle large video uploads by breaking them into smaller chunks.

Features

- Upload video chunks.
- Combine uploaded chunks into a complete video.
- Retrieve complete videos.

Getting Started

These instructions will help you set up and run the project on your local machine.

Prerequisites

- Python 
- Django 
- Django Rest Framework 
- PostgreSQL

 Installation

1. Clone the repository:

   
   git clone https://github.com/olatunde2/new-task.git

Install Python dependencies:

   pip install -r requirements.txt
   
Run database migrations:

  python manage.py migrate

Start the development server:

  python manage.py runserver

