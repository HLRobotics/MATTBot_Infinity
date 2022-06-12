import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("FireStorage/mattbotFirebase.json")
firebase_admin.initialize_app(cred)

def FireData_RECIEVE():     
    
    Message=[]  
    firestore_db = firestore.client()
    snapshots = list(firestore_db.collection(u'Messenger').get())
    for snapshot in snapshots:
        data=snapshot.to_dict()
        a=data['Person']
        b=data['Message']
        Message.append(str(a))
        Message.append(str(b))
    return(Message)
    
    

def FireData_SEND(User,Message):
    try:
        
        firestore_db = firestore.client()
        firestore_db.collection(u'Messenger').document(str(id)).set({'Person': User,'Message':Message})
        return(True)
    except:
        return(False)


