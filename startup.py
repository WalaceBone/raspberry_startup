import re


def parse_line(line):
    properties = open("startup.properties", "r")
    l = line.split('=')
    for p in properties:
        p = p.split("=")
        if p[0] == l[0]:
            p[1] = p[1].replace('\r\n', '')
            line = re.sub("(?<=\")(?P<value>.*?)(?=\")", p[1], line)

    properties.close()
    return line


def startup():
    wpa_conf = open("wpa_supplicant.conf", "w+")
    wpa_template = open("wpa_supplicant.conf.template", "r")

    for line in wpa_template:
        l = line.split('=')
        if len(l) > 1:
            wpa_conf.write(parse_line(line))
        else:
            wpa_conf.write(line)

    wpa_conf.close()
    wpa_template.close()


if __name__ == '__main__':
    startup()
