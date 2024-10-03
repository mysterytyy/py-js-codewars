

def check(seq, elem):
    for num in seq:
        if num == elem:
            return True
    return False

print(check([66, 101], 64))