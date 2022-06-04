avengers = ['hawkeye'
,
'iron man'
,
'thor'
,
'quicksilver']
names = ['barton'
,
'stark'
,
'odinson'
,
'maximoff']
z = zip(avengers, names)
[array1 , *fish] =  z
print(fish,array1)

array1 = [ num for num in range(10) if num %2 == 0]
pairs_2 = [(num1, num2) for num1 in range(0, 2)  for num2 in range(6,10)]
print(pairs_2)
print(array1)

pairs_3 = {num1 :[num1, num2] for num1 in range(0, 2) for num2 in range(6,10)}
print(pairs_3)


iter_pairs_2 = iter(pairs_2)
print(next(iter_pairs_2))
print(next(iter_pairs_2))
print(next(iter_pairs_2))
number = 90.41890417471841
print(f"In the last 2 years, {number:.2}% of the data was produced worldwide!")
name = "Python"
print(f"Python is called {name!r} due to a comedy series")

favorite = dict(flavor="chocolate")
my_string = Template('I love $flavor $cake very much')
my_string.substitute(favorite)

print(my_string)