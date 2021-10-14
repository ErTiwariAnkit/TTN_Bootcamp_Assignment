# Complete code
import os
import sys
import datetime
import argparse
import click
import mysql.connector
connec = mysql.connector.connect(user='root', password='password', host='localhost', database='todo')
def create_title(s):
    print("hello")
    myc = connec.cursor()
    sql = f"INSERT INTO todo_table (task_title,create_at) VALUES ('{s}','{datetime.datetime.today()}');"
    myc.execute(sql)
    print("New Task Succesfully Created")
    connec.commit()
    connec.close()


def edit_title(id,s):
    myc = connec.cursor()
    sql=f"UPDATE todo_table SET task_title ='{s}' where task_id='{id}';"
    myc.execute(sql)
    print(f"title edited : New title for id {id}: '{s}'")
    connec.commit()
    connec.close()
def edit_task(id,s):
    myc = connec.cursor()
    sql = f"UPDATE todo_table SET task_title ='{s}' where task_id='{id}';"
    myc.execute(sql)
    sql = f"UPDATE todo_table SET status ='completed' where task_id='{id}';"
    myc.execute(sql)
    sql = f"UPDATE todo_table SET completed_at='{datetime.datetime.today()}';"
    myc.execute(sql)
    print("task edited and mark as completed :")
    connec.commit()
    connec.close()
def edit_status(id,s):
    myc = connec.cursor()
    sql = f"UPDATE todo_table SET status ='{s}' where task_id='{id}';"
    myc.execute(sql)
    if s=="completed":
        sql=f"UPDATE todo_table SET completed_at='{datetime.datetime.today()}' where task_id='{id}';"
        myc.execute(sql)
        print(f"task edited :{s}")
    else:
        sql = f"UPDATE todo_table SET completed_at=NULL where task_id='{id}';"
        myc.execute(sql)
        print(f"task edited : {s}")
    connec.commit()
    connec.close()
def delete(id):
    myc = connec.cursor()
    myc.execute(f"select * from todo_table where task_id='{id}';")
    no=1
    for i in myc:
        print(f"deleted task :")
        print(no,"-",i)
    sql=f"DELETE FROM todo_table where task_id='{id}';"
    myc.execute(sql)
    connec.commit()
    connec.close()
def list_todo():
    print("list of all task :")
    sql="select * from todo_table"
    myc = connec.cursor()
    myc.execute(sql)
    no=1
    for i in myc:
        print(no,"-",i)
        no=no+1
    connec.commit()
    connec.close()
def completed():
    print("completed task :")
    sql="select * from todo_table where status='completed'"
    myc = connec.cursor()
    myc.execute(sql)
    no=1
    for i in myc:
        print(no,"-",i)
        no=no+1
    connec.commit()
    connec.close()
def incompleted():
    print("incompleted task :")
    sql="select * from todo_table where status='incomplete'"
    myc = connec.cursor()
    myc.execute(sql)
    no=1
    for i in myc:
        print(no,"-",i)
        no=no+1
    connec.commit()
    connec.close()
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--input1", help="first number")
        parser.add_argument("--input2",help="second number")
        parser.add_argument("--id",help="todo id")
        args = parser.parse_args()
        if args.input1=='list':
            list_todo()
        elif args.input1=="incompleted":
            incompleted()
        elif args.input1=="completed":
            completed()
        elif args.input1=="create_title":
            create_title(args.input2)
        elif args.input1=="edit_title":
            edit_title(args.id,args.input2)
        elif args.input1=="edit_task":
            edit_task(args.id,args.input2)
        elif args.input1=="edit_status":
            edit_status(args.id,args.input2)
        elif args.input1=="delete":
            delete(args.id)

    except:
        print("in except block")