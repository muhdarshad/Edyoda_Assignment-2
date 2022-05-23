vowels = ['a','e','i','o','u']
string = str(input("Enter string : "))
count = 0
for i in range(len(string)):
    for j in range(len(vowels)):
        if string[i].lower() == vowels[j]:
            count += 1
print("Vowels : ",count)