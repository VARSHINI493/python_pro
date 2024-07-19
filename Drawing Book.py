def page_count(n, p):
    return min(p // 2, (n // 2 - p // 2))

if __name__ == "__main__":
    n = 6
    p = 2
    print(page_count(n, p))
