astr = "Hello Nícollas"
try:
    istr = int(astr)
except:
    istr = -1

print("Primeiro:", istr)

astr = "123"

try:
    istr = int(astr)
except:
    istr = -1

print("Segundo:", istr)
