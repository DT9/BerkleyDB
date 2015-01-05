import bsddb3 as bsddb
import time

def hashTableQ1():
    answers = open('answers', 'a')    
    iKey = input("Input Key: ")
    iKey = iKey.encode(encoding='UTF-8')    
    start_time_hDB = time.time()
    HT_FILE = "/tmp/aredmond_db/hashtable"
    try:
        hDB = bsddb.hashopen(HT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    hNumRecords = 0
    if(hDB.has_key(iKey)):
        start_time_hDB = time.time()
        location = hDB.set_location(iKey)
        answers.write(location[0].decode('UTF-8'))
        answers.write("\n")
        answers.write(location[1].decode('UTF-8'))
        answers.write("\n")
        answers.write("\n")
        hNumRecords += 1
    try:
        hDB.close()
        answers.close()
    except Exception as e:
        print (e)
    end_time_hDB = time.time()
    print("Number of Records Retrieved: {}".format(hNumRecords))
    print("--- {} microseconds ---".format((end_time_hDB - start_time_hDB) * 1000000))

def bTreeQ1():
    answers = open('answers', 'a')    
    iKey = input("Input Key: ")
    iKey = iKey.encode(encoding='UTF-8')    
    start_time_bDB = time.time()
    BT_FILE = "/tmp/aredmond_db/btree"
    try:
        bDB = bsddb.btopen(BT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    bNumRecords = 0
    if(bDB.has_key(iKey)):
        location = bDB.set_location(iKey)
        answers.write(location[0].decode('UTF-8'))
        answers.write("\n")
        answers.write(location[1].decode('UTF-8'))
        answers.write("\n")
        answers.write("\n")
        bNumRecords += 1
    try:
        bDB.close()
        answers.close()
    except Exception as e:
        print (e)   
    end_time_bDB = time.time()
    print("Number of Records Retrieved: {}".format(bNumRecords))
    print("--- {} microseconds ---".format((end_time_bDB - start_time_bDB) * 1000000))
    
def indexFileQ1():
    answers = open('answers', 'a')    
    iKey = input("Input Key: ")
    iKey = iKey.encode(encoding='UTF-8')    
    start_time_iDB = time.time()
    I1_FILE = "/tmp/aredmond_db/indexFile1"
    try:
        iDB = bsddb.hashopen(I1_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    iNumRecords = 0
    if(iDB.has_key(iKey)):
        location = iDB.set_location(iKey)
        answers.write(location[0].decode('UTF-8'))
        answers.write("\n")
        answers.write(location[1].decode('UTF-8'))
        answers.write("\n")
        answers.write("\n")
        iNumRecords += 1
    try:
        iDB.close()
        answers.close()
    except Exception as e:
        print (e)        
    end_time_iDB = time.time()
    print("Number of Records Retrieved: {}".format(iNumRecords))
    print("--- {} microseconds ---".format((end_time_iDB - start_time_iDB) * 1000000))

def Query1(instruction): 
    instruction = int(instruction)
    if(instruction == 1):
        hashTableQ1()
        print("Hash Table Key Search.")
    elif(instruction == 2):
        bTreeQ1()
        print("B-Tree Key Search.")
    elif(instruction == 3):
        indexFileQ1()
        print("Index File Key Search.")