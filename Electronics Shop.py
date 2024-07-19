def get_money_spent(keyboards, drives, b):
    max_spent = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                max_spent = max(max_spent, keyboard + drive)
    return max_spent

if __name__ == "__main__":
    b = 60
    keyboards = [40, 50, 60]
    drives = [5, 8, 12]
    print(get_money_spent(keyboards, drives, b))
