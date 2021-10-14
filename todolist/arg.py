# Complete code
import os
import sys
import datetime
import argparse
import click
import mysql.connector
connec = mysql.connector.connect(user='root', password='password', host='localhost', database='todo')
@click.group(chain=True)
#@click.version_option(version='0.01',prog_name="arg")
def main():
    pass
@click.command()
@click.option('--create', help='number of greetings')
def create_title(create):
    print("hello")
    myc = connec.cursor()
    sql = f"INSERT INTO todo_table (task_title,create_at) VALUES ('{create}','{datetime.datetime.today()}');"
    myc.execute(sql)
    print("New Task Succesfully Created")
    connec.commit()
    connec.close()

@click.command("--list")
@click.option('--list', help='number of greetings')
def list_todo(list):
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
if __name__=="__main__":
    main()
    #create_title()
    #list_todo()