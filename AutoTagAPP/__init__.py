import os
from flask import Flask
from .view import app

@app.cli.command()
def init_db():
	param.init_param()


