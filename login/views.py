from django.shortcuts import render
from django import template
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from mysql.connector import (connection)
from login.user import User
from django.core.files.storage import default_storage
import fileinput
import pylint.lint
import pdb
import subprocess
import json
def make_connection():
    try:
        cnx = connection.MySQLConnection(user = 'root',password = '12345678',host = 'specialtopics.ciofydptdlh0.us-west-2.rds.amazonaws.com',database = 'secure_prog')
        print("Connection Successfull")
    except Exception as e:
        print(e)
    return cnx

# Create your views here.

def Check_User(user,conn):
    crsr = conn.cursor()
    query = "Select * from USERS where USERS.EMAIL='"+user.name+"' AND USERS.PASSWORD='"+user.passwd+"'"
    try:
        print(user.name)
        print(user.passwd)
        uname = str(user.name).strip()
        pwd = str(user.passwd).strip()
        crsr.execute(query)
        print("Query Executed")
        res = crsr.fetchall()
        print(res)
    except Exception as e:
        res = None
        print(e)
    return res


def Login_User(user):
    conn = make_connection()
    print(user.name)
    print(user.passwd)
    user_info = Check_User(user,conn)
    if(user_info):
        print(user_info)
        return user_info
    else:
        print("User not verified.")
        return "False"


def index(request):
    template = loader.get_template('templates/mainapp/login.html')
    context = {
        "hello":"hellostring"
    }
    return HttpResponse(template.render(context,request))


def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwod = request.POST['password']
        user = User(email,passwod)
        data = Login_User(user)
        if(data != "False"):
            template = loader.get_template('templates/mainapp/home_page.html')
        else:
            template = loader.get_template('templates/mainapp/Failed.html')
        context = {
            "hello":"hellostring"
        }
        return HttpResponse(template.render(context,request))

def upload_file(request):
    if request.method == "POST":
        print("file upload request recieved.")
        f = request.FILES["file_to_upload"]
        fileop = open("temp_op.txt",'w')
        filename = "tmp1.py"
        with default_storage.open(filename,'wb+') as destination :
            for chunk in f.chunks():
                destination.write(chunk)
        stdoutdata = subprocess.getoutput("pylint tmp1.py")
        print(str(stdoutdata))
        fileop.write(str(stdoutdata))
        fileop.close()
        print(type(f))
        # tmp_file.write(str(file_data))
        template = loader.get_template('templates/mainapp/upload_file.html')
        opdata = []
        with open("temp_op.txt","r") as fop:
            while(fop.readline()):
                opdata.append(fop.readline())

        context = {
            "outputdata": opdata
        }
        return HttpResponse(template.render(context,request))

