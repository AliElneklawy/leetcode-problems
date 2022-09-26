def reverse(x: int) -> int:
    negative = False
    if x < 0:
        negative = True
    reversedInt = int(''.join(reversed([i for i in str(abs(x))])))
    if reversedInt < (-2**31) or reversedInt > (2**31):
        return 0
    return int(-reversedInt) if negative else int(reversedInt)
