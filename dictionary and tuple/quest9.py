oldAge1={"name": "Aayush", "age": 24}
oldAge2={"name": "Aayush"}
def oldAge(d):
    if "age" in d:
        age=d['age']+50
        return age
    else:
        return 50
print(oldAge(oldAge1))
print(oldAge(oldAge2))