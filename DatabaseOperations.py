from flask import Flask,request,jsonify
# from SQl_Connection import db_connect
import mysql.connector as connection
app1= Flask(__name__)

#get means sending/posting data in URL
#post means sending data in body


#1.Write a program to insert a record in sql table via api database
#2. Write a program to update a record via api
#3. Write a program to delete a record via api
#4. Write a program to fetch a record via api
#5. All above question for mongodb as well

class db:
    def __init__(self):
        self.mydb = connection.connect(host="localhost",database= "projectdb", user="root", passwd="root", use_pure=True)
        self.cursor1 = self.mydb.cursor()
        self.commit1= self.mydb.commit()
        print("able to connect to MYSQL DATABASE")

#1.Write a program to insert a record in sql table via api database

@app1.route('/sql_insert_record',methods= ['GET','POST'])
def insert_record():
    mydb1 = db()
    cursor = mydb1.cursor1  # create a cursor to execute queries
    commit = mydb1.commit1  # create a cursor to execute queries
    print("we are in connect_db")
    show_db_query = "SHOW DATABASES"
    cursor.execute(show_db_query)
    print(cursor.fetchall())
    print("able to connect to MYSQL DATABASE")
    show_query = "select * from students;"
    cursor.execute(show_query)
    print(cursor.fetchall())
    if request.method == 'POST':
        print("inside Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        insert_query = f"insert into projectdb.students values({student_id_var} ,'{student_batch_var}','{student_name_var}','{student_stream_var}',{students_marks_var},'{student_mail_id_var}');"
        print(f"insert query :  {insert_query}")
        cursor.execute(insert_query)
        commit
        return jsonify("record added")



#2. Write a program to update a record via api

@app1.route('/sql_update_record',methods= ['GET','POST'])
def update_record():
    mydb2 = db()
    cursor = mydb2.cursor1  # create a cursor to execute queries
    commit = mydb2.commit1  # create a commit variable to commit
    print("we are in connect_db")
    show_db_query = "SHOW DATABASES"
    cursor.execute(show_db_query)
    print(cursor.fetchall())
    if request.method == 'POST':
        print("inside Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        update_query = f"update projectdb.students  set values(student_batch = '{student_batch_var}',student_name = '{student_name_var}','{student_stream_var}',{students_marks_var},'{student_mail_id_var}')" \
                       f"where student_id = {student_id_var};"
        print(f"Update query :  {update_query}")
        cursor.execute(update_query)
        commit
        return jsonify("record added")


#it will invoke entire python main classes
if __name__ =='__main__':
    app1.run()

