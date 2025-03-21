import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You_Are_Cooked'

    