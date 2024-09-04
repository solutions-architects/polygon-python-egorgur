from typing import Self, Sequence


class Matrix:
    """
    Matrix class.

    Represents the mathematical matrix and implements the method of the sum of two matrix.

    """

    def __init__(self: Self, init_data: Sequence[Sequence[int | float]]) -> None:
        """Init method."""
        self._matrix_data = init_data

    def __str__(self: Self) -> str:
        """Str method."""
        return str(self._matrix_data)

    def __add__(self: Self, other: Self) -> Self:
        """Sum method."""
        return Matrix(
            [
                [
                    self._matrix_data[row][col] + other._matrix_data[row][col]

                    for col in range(len(self._matrix_data[row]))
                ]
                for row in range(len(self._matrix_data))
            ]
        )

    def __eq__(self: Self, other: Self) -> bool:
        """Equality method."""
        return self._matrix_data == other._matrix_data
