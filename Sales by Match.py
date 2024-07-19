def sock_merchant(n, ar):
    from collections import Counter
    sock_counts = Counter(ar)
    return sum(count // 2 for count in sock_counts.values())

if __name__ == "__main__":
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sock_merchant(n, ar))
