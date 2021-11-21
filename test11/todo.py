import datetime
import argparse
import mysql.connector


class Todo:
    def __init__(self):
        try:
            self.connec = mysql.connector.connect(user='root', password='password', host='localhost', database='todo')
            parser = argparse.ArgumentParser()
            parser.add_argument("--list", nargs='?', help="list of all tasks", const='list')  # nargs=? 0 or 1 argument
            parser.add_argument("--create", nargs='?', help="create new task", const=True)
            parser.add_argument("--edit-title", dest='argument_title', nargs='*',
                                help="edit task name")  # dest=another name
            parser.add_argument("--edit-status", dest='argument_status', nargs='*',
                                help="edit task status :-complete/incomplete")  # nargs=* 1 or more argument
            parser.add_argument("--edit-task", dest='argument_task', nargs='*',
                                help="edit task name , mark as completed")
            parser.add_argument("--delete", nargs='?', help="delete task", const=True)
            parser.add_argument("--search", nargs='?', help="search task")
            parser.add_argument("--list-date", nargs='?', dest='argument_date', help="list with date", const=True)
            args = parser.parse_args()
            self.myc = self.connec.cursor()
            if args.list:  # list of all task
                if args.list == "complete":  # list of all complete task
                    self.complete()
                elif args.list == "incomplete":  # list of all incomplete task
                    self.incomplete()
                elif args.list == 'list':
                    self.list_todo()

                else:
                    print("you give wrong argument!please Enter any one from this:'complete'/'incomplete'")

            elif args.create:  # create title
                try:
                    self.create_title(args.create)
                except:
                    print("task already added in list")

            elif args.argument_title:  # edit title
                try:
                    self.edit_title(args.argument_title[0], args.argument_title[1])
                except:
                    print("task already exist")
            elif args.argument_status:  # edit task status
                self.edit_status(args.argument_status[0], args.argument_status[1])

            elif args.argument_task:  # edit task complete/incomplete
                try:
                    self.edit_task(args.argument_task[0], args.argument_task[1])
                except:
                    print("task already exist in todo try with different title")
            elif args.delete:  # delete task
                self.delete(args.delete)

            elif args.search:  # search task
                self.search_task(args.search)
            elif args.argument_date:
                self.list_date()

        except:
            print("Wrong command! use:--help for more help")
            Todo.help()
    def __del__(self):
        #self.connec.commit()
        self.connec.close()

    def help():
        print("   task               command")
        print("create title:---->--create <title>")
        print("edit-title:------>--edit-title <id> <new_task_title>")
        print("edit-status:----->--edit-status <id> <updated status>")
        print("edit-task:------->--edit-task <id> <updated title>")
        print("search task:----->--search <title>")
        print("delete task:----->--delete <id>")
        print("filter task with date:---->=--list-date")
        print("list of all task:------>--list\n    "
              "list of complete task:------>--list complete\n    "
              "list of incomplete task:---->--list incomplete")

    def create_title(self, task_title):
        sql = f"INSERT INTO todo_table (task_title,created_at) VALUES ('{task_title}','{datetime.datetime.today()}');"
        self.myc.execute(sql)
        print("New Task Successfully Created")

    def edit_title(self, id, new_task_title):
        sql = f"UPDATE todo_table SET task_title ='{new_task_title}' where task_id='{id}';"
        self.myc.execute(sql)
        print(f"title edited : New title for id {id}: '{new_task_title}'")

    def edit_task(self, id, new_task_title):
        sql = f"UPDATE todo_table SET task_title ='{new_task_title}' where task_id='{id}';"
        self.myc.execute(sql)
        sql = f"UPDATE todo_table SET status ='complete' where task_id='{id}';"
        self.myc.execute(sql)
        sql = f"UPDATE todo_table SET completed_at='{datetime.datetime.today()}' where task_id='{id}';"
        self.myc.execute(sql)
        print(f"Task edited and mark as COMPLETED :New task title --->{new_task_title}")

    def edit_status(self, id, new_task_status):
        sql = f"UPDATE todo_table SET status ='{new_task_status}' where task_id='{id}';"
        self.myc.execute(sql)
        if new_task_status == "complete":
            sql = f"UPDATE todo_table SET completed_at='{datetime.datetime.today()}' where task_id='{id}';"
            self.myc.execute(sql)
        else:
            sql = f"UPDATE todo_table SET completed_at=NULL where task_id='{id}';"
            self.myc.execute(sql)
        print(f"task edited :new task status--->{new_task_status}")
    def search_task(self, task_title):
        sql = f"select * from todo_table where task_title='{task_title}'"
        self.myc.execute(sql)
        not_found = True
        for i in myc:
            print(f"task for {task_title} found:")
            print(i)
            not_found = False
        if not_found:
            print(f"task title {task_title}: Not found")

    def delete(self, id):
        self.myc.execute(f"select * from todo_table where task_id='{id}';")
        found = False
        for i in myc:
            print("deleted task :")
            print(i)
            found = True
        if found:
            sql = f"DELETE FROM todo_table where task_id='{id}';"
            self.myc.execute(sql)
        else:
            print("task already deleted or task not exist")

    def list_todo(self):
        print("list of all task :")
        sql = "select * from todo_table"
        self.myc.execute(sql)
        no = 1
        for i in myc:
            print(no, "-", i)
            no = no + 1
        if no == 1:
            print("there are no task")

    def complete(self):
        print("complete task :")
        sql = "select * from todo_table where status='complete'"
        self.myc.execute(sql)
        no = 1
        for i in myc:
            print(no, "-", i)
            no = no + 1
        if no == 1:
            print("there are no complete task")

    def incomplete(self):
        print("incomplete task :")
        sql = "select * from todo_table where status='incomplete'"
        self.myc.execute(sql)
        no = 1
        for i in myc:
            print(no, "-", i)
            no = no + 1
        if no == 1:
            print("there are no incomplete task")

    def list_date(self):
        sql = "select task_title,created_at,completed_at from todo_table"
        self.myc.execute(sql)
        no = 1
        for i in myc:
            print(no, "-", i)
            no = no + 1
        if no == 1:
            print("there are no task")


if __name__ == '__main__':
    todo1 = Todo()
    del todo1
