#merge two sorted array
def merge(ar1,ar2,m,n):
    for i in range(n-1,-1,-1):
        last=ar1[m-1]
        j=m-2

        while j>=0 and ar1[j]>ar2[i]:
            ar1[j+1]=ar1[j]
            j-=1
        if j!=m-2 or last>ar2[i]:
            ar1[j+1]=ar2[i]
            ar2[i]=last

        

ar1=[6,7,12,44]
ar2=[2,5,10,11]
m=len(ar1)
n=len(ar2)
merge(ar1,ar2,m,n)
print(ar1+ar2)
