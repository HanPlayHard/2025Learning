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
# 1. Create a zero matrix of size (3,3)
zero_matrix = np.zeros((3, 3))
print("Zero Matrix:\n", zero_matrix)
"""
Zero Matrix:
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
"""
