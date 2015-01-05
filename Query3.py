import bsddb3 as bsddb
import time

def hashTableQ3():
    answers = open('answers', 'a')
    iKey1 = input("Input first Key: ")
    iKey1 = iKey1.encode(encoding='UTF-8')
    iKey2 = input("Input second Key: ")
    iKey2 = iKey2.encode(encoding='UTF-8')    
    start_time_hDB = time.time()
    HT_FILE = "/tmp/aredmond_db/hashtable"
    try:
        hDB = bsddb.hashopen(HT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    hNumRecords = 0
    try:
        item1 = hDB.set_location(iKey1)
        item2 = hDB.set_location(iKey2)
    except: 
        print("At least one key does not exist.")
        return 0        
    currentItem = hDB.first()
    for i in range(1, len(hDB)):       
        if(item1[0] <= item2[0]):
            if(item1[0] <= currentItem[0] and currentItem[0] <= item2[0]):
                answers.write(currentItem[0].decode('UTF-8'))
                answers.write("\n")
                answers.write(currentItem[1].decode('UTF-8'))
                answers.write("\n")
                answers.write("\n")
                hNumRecords += 1                
            currentItem = hDB.next()
        else:
            if(item2[0] <= currentItem[0] and currentItem[0] <= item1[0]):
                answers.write(currentItem[0].decode('UTF-8'))
                answers.write("\n")
                answers.write(currentItem[1].decode('UTF-8'))
                answers.write("\n")
                answers.write("\n")
                hNumRecords += 1                
            currentItem = hDB.next()
    answers.close()
    hDB.close()
    end_time_hDB = time.time()
    print("Number of Records Retrieved: {}".format(hNumRecords))        
    print("--- {} microseconds ---".format((end_time_hDB - start_time_hDB) * 1000000))
    
def bTreeQ3():
    answers = open('answers', 'a')
    iKey1 = input("Input first Key: ")
    iKey1 = iKey1.encode(encoding='UTF-8')
    iKey2 = input("Input second Key: ")
    iKey2 = iKey2.encode(encoding='UTF-8')    
    start_time_bDB = time.time()
    BT_FILE = "/tmp/aredmond_db/btree"
    try:
        bDB = bsddb.btopen(BT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0  
    bNumRecords = 0
    try:
        item1 = bDB.set_location(iKey1)
        item2 = bDB.set_location(iKey2)
    except:
        print("At least one key does not exist.")
        return 0
    if(item1[0] <= item2[0]):
        currentItem = bDB.set_location(iKey1)
        while True:
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            bNumRecords += 1
            if(currentItem[0] == item2[0]):
                break
            else:
                currentItem = bDB.next()
    else:
        currentItem = bDB.set_location(iKey2)
        while True:
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            bNumRecords += 1
            if(currentItem[0] == item1[0]):
                break
            else:
                currentItem = bDB.next()        
    answers.close()
    bDB.close()
    end_time_bDB = time.time()
    print("Number of Records Retrieved: {}".format(bNumRecords))            
    print("--- {} microseconds ---".format((end_time_bDB - start_time_bDB) * 1000000))
    
def indexFileQ3():
    answers = open('answers', 'a')
    iKey1 = input("Input first Key: ")
    iKey1 = iKey1.encode(encoding='UTF-8')
    iKey2 = input("Input second Key: ")
    iKey2 = iKey2.encode(encoding='UTF-8')    
    start_time_iDB = time.time()
    I3_FILE = "/tmp/aredmond_db/indexFile3"
    try:
        iDB = bsddb.btopen(I3_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    iNumRecords = 0
    try:
        item1 = iDB.set_location(iKey1)
        item2 = iDB.set_location(iKey2)
    except:
        print("At least one key does not exist.")
        return 0
    if(item1 <= item2):
        currentItem = iDB.set_location(iKey1)
        while True:
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            iNumRecords += 1
            if(currentItem[0] == item2[0]):
                break
            else:
                currentItem = iDB.next()
    else:
        currentItem = iDB.set_location(iKey2)
        while True:
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            iNumRecords += 1
            if(currentItem[0] == item1[0]):
                break
            else:
                currentItem = iDB.next()        
    answers.close()
    iDB.close()
    end_time_iDB = time.time()
    print("Number of Records Retrieved: {}".format(iNumRecords))            
    print("--- {} microseconds ---".format((end_time_iDB - start_time_iDB) * 1000000))
    
def Query3(instruction):
    instruction = int(instruction)
    if(instruction == 1):
        hashTableQ3()
        print("Hash Table Key Range Search.")
    elif(instruction == 2):
        bTreeQ3()
        print("B-Tree Key Range Search.")
    elif(instruction == 3):
        indexFileQ3()
        print("Index File Range Search.")

 