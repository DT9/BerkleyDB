import bsddb3 as bsddb
import time

def hashTableQ2():
    answers = open('answers', 'a')
    iValue = input("Input Value: ")
    iValue = iValue.encode(encoding='UTF-8')
    start_time_hDB = time.time()
    HT_FILE = "/tmp/aredmond_db/hashtable"
    try:
        hDB = bsddb.hashopen(HT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    hDB = bsddb.hashopen(HT_FILE, "w")
    hNumRecords = 0
    currentItem = hDB.first()
    for i in range(1, len(hDB)):       
        if (currentItem[1] == iValue):
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            hNumRecords += 1
        currentItem = hDB.next()
    try:
        hDB.close()
        answers.close()
    except Exception as e:
        print (e)    
    end_time_hDB = time.time()
    print("Number of Records Retrieved: {}".format(hNumRecords))    
    print("--- {} microseconds ---".format((end_time_hDB - start_time_hDB) * 1000000))
    
def bTreeQ2():
    answers = open('answers', 'a')
    iValue = input("Input Value: ")
    iValue = iValue.encode(encoding='UTF-8')    
    start_time_bDB = time.time()
    BT_FILE = "/tmp/aredmond_db/btree"
    try:
        bDB = bsddb.btopen(BT_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    bNumRecords = 0
    currentItem = bDB.first()
    for i in range(1, len(bDB)):       
        if (currentItem[1] == iValue):
            answers.write(currentItem[0].decode('UTF-8'))
            answers.write("\n")
            answers.write(currentItem[1].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            bNumRecords += 1
        currentItem = bDB.next()
    try:
        bDB.close()
        answers.close()
    except Exception as e:
        print (e)                    
    end_time_bDB = time.time()
    print("Number of Records Retrieved: {}".format(bNumRecords))        
    print("--- {} microseconds ---".format((end_time_bDB - start_time_bDB) * 1000000))
    
def indexFileQ2():
    answers = open('answers', 'a')    
    iKey = input("Input Value: ")
    iKey = iKey.encode(encoding='UTF-8')    
    start_time_iDB = time.time()
    I2_FILE = "/tmp/aredmond_db/indexFile2"
    try:
        iDB = bsddb.hashopen(I2_FILE, "r")
    except:
        print("DB doesn't exist.")
        return 0
    iNumRecords = 0
    if(iDB.has_key(iKey)):
        location = iDB.set_location(iKey)
        retKeys = location[1]
        retKeys = retKeys.decode('UTF-8')
        retKeys = retKeys.split(";;;")
        for k in retKeys:
            answers.write(k)
            answers.write("\n")
            answers.write(location[0].decode('UTF-8'))
            answers.write("\n")
            answers.write("\n")
            iNumRecords += 1
    try:
        iDB.close()
        answers.close()
    except Exception as e:
        print (e)        
    answers.close()
    end_time_iDB = time.time()
    print("Number of Records Retrieved: {}".format(iNumRecords))
    print("--- {} microseconds ---".format((end_time_iDB - start_time_iDB) * 1000000))
    
def Query2(instruction):
    instruction = int(instruction)
    if(instruction == 1):
        hashTableQ2()
        print("Hash Table Value Search.")
    elif(instruction == 2):
        bTreeQ2()
        print("B-Tree Value Search.")
    elif(instruction == 3):
        indexFileQ2()
        print("Index File Value Search.")