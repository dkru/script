#!/usr/bin/python3

import pandas as ps

remains_by_shop = ps.read_excel('remains_by_shop.xlsx', 'Sheet1')
remains_all = ps.read_excel('remains_all.xlsx', 'Sheet1')

id_by_shop = remains_by_shop['Штрихкод'].to_list()
id_all = remains_all['Штрихкод'].to_list()
for i, el in enumerate(id_by_shop):
    if id_all[i] != el:
        print(el)
        break
