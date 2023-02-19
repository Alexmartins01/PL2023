def read_file():
    d = dict()
    f = open("myheart.csv")
    i = 0
    for line in f:
        d[i] = line.split(",")
        i += 1
    return d


def dist_sex(d):
    male = 0
    female = 0
    disease_m = 0
    disease_f = 0
    for key in d.keys():
        if d[key][1] == "M":
            male += 1
            if d[key][5] == "1":
                disease_m += 1
        if d[key][1] == "F":
            female += 1
            if d[key][5] == "1":
                disease_f += 1
    print("M:" + disease_m + " doentes em " + male + " individuos")
    print("F:" + disease_f + " doentes em " + female + " individuos")


def get_old(d):
    old = 0
    for key in d.keys():
        if d[key][0] > old:
            old = d[key][0]
    return old


def get_range(d, a):
    count = 0
    for key in d.keys():
        if (d[key][0] >= a) and (d[key][0] < a + 5):
            count += 1
    return count


def dist_esc(d):
    d_aux = dict()
    old = get_old(d)
    for i in range(30, old):
        d_aux[i] = get_range(d, i)
        i += 5
    for key in d_aux.keys():
        print("[" + key + "," + key + 5 + "]: " + d_aux[key])
