# panama_blog
A Blog Application system built with Django. 

Table of Contents

Introduction
Installation
Usage
Features
Configuration
Contributing
Testing
License
Credits
Support and Contact
Authors

Introduction
The Blog Application is a web-based application that is a safe place for user to put out general ideas and to get entertained. Great ideas can be achieved by writing it down.

Key features of the Django Simple Library Project:
The blog app has an amazing backend in which all the data from Sign-up → Login → Blog-post are stored and can be retrieved at any time by the user.
It has a delete and edit button that will enable users to delete any unwanted post or make corrections to an existing post.
It also has a feature of editing profile information such as changing the profile picture from the default one to the picture of their choice.
It has a feature of “Forgot password” when clicked a mail containing a link will be sent to their email for authorization and that will enable the user to change their password in case they forget it.

Installation
To install and set up the Blog Application, follow these steps:

1 Clone the repository: from your command line or terminal

git clone https://github.com/Seun-Ayela/panama_blog.git
Navigate to the project directory: from your command line or terminal cd panama_blog

Create a virtual environment: from your command line or terminal

pipenv venv
or
mkdir virtualenv
Activate the virtual environment: On mac: venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install the dependencies: pip install -r requirements.txt

Run database migrations:

python manage.py makemigrations
python manage.py migrate
N.B: python3 manage.py for macOS

Start the development server: python manage.py runserver 8080

Access the application at http://localhost:8080 in your browser.

Usage
Once the Blog application is set up, follow these steps to use it:

Create an admin user: python manage.py createsuperuser

Log in to the admin dashboard at http://localhost:8000/admin using the created admin credentials.

From the admin dashboard, you can perform the following actions: Signup, then Login, Update Profile picture, Make a blog post and so on.

Manage Blog post: Add, edit, and delete blog post. Provide information such as Title and Blog Content.
Manage Blog users: Login, update profile pics 
Features
The blog app has an amazing backend in which all the data from Sign-up → Login → Blog-post are stored and can be retrieved at any time by the user.
It has a delete and edit button that will enable users to delete any unwanted post or make corrections to an existing post.
It also has a feature of editing profile information such as changing the profile picture from the default one to the picture of their choice.
It has a feature of “Forgot password” when clicked a mail containing a link will be sent to their email for authorization and that will enable the user to change their password in case they forget it.

Contributing
Contributions to the Blog Application are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch on your forked repository: git push origin feature-name.
Submit a pull request describing your changes. Please follow the coding style and conventions already established in the project.
Testing
the catalog/test/ directory contains all test modules implemented in the project. To run the test suite for the Django Blog Application, execute the following command:

python manage.py test You can also contribute to the test suite by adding new test cases or improving existing ones. Make sure to run the tests and ensure they pass before submitting a pull request.

License
This project is licensed under the MIT License. Public domain.

Credits
The Blog application utilizes the following technologies:

Django: The web framework used to build the application.
Python: The programming language in which the project is developed.
postgresql: to host databases in production for interacting with project.
Railway: Server used for deployment.
APIs and web services: enables communications and data exchange between different software systems.
Support and Contact
For any questions, issues, or support related to the Django Simple Library Project, please contact the project maintainer at seunayela@gmail.com. You can also open an issue on the project's GitHub repository for bug reports or feature requests.

Authors
Ayela Oluwaseun 
https://panamablog-production.up.railway.app/
