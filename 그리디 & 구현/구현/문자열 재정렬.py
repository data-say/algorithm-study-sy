## 문자열 재정렬
"""
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로
정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다
"""

# 아이디어: 구현

import re
def solution(s):
    string = re.findall('(?i)[A-Z]', s)
    num = re.findall('(?i)[0-9]', s)

    string.sort()
    nums = sum(map(int, num))

    return ''.join(string) + str(nums)

if __name__ == '__main__':
    print(solution("K1KA5CB7"))
