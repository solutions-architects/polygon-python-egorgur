from typing import Self, Sequence


class Matrix:
    """
    Matrix class.

    Represents the mathematical matrix and implements the method of the sum of two matrix.

    """

    def __init__(self: Self, init_data: Sequence[Sequence[int | float]]):
        """Init method."""
        print(init_data)
        self.matrix_list = init_data

    def __str__(self: Self):
        """Str method."""
        return str(self.matrix_list)

    def __add__(self: Self, other: Self):
        """Summ method."""
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
