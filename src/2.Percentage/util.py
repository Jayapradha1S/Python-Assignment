def average(dt, name):
    for key1, values in dt.items():
        if name == key1:
            s = sum(values)
            avg = s / len(values)
            print(f"{avg:.2f}")