# Complete code
import os
import sys
import datetime
import argparse
import click
import mysql.connector
connec = mysql.connector.connect(user='root', password='password', host='localhost', database='todo')
def help():
    print("create_title : --input1 create_title --input2 <your title>")
    print("edit_title : --input1 edit_title --id <id> --input2 <updated title>")
    print("edit_task : --input1 edit_task --id <id> --input2 <updated title>")
def create_title(s):
    myc = connec.cursor()
    sql = f"INSERT INTO todo_table (task_title,create_at) VALUES ('{s}','{datetime.datetime.today()}');"
    myc.execute(sql)
    print("New Task Succesfully Created")
    connec.commit()
    connec.close()


def edit_title(id1,s1):
    s=str(s1)
    id=int(id1)
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
def search_task(s):
    print(f"task for {s} :")
    sql = f"select * from todo_table where task_title='{s}'"
    myc = connec.cursor()
    myc.execute(sql)
    no = 1
    for i in myc:
        print(no, "-", i)
        no = no + 1
    connec.commit()
    connec.close()
def delete(id):
    myc = connec.cursor()
    myc.execute(f"select * from todo_table where task_id='{id}';")
    flag=False
    for i in myc:
        print("deleted task :")
        print(i)
        flag=True
    if flag:
        sql=f"DELETE FROM todo_table where task_id='{id}';"
        myc.execute(sql)
        for i in myc:
            print(i)
        connec.commit()
        connec.close()
    else:
        print("task alrady deleted or task not exist")
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
        parser.add_argument("--list",nargs='?',help="list of all tasks",const="list") #narsgs=? 0 or 1 argument
        parser.add_argument("--create",nargs='?', help="create new task",const=True)
        parser.add_argument("--edit-title",dest='argument_title',nargs='*', help="edit task name") #dest=another name
        parser.add_argument("--edit-status",dest='argument_status', nargs='*', help="edit task status :-compl/incompl") #nargs=* 1 or more argument
        parser.add_argument("--edit-task", dest='argument_task', nargs='*', help="edit task name , mark as completed")
        parser.add_argument("--delete",nargs='?',help="delete task",const=True)
        parser.add_argument("--search",nargs='?', help="search task")
        args = parser.parse_args()
        if args.list:                                           #list of all task
                    if args.list =="completed":                         #list of all completed task
                        completed()
                    elif args.list=="incompleted":                      #list of all incompleted task
                        incompleted()
                    elif args.list=="list":
                        list_todo()
                    else:
                        print("you give wrong argument!please Enter any one form this:'completed'/'incompleted'")
        elif args.create:                                       #create title
            try:
                create_title(args.create)
            except:
                print("task alrady added in list")
        elif args.argument_title:                                               #edit title
            edit_title(args.argument_title[0],args.argument_title[1])
        elif args.argument_status:                                              #edit task status
            edit_status(args.argument_status[0],args.argument_status[1])
        elif args.argument_task:                                                #edit task comple/incomple
            edit_task(args.argument_task[0],args.argument_task[1])
        elif args.delete:                                                       #delete task
                delete(args.delete)
        elif args.search:                                                       #search task
            search_task(args.search)

    except:
        print("Wrong command! use:--help for help")