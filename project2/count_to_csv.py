from count_module import countchar
import sys



counts = countchar()

print(counts)

for val in sys.argv:
    if '.csv' in val:
        f = open(val, mode = 'w', encoding = 'ASCII')
        for key in counts.keys():
            f.write(f"""{key}, {counts[key]}
""")






