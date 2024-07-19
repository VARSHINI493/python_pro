def climbing_leaderboard(scores, alice):
    scores = sorted(set(scores), reverse=True)
    result = []
    l = len(scores)
    for a in alice:
        while l > 0 and a >= scores[l-1]:
            l -= 1
        result.append(l + 1)
    return result

if __name__ == "__main__":
    scores = [100, 90, 90, 80]
    alice = [70, 80, 105]
    print(climbing_leaderboard(scores, alice))
