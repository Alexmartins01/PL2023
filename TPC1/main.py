def read_file():
    d = dict()
    f = open("myheart.csv")
    i = 0
    for line in f:
        if i != 0:
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
            if d[key][5] == "1\n":
                disease_m += 1
        if d[key][1] == "F":
            female += 1
            if d[key][5] == "1\n":
                disease_f += 1
    print("M:" + str(disease_m) + " doentes em " + str(male) + " individuos")
    print("F:" + str(disease_f) + " doentes em " + str(female) + " individuos")


def get_old(d):
    old = 0
    for key in d.keys():
        if int(d[key][0]) > old:
            old = int(d[key][0])
    return int(old)


def get_age(d, a):
    count = 0
    for key in d.keys():
        if (int(d[key][0]) >= a) and (int(d[key][0]) < a + 5):
            count += 1
    return count


def get_age_affected(d, a):
    count = 0
    for key in d.keys():
        if (int(d[key][0]) >= a) and (int(d[key][0]) < a + 5) and (int(d[key][5]) == 1):
            count += 1
    return count


def range_age(d):
    d_total = dict()
    d_affected = dict()
    old = get_old(d)
    i = 30
    while i in range(30, old):
        d_total[i] = get_age(d, i)
        d_affected[i] = get_age_affected(d, i)
        i += 5
    for key in d_total.keys():
        print("Idade - [" + str(key) + "," + str(key + 4) + "]: " + str(d_total[key]) + " individuos entre eles " + str(
            d_affected[key]) + " afetados")


def limits_col(d):
    lim = [9999, 0]
    for key in d.keys():
        if int(d[key][3]) > int(lim[1]):
            lim[1] = d[key][3]
        if int(lim[0]) > int(d[key][3]) > 70:
            lim[0] = d[key][3]
    return lim


def get_col(d, a):
    count = [0, 0]
    for key in d.keys():
        if (int(d[key][3]) >= a) and (int(d[key][3]) < a + 10):
            count[0] += 1
            if int(d[key][5]) == 1:
                count[1] += 1
    return count


def range_col(d):
    lim = limits_col(d)
    maxi = int(lim[1])
    mini = 0
    while mini < int(lim[0]):
        mini += 10
    mini -= 10
    d_total = dict()
    d_affected = dict()
    i = mini
    while i in range(mini, maxi):
        col = get_col(d, i)
        d_total[i] = col[0]
        d_affected[i] = col[1]
        i += 10
    for key in d_total.keys():
        print("Colestrol - [" + str(key) + "," + str(key + 9) + "]: " + str(d_total[key]) + " individuos, entre eles " +
              str(d_affected[key]) + " afetados")


def main():
    d = read_file()
    print("Distribuição baseada no sexo")
    dist_sex(d)
    print("Distribuição baseada em escalões etários")
    range_age(d)
    print("Distribuição baseada no colestrol")
    range_col(d)


if __name__ == "__main__":
    main()
