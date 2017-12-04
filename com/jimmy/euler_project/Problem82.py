# http://www.javashuo.com/content/p-4338566.html
ls = []
for line in open("p81-82-83_matrix.txt"):
    # print(line)
    a = line.split(',')
    a = [int(i) for i in a]
    ls.append(a)

ans = [ls[i][79] for i in range(80)]

print(ans)

for i in range(78, -1, -1):
    ans[0] = ans[0] + ls[0][i]

    # 向下
    for j in range(1, 80):
        ans[j] = min(ans[j] + ls[j][i], ans[j - 1] + ls[j][i])

    # 向上
    for j in range(78, -1, -1):
        ans[j] = min(ans[j], ans[j + 1] + ls[j][i])

print(min(ans))
