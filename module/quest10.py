import requests
def http():
    r1=requests.get("https://httpbin.org")
    r2=requests.put("https://httpbin.org/put",data={"key":"value"})
    r3=requests.post("https://httpbin.org/post",data={"key":"value"})
    r4=requests.delete("https://httpbin.org/delete",data={"key":"value"})
    r5=requests.head("https://httpbin.org",data={"key":"value"})
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r5.headers)
http()