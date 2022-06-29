sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)

total = float(sp + rj + mg + es + out)

psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print('Porcentagem de SP: {:.2f}%'.format(psp))
print('Porcentagem de RJ: {:.2f}%'.format(prj))
print('Porcentagem de MG: {:.2f}%'.format(pmg))
print('Porcentagem de ES: {:.2f}%'.format(pes))
print('Porcentagem de OUTROS: {:.2f}%'.format(pout))