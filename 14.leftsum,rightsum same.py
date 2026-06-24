n = [1, 3, 5, 2, 2]

total = sum(n)
left = 0

for i in range(len(n)):
    if left == total - left - n[i]:
        print(i)
        break
    left += n[i]