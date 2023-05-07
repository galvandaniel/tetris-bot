"""
Constants for defining all possible shapes all tetrominos can take.

These shapes are indexed from 0 to 3 for each tetromino, defined according to 
the Standard Rotation System (SRS).

The main idea is to define a dictionary to obtain a list of possible shapes for
each tetromino, by name.

What follows is a series of shapes, grouped by tetromino.

(It is possible to compute each rotation with some linear algebra, but this
approach is simpler and hopefully less computationally expensive.)

"""


# I shapes.
I_SHAPE_0 = [[0, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

I_SHAPE_1 = [[0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0]]

I_SHAPE_2 = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 0, 0]]

I_SHAPE_3 = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]


# J shapes.
J_SHAPE_0 = [[1, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

J_SHAPE_1 = [[0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

J_SHAPE_2 = [[0, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]]

J_SHAPE_3 = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 0]]


# L shapes
L_SHAPE_0 = [[0, 0, 1, 0],
             [1, 1, 1, 0],
             [0, 0, 0 ,0],
             [0, 0, 0, 0]]

L_SHAPE_1 = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]

L_SHAPE_2 = [[0, 0, 0, 0],
             [1, 1, 1, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]]

L_SHAPE_3 = [[1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]


# O shapes (O does not change with rotation)
O_SHAPE_0 = [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

O_SHAPE_1 = O_SHAPE_0

O_SHAPE_2 = O_SHAPE_0

O_SHAPE_3 = O_SHAPE_0


# S shapes
S_SHAPE_0 = [[0, 1, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

S_SHAPE_1 = [[0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]]

S_SHAPE_2 = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 0]]

S_SHAPE_3 = [[1, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]


# T shapes
T_SHAPE_0 = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

T_SHAPE_1 = [[0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

T_SHAPE_2 = [[0, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

T_SHAPE_3 = [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]


# Z shapes
Z_SHAPE_0 = [[1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

Z_SHAPE_1 = [[0, 0, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]]

Z_SHAPE_2 = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]

Z_SHAPE_3 = [[0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 0, 0]]


# Enpasulating all our established data.
I_SHAPES = [I_SHAPE_0, I_SHAPE_1, I_SHAPE_2, I_SHAPE_3]

J_SHAPES = [J_SHAPE_0, J_SHAPE_1, J_SHAPE_2, J_SHAPE_3]

L_SHAPES = [L_SHAPE_0, L_SHAPE_1, L_SHAPE_2, L_SHAPE_3]

O_SHAPES = [O_SHAPE_0, O_SHAPE_1, O_SHAPE_2, O_SHAPE_3]

S_SHAPES = [S_SHAPE_0, S_SHAPE_1, S_SHAPE_2, S_SHAPE_3]

T_SHAPES = [T_SHAPE_0, T_SHAPE_1, T_SHAPE_2, T_SHAPE_3]

Z_SHAPES = [Z_SHAPE_0, Z_SHAPE_1, Z_SHAPE_2, Z_SHAPE_3]

TETROMINO_TYPES = ["I", "J", "L", "O", "S", "T", "Z"]
TETROMINO_SHAPES = [I_SHAPES, J_SHAPES, L_SHAPES, O_SHAPES, S_SHAPES, T_SHAPES, Z_SHAPES]

# Each tetromino has 4 shapes.
TOTAL_SHAPES = 4

# End goal of a map mapping types to shape lists.
SHAPE_MAP = dict(zip(TETROMINO_TYPES, TETROMINO_SHAPES))
