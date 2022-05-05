def mysum(n):
    print(n*(n+1)/2)

a = int(input("자연수를 입력해주세요: "))
mysum(a)

###

text = input("단어를 입력해주세요: ").lower()
print("a는",text.count('a'),"개 포함되어 있습니다.")
print("e는",text.count('e'),"개 포함되어 있습니다.")
print("i는",text.count('i'),"개 포함되어 있습니다.")
print("o는",text.count('o'),"개 포함되어 있습니다.")
print("u는",text.count('u'),"개 포함되어 있습니다.")

###

sentence = input("문장을 입력해주세요: ")
stc_list = sentence.split(' ')
print("단어는", len(stc_list), "개 입니다.")

###

num_list = []

while True:
    num = input("숫자를 입력해주세요 (그만하려면 q): ")
    if num == 'q':
        break
    else:
        num_list.append(int(num))

sort_list = sorted(num_list)
min_num = sort_list[0]
max_num = sort_list[-1]

print(len(num_list),"개의 숫자 중 최솟값은", num_list.index(min_num)+1, "번째 수", min_num, "입니다.")
print(len(num_list),"개의 숫자 중 최댓값은", num_list.index(max_num)+1, "번째 수", max_num, "입니다.")

###

import math

H = int(input("나무 막대의 높이 H를 입력해주세요: "))
X = int(input("낮 동안 올라가는 높이 X를 입력해주세요: "))
Y = int(input("밤 동안 미끄러지는 높이 Y를 입력해주세요: "))

print("달팽이는", math.ceil(H/(X-Y)), "일 후에 정상에 도달할 수 있겠네요!")