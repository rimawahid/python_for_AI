numbers = [1, 2, 3, 4, 5, 6]

# print even numbers
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

odd = [num for num in numbers if num % 2 != 0]

odd_num = len(odd)
even_num = len(even)

sum_odd = sum(odd)

print( 'even :', even)
print( 'odd :', odd)
print( 'odd num :', odd_num)
print( 'even num :', even_num)
print('sum of odd :', sum_odd)