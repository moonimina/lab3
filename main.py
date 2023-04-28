from hash_func import simple_func, compl_func
from overloadings import Products
import pandas as pd
import time
import random
import timeit

n_ = [100, 500, 1000, 5000, 10000, 50000, 100000]
t_simple, t_compl = [], []
total_collis_simple, total_collis_compl = [], []

products = {}
for j in n_:
    d = pd.read_excel('./export1.xlsx', sheet_name=f'n={j}').to_dict('records')
    products[j] = [Products(
        product['Наименование'], product['Страна'], product['Oбъем'], product['Сумма']) for product in d]

"""time_start = time.time()
for a in range(500):
    simple_func(products[500][a].prod_name)
time_end = time.time() - time_start
t_simple.append(time_end)
time_start = time.time()
for a in range(500):
    compl_func(products[500][a].prod_name)
time_end = time.time() - time_start
t_compl.append(time_end)"""

for l in n_:
    table_simple, table_compl = {}, {}
    collis_simple, collis_compl = 0, 0

    for k in range(l):
        hash_compl = products[l][k].compl_hash
        hash_simple = products[l][k].simple_hash

        if hash_compl not in table_compl:
            table_compl[hash_compl] = []
            table_compl[hash_compl].append(products[l][k])
        else:
            for m in table_compl[hash_compl]:
                if products[l][k].prod_name == m.prod_name:
                    break
            else:
                collis_compl += 1
            table_compl[hash_compl].append(products[l][k])

        if hash_simple not in table_simple:
            table_simple[hash_simple] = []
            table_simple[hash_simple].append(products[l][k])
        else:
            for m in table_simple[hash_simple]:
                if products[l][k].prod_name == m.prod_name:
                    break
            else:
                collis_simple += 1
            table_simple[hash_simple].append(products[l][k])

    total_collis_compl.append(collis_compl)
    total_collis_simple.append(collis_simple)

    prod_n = [s.prod_name for s in products[l]]
    key_n = Products(random.choice(prod_n), "", "", "").prod_name
    # key_n = Products("фнысыътц", "", "", "")
    # time_start = time.time()
    time_start = timeit.default_timer()
    key_hash_simple = simple_func(key_n)
    for f in table_simple[key_hash_simple]:
        if f.prod_name == key_n:
            print(f.prod_name)
    # time_end = time.time() - time_start
    time_end = timeit.default_timer() - time_start
    t_simple.append(time_end)

    time_start = timeit.default_timer()
    # time_start = time.time()
    key_hash_compl = compl_func(key_n)
    for r in table_compl[key_hash_compl]:
        if r.prod_name == key_n:
            print(r.prod_name)
    time_end = timeit.default_timer() - time_start
    # time_end = time.time() - time_start
    t_compl.append(time_end)

print(t_simple)
print(t_compl)
print(total_collis_compl)
print(total_collis_simple)
