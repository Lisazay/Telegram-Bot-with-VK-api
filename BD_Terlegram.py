
import pymysql
import string

try:
    conn = pymysql.connect(host="localhost", user="admin",
                           passwd="123", db="tg")

except pymysql.Error as err:
    print("Connection error: {}".format(err))
    conn.close()

sql = "UPDATE `telegram` SET `next` = `next` + 1"
sqlA = "SELECT * FROM telegram"
sqlB = "SELECT `next` FROM `telegram` "

try:
    cur = conn.cursor(pymysql.cursors.DictCursor)
    k = cur.execute(sqlB)
    k = cur.fetchone()
    data = cur.fetchall()

    conn.commit()
except pymysql.Error as err:
    print("Query error: {}".format(err))

cur.execute("CREATE TABLE IF NOT EXISTS telegram ( id INT NOT NULL AUTO_INCREMENT, next TINYINT NOT NULL, advertising TINYINT NOT NULL, PRIMARY KEY (id) , publick VARCHAR(32) NOT NULL DEFAULT '',  pub1 VARCHAR(32) NOT NULL DEFAULT '',"
            "pub2 VARCHAR(32) NOT NULL DEFAULT '',pub3 VARCHAR(32) NOT NULL DEFAULT '',pub4 VARCHAR(32) NOT NULL DEFAULT '',pub5 VARCHAR(32) NOT NULL DEFAULT '',pub6 VARCHAR(32) NOT NULL DEFAULT '',pub7 VARCHAR(32) NOT NULL DEFAULT '',"
            "pub8 VARCHAR(32) NOT NULL DEFAULT '' )")
conn.close()
print(data)
