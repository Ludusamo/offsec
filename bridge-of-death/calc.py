locs=[0x60d915, 0x605a67, 0x60795a, 0x60746b, 0x603f3f, 0x60398d, 0x606f8e, 0x60a773, 0x60ea2d]
for loc in locs:
    offset = loc - 0x6020a0
    num1 = offset // 256
    num2 = offset - (num1 * 256)

    print(num1)
    print(num2)
