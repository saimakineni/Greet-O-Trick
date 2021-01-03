from flask import Flask

app = Flask("greet-o-treet")

from app import routes
