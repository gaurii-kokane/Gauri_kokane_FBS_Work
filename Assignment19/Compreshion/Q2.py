#  Find all of the numbers from 1–1000 that have a 6 in them

have_6 = [x for x in range(1, 1001) if '6' in str(x)]
print(have_6)
