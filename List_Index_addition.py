# input=[[25, 33, 45], [13, 47, 9], [34, 32, 28]]
# output=[72, 112, 82]


n=[[25, 33, 45], [13, 47, 9], [34, 32, 28]]
result=[]
for i in range(len(n)):
    sum=0
    for j in range(len(n[i])):
        sum+=n[j][i]
    result.append(sum)

print(result)