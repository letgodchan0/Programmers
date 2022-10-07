def solution(tickets):
    check = {}
    for ticket1, ticket2 in tickets:
        check[ticket1] = check.get(ticket1, []) + [ticket2]
    for city in check.keys(): check[city].sort(reverse = True)


    stack = ["ICN"]
    res = []
    while stack:

        city = stack[-1]
        if not check.get(city) or not len(check[city]):
            res.append(stack.pop())
        else:
            stack.append(check[city].pop())
            
    return res[::-1]
