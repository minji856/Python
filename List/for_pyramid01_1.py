# 문자열*연산자로 피라미드 만들기
# 문자열 초기화
output = ""

for i in range(1, 10):
    # i값에 해당하는 개수만큼 별표를 생성하여 추가함
    output += ("*" * i)
    output += "\n"

print(output)