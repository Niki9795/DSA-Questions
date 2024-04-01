def ContainsDuplicate():
    N = [1, 2, 3, 5, 4]

    M = set()

    for i in N:
        if i in M:
            return True
        M.add(i)
    return False
    
print(ContainsDuplicate())