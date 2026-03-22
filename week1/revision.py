#Create Variables 

a = 10
b = 5.5
name = "Rima"
is_active = True

print(a, b, name, is_active)


#Use Lists 
fruits= ['apple', 'banana', 'cherry']
fruits.append('orange')    # Add element
print(fruits[0])           # Access element
print(fruits[-1])          # Last element


#Use Dictionaries 
student = {
    'name' : 'Rima',
    'age' : '33',
    'subjects' : ["Math", "English"]
 }


print(student["name"])         # Access value
student["grade"] = "A"        # Add new key-value

# while loops 
# For loop
for fruit in fruits:
    print(fruit)

#While loop
count = 0
while count < 3 :
    print(count)
    count += 1


#function

def greet(name):
    return f"Hello , {name} !"

print(greet("Rima"))

#Use If/Else
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Handle Errors
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This runs anyway.")