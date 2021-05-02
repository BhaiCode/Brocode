t = int(input())

for i in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]

    picked_numbers = sorted([int(s) for s in input().split(" ")])
    dist = []

    d = picked_numbers[0] - 1
    dist.append(d)

    for ind in range(0, len(picked_numbers) - 1):
        d = picked_numbers[ind + 1] - picked_numbers[ind] - 1
        if d > 1:
            d -= 1
            dist.append(1)
        dist.append(d)

    dist.append(K - picked_numbers[-1])

    dist = sorted(dist)

    try:
        prob = (dist[-1] + dist[-2]) / K
    except:
        prob = dist[-1] / K

    print("Case #{}: {}".format(i, "%.6f" % prob))
