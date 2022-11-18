from sqlite3 import ProgrammingError
from django.shortcuts import render
from django.http import HttpResponse
from mysql.connector import connect

def login(request):
    return render(request,'mysql_app/login_page.html')

def get_login(request):
    uname=request.POST.get('username')
    pname=request.POST.get('password')
    if uname=='mysql' and pname=='workbench':
        return render(request,'mysql_app/home_page.html')
    else:
        return HttpResponse('<h1><center>Wrong username or password</center></h1>')

def home(request):
    return render(request, 'mysql_app/home_page.html')

def mysql(request):
    global host_,user_,password_
    host_ = request.POST.get('host')
    user_ = request.POST.get('user')
    password_ = request.POST.get('password')
    return render(request, 'mysql_app/index.html')
    
def New_DB(request):
    return render(request, 'mysql_app/new_db.html')

def success(request):
    db_name = request.POST.get('DB_Name')
    db=connect(
        host= host_,
        user=user_,
        password=password_
    )
    try:
        mycursor=db.cursor()
        mycursor.execute(f'CREATE DATABASE {db_name}')
        return render(request,'mysql_app/success.html',{'db_name':'databese '+db_name})
    except:
        return render(request,'mysql_app/error.html')

def quary_DB(request):
    return render(request,'mysql_app/query_login.html')

def query_DB_details(request):
    global _db_name
    _db_name = request.POST.get('_db_name')
    return render(request, 'mysql_app/query_selection.html')

def create(request):
    return render(request, 'mysql_app/create.html')

def create1(request):
    try:
        global table_name,column_data
        table_name = request.POST.get('table_name')
        column_data = request.POST.get('column_details')

        db=connect(
            host =  host_,
            user = user_,
            password = password_,
            database =  _db_name
        )
        
        mycursor=db.cursor()
        mycursor.execute(f'CREATE TABLE {table_name} ({column_data})')
        return render(request,'mysql_app/success.html',{'db_name':'table '+table_name})
    except ProgrammingError:
        return render(request,'mysql_app/error.html')

def insert(request):
    return render(request,"mysql_app/insert.html")

def insert1(request):
    t_name = request.POST.get('t_name')
    column_name = request.POST.get('columns')
    value = request.POST.get('value')
    db=connect(
        host =  host_,
        user = user_,
        password = password_,
        database =  _db_name
    )
    
    mycursor=db.cursor()
    try:
        mycursor.execute(f'INSERT INTO {t_name}({column_name}) VALUES ({value})')
        db.commit()
        return render(request,'mysql_app/success.html',{'db_name':table_name +' values'})
    except:
        return render(request,'mysql_app/error.html')


def select(request):
    return render(request,'mysql_app/select.html')

def select1(request):
    column_name=request.POST.get('c_name')
    t_name=request.POST.get('table_name')
    
    db=connect(
        host =  host_,
        user = user_,
        password = password_,
        database =  _db_name
    )
    
    mycursor=db.cursor()
    mycursor.execute(f'SELECT {column_name} FROM {_db_name}.{t_name}')
    result = mycursor.fetchall()
    for i in result:    
        return render(request,'mysql_app/select1.html',{'data':i})

def where(request):
    return render(request,'mysql_app/where.html')

def where1(request):
    column_name = request.POST.get('c_name')
    t_name = request.POST.get('table_name')
    where = request.POST.get('where')

    db=connect(
        host =  host_,
        user = user_,
        password = password_,
        database =  _db_name
    )
    
    mycursor=db.cursor()
    mycursor.execute(f'SELECT {column_name} FROM {_db_name}.{t_name} WHERE {where}')
    result = mycursor.fetchall()
    print(result)
    for i in result:    
        return render(request,'mysql_app/where1.html',{'data':i})

def drop(request):
    return render(request,'mysql_app/drop.html')

def drop1(request):
    t_name = request.POST.get('t_name')
    
    db=connect(
        host =  host_,
        user = user_,
        password = password_,
        database =  _db_name
    )
    
    mycursor=db.cursor()
    mycursor.execute(f'DROP TABLE {_db_name}.{t_name}')
    return HttpResponse('<h1><center>table dropped succesfully</center></h1>')

def delete(request):
    return render(request,'mysql_app/delete.html')

def delete1(request):
    t_name = request.POST.get('t_name')
    
    db=connect(
        host =  host_,
        user = user_,
        password = password_,
        database =  _db_name
    )
    
    mycursor=db.cursor()
    mycursor.execute(f'DELETE FROM {_db_name}.{t_name}')
    db.commit()
    return HttpResponse('<h1><center>table data deleted succesfully</center></h1>')

def exit(request):
    return render(request,'mysql_app/exit_page.html')
   
def update(request):
    return render(request,'mysql_app/update.html')

def update1(request):
    pass