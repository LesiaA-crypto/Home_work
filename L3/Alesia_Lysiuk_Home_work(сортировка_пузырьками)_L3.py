li = [3, 5, 2, 0]

swapped = True

while swapped:
    swapped = False
    for i in range(len(li) - 1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            swapped = True

print(li)
          