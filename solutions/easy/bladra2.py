vat = input()

v, a, t = vat.split()
vfloat = float(v)
afloat = float(a)
tfloat = float(t)

# d = vt + 1/2 at^2
d = vfloat * tfloat + ((1/2) * afloat *(tfloat**2))
print(f"{d:.9f}")
