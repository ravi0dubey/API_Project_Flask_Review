from flask import Flask,request,jsonify
import mysql.connector as connection
import pymongo

app = Flask(__name__)


@app.route("/testfun")
def test():
    get_name = request.args.get("getname")
    mobile_number = request.args.get("mobileno")
    email_id = request.args.get("emailid")
    return "this is my first function for get: {}:{}:{} ".format(get_name,mobile_number,email_id)

#accessing database details from server
@app.route("/pymongo/webaccess")
def pymongo_read():
    print("inside pymongo_read")
    client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
    pymongo_db_name = request.args.get("pymongodbname")
    pymongo_table_name = request.args.get("pymongotablename")
    student_id = request.args.get("studentid")
    database = client[pymongo_db_name]
    collection = database[pymongo_table_name]
    d = collection.find({'student_id_var': student_id})
    print(d)
    for i in d:
        print(i['student_id_var'])

    # return jsonify(str(f"able to read record: {i['student_id_var'],i['student_batch']}"))
    return jsonify(str(f"able to read record: "))

#accessing database details from server
@app.route("/sql/webaccess")
def sql_read():
    print("inside sql_read")
    mydb = connection.connect(host="localhost", database="projectdb", user="root", passwd="root", use_pure=True)
    cursor1 = mydb.cursor()
    student_id_var = request.args.get("student_id")
    view_query = f"select * from projectdb.students where student_id > {student_id_var};"
    print(f"view query :  {view_query}")
    cursor1.execute(view_query)
    # cursor1.fetchall()
    return jsonify(str(f"able to read record: {cursor1.fetchall()}"))

if __name__=="__main__":
    app.run(port= 5002)