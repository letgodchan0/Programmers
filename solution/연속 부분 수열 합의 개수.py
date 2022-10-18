def solution(elements):
    new_elements = elements + elements
    result = []
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            add = sum(new_elements[j:j+i])
            result.append(add)

    return len(set(result))