class fraction:
    """
    A class to represent fractions and perform basic arithmetic operations.
    
    Attributes:
        num (int): The numerator of the fraction
        den (int): The denominator of the fraction
    """
    
    def __init__(self, n, d):
        """
        Initialize a fraction with numerator and denominator.
        
        Args:
            n (int): Numerator
            d (int): Denominator
            
        Raises:
            ValueError: If denominator is zero
        """
        if d == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = n
        self.den = d
    
    def __str__(self):
        """
        Return string representation of the fraction.
        
        Returns:
            str: Fraction in the format "numerator/denominator"
        """
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        """
        Add two fractions.
        
        Formula: a/b + c/d = (a*d + b*c) / (b*d)
        
        Args:
            other (fraction): The fraction to add
            
        Returns:
            fraction: The sum of the two fractions
        """
        temp_num = (self.num * other.den) + (self.den * other.num)
        temp_den = (self.den * other.den)
        return fraction(temp_num, temp_den)
    
    def __sub__(self, other):
        """
        Subtract one fraction from another.
        
        Formula: a/b - c/d = (a*d - b*c) / (b*d)
        
        Args:
            other (fraction): The fraction to subtract
            
        Returns:
            fraction: The difference of the two fractions
        """
        temp_num = (self.num * other.den) - (self.den * other.num)
        temp_den = (self.den * other.den)
        return fraction(temp_num, temp_den)
    
    def __mul__(self, other):
        """
        Multiply two fractions.
        
        Formula: a/b * c/d = (a*c) / (b*d)
        
        Args:
            other (fraction): The fraction to multiply by
            
        Returns:
            fraction: The product of the two fractions
        """
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return fraction(temp_num, temp_den)
    
    def __truediv__(self, other):
        """
        Divide one fraction by another.
        
        Formula: (a/b) / (c/d) = (a*d) / (b*c)
        
        Args:
            other (fraction): The fraction to divide by
            
        Returns:
            fraction: The quotient of the two fractions
            
        Raises:
            ValueError: If dividing by a fraction with numerator of zero
        """
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return fraction(temp_num, temp_den)


# Example usage
if __name__ == "__main__":
    # Create fractions
    f1 = fraction(1, 2)  # 1/2
    f2 = fraction(1, 3)  # 1/3
    
    # Test operations
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")