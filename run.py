import os

os.environ["FLASK_APP"] = "application.py"
os.environ["FLASK_DEBUG"] = "1"
os.environ["FLASK_ENV"] = "development"
os.system('flask run')
