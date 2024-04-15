import sys
import cognitive_face as CF
from global_variables import personGroupId, Key, endpoint
import sqlite3

personGroupId = 'user'
CF.BaseUrl.set(endpoint)
CF.Key.set(Key)
if len(sys.argv) != 1:
    res = CF.person.create(personGroupId, str(sys.argv[1]))
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          
        isRecordExist = 1
    if isRecordExist == 1:                                                      
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))
    connect.commit()                                                           
    connect.close()
    print("Person ID successfully added to the database")
