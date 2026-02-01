import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_company_data(domain, data):
    db.collection("companies").document(domain).set(data)

def get_company_data(domain):
    doc = db.collection("companies").document(domain).get()
    return doc.to_dict() if doc.exists else None
