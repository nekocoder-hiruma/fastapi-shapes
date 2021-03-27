"""
Config File for fast api project
"""
import os

SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_HOST = os.getenv("SERVER_HOST")
BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")
API_VERSION = "v1"

SECRET_KEY = "6v9y/B?E(H+MbQeThWmZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r5u8x/A?D(G+KbPeSh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


