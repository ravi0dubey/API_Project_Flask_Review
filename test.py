from flask import Flask,request,jsonify

app1= Flask(__name__)

#get means sending/posting data in URL
#post means sending data in body

@app1.route('/add',methods= ['GET','POST'])
def test1():
    if request.method=='POST':
        a=request.json['num1']
        b=request.json['num2']
        result = a +b
        return jsonify(result)



@app1.route('/mult',methods= ['GET','POST'])
def test2():
    if request.method=='POST':
        a=request.json['num1']
        b=request.json['num2']
        result = a* b
        return jsonify(result)

#it will invoke entire python main classes
if __name__ =='__main__':
    app1.run()
