grope1 = {"رضا", "محمد", "زهرا", "علی"}
grope2 = {"نگار", "سارا", "رضا", "محمد"}

grope1.add("امیر")

grope1.add("زهرا")

print(len(grope1))

print("محمد" in grope1)

print(grope1.union(grope2))

print(grope1.intersection(grope2))

numbers = [5, 8, 3, 8, 2, 5, 10, 3, 7]
numbers = set(numbers)
print(numbers)