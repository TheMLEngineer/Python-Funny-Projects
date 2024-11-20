def fibonacci_series(n):
    a, b = 0, 1
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
n_terms = 10
print(fibonacci_series(n_terms))

print("Hello World!")
