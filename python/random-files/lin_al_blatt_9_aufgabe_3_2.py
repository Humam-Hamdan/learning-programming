import numpy as np

M = np.array([
    [1,2,-3,0],
    [3,0,3,1],
    [1,1,-1,0]
])

# T_2,3: Tausche Zeile 2 und 3
T_2_3 = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
])

# S_3(-1): Zeile 3 mal -1
S_3_neg1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, -1]
])

# R_1,3(2): Zeile 1 plus 2 * Zeile 3
R_1_3_2 = np.array([
    [1, 0, 2],
    [0, 1, 0],
    [0, 0, 1]
])

# R_2,3(-6): Zeile 2 plus (-6) * Zeile 3
R_2_3_neg6 = np.array([
    [1, 0, 0],
    [0, 1, -6],
    [0, 0, 1]
])

# R_3,1(-1): Zeile 3 plus (-1) * Zeile 1
R_3_1_neg1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [-1, 0, 1]
])

# R_2,1(-3): Zeile 2 plus (-3) * Zeile 1
R_2_1_neg3 = np.array([
    [1, 0, 0],
    [-3, 1, 0],
    [0, 0, 1]
])

K = T_2_3    @ S_3_neg1    @ R_1_3_2    @ R_2_3_neg6    @ R_3_1_neg1    @ R_2_1_neg3

print('M = \n', M, '\nK = \n', K, '\nM mal K =\n', K@M)
