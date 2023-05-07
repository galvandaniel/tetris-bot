"""
Classes for implementing the logic of Tetris.

"""

from typing import List, Tuple, Optional
from tetromino_shapes import SHAPE_MAP, SKIRT_MAP, TOTAL_SHAPES, BRICK_COUNT


class TetrominoShape:
    """
    Class for holding the 2D shape data of a defined tetromino.

    A tetromino's shape is a 4x4 2D list of either 1 or 0.
    1 if the tetromino shape is defined, 0 otherwise.

    A tetromino's "skirt" is the space each column of the tetromino needs in
    order to not overlap with anything above or below it. A skirt value of 0
    denotes 0 space (no bricks in that column), a skirt value of 1 denotes 1
    brick space needed.

    Attributes:
        possible_shapes - List of all shapes the tetromino type can take.
        possible_skirts - List of all skirts the tetromino type can have.
        current_shape - Current shape held for the tetromino type.
        current_skirt - Current skirt of the current shape.
        rotation_index - Index of current_shape within possible_shapes.

    """

    def __init__(self, name: str) -> None:
        """
        TetrominoShape constructor.

        Args:
            name - Name of the shapes to define, such as "S", "T", "Z", etc...

        """
        # A tetromino begins with initial shape of index 0.
        self.possible_shapes: List[List[List[int]]] = SHAPE_MAP[name]
        self.possible_skirts: List[List[int]] = SKIRT_MAP[name]

        self.current_shape: List[List[int]] = self.possible_shapes[0]
        self.current_skirt: List[int] = self.possible_skirts[0]

        self.rotation_index: int = 0


    def next_clockwise_shape(self) -> Tuple[List[List[int]], int]:
        """
        Determine the resulting shape and rotation index if the current shape
        were to turn clockwise.

        Returns:
            Tuple[List[List[int]], int] - Shape of the tetromino if it were to
            turn clockwise, and the corresponding rotation index.

        """
        # "Rollover" the rotation index if it goes out of bounds.
        next_rotation_index = (self.rotation_index + 1) % TOTAL_SHAPES
        return (self.possible_shapes[next_rotation_index], next_rotation_index)


    def next_counterclockwise_shape(self) -> Tuple[List[List[int]], int]:
        """
        Determine the resulting shape and rotation index if the current shape
        were to turn counterclockwise.

        Returns:
            Tuple[List[List[int]], int] - Shape of the tetromino if it were to
            turn counterclockwise, and the corresponding rotation index.

        """
        # "Rollover" the rotation index if it goes out of bounds at index -1
        next_rotation_index = self.rotation_index - 1

        if next_rotation_index == -1:
            next_rotation_index = 3
        return (self.possible_shapes[next_rotation_index], next_rotation_index)

    def rotate_shape_clockwise(self) -> None:
        """
        Rotate the tetromino shape clockwise, updating current shape, skirt,
        and rotation index.

        """
        new_shape, new_index = self.next_clockwise_shape()
        self.current_shape = new_shape
        self.current_skirt = self.possible_skirts[new_index]
        self.rotation_index = new_index

    def rotate_shape_counterclockwise(self) -> None:
        """
        Rotate the tetromino shape counterclockwise, updating current shape,
        skirt, and rotation index.

        """
        new_shape, new_index = self.next_counterclockwise_shape()
        self.current_shape = new_shape
        self.current_skirt = self.possible_skirts[new_index]
        self.rotation_index = new_index


