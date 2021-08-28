#1到100 的偶数he

'''

sum=0
i=0
while i<=100:
    sum+=i
    i+=2
print(sum)
'''


sum=0
i=1
while i<=100:
    if not i%2:
        sum=sum+i
    i=i+1
print(sum)