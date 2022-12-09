from flask import Flask
app = Flask(__name__)
app.secret_key = "kikiki"
DATABASE = "users_schema"