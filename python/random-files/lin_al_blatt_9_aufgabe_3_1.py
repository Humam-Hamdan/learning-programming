import numpy as np

A = np.array([
    [1,2,-3],
    [3,1,2],
    [1,1,-1]
])

# R_1,3 (3): Add 3 times row 3 to row 1
R_1_3_3 = np.array([
    [1, 0, 3],
    [0, 1, 0],
    [0, 0, 1]
])

# R_1,2 (-2): Add -2 times row 2 to row 1
R_1_2_m2 = np.array([
    [1, -2, 0],
    [0,  1, 0],
    [0,  0, 1]
])

# T_2,3: Swap row 2 and row 3
T_2_3 = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
])

# S_3 (-1): Scale row 3 by -1
S_3_m1 = np.array([
    [1, 0,  0],
    [0, 1,  0],
    [0, 0, -1]
])

# R_3,2 (-2): Add -2 times row 2 to row 3
R_3_2_m2 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, -2, 1]
])

# R_2,3 (-2): Add -2 times row 3 to row 2
R_2_3_m2 = np.array([
    [1, 0, 0],
    [0, 1, -2],
    [0, 0, 1]
])

# R_3,1 (-1): Add -1 times row 1 to row 3
R_3_1_m1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [-1, 0, 1]
])

# R_2,3 (-3): Add -3 times row 3 to row 2
R_2_3_m3 = np.array([
    [1, 0, 0],
    [0, 1, -3],
    [0, 0, 1]
])

# Optional: Print all matrices for verification
M = R_1_3_3 @ R_1_2_m2 @ T_2_3 @ S_3_m1 @ R_3_2_m2 @ R_2_3_m2 @ R_3_1_m1 @ R_2_3_m3 
print('M = \n', M, '\nM mal A = \n',  M@A)
