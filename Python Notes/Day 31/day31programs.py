# Day 31 - NumPy Programs
# Install NumPy if required: pip install numpy

import numpy as np


# 1. Create 1D, 2D and 3D arrays
def program_1():
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    print("1D:", arr1)
    print("2D:", arr2)
    print("3D:", arr3)


# 2. Create arrays with specific values
def program_2():
    print("Zeros:\n", np.zeros((3, 3)))
    print("Ones:\n", np.ones((2, 4)))
    print("Identity:\n", np.eye(4))
    print("Full:\n", np.full((2, 3), 7))


# 3. Generate ranges
def program_3():
    print("Range:", np.arange(1, 11, 2))
    print("Linear space:", np.linspace(0, 100, 5))


# 4. Generate random values
def program_4():
    np.random.seed(42)
    print("Random integers:\n", np.random.randint(1, 100, (3, 3)))
    print("Random floats:\n", np.random.rand(3, 3))
    print("Normal values:\n", np.random.randn(3, 3))
    print("Random choices:", np.random.choice([10, 20, 30, 40, 50], 5))


# 5. Shape, reshape, flatten and transpose
def program_5():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    print("Shape:", arr.shape)
    print("Reshaped:\n", arr.reshape(3, 2))
    print("Flattened:", arr.flatten())
    print("Transposed:\n", arr.T)


# 6. 1D indexing and slicing
def program_6():
    arr = np.array([10, 20, 30, 40, 50])

    print("First:", arr[0])
    print("Last:", arr[-1])
    print("Index 1 to 3:", arr[1:4])
    print("First 3:", arr[:3])
    print("Every second:", arr[::2])


# 7. 2D indexing and slicing
def program_7():
    matrix = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])

    print("Element:", matrix[1, 2])
    print("Second column:", matrix[:, 1])
    print("Subset:\n", matrix[0:2, 1:3])


# 8. Mathematical and statistical operations
def program_8():
    arr = np.array([1, 2, 3, 4, 5])

    print("Add 10:", arr + 10)
    print("Multiply by 2:", arr * 2)
    print("Square:", arr ** 2)
    print("Square root:", np.sqrt(arr))
    print("Sum:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard deviation:", np.std(arr))
    print("Variance:", np.var(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))
    print("Cumulative sum:", np.cumsum(arr))
    print("Cumulative product:", np.cumprod(arr))


# 9. Boolean indexing and filtering
def program_9():
    arr = np.array([10, 20, 30, 40, 50])
    mask = arr > 25

    print("Boolean mask:", mask)
    print("Filtered values:", arr[mask])


# 10. Matrix multiplication
def program_10():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix product:\n", np.dot(A, B))


# 11. Determinant and inverse
def program_11():
    A = np.array([[1, 2], [3, 4]])

    print("Determinant:", np.linalg.det(A))
    print("Inverse:\n", np.linalg.inv(A))


# 12. Eigenvalues and eigenvectors
def program_12():
    A = np.array([[1, 2], [3, 4]])
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)


# 13. Solve linear equations
def program_13():
    A = np.array([[1, 2], [3, 4]])
    C = np.array([5, 11])

    print("Solution:", np.linalg.solve(A, C))


# 14. Sorting and unique values
def program_14():
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

    print("Sorted:", np.sort(arr))
    print("Unique:", np.unique(arr))


# 15. Vertical and horizontal stacking
def program_15():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Vertical stack:\n", np.vstack((A, B)))
    print("Horizontal stack:\n", np.hstack((A, B)))


# 16. Split an array
def program_16():
    arr = np.array([1, 2, 3, 4, 5, 6])

    print("Split:", np.split(arr, 3))


# 17. View and copy
def program_17():
    arr = np.array([10, 20, 30])

    view_arr = arr.view()
    view_arr[0] = 100
    print("After changing view:", arr)

    copy_arr = arr.copy()
    copy_arr[0] = 200
    print("After changing copy:", arr)


# 18. Mini data-analysis example
def program_18():
    sales = np.array([1200, 1500, 1100, 1800, 1600])

    print("Sales:", sales)
    print("Total:", np.sum(sales))
    print("Average:", np.mean(sales))
    print("Highest:", np.max(sales))
    print("Lowest:", np.min(sales))
    print("Above 1400:", sales[sales > 1400])


if __name__ == "__main__":
    program_1()
    program_2()
    program_3()
    program_4()
    program_5()
    program_6()
    program_7()
    program_8()
    program_9()
    program_10()
    program_11()
    program_12()
    program_13()
    program_14()
    program_15()
    program_16()
    program_17()
    program_18()
