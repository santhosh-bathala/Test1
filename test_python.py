# What is iterator?
# An object that produces successive values from an iterable. You can create an iterator from an iterable using the built-in iter() function.
my_list = [1, 2, 3, 'Numbers']
my_iter = iter(my_list)
# for a in my_iter:
#  print(a)
print(next(my_iter))
print(next(my_iter))

# What is Generator
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))
