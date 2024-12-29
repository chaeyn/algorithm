a = []
a = list(map(int, input().split())) #고유번호 5자리를 1자리씩 나눠 a에 저장

a1 = int(a[0]*a[0]) # 각 자리수를 제곱
a2 = int(a[1]*a[1])
a3 = int(a[2]*a[2])
a4 = int(a[3]*a[3])
a5 = int(a[4]*a[4])

sum = a1 + a2 + a3 + a4 + a5

result = int(sum%10) #결과 계산

print(result)