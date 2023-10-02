

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

 Installation

1. Clone the repository:

   
   git clone https://github.com/olatunde2/new-task.git

Install Python dependencies:

     pip install -r requirements.txt
   
Run database migrations:

    python manage.py migrate

Start the development server:

    python manage.py runserver
    
service run at post 8000 

    127.0.0.1:8000/
    
Access ReDoc Documentation

    127.0.0.1:8000/redoc/
    

API Endpoints

1. Combine and Save Video
   
URL: /combine_video/

Method: POST

Description: Combines video chunks into a complete video and saves it to the database.

2. Get All Videos
 
URL: /videos_all/

Method: GET

Description: Retrieves a list of all videos stored in the database.

3. Get Complete Video
 
URL: /complete_video/<str:session_id>/

Method: GET

Description: Retrieves the complete video based on the session ID.



