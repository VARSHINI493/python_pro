def picking_numbers(a):
    from collections import Counter
    frequency = Counter(a)
    max_count = 0
    for number in frequency:
        max_count = max(max_count, frequency[number] + frequency[number + 1])
    return max_count

if __name__ == "__main__":
    a = [4, 6, 5, 3, 3, 1]
    print(picking_numbers(a))
