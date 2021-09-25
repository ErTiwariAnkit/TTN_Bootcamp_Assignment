str1="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
dict1={}
for i in str1:
    if i!=" ":
        if i in dict1:
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1

print("number of occurances of each character")
print(dict1)
temp=-1
key=-1
for i in dict1:
    if dict1[i]>temp:
        temp=dict1[i]
        key=i
print("character with most number of occurances")
print([key,temp])
