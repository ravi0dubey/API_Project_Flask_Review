from flask import Flask,request,jsonify
import pymongo

app1= Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['studentdb']
collection = database["student_details"]


@app1.route('/pymongo/insert_record',methods= ['GET','POST'])
def insert_record():
    if request.method == 'POST':
        print("inside insert Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        collection.insert_one({'student_id_var' :student_id_var,'student_batch': student_batch_var,'student_name':student_name_var,'student_stream':student_stream_var,'students_marks':students_marks_var,'student_mail_id':student_mail_id_var})
        return jsonify("mongodb record added")


@app1.route('/pymongo/update_record',methods= ['GET','POST'])
def update_record():
    if request.method == 'POST':
        print("inside Update Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        collection.find_one_and_update({'student_id_var' :student_id_var}, {'$set': {'student_batch': student_batch_var,'student_name':student_name_var,'student_stream':student_stream_var,'students_marks':students_marks_var,'student_mail_id':student_mail_id_var}})
        return jsonify("mongodb record updated")

@app1.route('/pymongo/delete_record',methods= ['GET','POST'])
def delete_record():
    if request.method == 'POST':
        print("inside Delete Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        collection.delete_one({'student_id_var' :student_id_var})
        return jsonify(f"mongodb {student_id_var} record deleted")

@app1.route('/pymongo/view_record',methods= ['GET','POST'])
def view_record():
    if request.method == 'POST':
        print("inside view Post")
        student_id_var = request.json['student_id']
        student_batch_var = request.json['student_batch']
        student_name_var = request.json['student_name']
        student_stream_var = request.json['student_stream']
        students_marks_var = request.json['students_marks']
        student_mail_id_var = request.json['student_mail_id']
        # collection.find({'student_id_var': student_id_var})
        find1= collection.find({'student_id_var' :student_id_var})
        for i in find1:
            print(i)

        return jsonify(f"mongodb {student_id_var} record ")
        return jsonify(f"mongodb {collection.find({'student_id_var': student_id_var})} record ")
#it will invoke entire python main classes
if __name__ =='__main__':
    app1.run(port=5001)