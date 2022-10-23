def solution(survey, choices):
    score = {"R": 0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i in range(len(survey)):
        if choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 5:
            score[survey[i][1]] += 1
        elif choices[i] == 6:
            score[survey[i][1]] += 2
        elif choices[i] == 7:
            score[survey[i][1]] += 3
    
    answer = ''
    print(score)
    
    if score["R"] == score["T"]:
        answer += "R"
    elif score["R"] > score["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if score["C"] == score["F"]:
        answer += "C"
    elif score["C"] > score["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if score["J"] == score["M"]:
        answer += "J"
    elif score["J"] > score["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if score["A"] == score["N"]:
        answer += "A"
    elif score["A"] > score["N"]:
        answer += "A"
    else:
        answer += "N"
        
    
    return answer