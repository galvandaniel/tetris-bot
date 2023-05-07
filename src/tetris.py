"""
Classes for implementing the logic of Tetris.

"""

from tetromino_shapes import SHAPE_MAP, TOTAL_SHAPES
from typing import List, Tuple


class TetrominoShape:
    """
    Class for holding the 2D shape data of a defined tetromino.

    A tetromino's shape is a 4x4 2D list of either 1 or 0.
    1 if the tetromino shape is defined, 0 otherwise.

    Attributes:
        possible_shapes - List of all shapes the tetromino type can take.
        current_shape - Current shape held for the tetromino type.
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
        self.current_shape: List[List[int]] = self.possible_shapes[0]
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
            turn counterclockwise, and the corresponding rotation index/

        """
        # "Rollover" the rotation index if it goes out of bounds at index -1
        next_rotation_index = self.rotation_index - 1

        if next_rotation_index == -1:
            next_rotation_index = 3
        return (self.possible_shapes[next_rotation_index], next_rotation_index)

    def rotate_shape_clockwise(self) -> None:
        """
        Rotate the tetromino shape clockwise, updating current shape and
        rotation index.

        """
        new_shape, new_index = self.next_clockwise_shape()
        self.current_shape = new_shape
        self.rotation_index = new_index

    def rotate_shape_counterclockwise(self) -> None:
        """
        Rotate the tetromino shape counterclockwise, updating current shape and
        rotation index.

        """
        new_shape, new_index = self.next_counterclockwise_shape()
        self.current_shape = new_shape
        self.rotation_index = new_index


class Tetromino:
    """
    Class for representing a single 4-piece tetromino.

    Attributes:
        shape - Data for the current shape the tetromino has, alongside all
        possible shapes it can potentially take.
        topleft - Position of the tetromino's topleft entry in its shape within
        the context of a game board.
        
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
