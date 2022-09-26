def reverseBits(n, p=0, q=0):
    if p >= q:
        return n[p]
    mid = (p+q)//2
    return reverseBits(n, mid+1, q) + reverseBits(n, p, mid)

n = list(str(int(input("Enter the bits: "))))
print(reverseBits(n, 0, len(n)-1))

