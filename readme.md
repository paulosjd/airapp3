An application for plotting air pollution data, created using Flask and a JavaScript plotting library. It enables graphs of recent air pollution measurements from various monitoring sites in London to be served via http://air-aware.com:8080/chart/index. The data is from the London Air Quality Network and is served by the King's College London API.

![](https://lh3.googleusercontent.com/ny4-G7it1aIisYGiqyMmfPPssrOfZmKrm3Ct4cxzOhy2cOvQBDMTru5tr-WsbKecwF3Z17zuLizQHVKpkIq8-3uyMIV7URs8SeLpeUei4xLvSLFN5MNnZlkvSRAaC4J1GhxD5XiiUf41CyGKblr7Ts3bi8UvavZMHWI5rGlUaI3zyJI5tiqd5_bTr1mIDbARopTUJTqEccDlID9LPTnZxpWEhS-fkUuW2pzX9qQ61_CZuPiKkvA0I5s1Ir4HYfQ7sswoTr8n48lBoF1ogJt5JkPCp_s7GvMKqKeUUbDEu7AWc2VOMjShTm-KFp-wFQSGtWilug5aCEhfp5IECQOMzslpcurxNynuw0gWlS8tJZlK3iLSU1i3Yp3J1es8PLW6JIjfcln7xnnL2ZrvET6mImHrta3UXD263O9eBnGH3rp0BGBXnmstz4hQv3vmJn9CjENWN2GGiUjj4DIYeDyk3Dw1-WJiB3MY4ctPxB5LbjTvorV12vRkM0uqWvyp5iVJtAn0OuhQdcAXUUg1cYZMYSJtTQqJdWlhHt8-eXZTvmo2oIYDoH4QcSpkYPDuNnzmO_W6oBEBAs6FIiU6oSRvWdGqxNMG1kiXmWkGWUCZ4Zq1Aa1kNKmO49-FsYkO9KYQKrR40jp3Y_XvFysn4OLmDjtP9_8RVRieBDFSm_5u11e0=w1259-h925-no)

Getting Started
---------------


**Prerequisites**

Python 3.4, pip, virtualenv

**1. Clone or copy repository**

**2. Set up Virtual Environment**

Create a virtual environment named londonair-venv:

    $ virtualenv londonair-venv

Activate the virtual environment:

    $ source aurn-venv/bin/activate
    (londonair-venv) $

Use *pip* to install requirements:

    (londonair-venv) $ pip install requirements.txt

Verify that packages have been installed:

    (londonair-venv) $ pip freeze
    Flask==0.12
    requests==2.13.0


**4. Run the API**

After ensuring correct settings run the server:

    $ python app.py

