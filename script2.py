print("Hello there ")
print("<-------------------------------------->")
#reverse:
str="ytreza"
s=""
for i in range(len(str)):
   s += str[len(str)-i-1 : len(str)-i]
   print(s) 

print("<-------------------------------------->")
def stars():
    x = input("how many stars you want ?")
    s=''
    output=''
    for i in range(int(x)) :
        s += 'x'
        if (len(s) <= int(x)) :
            output += s[len(s) - (i+1) : len(s) - i]
        # print(f"{output} [{len(str) - (i+1)}:{len(str) - i}]")
        print(output)

stars()