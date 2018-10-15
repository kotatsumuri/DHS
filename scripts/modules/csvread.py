import csv
import json

def csv_to_json(file):
    csv_file = open('../upload/'+file, "r", encoding="ms932", errors="", newline="" )
    #リスト形式
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    #print(header)
    dic={}
    i=0
    for row in f:
        #rowはList
        #row[0]で必要な項目を取得することができる
        dic[i]={"time":row[0],"lon":float(row[9]),"lat":float(row[10])}
        i+=1
    f2=open("./jsons/info.json",'w')
    json.dump(dic,f2,indent=4)
