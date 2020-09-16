def solve(people,length):
    flag=True;
    for i in people :
        if flag:
            flag=False;
            print(i)
            end=i+length;
        elif i>end :
            print(i)
            end=i+length;

people=[]
length=input()
num_elements=int(input())
for i in range(1,num_elements+1):
    people.append(int(input()))

people.sort();
solve(people,int(length))
