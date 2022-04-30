lst = input().split("-")
answer = 0

for i in lst[0].split("+"):
    answer += int(i)

for i in lst[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)

## -로 나눠지는 부분에서 최대한 많이 괄호를 반영한다.
## 시간복잡도: O(n)