from datetime import datetime


class MT:
    def __init__(self, code, name, method):
        self.code = code
        self.name = name
        self.method = method


class CA:
    def __init__(self, i, date, time, room):
        self.code = f'C{i:03d}'
        self.strdate = date
        self.strtime = time
        self.date = datetime.strptime(
            f'{date} {time}', '%d/%m/%Y %H:%M'
        )
        self.room = room


class SCHE:
    def __init__(self, ca, mt, group, num):
        self.ca = ca
        self.mt = mt
        self.group = group
        self.num = num

    def __str__(self):
        return (
            f'{self.ca.strdate} {self.ca.strtime} '
            f'{self.ca.room} {self.mt.name} '
            f'{self.group} {self.num}'
        )


with open('MONTHI.in') as f:
    n = int(f.readline())
    mon_thi = {}

    for _ in range(n):
        mt = MT(f.readline().strip(),
                f.readline().strip(),
                f.readline().strip())
        mon_thi[mt.code] = mt


with open('CATHI.in') as f:
    m = int(f.readline())
    ca_thi = {}

    for i in range(1, m + 1):
        ca = CA(i, f.readline().strip(),
                f.readline().strip(),
                f.readline().strip())
        ca_thi[ca.code] = ca


with open('LICHTHI.in') as f:
    k = int(f.readline())
    lich_thi = []

    for _ in range(k):
        ma_ca, ma_mt, nhom, so_sv = f.readline().split()
        lich_thi.append(
            SCHE(ca_thi[ma_ca], mon_thi[ma_mt], nhom, so_sv)
        )


lich_thi.sort(key=lambda x: (x.ca.date, x.ca.code))

for lich in lich_thi:
    print(lich)