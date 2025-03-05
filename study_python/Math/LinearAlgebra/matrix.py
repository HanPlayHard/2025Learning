import numpy as np

"""
Basic Matrix Creation 基本矩阵创建

    Create a zero matrix of size (3,3).
    创建一个大小为（3,3）的零矩阵。

    Create an identity matrix of size (4,4).
    创建一个大小为（4,4）的单位矩阵。

    Create a random matrix of size (3,3) with values between 0 and 1.
    创建一个大小为（3,3）、取值在0到1之间的随机矩阵。

    Create a diagonal matrix from a given list [1, 2, 3, 4].
    根据给定的列表[1,2,3,4]创建一个对角矩阵。

    Create a matrix filled with a specific number (e.g., all 7s) of size (3,3).
    创建一个矩阵，填充一个特定的数值（例如，所有的7），大小为（3,3）。

Matrix Properties & Indexing 矩阵属性和索引

    Get the shape, size, and data type of a given matrix.
    获取给定矩阵的形状、大小和数据类型。

    Extract the first row, last column, and a submatrix from a 4x4 matrix.
    从一个4x4矩阵中提取第一行、最后一列和一个子矩阵。

    Find the maximum and minimum values in a matrix and their indices.
    找出矩阵中的最大值和最小值及其下标。

    Compute the sum of all elements, sum of rows, and sum of columns.
    计算所有元素的和、行和和列的和。

Matrix Arithmetic Operations 矩阵算术运算

    Add two matrices element-wise.将两个矩阵元素相加。
    Subtract one matrix from another.用一个矩阵减去另一个矩阵。
    Multiply two matrices element-wise.两个矩阵按元素相乘。
    Perform matrix dot product (matrix multiplication).执行矩阵点积（矩阵乘法）。
    Compute the transpose of a given matrix.计算给定矩阵的转置。

Advanced Matrix Operations 高级矩阵运算

    Compute the determinant of a 3x3 matrix.计算一个3 × 3矩阵的行列式。
    Find the inverse of a square matrix.求方阵的逆矩阵。

    Compute the eigenvalues and eigenvectors of a matrix.
    计算矩阵的特征值和特征向量。
    Solve a system of linear equations using NumPy.使用NumPy求解线性方程组。

    Perform Singular Value Decomposition (SVD) on a matrix.
    对矩阵进行奇异值分解（Singular Value Decomposition， SVD）。

    Flatten a matrix into a 1D array and reshape it back.
    将矩阵展平为一维数组，并重塑它。
"""

# Basic Matrix Creation 基本矩阵创建
# 1. Create a zero matrix of size (3,3) 零矩阵
zero_matrix = np.zeros((3, 3))
print("Zero Matrix:\n", zero_matrix)
"""
Zero Matrix:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
"""
# 2. Create an identity matrix of size (4,4) 单位矩阵
identity_matrix = np.eye(4)
print("Identity Matrix:\n", identity_matrix)
"""
Identity Matrix:
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""

# 3. Create a random matrix of size (3,3) with values between 0 and 1 随机矩阵
random_matrix = np.random.rand(3, 3)
print("Random Matrix:\n", random_matrix)
"""
Random Matrix:
 [[0.5936277  0.10346343 0.85167288]
 [0.48700865 0.64711246 0.37796317]
 [0.55806651 0.93360625 0.36054304]]
