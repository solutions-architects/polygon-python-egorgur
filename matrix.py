from typing import Self


class Matrix:
    """
    Matrix class.

    Represents the mathematical matrix and implements the method of the sum of two matrix.

    """

    def __init__(self: Self, init_data: list[list[int | float]] | tuple[list[int | float], ...]):
        """
        Init method.

        Takes the matrix parameters (width and height of a matrix) as a list of lists.
        """
        print(init_data)
        self.matrix_list = init_data

    def __str__(self: Self):
        """
        Str method.

        Gets called when a Matrix object gets printed via print()
        """
        return str(self.matrix_list)

    def __add__(self: Self, other: Self):
        """
        Summ method.

        Gets called in summing operations.
        """
        return Matrix(
            tuple(map(
                lambda row1, row2: list(
                    map(
                        lambda element1, element2: element1 + element2,
                        row1,
                        row2
                    )
                ),
                self.matrix_list,
                other.matrix_list
            ))
        )
