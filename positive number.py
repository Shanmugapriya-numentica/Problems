


user=input("Enter values: ")    #"-14 4 5 -2 76"
s= user.split()
t =0 
newarr=[]

for i in s:
    t= int(i)
    if t >0:
        newarr.append(t)
    elif t <= 0:
        pass
print("Positive numbers are: ", newarr)
    







