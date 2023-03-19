import re
from sys import stdin


d = dict()


def price(num):
    if re.match(r'601|641', num):
        return -1
    elif re.match(r'00', num):
        return 150
    elif re.match(r'2', num):
        return 25
    elif re.match(r'800', num):
        return 0
    elif re.match(r'808', num):
        return 10


def parser(action, dic):
    res = list()
    if re.match(r'LEVANTAR', action):
        dic["estado"] = 1
        res.append(1)
    elif re.match(r'POUSAR', action):
        dic["estado"] = 0
        res.append(0)
    elif re.match(r'MOEDA (\d+(c|e)(, |.))+', action) and dic["estado"] == 1:
        cents = re.findall(r'\d+c', action)
        euros = re.findall(r'\d+e', action)
        for coin in cents:
            cent = re.match(r'\d+', coin)
            dic["saldo"] += int(cent.group(0))
        for coin in euros:
            euro = re.match(r'\d+', coin)
            dic["saldo"] += 100 * int(euro.group(0))
        res.append(2)
    elif re.match(r'T=(\d+)', action) and dic["estado"] == 1:
        number = re.match(r'T=(00\d+|\d{9})', action)
        pay = price(number.group(1))
        if not pay == -1:
            dic["used"] = pay
        res.append(3)
        res.append(pay)
    elif re.match(r'ABORTAR', action):
        dic["estado"] = 0
        res.append(4)
    return res


for line in stdin:
    d.setdefault("estado", 0)
    d.setdefault("saldo", 0)
    d.setdefault("used", 0)
    ret = parser(line, d)
    if len(ret) > 1:
        if ret[1] == -1:
            print("Esse número não é permitido neste telefone. Queira discar novo número!")
        elif d["saldo"] < d["used"]:
            print("Saldo insuficiente!")
        else:
            d["saldo"] -= d["used"]
            print(d["saldo"])
    elif len(ret) == 1:
        if ret[0] == 0 or ret[0] == 4:
            me = d["saldo"]//100
            mc = d["saldo"] - me * 100
            print("Troco=" + str(me) + "e" + str(mc) + "c. Volte sempre!")
            d["saldo"] = 0
            d["used"] = 0
        elif ret[0] == 3:
            print(d["saldo"])
        elif ret[0] == 1:
            print("Introduza moedas")
        elif ret[0] == 2:
            print(d["saldo"])
