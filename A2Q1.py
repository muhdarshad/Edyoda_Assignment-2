string1 = "Python is a high level programming language"
list1 =[]
list1 = string1.split(' ')
string2 = []

for i in range(len(list1)):
    string2 = list1[i]  
    print(string2[0].upper(),end='')

    if len(list1[i])==1:
        print(end=' ')
        continue
    
    print(string2[1:-1],end='')
    print(string2[-1].upper(),end=' ')