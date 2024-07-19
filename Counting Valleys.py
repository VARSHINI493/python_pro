def counting_valleys(steps, path):
    sea_level = 0
    valleys = 0
    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if sea_level == 0 and step == 'U':
            valleys += 1
    return valleys

if __name__ == "__main__":
    steps = 8
    path = "UDDDUDUU"
    print(counting_valleys(steps, path))
