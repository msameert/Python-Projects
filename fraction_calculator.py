""" What is a Fraction?
 A fraction is a way of representing a part of a whole:
 numerator/denominator
 Example:

 \frac{2}{4} \] means 2 parts out of 4. 🔹 Why Reduce to Lowest Form? 
 We reduce a fraction to lowest form (simplest form) to make it **clear, standardized, and easier to compare**.
 1. Fractions can look different but mean the same thing \[ \frac{2}{4} = \frac{1}{2}
 Both represent the same quantity: half.
 But 1/2 is simpler and standard.
  
   Imagine comparing:
      4/8 and 3/6
      if we reduce both then both has 1/2 
      
      Reducing to lowest terms makes fractions:
      ~Easier to understand
      ~Easier to compare
      ~The standard, clean representation"""

import math

class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()   # this function simplifies the fraction with GCD Greatest Common Divisor, If it's 8/12 then GCD for both is 4, and simplified version is 2/3

    
    
    def simplify(self,):
        gcd = math.gcd(self.numerator, self.denominator)   #this gets the GCD of fractions like if fraction is 8/12 then GCD is 4
        self.numerator = self.numerator // gcd  # this divides numerator with GCD 
        self.denominator = self.denominator // gcd # this divides denominator with GCD

    def __str__(self): # this controls the formation of output - when terminal is going to give output - it looks for this function to find the format 
        return f"{self.numerator}/{self.denominator}"   # format here is numerator/denominator
    
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fractions(num, den)  
    
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fractions(num, den)
    
    def __mul__(self, other):
        return Fractions(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __truediv__(self, other):
        return Fractions(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator
    
f1 = Fractions(8,12)
f2 = Fractions(3,6)

print("f1:", f1)
print("f2:", f2)

print("Add :", f1 + f2)
print("Sub :", f1 - f2)
print("Multiply :", f1 * f2)
print("Divide :", f1/f2)
print("Equal :", f1 == f2)
print("less than", f1 < f2)
    
