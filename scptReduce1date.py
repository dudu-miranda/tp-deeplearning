
import sys

arq = sys.argv[1]
lines = []
with open(arq, 'r') as f:
    lines = f.readlines()

with open(arq, 'w') as f:
    for line in lines:
        if line:
            div = line.split(',')
            f.write(div[0] + ',' + div[2])


