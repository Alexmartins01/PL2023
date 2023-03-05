# Pasta | Data | Nome | Pai | Mãe | Observações
import re


def get_freq_year(d):
    fd = dict()
    for key in d.keys():
        data = re.split(r'-', d[key][1])
        if data[0] in fd.keys():
            fd[data[0]] += 1
        else:
            fd[data[0]] = 1
    return fd


def name_freq(d, name):
    namep = name[0]
    namel = name[-1]
    if namep in d.keys():
        d[namep] += 1
    else:
        d[namep] = 1
    if namel in d.keys():
        d[namel] += 1
    else:
        d[namel] = 1
    return d


def get_name_cent(d):
    sd = dict()
    for key in d.keys():
        data = re.split(r'-', d[key][1])
        new = int(data[0]) // 100
        if new in sd.keys():
            sd[new] = name_freq(sd[new], re.split(r' ', d[key][2]))
        else:
            sd[new] = {d[key][2]: 1}
    return sd


def max_freq(d):
    chave = ""
    maxi = 0
    for key in d.keys():
        if d[key] > maxi:
            chave = key
            maxi = d[key]
    return chave, maxi


def fam_freq(d):
    fd = dict()
    fd["tio"] = 0
    fd["irmao"] = 0
    times = 0
    for key in d.keys():
        times = len(re.findall(r"(?i:tio)", d[key][5]))
        fd["tio"] += times
        times = len(re.findall(r"(?i:irmao)", d[key][5]))
        fd["irmao"] += times
    return fd


def main():
    d = dict()
    f = open("processos.txt")
    i = 0
    for line in f:
        if line != "\n":
            pasta, data, nome, pai, mae, obs, last = re.split(r'::', line)

            d[i] = (int(pasta), data, nome, pai, mae, obs)
            i += 1
    fd = get_freq_year(d)
    sd = get_name_cent(d)
    fam = fam_freq(d)
    print(fd)
    print("----------------------------------------")
    for key in sd.keys():
        i = 0
        print("------ Sec " + str(key) + " ------")
        for i in range(0, 5):
            maxi = max_freq(sd[key])
            print("|" + str(maxi) + "|")
            del sd[key][maxi[0]]
        print("--------------------")
    print("----------------------------------------")
    print(fam)


if __name__ == "__main__":
    main()
