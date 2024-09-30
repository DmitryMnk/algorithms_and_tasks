def reverse_bits(n: int):

    # result = 0
    # for i in range(32):
    #     lsb = n & 1
    #     n >>= 1
    #     result = (result << 1) | lsb
    #     print(bin(result)[2::], bin(n)[2::])
    # return result
    return int(bin(n)[2:].zfill(32)[::-1], 2)

print(int('00000010100101000001111010011100', 2))

print(reverse_bits(
    43261596
))