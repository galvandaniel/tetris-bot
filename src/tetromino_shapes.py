"""
Constants for defining all possible shapes all tetrominos can take.

These shapes are indexed from 0 to 3 for each tetromino, defined according to 
the Standard Rotation System (SRS).

The main idea is to define a dictionary to obtain a list of possible shapes for
each tetromino, by name.

What follows is a series of shapes, grouped by tetromino.

Each shape also has a "skirt": the space each column needs in order to not
overlap with anything below or above.

For example:
I_SHAPE_1 has skirt: [0, 0, 4, 0]
L_SHAPE_1 has skirt: [0, 3, 3, 0]

Predefining skirts helps make hard drop computations faster.

(It is possible to compute each rotation with some linear algebra, but this
approach is simpler and hopefully less computationally expensive.)

"""

# Each tetromino has 4 shapes and a total brick count of 4.
TOTAL_SHAPES = 4
BRICK_COUNT = 4

def compute_skirt(shape):
    """
    Compute the largest row index where a brick appears for each column in a
    tetromino shape, called a "skirt."

    Args:
        shape (List[List[int]]) - Tetromino shape to compute skirt for.
    
    Returns:
        List[int] - Index for each column of largest occupied row index.

    """
    column_buckets = [0] * BRICK_COUNT

    # Every time we encounter a brick in a column, update the maximum amount
    # of space needed to accomodate that brick.
    for row_index, row in enumerate(shape):
        for column_index, shape_space in enumerate(row):
            if shape_space == 1:
                column_buckets[column_index] = row_index + 1
    return column_buckets


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
TETROMINO_SKIRTS = [list(map(compute_skirt, shape_list)) for shape_list in TETROMINO_SHAPES]

# End goal of a map mapping types to shape lists and shape skirts.
SHAPE_MAP = dict(zip(TETROMINO_TYPES, TETROMINO_SHAPES))
SKIRT_MAP = dict(zip(TETROMINO_TYPES, TETROMINO_SKIRTS))
