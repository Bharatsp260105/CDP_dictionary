a={"name":"rahul","age":"18","mob_no":"1234567890"}

print(a)

for y in a:
    print(y)

for x,y in a.items():
    print(x,y)

# ---------------------------------------------------------------
current_dict={
    
    "brand":"BMW",
    "model":"I20",
    "year":"2024",
    "colour":["red","blue"]
}
if "model" in current_dict:
    print("Yes")
    
print((current_dict))

for x in current_dict:
    print(x)
    
for x,y in current_dict.items():
    print(x,y)
    
# ------------------------------------------------
user_dict={}
while True:
    key=input("Enter a key :")
    value=input("Enter a value:")
    user_dict.update({key:value})
    
    check=input("want to add one more pair?(y/n):")
    if check=="n":
        break
    
print(user_dict)
