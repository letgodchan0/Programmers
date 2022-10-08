def solution(cards):
    check = []
    res = []
    for card in cards:
        cnt = 0
        if card not in check:
            while True:
                if card in check:
                    break
                check.append(card)
                idx = card - 1
                card = cards[idx]
                cnt += 1
        res.append(cnt)
    res.sort()
    return res[-1] * res[-2]
