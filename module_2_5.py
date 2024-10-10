def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        string = []
        matrix.append(string)
        for j in range(m):
            string.append(value)
            if value <= 0:
                string.clear()
    return matrix


result1 = get_matrix(2, 3, 1)
result2 = get_matrix(3, 5, 10)
result3 = get_matrix(5, 2, -2)
print(result1)
print(result2)
print(result3)
