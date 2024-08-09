def calc_redundant_bits(m):
    """Calculate the number of redundant bits needed."""
    for i in range(m):
        if 2**i >= m + i + 1:
            return i


def pos_redundant_bits(data, r):
    """Determine the positions of redundant bits in the data."""
    j = 0
    k = 1
    m = len(data)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[-k]
            k += 1

    return res[::-1]


def calc_parity_bits(arr, r):
    """Calculate the parity bits for the data with redundant bits."""
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(arr[-j])

        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr


def detect_error(arr, nr):
    """Detect the position of an error in the transmitted data."""
    n = len(arr)
    res = 0

    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(arr[-j])

        res += val * (10**i)

    return int(str(res), 2)
