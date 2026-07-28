# Matrix Multiplication

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    A = []
    B = []

    print("Enter Matrix A elements:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    print("Enter Matrix B elements:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    result = []

    for i in range(r1):
        row = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)

    print("Resultant Matrix:")
    for row in result:
        print(row)
