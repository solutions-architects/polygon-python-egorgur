import pytest
from typing import NamedTuple
from matrix import Matrix


@pytest.fixture
def create_matrix_first():
    """Fixture for creating a ``Matrix`` instance."""
    first_matrix = Matrix([[0, 1, 2], [0, 1, 2]])
    return first_matrix


@pytest.fixture
def create_matrix_second():
    """Fixture for creating a ``Matrix`` instance"""
    second_matrix = Matrix([[2, 1, 0], [2, 1, 0]])
    return second_matrix


@pytest.fixture
def create_matrix_sum_expected():
    """Fixture for creating a ``Matrix`` instance"""
    expected_matrix = Matrix([[2, 2, 2], [2, 2, 2]])
    return expected_matrix


@pytest.fixture
def use_first_second_sum_expected_matrices_dataset(create_matrix_first: Matrix,
                                                   create_matrix_second: Matrix,
                                                   create_matrix_sum_expected: Matrix) -> NamedTuple:
    """Returns a dataset of three matrices for testing the ``__add__`` method."""
    first_matrix = create_matrix_first
    second_matrix = create_matrix_second
    expected_matrix = create_matrix_sum_expected
    first_second_sum_expected_dataset = first_second_sum_expected_namedtuple(
        first=first_matrix,
        second=second_matrix,
        expected=expected_matrix
    )
    return first_second_sum_expected_dataset


first_second_sum_expected_namedtuple = NamedTuple(
    "first_second_sum_expected_namedtuple",
    [
        ("first", Matrix),
        ("second", Matrix),
        ("expected", Matrix)
    ]
)
