from itertools import product
def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    
    discount = [40, 30, 20, 10]
    discounts = product(discount, repeat=m)
    
    answer = []
    for discount in discounts:
        total, cnt = 0, 0
        for user in users:
            user_total = 0
            for i in range(len(discount)):
                if user[0] <= discount[i]:
                    user_total += int((100 - discount[i]) * 0.01 * emoticons[i])

            # 이모티콘 사야함
            if user_total < user[1]:
                total += user_total
            else:
                cnt += 1
                
        answer.append((cnt, total))
                
            
    answer.sort(key = lambda x : (-x[0], -x[1]))
            
    return answer[0]