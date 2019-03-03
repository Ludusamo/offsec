def pseudo_fib(n):
    if n == 0: return 1
    if n == 1: return 2
    return pseudo_fib(n - 1) + pseudo_fib(n - 2)

def find(x=0, y=45, expected=116369):
    s = x * 1597 + y * 2584
    if s == expected:
        return (x, y)
    if s < expected:
        return find(x + 1, y, expected)
    if s > expected:
        return find(x, y - 1, expected)

#print(pseudo_fib(16))
print(find())

