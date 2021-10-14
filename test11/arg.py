import mysql.connector
connec=mysql.connector.connect(user='root',password='password',host='localhost',database='db')
print(connec.is_connected())
sql="create table tble2 (task_id int NOT NULL AUTO_INCREMENT,task_title varchar(255),create_at date,completed_at date,status varchar(255),PRIMARY KEY (task_id))"
myc=connec.cursor()
myc.execute(sql)
for d in myc:
    print(d)
myc.close()
connec.close()
""""""
def help1():
    sa = """Usage :-
$ ./todo add "todo item" # Add a new todo
$ ./todo ls			 # Show remaining todos
$ ./todo del NUMBER	 # Delete a todo
$ ./todo done NUMBER	 # Complete a todo
$ ./todo help			 # Show usage
$ ./todo report		 # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))

    """
    f = open(f'{title}', 'a')
    f.write(s)
    f.write(" create at ")
    f.write(str(datetime.datetime.today()).split()[0])
    f.write("\n")
    f.close()
    s = '"' + s + '"'
    print(f"Added todo: {s}")"""
def edit_title(id,s):
    nec()
    f=open("todo.txt","wt")
    d.update({int(id):s})
    data=str(d)
    for i in d:
        f.write(d[i])
        f.write("\n")



def list_todo():
    print("hello")
 """myc = connec.cursor()
    sql = "show tables"
    myc = connec.cursor()
    #print("hello2")
    myc.execute(sql)

    list1=[]
    for i in myc:
        list1.append(str(i[0]))
    print("1",connec.is_connected())
    for i in list1:
        connec2 = mysql.connector.connect(user='root', password='password', host='localhost', database='db')
        myc2 = connec2.cursor()
        print("2",connec2.is_connected())
        myc2.execute(f"desc {i}")
        for j in myc2:
            print(j)
    try:
        nec()
        l = len(d)
        print(d)
        k = l
        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l - 1

    except Exception as e:
        raise e
    """
def list_complete():
    nec()
    nf=open("done.txt","r")
    print(nf.readlines())
def list_incomplete():
    nec()
    nf=open("todo.txt","r")
    print(nf.readlines())
def delete(no):
    try:
        no = int(no)
        nec()
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{no}")

    except Exception as e:
        print(f"Error: todo #{no} does not exist. Nothing deleted.")
def edit_status(no):
    try:
        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = 'x ' + str(datetime.datetime.today()).split()[0] + ' ' + d[no]
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked todo #{no} as done.completed at {datetime.datetime.today()}")

        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")
def report():
    nec()
    try:

        nf = open('done.txt', 'r')
        c = 1
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c + 1
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')
    except:
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')


def nec():
    try:
        f = open('todo.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c + 1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))