def primes(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    return flag

n,m=input().split()
m=int(m)
n=int(n)
prime1=[]

for i in range(n,m+1):
    if primes(i)==0:
        prime1.append(i)

print(prime1)

prime2=[]
for i in range(0,len(prime1)):
    for j in range(0,len(prime1)):
        cross=int(str(prime1[i])+str(prime1[j]))
        if i!=j and primes(cross)==0:
            prime2.append(cross)

prime3=[]
prime3=list(set(prime2))
#print(prime3)
num1=min(prime3)
num2=max(prime3)

for i in range(len(prime3)-2):
    sum=num1+num2
    num1=num2
    num2=sum

print(sum,end="")