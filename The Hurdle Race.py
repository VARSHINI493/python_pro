def hurdle_race(k, height):
    max_height = max(height)
    return max(0, max_height - k)

if __name__ == "__main__":
    k = 4
    height = [1, 6, 3, 5, 2]
    print(hurdle_race(k, height))
