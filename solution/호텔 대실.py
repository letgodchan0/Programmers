def solution(book_time):
    book_time.sort(key = lambda x: (x[0], x[1]))
    for i in range(len(book_time)):
        book_time[i][0] = int(book_time[i][0][:2])*60 + int(book_time[i][0][3:])
        book_time[i][1] = int(book_time[i][1][:2])*60 + int(book_time[i][1][3:])
    
    stack = []
    stack.append(book_time[0])

    for i in range(1, len(book_time)):
        for j in range(len(stack)):
            start, end = stack[j]
            if book_time[i][0] >= end + 10:
                stack[j] = book_time[i]
                break
        else:
            stack.append(book_time[i])
                
    return len(stack)