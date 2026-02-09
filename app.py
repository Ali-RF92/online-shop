from flask import Flask
from blueprints.general import app as general_app


app = Flask(__name__)
app.register_blueprint(general_app)




if __name__ == '__main__':
    app.run()
