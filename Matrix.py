class Matrix:
    def __init__(self, *args, **kwargs):
        self.matrix_list = list(args)

    def __str__(self):
        return str(self.matrix_list)

    def __add__(self, other):
        return Matrix(
            *tuple(map(
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
