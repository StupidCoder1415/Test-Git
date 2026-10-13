with open('file1.txt', encoding='utf-8') as f:
    lines = [line.rstrip('\n').split('\t') for line in f]

data = {}
for a in lines:
    a = (a + ['NONE'] * 3)[:3]
    if a[0] in data:
        data[a[0]] = a
    else:
        data[a[0]] = a

with open('file2.txt', encoding='utf-8') as f:
    ids = [line.strip() for line in f if line.strip()]

found = [data[x] for x in ids if x in data]
notfound = [x for x in ids if x not in data]

with open('B24DCCN468_result.txt', 'w', encoding='utf-8') as f:
    seen = set()
    for a in found:
        if a[0] not in seen:
            f.write('\t'.join(a) + '\n')
            seen.add(a[0])

with open('B24DCCN468_notfound.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(notfound))

with open('B24DCCN468_report.txt', 'w', encoding='utf-8') as f:
    f.write(f'Tong so ho so: {len(lines)}\n')
    f.write(f'So ban ghi trung: {len(lines) - len(data)}\n')
    f.write(f'So ma tim thay: {len(set(ids) & set(data))}\n')
    f.write(f'So ma khong tim thay: {len(set(notfound))}\n')