class BoardClass:
    def __init__(self, rows, columns):
        self.rows = rows  # We save the number of rows
        self.columns = columns  # and columns, will be useful later
        self.slots = [[0] * columns for _ in range(rows)]  # Initialize all slots as empty

    def __print__(self):  # Simple method to print the board without writing a loop each time
        for slot in self.slots:
            print(slot)