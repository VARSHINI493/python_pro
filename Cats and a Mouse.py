def cat_and_mouse(x, y, z):
    cat_a_dist = abs(x - z)
    cat_b_dist = abs(y - z)
    if cat_a_dist < cat_b_dist:
        return "Cat A"
    elif cat_b_dist < cat_a_dist:
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == "__main__":
    x = 1
    y = 2
    z = 3
    print(cat_and_mouse(x, y, z))
