import re
def myAtoi(s: str) -> int:
    s = s.strip()
    try:
        x = int(''.join((re.findall(r"^[-|+]?\d+", s))))
        if x < (-2**31):
            return -2**31
        if x >= (2**31):
            return (2**31) - 1
        return x
    except:
        return 0
