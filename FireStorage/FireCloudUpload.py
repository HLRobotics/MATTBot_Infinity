def fireData(User,Message):
    try:

        import firebase_admin
        from firebase_admin import credentials, firestore
        cred = credentials.Certificate("FireStorage/mattbotFirebase.json")
        firebase_admin.initialize_app(cred)

        firestore_db = firestore.client()
        firestore_db.collection(u'Messenger').document(str(id)).set({'Person': User,'Message':Message})
        return(True)
    except:
        return(False)


