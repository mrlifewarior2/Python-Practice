#Smallest divisible no.

N = int(input("Enter No:"))
f = 0
No = N+1
while(f != 1):
    for i in range(2, N+1):
        if No % i == 0:
            f = 1
        else:
            f = 0
            No = No + 1
            break

print("Divisible No==",No)


