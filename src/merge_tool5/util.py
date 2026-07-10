def remove_duplicates(sub):
    b = []

    for ch in sub:
        if ch not in b:
            b.append(ch)

    return "".join(b)