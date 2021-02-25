import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


# UPLOAD_FOLDER = 'C:\\Users\\jamar\\Documents\\UWI Courses\\Year Two\\Semester II\\INFO3180\\Labs\\Lab Solutions\\info3180-lab4\\uploads'


class Config(object):
    """Base Config Object"""
    UPLOAD_FOLDER = 'C:\\Users\\jamar\\Documents\\UWI Courses\\Year Two\\Semester II\\INFO3180\\Labs\\Lab Solutions\\info3180-lab4\\uploads'
    # UPLOAD_FOLDER = './app/static/uploads'
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123'


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False

# from app import views