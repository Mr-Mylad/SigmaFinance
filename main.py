# We are cooked
#Indeed we are 

##Imports
import firebase_admin
from firebase_admin import firestore
import json
import os
from pathlib import Path
juson = Path(__file__).with_name('socialsim-c1733-firebase-adminsdk-deian-7814012123.json')
cred = firebase_admin.credentials.Certificate(juson)
app = firebase_admin.initialize_app(cred)
db = firestore.client()

## Firebase config, put the details that we have in
import pyrebase
fireConfig = {
  "apiKey": "AIzaSyABEMJ-HTQcH87GusaT5be8wvnhVxgdQy4",
  "authDomain": "socialsim-c1733.firebaseapp.com",
  "databaseURL": "xhttps://socialsim-c1733-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "projectId": "socialsim-c1733",
  "storageBucket": "socialsim-c1733.appspot.com",
  "messagingSenderId": "793299840466",
  "appId": "1:793299840466:web:45ff70ef74f8317ed66c0b",
  "measurementId": "G-6NFNTL5RX9"
}

firebase = pyrebase.initialize_app(fireConfig)
auth = firebase.auth()
database = firebase.database()

