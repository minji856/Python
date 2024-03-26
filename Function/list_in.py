# 리스트 내포
# 최종 결과를 앞에 작성 (i*i)
# [ 표현식 for 반복자 in 반복할 수 있는 것 (if 조건문)]
array = [i*i for i in range(0, 20, 2)]
print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if  fruit != "초콜릿"]
# print(array)하면 초콜릿 표함 된 채로 출력됨
print(output)