import pytest
from tests.conftest import first_second_sum_expected_namedtuple


def test_sum_matrices(use_first_second_sum_expected_matrices_dataset: first_second_sum_expected_namedtuple):
    """Test the sum of two matrices."""
    assert (use_first_second_sum_expected_matrices_dataset.first +
            use_first_second_sum_expected_matrices_dataset.second ==
            use_first_second_sum_expected_matrices_dataset.expected)
