string = str(input("Enter your string : "))
flag=0
for i in range(len(string)):
    if (ord(string[i])>=65 and ord(string[i])<=90) or (ord(string[i])>=97 and ord(string[i])<=122) or (ord(string[i])==32):
        continue
    else :
        flag = 1

if flag==1:
    print("String not accepted")
else:
    print("String is accepted")     