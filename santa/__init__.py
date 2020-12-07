from flask import Flask
from santa.db import db

from santa.base.views import base_blueprint

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(base_blueprint, url_prefix='/')

if __name__ == "__main__":
    app.run()
