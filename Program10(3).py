celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
above_100 = list(filter(lambda f: f > 100, fahrenheit))
print(fahrenheit)
print(above_100)
