import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Le credenziali vengono ora prese dalle variabili ambiente di Render
CLIENT_ID = os.environ.get('CLIENT_ID')
TENANT_ID = os.environ.get('TENANT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

# Funzione per ottenere il token di accesso
def get_access_token():
    url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'
    }

    response = requests
