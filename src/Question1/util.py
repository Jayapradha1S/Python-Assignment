def execute(list, st):
    strl = st.split()
    a = strl[0]

    match(a):
        case "append":
            list.append(int(strl[1]))
        case "insert":
            list.insert(int(strl[1]), int(strl[2]))
        case "pop":
            list.pop()
        case "sort":
            list.sort()
        case "reverse":
            list.reverse()
        case "remove":
            list.remove(int(strl[1]))
        case "print":
            print(list)
