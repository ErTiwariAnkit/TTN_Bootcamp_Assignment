oldAge1={"name": "Aayush", "age": 24}
oldAge2={"name": "Aayush"}
def oldAge(d):
    if "age" in d:
        age=d['age']+50
        print(age)
    else:
        print("50")
oldAge(oldAge1)
oldAge(oldAge2)