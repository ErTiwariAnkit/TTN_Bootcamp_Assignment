class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def __str__(self):
        return self.email
user1=User("amit","amit.dubey@tothenew.com")
print(user1)
#user2=User()
#user3=User()
#user4=User()