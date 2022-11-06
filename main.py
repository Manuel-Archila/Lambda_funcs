alpha = lambda x: x + 1 
beta = lambda x: 2 * x 

zero = lambda f: lambda x: x
one = lambda f: lambda x: f(x)
two = lambda f: lambda x: f(f(x))
three = lambda f: lambda x: f(f(f(x)))
successor = lambda n: lambda f: lambda x: f(n(f)(x))
addition = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
multiplication = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)
power = lambda m: lambda n: lambda f: lambda x: n(m)(f)(x)

print("2^3 =", power(two)(three)(alpha)(0))
print("2 + 3 =", addition(two)(three)(alpha)(0))
print("2 * 3 =", multiplication(two)(three)(alpha)(0))
print("El sucesor de 3 es: ", successor(three)(alpha)(0))