# ---- studies ----
# The sum() function returns the sum of the items in the iterable 
#which is passed as its argument.
test1 = lambda x: x * 2
print(sum(map(test1, [2,3,5,8])))

test2 = lambda x: x * 2
#To obtain a readable output to turn the map object into a list.
print(list(map(test2, [2, 3, 5, 8])))

#filter() takes a function as its first argument and an iterable 
#as its second argument.
 #filter(my_function, my_list)

# A while loop runs a portion of code as long as a 
#specified condition is True.
#while condition:
   # <code>

#The float() function takes a string or an integer number 
#as argument and returns a floating point number.

# ------ List Comprehension is a way to construct a new Python list ----
# -------from an iterable types: lists, tuples, and strings ------

# .isupper() string method to check if a character is uppercase.
#returns True if the character is uppercase and False if it is not

# .lower() string method to convert uppercase characters to lowercase characters

# .append()adds a given object to the end 

#The join method works by concatenating each element of a list into a
#string, separated by a designated string, known as the separator.
# result_string = ''.join(characters)

#The strip() removes any leading and trailing underscore.
# clean_string = original_string.strip('_')

#A basic list comprehension consists of an expression followed by a for clause:
# spam = [i * 2 for i in iterable]

# differently from the if clause, the if/else construct
#must be placed between the expression and the for keyword.
# spam = [i * 2 if i > 0 else -1 for i in iterable]

#The raise statement allows you to force a specific exception to occur.
#It consists of the raise keyword followed by the exception type, and
#enables you to provide a custom error message:
# raise ValueError("Invalid value") 

# In Python, the max() function returns the largest of the input values.
# max(1, 2, 3) # Output: 3

#   the range function, which generates a sequence of numbers you can iterate over. The syntax is range(start, stop,
#step), where start is the starting integer (inclusive), stop is the last
#integer (not inclusive), and step is the difference between a number
#and the previous one in the sequence.
#  Also, use _ as a loop variable. The _ acts as a placeholder and is useful
#when you need to use a variable but don't actually need its value.


def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        # Обработка положительных чисел, отличных от 1 и 0
        low = 0
        high = square_target
        iteration = 0

        while iteration < max_iterations:
            guess = (low + high) / 2
            guess_squared = guess ** 2

            if abs(guess_squared - square_target) <= tolerance:
                root = guess
                print(f'The square root of {square_target} is approximately {root}')
                break

            if guess_squared < square_target:
                low = guess
            else:
                high = guess

            iteration += 1

        if iteration == max_iterations:
            print('Maximum number of iterations reached without finding the result.')

# --------- The regex pattern -----------

# The choice() function from the random module takes a sequence and returns a random item of the sequence.

# The compile() function from the re module compiles the string passed as the argument into a regular
# expression object that can be used by other re methods.

# The search() function from the re module analyzes the string passed as the argument looking
# for the first place where the regex pattern matches the string.

# The findall() function from the re module. It's similar to search but it returns a list with 
# all the occurrences of the matched pattern.

# The caret, ^, placed at the beginning of the character class, matches all the characters
#  except those specified in the class.

# The character class \d is a shorthand for [0-9]. Replace this character class with the
#  shorthand inside your first constraint tuple.

#In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. 
# Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W


#------------ Shortest Path algorithm -----------

# So far, you have already met different data types:

#    Immutable data types, such as integers, strings, tuples, and Booleans.
#    Mutable data types, such as lists, and dictionaries.
#    A dictionary is identified by a pair of curly braces, {}.

# Dictionaries store data in the form of key-value pairs

# my_dict = {
#     'name': 'Michael',
#     'occupation': 'Lumberjack'
# }
# my_dict['name'] # 'Michael' You can access the data stored in a dictionary through its keys
# my_dict['food'] = 'hay' #The same syntax can be used to change the value of an existing key.
# if you want to be able to go through the key-value pairs, you can use the .items() method.

# Dictionary comprehensions support conditional if/else syntax too:
# {key: val_1 if condition else val_2 for key in dict}

# min() function. It returns the smallest item from the iterable passed as the argument.

# The .remove() method removes from a list the first matching element that is passed as the argument
# my_list = ['larch', 1, True, 1]
# my_list.remove(1)
# print(my_list) # Output: ['larch', True, 1]

# ------------------- 
#You can use the __name__ variable to determine if a Python script is being run as the main 
# program or if it is being imported as a module (code written in another Python file).
#If the value of __name__ is set to '__main__', it implies that the current script is the main
# program, and not a module.

# ---------- Class Object

#class ClassName:
#    def method_name(self):
#       pass

#instance_name.method_name()

# The enumerate built-in function takes an iterable as its argument
# and returns an enumerate object you can iterate over. It provides 
# the count (which by default starts at zero) and the value from the 
# iterable.
#iterable = ['a', 'b', 'c']
#for i, j in enumerate(iterable):
#    print(i, j)
# The loop from the example above would output the tuples 0, a, 1, b, and 2, c.
