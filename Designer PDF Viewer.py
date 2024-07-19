def designer_pdf_viewer(h, word):
    max_height = max(h[ord(c) - ord('a')] for c in word)
    return max_height * len(word)

if __name__ == "__main__":
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    word = "abc"
    print(designer_pdf_viewer(h, word))
