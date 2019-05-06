
def list_content(li, n):
    full_set = {i+1 for i in range(n)}
    return list(full_set - set(li))


print(list_content([2,3,7,4,9], 10))

