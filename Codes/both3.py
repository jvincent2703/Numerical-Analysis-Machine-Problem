import numpy as np

class InterpolationCalculator:
    def __init__(self):
        self.data_source = 'Pre-defined'
        self.x_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.y_values = np.array([201.20, 239.60, 229, 232, 245, 230, 238, 240, 224, 225])

    def set_data_source(self, source):
        self.data_source = source

    def set_user_defined_data(self, x_values, y_values):
        self.data_source = 'User-defined'
        self.x_values = np.array(x_values)
        self.y_values = np.array(y_values)

    def calculate(self, xp):
        n = len(self.x_values)
        p = np.zeros((n, n))
        p[:, 0] = self.y_values

        for j in range(1, n):
            for i in range(n - j):
                p[i][j] = (p[i + 1][j - 1] - p[i][j - 1]) / (self.x_values[i + j] - self.x_values[i])

        res = p[0][0]

        for i in range(1, n):
            prod = 1
            for j in range(i):
                prod *= (xp - self.x_values[j])
            res += prod * p[0][i]

        return res


def get_user_defined_data():
    x_values = []
    y_values = []
    num_points = int(input("Enter the number of data points: "))
    for i in range(num_points):
        x = float(input("Enter x value for point {}: ".format(i + 1)))
        y = float(input("Enter y value for point {}: ".format(i + 1)))
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values


def main():
    calculator = InterpolationCalculator()

    print("Machine Problem 3")
    print("-----------------")

    while True:
        print("\nSelect an option:")
        print("1. Use pre-defined data")
        print("2. Enter user-defined data")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            calculator.set_data_source('Pre-defined')
            print("Pre-defined data selected.")
            xp = float(input("Enter interpolation point (f(n)): "))
            result = calculator.calculate(xp)
            print("f({:.8f}) = {:.8f}".format(xp, result))

        elif choice == '2':
            x_values, y_values = get_user_defined_data()
            calculator.set_user_defined_data(x_values, y_values)
            print("User-defined data selected.")
            xp = float(input("Enter interpolation point (f(n)): "))
            result = calculator.calculate(xp)
            print("f({:.8f}) = {:.8f}".format(xp, result))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")