from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool('DEBUG', True)
HOST = env('HOST', '0.0.0.0')
SECRET_KEY = env('SECRET_KEY')
DATABASE_URL = env('DATABASE_URL')
