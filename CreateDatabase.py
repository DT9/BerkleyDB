import bsddb3 as bsddb
import random
import sys
import os

DB_SIZE = 100000
SEED = 10000000
DB_PATH = "/tmp/aredmond_db/"

if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

def get_random():
    return random.randint(0, 63)
def get_random_char():
    return chr(97 + random.randint(0, 25))

def hashTableCD():
    data = open('data', 'a') 
    HT_FILE = "/tmp/aredmond_db/hashtable"
    try:
        hDB = bsddb.hashopen(HT_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        hDB = bsddb.hashopen(HT_FILE, "c")
    random.seed(SEED)
    keySet = set()
    for index in range(DB_SIZE):
        while(True):
            krng = 64 + get_random()
            key = "" 
            for i in range(krng):
                key += str(get_random_char())
            vrng = 64 + get_random()
            value = ""
            for i in range(vrng):
                value += str(get_random_char())
            data.write(key)
            data.write("\n")            
            data.write(value)
            data.write("\n")            
            data.write("\n")            
            key = key.encode(encoding='UTF-8')
            value = value.encode(encoding='UTF-8')
            if(not (key in keySet)):
                keySet.add(key)
                hDB[key] = value
                break
    try:
        hDB.close()
        data.close()
    except Exception as e:
        print (e)    
    

def bTreeCD():
    data = open('data', 'a') 
    BT_FILE = "/tmp/aredmond_db/btree"
    try:
        bDB = bsddb.btopen(BT_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        bDB = bsddb.btopen(BT_FILE, "c")
    random.seed(SEED)
    keySet = set()
    for index in range(DB_SIZE):
        while(True):
            krng = 64 + get_random()
            key = "" 
            for i in range(krng):
                key += str(get_random_char())
            vrng = 64 + get_random()
            value = ""
            for i in range(vrng):
                value += str(get_random_char())
            print ("Key: " + key)
            data.write(key)
            data.write("\n")            
            print ("Value: " + value)
            data.write(value)
            data.write("\n")            
            print ("")
            data.write("\n")            
            key = key.encode(encoding='UTF-8')
            value = value.encode(encoding='UTF-8')
            if(not (key in keySet)):
                keySet.add(key)
                bDB[key] = value
                break
    try:
        bDB.close()
        data.close()
    except Exception as e:
        print (e)
        
def indexFileCD():
    data = open('data', 'a') 
    I1_FILE = "/tmp/aredmond_db/indexFile1"
    I2_FILE = "/tmp/aredmond_db/indexFile2"
    I3_FILE = "/tmp/aredmond_db/indexFile3"
    try:
        i1DB = bsddb.hashopen(I1_FILE, "w")
        i2DB = bsddb.hashopen(I2_FILE, "w")
        i3DB = bsddb.btopen(I3_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        i1DB = bsddb.hashopen(I1_File, "c")
        i2DB = bsddb.hashopen(I2_FILE, "c")
        i3DB = bsddb.btopen(I2_FILE, "c")
    random.seed(SEED)
    keySet = set()
    valueSet = set()
    for index in range(DB_SIZE):
        while(True):
            krng = 64 + get_random()
            key = "" 
            for i in range(krng):
                key += str(get_random_char())
            vrng = 64 + get_random()
            value = ""
            for i in range(vrng):
                value += str(get_random_char())
            print ("Key: " + key)
            data.write(key)
            data.write("\n")            
            print ("Value: " + value)
            data.write(value)
            data.write("\n")            
            print ("")
            data.write("\n")            
            key = key.encode(encoding='UTF-8')
            value = value.encode(encoding='UTF-8')
            if(not (key in keySet)):
                keySet.add(key)
                i1DB[key] = value
                i3DB[key] = value
                if(not (value in valueSet)):
                    valueSet.add(value)
                    i2DB[value] = key
                else:
                    i2DB[value] = i2DB[value] + ";;;".encode('UTF-8') + key
                break   
    try:
        i1DB.close()
        i2DB.close()
        data.close()
    except Exception as e:
        print (e)           

def CreateDatabase(instruction): 
    instruction = int(instruction)
    if(instruction == 1):
        print("Creating Database Please Wait...")
        hashTableCD()
        print("Hash Table Created.")
    elif(instruction == 2):
        print("Creating Database Please Wait...")
        bTreeCD()
        print("B-Tree Created.")
    elif(instruction == 3):
        print("Creating Database Please Wait...")
        indexFileCD()
        print("Index File Created.")