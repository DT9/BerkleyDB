import os

def Destroy(instruction):
    instruction = int(instruction)
    try:
        if(instruction == 1):
            os.remove("/tmp/aredmond_db/hashtable")
        elif(instruction == 2):
            os.remove("/tmp/aredmond_db/btree")
        elif(instruction == 3):
            os.remove("/tmp/aredmond_db/indexFile1")
            os.remove("/tmp/aredmond_db/indexFile2")
            os.remove("/tmp/aredmond_db/indexFile3")
    except:
        print("No database exists.")
        return 0
    print("Database destroyed.")