import re
import json


def headers(line):
    header = re.split(r',', line)
    final = list()
    border = list()
    i = 0
    fill = False
    for campo in header:
        new_campo = re.match(r'\w+', campo)
        new_border = re.search(r'\d+', campo)
        if new_border:
            if not fill:
                border.append(i)
                fill = True
            border.append(new_border.group(0))
        if new_campo:
            if re.match(r'\D+', campo):
                final.append(new_campo.group(0))
        i += 1
    return final, border


def main():
    d = dict()
    f = open(input(), encoding='utf-8')
    h = True
    for line in f:
        line = line.strip()
        if h:
            header, border = headers(line)
            h = False
        else:
            if line:
                data = re.split(r',', line)
                i = 0
                for campo in header:
                    if len(border) == 0 or int(border[0]) != i:
                        d.setdefault(campo, list())
                        d[campo].append(data[i])
                        i += 1
                    else:
                        if len(border) == 2:
                            aux_list = list()
                            for j in range(0, int(border[1])):
                                aux_list.append(data[i+j])
                            d.setdefault(campo, list())
                            d[campo].append(aux_list)
                        if len(border) == 3:
                            print("idk")
    json_object = json.dumps(d, indent=4, ensure_ascii=False)
    encoded_output = json_object.encode('utf-8')
    decoded_output = encoded_output.decode('utf-8')
    print(decoded_output)
    with open('output.json', 'w', encoding='utf-8') as outfile:
        outfile.write(decoded_output)


if __name__ == "__main__":
    main()
