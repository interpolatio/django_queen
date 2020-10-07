class QueenClass:
    def __init__(self, n):
        self.a = 10
        self.desk = [[0 for x in range(n)] for y in range(n)]
        self.main_diag = [0 for x in range(2 * n - 1)]
        self.side_diag = [0 for x in range(2 * n - 1)]
        self.horizont = [0 for x in range(n)]
        self.vertical = [0 for x in range(n)]
        self.coordinate = []
        self.all_solution = []

    def step(self, i, j):
        if (self.main_diag[7 - (i - j)] + self.side_diag[j + i] + self.horizont[i] + self.vertical[j]) == 0:
            self.desk[i][j] = 1
            self.main_diag[7 - (i - j)] = 1
            self.side_diag[j + i] = 1
            self.horizont[i] = 1
            self.vertical[j] = 1
            self.coordinate.append((i, j))
            self.fff = []

            return True
        else:
            return False

    def revert(self):
        i, j = self.coordinate.pop()
        self.desk[i][j] = 0
        self.main_diag[7 - (i - j)] = 0
        self.side_diag[j + i] = 0
        self.horizont[i] = 0
        self.vertical[j] = 0
        return i, j

    def find(self, horizont, vertical):
        # print(self.coordinate)
        result = False
        for horizont in range(horizont, 8):
            if self.step(horizont, vertical):
                if (vertical == 7):
                    result = True
                else:
                    result = self.find(0, (vertical + 1))
                    if not (result):
                        self.revert()

            if (result):
                self.all_solution.append(list(self.coordinate))
                # print(self.all_solution)
                self.revert()
                result = self.find(0, (vertical - 1))
                break
        return result