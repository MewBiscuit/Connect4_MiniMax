class BoardClass:
    def __init__(self, rows, columns):
        self.rows = rows  # We save the number of rows
        self.columns = columns  # and columns, will be useful later
        self.slots = [[0] * columns for _ in range(rows)]  # Initialize all slots as empty

        def __print__(self):  # Simple method to print the board
        for row in self.slots:
            for element in row:
                if element == 0:
                    print("[ ]", end='')
                elif element == 1:
                    print("[X]", end='')
                elif element == 2:
                    print("[O]", end='')
            print()
