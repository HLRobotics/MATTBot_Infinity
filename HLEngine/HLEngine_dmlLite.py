#author:Akhil P Jacob
#HLDynamic-Integrations

import sqlite3

def dmlLite_create(dbname,query):
    try:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(query)
    except:
        return ("HLEngine:Couldnt create DB "+dbname)

def dmlLite_insert(dbname,query):
    try:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        c.close()
        return ("HLEngine:Data Saved")
    except:
        return ("HLEngine:Couldnt insert DB "+dbname)

def dmLite_delete(dbname,query):
    try:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        return ("HLEngine:Cleared all Data")
    except:
        return ("HLEngine:Couldnt clear elements in DB "+dbname)

def dmLite_findData(dbname,query):
    try:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(query)
        data = c.fetchall()
        if len(data) == 0:
            return ("null")
        else:
            d = data[0]
            # print(data)
            # print(type(d[0]))
            return (d[0])
    except:
        return ("HLEngine:Connectivity issue detected to "+dbname)


def dmLite_findAll(dbname,query):
    try:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute(query)
        data = c.fetchall()
        for row in data:
            return (row)

    except:
        return ("HLEngine:Connectivity issue detected to " + dbname)


