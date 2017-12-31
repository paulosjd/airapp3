from flask import Flask
from views.index import index_blueprint
from views.charts import charts_blueprint


application = Flask(__name__)
app = application
app.register_blueprint(index_blueprint)
app.register_blueprint(charts_blueprint)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, passthrough_errors=True)
