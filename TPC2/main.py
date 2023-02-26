def on_off(v, i):
    if v[i + 1] == 'N' or v[i + 1] == 'n':
        return 1
    if v[i + 1] == 'F' or v[i + 1] == 'f':
        if v[i + 2] == 'F' or v[i + 2] == 'f':
            return -1
    return 0


def calc_digit(v, i):
    res = 0
    aux = 0
    for c in v:
        if c.isdigit() and aux >= i:
            res = res*10 + int(c)
        elif aux > i:
            return res
        aux += 1
    return res


def main():
    val = input("Enter input string: ")
    i = 0
    state = 1
    new_state = 0
    res = 0
    buffer = 0
    for c in val:
        if c.isdigit() and state == 1 and buffer == 0:
            res += calc_digit(val, i)
            buffer = 1
        elif not c.isdigit():
            buffer = 0

        if c == 'o' or c == 'O':
            new_state = on_off(val, i)
            if new_state != 0:
                state = new_state
        if c == '=':
            print(res)
        i += 1


if __name__ == '__main__':
    main()