"""

# 4. Create a diagonal matrix from a given list [1, 2, 3, 4] 对角矩阵
diagonal_matrix = np.diag([1, 2, 3, 4])
print("Diagonal Matrix:\n", diagonal_matrix)
"""
Diagonal Matrix:
 [[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
"""

# 5. Create a matrix filled with a specific number (e.g., all 7s) of size (3,3)
# 特定的数值
filled_matrix = np.full((3, 3), 7)
print("Matrix Filled with 7s:\n", filled_matrix)
"""
Matrix Filled with 7s:
 [[7 7 7]
 [7 7 7]
 [7 7 7]]
"""

# Matrix Properties & Indexing 矩阵属性和索引
# 6. Get the shape, size, and data type of a given matrix
# 获取给定矩阵的形状、大小和数据类型
print(
    "Shape:",
    random_matrix.shape,
    "Size:",
    random_matrix.size,
    "Data Type:",
    random_matrix.dtype,
)
# Shape: (3, 3) Size: 9 Data Type: float64

# 7. Extract the first row, last column, and a submatrix from a 4x4 matrix
# 一个4x4矩阵中提取第一行、最后一列和一个子矩阵。
matrix_4x4 = np.random.randint(1, 10, (4, 4))
print("4x4 Matrix:\n", matrix_4x4)
print("First Row:", matrix_4x4[0])
print("Last Column:\n", matrix_4x4[:, -1])
print("Submatrix (2x2 from top-left corner):\n", matrix_4x4[:2, :2])
"""
4x4 Matrix:
 [[3 4 2 2]
 [6 9 7 6]
 [8 4 5 6]
 [7 7 7 1]]

 First Row: [3 4 2 2]
Last Column:
 [2 6 6 1]
 
Submatrix (2x2 from top-left corner):
 [[3 4]
 [6 9]]
"""

# 8. Find the maximum and minimum values in a matrix and their indices
# 找出矩阵中的最大值和最小值及其下标
print(
    "Max Value:",
    matrix_4x4.max(),
    "at index",
    np.unravel_index(matrix_4x4.argmax(), matrix_4x4.shape),
)
"""
Max Value: 9 at index (np.int64(1), np.int64(1))
Min Value: 1 at index (np.int64(3), np.int64(3))
"""
print(
    "Min Value:",
    matrix_4x4.min(),
    "at index",
    np.unravel_index(matrix_4x4.argmin(), matrix_4x4.shape),
)

# 9. Compute the sum of all elements, sum of rows, and sum of columns
# 计算所有元素的和、行和和列的和。
print("Sum of all elements:", matrix_4x4.sum())  # 84
print("Sum of each row:", matrix_4x4.sum(axis=1))  # [11 28 23 22]
print("Sum of each column:", matrix_4x4.sum(axis=0))  # [24 24 21 15]


# Matrix Arithmetic Operations 矩阵算术运算
# 10. Add two matrices element-wise 两个矩阵元素相加
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Element-wise Addition:\n", A + B)
"""
 [[ 6  8]
 [10 12]]
"""

# 11. Subtract one matrix from another 用一个矩阵减去另一个矩阵
print("Element-wise Subtraction:\n", A - B)
"""
 [[-4 -4]
 [-4 -4]]
"""

# 12. Multiply two matrices element-wise 两个矩阵按元素相乘
"""
Hadamard product，哈达玛积,
又称：逐元素积、element-wise product、entrywise product、Schur product等
符号为 ∘ 或 ⊙ ,矩阵对应元素相乘，要求矩阵维度相同
"""
print("Element-wise Multiplication:\n", A * B)
"""
 [[ 5 12]
 [21 32]]
 对应元素依次相乘(逐元素积)
"""

# 13. Perform matrix dot product (matrix multiplication) 执行矩阵点积（矩阵乘法）
print("Matrix Multiplication:\n", np.dot(A, B))
"""
Standard matrix multiplication， 矩阵乘积,
符号为 ⋅ ，要求A的列数要与B的行数相等，是最一般的矩阵间乘法。

 [[19 22]
 [43 50]]
"""

# 14. Compute the transpose of a given matrix 计算给定矩阵的转置
print("Transpose of A:\n", A.T)
"""
 [[1 3]
 [2 4]]
"""


# Advanced Matrix Operations 高级矩阵运算
# 15. Compute the determinant of a 3x3 matrix 计算一个3 × 3矩阵的行列式
C = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("Determinant of C:", np.linalg.det(C))
# Determinant of C: -306.0


# 16. Find the inverse of a square matrix 求方阵的逆矩阵
if np.linalg.det(A) != 0:  # Ensure the matrix is invertible 确保矩阵是可逆的
    print("Inverse of A:\n", np.linalg.inv(A))
else:
    print("Matrix A is singular and cannot be inverted.")
"""
Inverse of A:
 [[-2.   1. ]
 [ 1.5 -0.5]]
"""

# 17. Compute the eigenvalues and eigenvectors of a matrix
# 计算矩阵的特征值和特征向量。
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
"""
Eigenvalues:
 [-0.37228132  5.37228132]
Eigenvectors:
 [[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
"""

# 18. Solve a system of linear equations Ax = b 解一个线性方程组Ax = b
b = np.array([5, 11])
solution = np.linalg.solve(A, b)
print("Solution to Ax = b:\n", solution)  #  [1. 2.]

# 19. Perform Singular Value Decomposition (SVD) on a matrix
# 对矩阵进行奇异值分解（Singular Value Decomposition， SVD）
U, S, V = np.linalg.svd(A)
print("Singular Value Decomposition:\nU:\n", U, "\nS:\n", S, "\nV:\n", V)
"""
U:
 [[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]]
S:
 [5.4649857  0.36596619]
V:
 [[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]
"""

# 20. Flatten a matrix into a 1D array and reshape it back
# 将矩阵展平为一维数组，并重塑它
flattened = A.flatten()
reshaped = flattened.reshape(2, 2)
print("Flattened Matrix:\n", flattened)
print("Reshaped Back to Original:\n", reshaped)
"""
Flattened Matrix:
 [1 2 3 4]
Reshaped Back to Original:
 [[1 2]
 [3 4]]

"""
