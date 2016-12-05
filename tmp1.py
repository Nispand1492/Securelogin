def ins_sort(a) :
    i = 1
    while(i < len(a)):
        num = a[i]
        if(i==1):
            a[1]=a[i]
        else :
            j = 1
            while (a[j]< a[i]):
                j = j + 1
            index = j + 1
            k = i - 1
            while k>=j :
                a[k+1] = a[k]
                k = k - 1
            a[index] = num
        i = i + 1
    return a

n = input()
a = []

for i in range(1,int(n)):
    a.append(int(input()))

print(ins_sort(a))