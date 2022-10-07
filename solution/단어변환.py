from collections import deque

def solution(begin, target, words):
    q = deque([])
    q.append((begin, 0))
    visited = [0] * len(words)
    while q:
        word, answer = q.popleft()
        if word == target:
            return answer
        for w in words:
            cnt = 0
            word_check = sorted(word)
            w_check = sorted(w)
            for i in range(len(word)):
                if word[i] != w[i]:
                    cnt += 1
            idx = words.index(w)
            if cnt == 1 and not visited[idx]:
                q.append((w, answer + 1))
                visited[idx] = 1
            
    return 0