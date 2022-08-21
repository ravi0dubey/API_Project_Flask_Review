import mysql.connector as connection

def db_connect():
    try:
        mydb = connection.connect(host="localhost",database= "projectdb", user="root", passwd="root", use_pure=True)
        show_query = "SHOW DATABASES"
        print("we are in connect_db")
        cursor = mydb.cursor()  # create a cursor to execute queries
        cursor.execute(show_query)
        print("able to connect to MYSQL DATABASE")
        return(mydb)
    except Exception as e:
            mydb.close()
            return (str(e))