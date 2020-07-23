no=int(input("Enter No:"))
if no%2==0:
    print("no is even ")
else :
    print("no is odd")
    
fact=1
for i in range(1,no+1,1):
    fact=fact*i
    
print("factorial :",fact);
