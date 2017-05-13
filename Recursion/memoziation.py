def reverse(str):
    if len(str) == 1:
        return str
    return reverse(str[1:]) + str[0]

print(reverse("Ravi"))

def permute(str):
    out = []
    if len(str) == 1:
        out = [str]
    else:
        for i,let in enumerate(str):
            for perm in permute(str[:i] + str[i+1:]):
                print(perm)
                out += [let+perm]
    return out



print(permute('abc'))