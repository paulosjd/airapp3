'''from flask import url_for
import yourapp

test_client = yourapp.app.test_client()
response = test_client.get(url_for('whatever.url'), follow_redirects=True)

# check that the path changed
assert response.request.path == url_for('redirected.url')'''