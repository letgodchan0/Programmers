from collections import Counter
import math
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    
    lst1, lst2 = [], []
    
    for i in range(1, len(str1)):
        tmp = str1[i-1:i+1]
        if 97 <= ord(tmp[0]) <= 122 and 97 <= ord(tmp[1]) <= 122:
            lst1.append(tmp)
        
    for i in range(1, len(str2)):
        tmp = str2[i-1:i+1]
        if 97 <= ord(tmp[0]) <= 122 and 97 <= ord(tmp[1]) <= 122:
            lst2.append(tmp)

    counter1, counter2 = Counter(lst1), Counter(lst2)
    _share, _sum = 0, 0

    for key in counter1.keys():
        if key in counter2.keys():
            _share += min(counter1.get(key), counter2.get(key))
    
    check = set()
    for string in lst1+lst2:
        check.add(string)
    
    for c in check:
        _sum += max(counter1.get(c, 0), counter2.get(c, 0))
    
    if _share == 0 and _sum == 0:
        return 1 * 65536
    answer = (_share / _sum) * 65536
    return math.trunc(answer)