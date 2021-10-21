import csv
from io import FileIO

l = []
with open('business-price-indexes.csv', 'r') as file:
    datas = csv.DictReader(file)
    for row in datas:
        # print(row)
        l.append(row)

with open('data.csv', 'w') as file:
    data = csv.DictWriter(file, fieldnames=["Series reference","Description","Period","Previously published","Revised"])
    data.writeheader()
    for i in l:
        data.writerow(i)

with open('data.csv', 'r') as file:
    data = list(csv.DictReader(file))
    l = []
    for i in data:
        for key, val in i.items():
            if key == 'Revised':
                l.append(int(val))
                # if val == '1603':
                #     print(i)
    l_max = max(l)
    print(l_max)
    