class Tetromino:
    """
    Class for representing a single 4-piece tetromino.

    Attributes:
        shape - Data for the current shape the tetromino has, alongside all
        possible shapes it can potentially take.
        topleft - Position of the tetromino's topleft entry in its shape within
        the context of a game board, as (row, col).

    """

    def __init__(self, name: str, start: Tuple[int, int]) -> None:
        """
        Tetromino constructor

        Args:
            name - Name of the Tetromino's type, such as "S", "T", "Z", etc...
            start - Starting position of the tetromino's topleft entry in its
            shape within the context of a game board.

        """
        self.shape: TetrominoShape = TetrominoShape(name)
        self.topleft = start


    def rotate_clockwise(self) -> None:
        """
        Rotate the tetromino clockwise.

        This causes a change in where the tetromino is defined in its shape, but
        does not change where the topleft entry of the shape is located within
        the board.

        """
        self.shape.rotate_shape_clockwise()


    def rotate_counterclockwise(self) -> None:
        """
        Rotate the tetromino counterclockwise.

        This causes a change in where the tetromino is defined in its shape, but
        does not change where the topleft entry of the shape is located within
        the board.

        """
        self.shape.rotate_shape_counterclockwise()


    def __repr__(self) -> str:
        """
        Gives a string representation of a tetromino.

        A tetromino is represented by a string as a series of "o" characters
        delimited by newlines such that they visually look like the tetromino.

        Returns:
            str - String representation of tetromino

        """
        last_index = TOTAL_SHAPES - 1
        current_shape = self.shape.current_shape
        representation = ""

        # Iterate through the entries of the shape.
        # If we encounter a place where the tetromino is defined, put a "o".
        # Once the last element of a row has been reached, delimit with newline.
        for row in current_shape:
            for index, shape_entry in enumerate(row):
                if shape_entry == 1:
                    representation += "o"
                else:
                    representation += " "

                if index == last_index:
                    representation += "\n"
        return representation



