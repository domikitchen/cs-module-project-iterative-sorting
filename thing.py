arr = ["85", "46", 27, "81", 94, "9", "27", 38, "43", "99", 37, 63, 31, "42", 14]

count = 0

while len(arr) > count:
    if int(arr[count]) % 3 == 0:
        print(arr[count])
    count += 1