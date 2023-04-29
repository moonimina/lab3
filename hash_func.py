def simple_func(name):
    hash_ = 0
    for i in range(0, len(name)):
        hash_ = (hash_ + ord(name[i]) ** 5) // 2000
    return hash_ % 4294967295


def compl_func(name):  # rs
    b = 378551
    a = 63689
    hash_ = 0
    for i in range(0, len(name)):
        hash_ = hash_ * a + ord(name[i])
        a *= b
    return hash_ % 4294967295


"""def rot13(name):
    hash_ = 0
    for i in range(len(name)):
        hash_ += ord(name[i])
        hash_ -= (hash_ << 13) | (hash_ >> 19)
    return abs(hash_)
"""
