class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        pass

    def row(self, index):
        rows = self.matrix_string.split('\n')
        return list(map(int, rows[index - 1].split(" ")))

    def column(self, index):
        columns = []
        rows = self.matrix_string.split('\n')
        len_columns = len(rows[0].split(" "))

        for i in range(0, len_columns):
            column = []
            for row in rows:
                row = row.split(" ")
                column.append(int(row[i]))

            columns.append(column)

        return columns[index - 1]

