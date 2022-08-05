# cython: language_level=3

cpdef unsigned char fast_checksum(str msg):
    cdef unsigned char s = 0
    for c in msg:
        s += <unsigned char>c
    return s
