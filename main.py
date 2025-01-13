def change_caps(word):
    s = ""
    for i in range(len(word)):
        if i % 2 == 1:
            s += word[i].lower()
        else:
            s += word[i].upper()
    print(s)
change_caps("hello")