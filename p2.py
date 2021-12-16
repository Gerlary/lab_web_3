class Matrix:
    def __init__(self, first, second):
        self.matrix = [first, second]
        self.det = first[0] * second[1] - first[1] * second[0]

    def __gt__(self, other):
        return self.det > other.det

    def __lt__(self, other):
        return self.det < other.det

    def __add__(self, other):
        for i in range(2):
            for j in range(2):
                self.matrix[i][j] += other.matrix[i][j]

    def __mul__(self, other):
        matrix = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                sum = 0
                for k in range(2):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                matrix[i][j] = sum
        self.matrix = matrix