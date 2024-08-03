def minmax(a,i,j):
    if i==j:
        return a[i],a[j]
    elif i==0 and j==i+1:
        if a[i]<a[j]:
            return a[i],a[j]
        else:
            return a[j],a[i]
    else:
        mid=(i+j)//2
        min1,max1=minmax(a,i,mid)
        min2,max2=minmax(a,mid+1,j)
        final_min=min(min1,min2)
        final_max=max(max1,max2)
    return final_min,final_max
a=[33,22,77,55,99]
i=0
j=len(a)-1
min_val=999999
max_val=0
print(minmax(a,i,j))
