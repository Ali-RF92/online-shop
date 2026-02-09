from flask import Flask
from blueprints.general import app as general_app
from blueprints.admin import app as admin_app
from blueprints.user import app as user_app

app = Flask(__name__)
app.register_blueprint(general_app)
app.register_blueprint(admin_app)
app.register_blueprint(user_app)




if __name__ == '__main__':
    app.run()