class Board:
    """
    Class for representing a single Tetris board.

    Attributes:
        grid - Placed pieces as a 2D array of 0's and 1's, where 1 represents an
        occupied space and 0 represents a free space.
        filled_rows - Stores number of occupied spaces in each row of grid.
        filled_columns - Stores maximum height to which each column is occupied.
        row_count - Number of board rows.
        col_count - Number fo board columns.

    """

    def __init__(self, col: int = 10, row: int = 16) -> None:
        """
        Board constructor.

        Args:
            rows, cols - Dimension of board, resulting in a colxrow grid.
            Defaults to 10x16.

        """
        # Begin with an entirely empty board. with nothing filled.
        self.grid: List[List[int]] = [[0] * col for _ in range(row)]
        self.filled_rows: List[int] = [0] * row
        self.filled_columns: List[int] = [0] * col

        self.row_count = row
        self.col_count = col


    def place_tetromino(self, tetromino: Tetromino) -> None:
        """
        Place the given tetromino on the board wherever it is, adding its data
        to the grid, and updating filled_rows, and filled_columns.

        If the tetromino cannot be placed due to overlap or going out of bounds,
        this method silently fails.

        Args:
            tetromino - Tetromino to place into board.

        """
        to_update = self.valid_spaces(tetromino)

        if to_update is not None:
            self.update_grid(to_update)

    def drop_tetromino(self, tetromino: Tetromino) -> None:
        """
        Place the given tetromino on the board wherever it is horizontally,
        but force it to drop as far as possible before being placed.

        Grid data, filled_rows, and filled_columns are updated to reflect the
        placement.

        Args:
            tetromino - Tetromino to drop into board.

        """

        # The row to place a hard dropped tetromino on depends on the room each
        # column of the tetromino needs.
        #
        # The final row placement will be the row that allows the column that
        # needs the most amount of space to fit.
        suggested_placements: List[int] = []

        topleft_row, topleft_col = tetromino.topleft
        skirt = tetromino.shape.current_skirt

        # The space each column needs is contained in the skirt.
        for shape_column, minimum_space in enumerate(skirt):

            # If the skirt value for a tetromino column is 0, the tetromino
            # has no bricks in that shape column. (0 space for that column)
            if minimum_space == 0:
                continue

            # Get the location of each tetromino column in the context of the
            # board.
            board_column = topleft_col + shape_column

            # An out of bounds column can only occur if the tetromino is not
            # defined in that column. Hence we skip any "space" computations.
            if self.is_out_of_bounds(topleft_row, board_column):
                continue

            # Skip to the first free row index below the tetromino column.
            already_filled = self.filled_columns[board_column]
            next_free_row = self.row_count - already_filled

            # After the first free row index, take away however much space is
            # is needed for the skirt.
            vertical_placement = next_free_row - minimum_space

            suggested_placements.append(vertical_placement)

        # Take the row index that calls for the most amount of space,
        # change the tetromino's position to that location, then place it.
        #
        # If the tetromino shaped turned out to be entirely out of bounds,
        # meaning suggested_placements is empty, default to the original row.
        new_row = min(suggested_placements, default=topleft_row)
        tetromino.topleft = (new_row, topleft_col)
        self.place_tetromino(tetromino)


    def valid_spaces(self, tetromino: Tetromino) -> Optional[List[Tuple[int, int]]]:
        """
        Compute a list of the valid spaces a given tetromino could move to on
        the board or be placed on.

        If any portion of a tetromino is either out of bounds or occupied on
        the board, the tetromino has no valid spaces.

        A point of the tetromino's shape being out of bounds does not disqualify
        the tetromino from being valid if the tetromino is not defined at that
        point in its shape.

        Args:
            tetromino - Tetromino to compute valid spaces for.

        Return:
            List of (row, col) board coordinates the tetromino could be placed
            on without going out of bounds or overlapping.

            None if any portion of the tetromino does not fulfill this criteria.

        """
        # Setup a collection of valid coordinates in grid to return on success.
        valid_spaces: List[Tuple[int, int]] = []

        for row_index, row in enumerate(tetromino.shape.current_shape):
            for col_index, shape_space in enumerate(row):

                # If we've successfully found all bricks of the tetromino to be
                # valid, we're done.
                if len(valid_spaces) == BRICK_COUNT:
                    break

                # If the shape isn't defined at this index, move on.
                if shape_space == 0:
                    continue

                # Find where the current non-zero shape space is in the context
                # of the board
                topleft_row, topleft_col = tetromino.topleft
                row_board_pos = topleft_row + row_index
                col_board_pos = topleft_col + col_index

                # If the tetromino goes out of bounds or overlaps, fail.
                if self.is_out_of_bounds(row_board_pos, col_board_pos):
                    print("Tetromino goes out of bounds at", row_board_pos, col_board_pos)
                    return None

                if self.grid[row_board_pos][col_board_pos] == 1:
                    print("Tetromino overlaps with another at", row_board_pos, col_board_pos)
                    return None

                # The current space is valid, so add it to the list of valid
                # coordinates.
                valid_spaces.append((row_board_pos, col_board_pos))
        return valid_spaces


    def update_grid(self, to_update: List[Tuple[int, int]]) -> None:
        """
        Update occupied spaces in the grid given a list of collected (row, col)
        coordinates to process.

        Grid data, filled_rows, and filled_columns are updated to reflect
        changes to the board.

        Args:
            to_place: Coordinates to occupy spaces in the board.

        """
        ###### BUGGED: filled_columns does not properly account for overhangs!!
        for row, col in to_update:
            self.grid[row][col] = 1
            self.filled_rows[row] += 1
            self.filled_columns[col] += 1


    def is_out_of_bounds(self, row: int, col: int) -> bool:
        """
        Compute whether the given coordinates are out of bounds of the board
        or not.

        Args:
            row, col - Board coordinates to determine if out of bounds.

        Returns:
            True if out of bounds, False otherwise.
        """
        row_in_bounds = 0 <= row < self.row_count
        col_in_bounds = 0 <= col < self.col_count
        in_bounds = row_in_bounds and col_in_bounds

        return not in_bounds


    def __repr__(self) -> str:
        """
        Give a string representation of a tetris board.

        A tetris board is represented by " " where the board is open, and "O"
        where the board is occupied, delimited by newlines to create a visual
        colxrow size grid.

        Returns:
            String representation of board.

        """
        representation = ""

        for row in self.grid:
            for column_index, grid_space in enumerate(row):
                if grid_space == 0:
                    representation += " "
                else:
                    representation += "O"

                if column_index == (self.col_count - 1):
                    representation += "\n"
        return representation
