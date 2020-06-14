import pymysql
from datetime import datetime
from app import app
from config import mysql
from flask import jsonify, request

@app.route('/')
def home():
    return "API is ready!"

@app.route('/users/create', methods=['POST'])
def create_user():
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')
    email = request.form.get('email')
    if (not fname) or (not lname) or (not email):
        return jsonify(["Request failed! The fiels 'First Name', 'Last Name' and 'Email' must be all provided for user creation.", "Status code: 400"])
    elif (len(fname)>100) or (len(lname)>100) or (len(email)>100):
        return jsonify(["Request failed! The fiels 'First Name', 'Last Name' and 'Email' must each have a maximum of 100 characters.", "Status code: 400"])
    else:
        try:
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT 1 FROM apiusers WHERE email = %s LIMIT 1", email)
            if cur.fetchone():
                return jsonify(["Request failed! The email provided is already in use.", "Status code: 400"])
            sql = "INSERT INTO apiusers(first_name, last_name, email, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)"
            user_values = (fname, lname, email, datetime.utcnow(), datetime.utcnow())
            cur.execute(sql, user_values) 
            conn.commit()    
            return jsonify(["User record created.", "Status code: 201"])
        except Exception as e: 
            err_mess = 'Request failed! Exception raised: ' + str(e)
            return jsonify(err_mess)
        finally:
            cur.close() 
            conn.close()
        
@app.route('/users', methods=['GET'])
def getAllUsers():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM apiusers") 
        users = cur.fetchall()
        return jsonify([users, "Status code: 200"])
    except Exception as e: 
        err_mess = 'Request failed! Exception raised: ' + str(e)
        return jsonify(err_mess)
    finally:
        cur.close() 
        conn.close()

@app.route('/users/update/<int:user_id>', methods=['POST'])
def updateUser(user_id):
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')
    email = request.form.get('email')
    if (not fname) and (not lname) and (not email):
        return jsonify(["Request failed! At least one field to be updated must be provided.", "Status code: 400"])
    elif (fname and len(fname)>100) or (lname and len(lname)>100) or (email and len(email)>100):
        return jsonify(["Request failed! The fiels 'First Name', 'Last Name' and 'Email' must each have a maximum of 100 characters.", "Status code: 400"])
    else:
        try:
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT 1 FROM apiusers WHERE id = %s LIMIT 1", user_id)
            if not cur.fetchone():
                return jsonify(["User not found.", "Status code: 404"])
            if email:
                cur.execute("SELECT 1 FROM apiusers WHERE email = %s and id <> %s LIMIT 1", (email, user_id))
                if cur.fetchone():
                    return jsonify(["Request failed! The email provided is already in use.", "Status code: 400"])
                else:
                    cur.execute("UPDATE apiusers SET email = %s, updated_at = %s WHERE id = %s", \
                                                        (email, datetime.utcnow(), user_id))
            if fname:
                cur.execute("UPDATE apiusers SET first_name = %s, updated_at = %s WHERE id = %s", \
                                                        (fname, datetime.utcnow(), user_id))
            if lname:
                cur.execute("UPDATE apiusers SET last_name = %s, updated_at = %s WHERE id = %s", \
                                                        (lname, datetime.utcnow(), user_id))
            conn.commit()    
            return jsonify(["Request processed successfully.", "Status code: 200"])
        except Exception as e: 
            err_mess = 'Request failed! Exception raised: ' + str(e)
            return jsonify(err_mess)
        finally:
            cur.close() 
            conn.close()
                
@app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT 1 FROM apiusers WHERE id = %s LIMIT 1", user_id)
        if not cur.fetchone():
            return jsonify(["User not found.", "Status code: 404"])
        else:
            cur.execute("DELETE FROM apiusers WHERE id = %s", user_id)
            conn.commit()    
            return jsonify(["User record deleted.", "Status code: 200"])
    except Exception as e: 
        err_mess = 'Request failed! Exception raised: ' + str(e)
        return jsonify(err_mess)
    finally:
        cur.close() 
        conn.close()
        
if __name__ == "__main__":
    app.run()
