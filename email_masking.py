import re
with open(r"C:\Users\admin\Downloads\contacts_100k.txt","r") as file:
    text=file.read()
    #print(text)
original_email=re.findall("[\w]+[@]+[\w]+[.][\w]+",text)
email=original_email
print("Original_Email  ")
for email in original_email:
    result=re.sub(r"[\w]+[@]+[\w]+[.][\w]+","xxxxxxxxx",email)
    print(f"{email}:{result}")