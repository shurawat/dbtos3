import pymysql
import json
import boto3

var = pymysql.connect(host='localhost', user='root', passwd='root')
cursor = var.cursor()
cursor.execute('select * from my_db.employee')

row_headers = [x[0] for x in cursor.description]
values = cursor.fetchall()

json_data = []
for result in values:
    json_data.append(dict(zip(row_headers, result)))

final = json.dumps(json_data).replace('[', '', 1).replace(']', '', -1)

with open("db.json", "w") as text_file:
    text_file.write(final)

s3 = boto3.resource('s3')
s3.meta.client.upload_file('db.json', 'myshubhbucket', 'db.json')
