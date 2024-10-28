import hashlib

def hashfunc(x):
    return bin(int(hashlib.md5(str(x).encode()).hexdigest(), 16))
    
def trailzero(hash_bin):
    return len(hash_bin) - len(hash_bin.rstrip('0'))

def flajolet(stream):
    mx = 0
    for item in stream:
        hb = hashfunc(item)
        tz = trailzero(hb)
        mx = max(tz, mx)
    return 2 ** mx

stream = [1,2,3,1,2,1,2,3,3,1,4,1,3, 4]
op = flajolet(stream)
print(f"The number of unique elements are: {op}")