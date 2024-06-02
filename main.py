class EuclideanAlgorithm:
    """
    A class to encapsulate the Euclidean Algorithm for finding the greatest common divisor (GCD).
    """

    def __init__(self, a, b):
        """
        Initializes the EuclideanAlgorithm class with two integers a and b.

        Parameters:
        a (int): The first integer
        b (int): The second integer
        """
        self.a = a
        self.b = b

    def compute_gcd(self):
        """
        Computes the greatest common divisor (GCD) of the two integers using the Euclidean Algorithm.

        Returns:
        int: The GCD of the two integers
        """
        a, b = self.a, self.b

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a


def get_valid_input(prompt):
    """
    Prompts the user for input and validates that it is a positive integer.

    Parameters:
    prompt (str): The prompt message to display to the user.

    Returns:
    int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    # Get valid inputs from the user
    a = get_valid_input("Enter the first positive integer: ")
    b = get_valid_input("Enter the second positive integer: ")

    # Initialize the EuclideanAlgorithm class with the inputs
    euclidean_algo = EuclideanAlgorithm(a, b)

    # Compute the GCD
    gcd = euclidean_algo.compute_gcd()

    # Print the result
    print(f"The GCD of {a} and {b} is: {gcd}")

