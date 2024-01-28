# 유닉스 타임과 while 반복문을 조합하면 특정 시간 동안 프로그램을 정지시킬 수 있다
# 시간과 관련된 기능을 가져옵니다.
import time

# 변수를 선언합니다.
number = 0

# 5초동안 반복합니다.
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))