def find(num):
    result = [num]
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            result.append(i)
            result.append(num//i)
    return result

def check(lst, num):
    for l in lst:
        if l % num:
            return False
    return True

def solution(arrayA, arrayB):
    A, B = min(arrayA), min(arrayB)
    a, b = find(A), find(B)
    a.sort(reverse=True)
    b.sort(reverse=True)
    lst=[]

    for num in a:
        if not check(arrayA, num):
            continue
        
        for n in arrayB:
            if not n % num:
                break
        else:
            lst.append(num)

    for num in b:
        if not check(arrayB, num):
            continue
            
        for n in arrayA:
            if not n % num:
                break
        else:
            lst.append(num)
            
    return max(lst) if lst else 0