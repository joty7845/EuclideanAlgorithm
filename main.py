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


# Example usage
if __name__ == "__main__":
    # Initialize with two integers
    euclidean_algo = EuclideanAlgorithm(66, 8)

    # Compute the GCD
    gcd = euclidean_algo.compute_gcd()

    # Print the result
    print(f"The GCD of 48 and 18 is: {gcd}")
