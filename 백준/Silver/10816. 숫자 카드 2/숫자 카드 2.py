import sys

n = int(input())
my_list = list(map(int, sys.stdin.readline().split()))  # 상근이가 가진 카드들
m = int(input())
number_list = list(map(int, sys.stdin.readline().split()))  # 확인할 숫자들

card_count = {}  # 카드들의 개수를 저장할 딕셔너리
for card in my_list:  # 상근이가 가진 카드를 하나씩 꺼낸 후
    if card in card_count:  # 딕셔너리에 있으면
        card_count[card] += 1  # 개수 +1
    else: # 딕셔너리에 없으면
        card_count[card] = 1 # 개수 = 1

for number in number_list:  # 확인할 숫자를 하나씩 꺼내서
    if number in card_count:  # 상근이가 그 카드를 가지고 있으면
        print(card_count[number], end=" ")  # 개수 출력
    else:
        print(0, end=" ")