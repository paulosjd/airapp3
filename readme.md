An application for plotting air pollution data, created using Flask and a JavaScript plotting library. It enables graphs of recent air pollution measurements from various monitoring sites in London to be served via http://air-aware.com:8080/chart/index. The data is from the London Air Quality Network and is served by the King's College London API.

![](https://lh3.googleusercontent.com/ny4-G7it1aIisYGiqyMmfPPssrOfZmKrm3Ct4cxzOhy2cOvQBDMTru5tr-WsbKecwF3Z17zuLizQHVKpkIq8-3uyMIV7URs8SeLpeUei4xLvSLFN5MNnZlkvSRAaC4J1GhxD5XiiUf41CyGKblr7Ts3bi8UvavZMHWI5rGlUaI3zyJI5tiqd5_bTr1mIDbARopTUJTqEccDlID9LPTnZxpWEhS-fkUuW2pzX9qQ61_CZuPiKkvA0I5s1Ir4HYfQ7sswoTr8n48lBoF1ogJt5JkPCp_s7GvMKqKeUUbDEu7AWc2VOMjShTm-KFp-wFQSGtWilug5aCEhfp5IECQOMzslpcurxNynuw0gWlS8tJZlK3iLSU1i3Yp3J1es8PLW6JIjfcln7xnnL2ZrvET6mImHrta3UXD263O9eBnGH3rp0BGBXnmstz4hQv3vmJn9CjENWN2GGiUjj4DIYeDyk3Dw1-WJiB3MY4ctPxB5LbjTvorV12vRkM0uqWvyp5iVJtAn0OuhQdcAXUUg1cYZMYSJtTQqJdWlhHt8-eXZTvmo2oIYDoH4QcSpkYPDuNnzmO_W6oBEBAs6FIiU6oSRvWdGqxNMG1kiXmWkGWUCZ4Zq1Aa1kNKmO49-FsYkO9KYQKrR40jp3Y_XvFysn4OLmDjtP9_8RVRieBDFSm_5u11e0=w1259-h925-no)

Getting Started
---------------


**Prerequisites**

Python 3.4, pip, virtualenv

**1. Clone or copy repository**

**2. Set up Virtual Environment**

Create a virtual environment named aurn-venv:

    $ virtualenv aurn-venv

Activate the virtual environment:

    $ source aurn-venv/bin/activate
    (aurn-venv) $

Use *pip* to install requirements:

    (aurn-venv) $ pip install requirements.txt

Verify that packages have been installed:

    (aurn-venv) $ pip freeze
    Flask==0.12
    Flask_SQLAlchemy==2.1
    pytz==2017.2
    flask-migrate==2.1.1
    requests==2.13.0
    beautifulsoup4==4.6.0

**3. Push Flask application context**

Run the following commands in Python within the virtual environment:

    >>> from app import create_app()

    >>> create_app().app_context().push()


Create and populate a database using the create_db() and update_db() functions.

    >>> from app.data.hourly import create_db, update_db

    >>> create_db()

    >>> update_db()

The create_db() function creates the database schema. The update_db() function runs the webscraping script and inserts the air quality data in the 'data' table. This should be set up to run on an hourly basis; n.b. the webpage https://uk-air.defra.gov.uk/latest/currentlevels updates at 40 minutes past the hour.


**4. Configure and run the API**

After ensuring correct settings within app/config, the database can be queried through the API after running the server:

    $ python run.py
    
    Running the application

After downloading project files, run the following commands from the project's root directory:

pip install -r requirements.txt

python app.py

