from flask import Flask, render_template
import pymysql.cursors
import sys
from flask import Flask


app = Flask(__name__, template_folder="templates")



connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             password='123456',
                             database='db',
                             charset = 'utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# *****************
# Table yaradilir
# *****************
if sys.argv[-2] == "create" and sys.argv[-1] == "table":
    def create_table():
        with connection.cursor() as cursor:
            sql = """
                create table if not exists blogs(
                    id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
                    title varchar(250) NOT NULL,
                    description varchar(250) NOT NULL,
                    exist boolean default true   
            )
            """
            cursor.execute(sql)
        connection.commit()
    create_table()




# *********************
# Table-a insert olunur
# *********************

if sys.argv[-2] == "add" and sys.argv[-1] == "blogs":  
    def create_book(title, description, exist):
        with connection.cursor() as cursor:
            sql = """
            insert into blogs(title, description, exist) values(%s, %s, %s)
            """
            cursor.execute(sql,(title, description, exist)) 
        connection.commit() 
    title_inp = input("title daxil edin :")
    description_inp = input("description daxil edin :")
    create_book(title_inp,  description_inp, 1 )





# # **************
# Show all olur
# **************

@app.route("/<int:id>")
def show_all(id):
    with connection.cursor() as cursor:
        sql = f"""
            select * from blogs limit 5 offset {id*5}
        """
        cursor.execute(sql)
        x = cursor.fetchall()
    
    with connection.cursor() as cursor:
        sql = f"""
            select * from blogs 
        """
        cursor.execute(sql)
        y = cursor.fetchall()
    return render_template("index.html", x=x, y=y, id=id)


