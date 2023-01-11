def solution(today, terms, privacies):
    answer = []
    y,m,d = today.split('.')
    today = int(y)*12*28 + int(m)*28 + int(d)

    terms = {i[:1]:int(i[2:])*28 for i in terms}

    for i,p in enumerate(privacies):
        y,m,d = p.split('.')
        d,c = d.split()
        p = int(y)*12*28 + int(m)*28 + int(d)

        if p+terms[c] <= today:
            answer.append(i+1)

    return answer