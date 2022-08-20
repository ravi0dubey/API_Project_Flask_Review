from flask import Flask,request,jsonify
from SQl_Connection import db_connect
import mysql.connector as connection
app1= Flask(__name__)

#get means sending/posting data in URL
#post means sending data in body


#1.Write a program to insert a record in sql table via api database
#2. Write a program to update a record via api
#3. Write a program to delete a record via api
#4. Write a program to fetch a record via api
#5. All above question for mongodb as well

@app1.route('/sql_insert_record',methods= ['GET','POST'])
def connect_database():
    try:
        mydb1 = connection.connect(host="localhost",database= "projectdb", user="root", passwd="root", use_pure=True)
        cursor = mydb1.cursor()  # create a cursor to execute queries
        show_query = "SHOW DATABASES"
        print("we are in connect_db")
        cursor.execute(show_query)
        print("able to connect to MYSQL DATABASE")
        # use_db_query = "use projectdb ; "
        # cursor.execute(use_db_query)
        # print("able to use MYSQL DATABASE")
    except Exception as e:
            mydb1.close()
            print(f"Error in DB Connection: {e}")

def update_record():
    if request.method=='POST':
        print(request.method)
        a=request.json['num1']
        b=request.json['num2']
        result = a* b
        return jsonify(result)

def insert_record():
    if request.method == 'POST':
        print("inside Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        insert_query = f"insert into projectdb.students values({student_id_var},{student_batch_var},{student_name_var},{student_stream_var},{students_marks_var},{student_mail_id_var});"
        print(f"insert query :  {insert_query}")
        # cursor.execute(insert_query)
        return jsonify("record added")



@app1.route('/sql_update_record',methods= ['GET','POST'])
def update_record():
    if request.method=='POST':
        print(request.method)
        a=request.json['num1']
        b=request.json['num2']
        result = a* b
        return jsonify(result)

#it will invoke entire python main classes
if __name__ =='__main__':
    app1.run()

