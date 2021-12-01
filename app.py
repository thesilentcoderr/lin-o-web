#!/bin/python3
from flask import Flask, render_template,request,json,url_for,session,flash,redirect
from flask_mysqldb import MySQL
import os
from subprocess import getstatusoutput as spo
from werkzeug.utils import  secure_filename
from werkzeug.security import generate_password_hash as gen, check_password_hash as check
import functions
app = Flask(__name__)


with open('vars.json','r') as v:
    variable = json.load(v)
    
var = variable["variables"]
db_keeps = variable["sql_conf"]



mysql = MySQL(app)
# MySQL Configuration
app.config['MYSQL_HOST'] = db_keeps["mysql_host"]
app.config['MYSQL_USER'] = db_keeps["mysql_user"]
app.config['MYSQL_PASSWORD'] = db_keeps["mysql_password"]
app.config['MYSQL_DB'] = db_keeps["mysql_db"]
app.config['MYSQL_PORT'] = db_keeps['mysql_port']
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return redirect("/user/login")

@app.route("/user/login",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['pass']
        cur = mysql.connection.cursor()
        users = cur.execute("SELECT * FROM users WHERE email_id=%s;", ([email]))
        if users > 0:
            user = cur.fetchone()
            #if(user[3]==password):
            pass_check = True
            if pass_check:
                session['logged_in'] = True
                session['full_name'] = user[0]
                session['id'] = user[3]
                print("id",session['id'])
                flash(f"Welcome {session['full_name']}!! Your Login is Successful", 'success')
            else:
                cur.close()
                flash('Wrong Password!! Please Check Again.', 'danger')
                return render_template('login.html')
        else:
            cur.close()
            flash('User Does Not Exist!! Please Enter Valid Username.', 'danger')
            return render_template('login.html')
        cur.close()
        return render_template('main_page.html',id=session['id'])
    return render_template("login.html")

@app.route("/user/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        password = form['pass']
        cur = mysql.connection.cursor()
        users = cur.execute("SELECT * FROM users;")
        if users > 0:
            all_users = cur.fetchall()
            for user in all_users:
                if (user[2] == email) :
                    flash("User Already Exists!, Please Login...")
                    return redirect('/user/customer_login')
        output = spo(f"podman run -dit --name {name} docker.io/sron13/lin_o_web")[1]
        #os.system(f"docker stop {output}")
        cur.execute("INSERT INTO users (name,email_id,password,docker_id) values (%s,%s,%s,%s);", (name,email,password,output))
        mysql.connection.commit()
        cur.close()
        return redirect('/user/login')

    return render_template("register.html")

@app.route("/takecmd/<cmd>/<args>",methods=['GET','POST'])
def takecmd(cmd,args):
    print("takcmd-",cmd,args,session['id'])
    if 'id' in session:
        output = functions.query(cmd,session['id'],args)
    return render_template("main_page.html",output=output)

@app.route("/user_defined/<cmd>",methods=['GET','POST'])
def user_defined(cmd):
    print("In user defined")
    if 'id' in session:
        print("Id checked")
        output=functions.user_defined(session['id'],cmd)
        print("Output :",output)
    return render_template("main_page.html",output=output)
@app.route("/logout")
def logout():
    if 'id' in session:
        session['logged_in'] = False 
        session.pop('full_name') 
        session.pop('id')
        flash('User Logged Out','success')
    return redirect('/')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port="80",debug=True)
