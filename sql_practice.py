import pymysql
connect=pymysql.connect(
    database="world",
    user="djames",
    password="228118717",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)
cursor=connect.cursor()
cursor.execute("SELECT `Name`,`Population`, `HeadOfState` FROM `country`")
results=cursor.fetchall()
from pprint import pprint as print
print(results[0])
for x in results:
    print(x['HeadOfState'])