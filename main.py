### PART 1 - String comparisons
#
# Comparison is defined on strings! That means that there are overloads for:
#  < : (String, String) --> Boolean
#  =< : (String, String) --> Boolean
#  > : (String, String) --> Boolean
#  >= : (String, String) --> Boolean
#
# But, what logic do they do? That's up to you to find out!

# Your goal - set the values of first, second, third, and fourth
# Such that first < second < third < fourth.

# TODO(you) - set the values of these.
# Any four strings such that first < second < third < fourth.
first = ""
second = ""
third = ""
fourth = ""

# TODO(you) - answer the following question:
# Note that you may need to find multiple valid sets of four
# as well as disprove some hypotheses to find the correct answer.
#
# I think strings are compared by [your answer]

# No need to change these.
print("Part 1 - String comparison:")
print("First: " + first)
print("Second: " + second)
print("Third: " + third)
print("Fourth: " + fourth)
print("First < Second: " + str(first < second))
print("Second < Third: " + str(second < third))
print("Third < Fourth: " + str(third < fourth))
print("")

### PART 2 - int(...) casting
#
# The int(...) method turns whatever you give it into an integer (if it can).
# This works on strings that look like ints (like "2"), but not on strings like 
# "Hello".
#
# On floats, int(...) always works. But, it's not immediately clear what it does.
# Consider the output of these statements:

# No need to change these.
print("Part 2 - int(...) casting")
print("int(2.3) = " + str(int(2.3)))
print("int(2.9) = " + str(int(2.9)))
print("int(-1.2) = " + str(int(-1.2)))
print("int(-4.6) = " + str(int(-4.6)))
print("")

# TODO(you) - answer the following question:
# I think int(...) transforms a float to an int by ...

### PART 3 - bool(...) casting
#
# The bool(...) method turns whatever you give it into an integer (if it can).
# This works on just about (I think) * ever * single type.
# The question then becomes, which values convert to True and which to False?

# To get you started, for ints you could say...

# An int value that converts to True.
trueInt = 1
# An int value that converts to False.
falseInt = 0

# TODO(you) - fill in the rest of these. (Replacing None.)

# A float value that converts to True.
trueFloat = None
# A float value that converts to False.
falseFloat = None

# A string value that converts to True.
trueString = None
# A string value that converts to False.
falseString = None

# No need to change these.
print("Part 3 - bool(...) casting")
print("True Int: " + str(trueInt) + " = " + str(bool(trueInt)))
print("False Int: " + str(falseInt) + " = " + str(bool(falseInt)))
print("True Float: " + str(trueFloat) + " = " + str(bool(trueFloat)))
print("False Float: " + str(falseFloat) + " = " + str(bool(falseFloat)))
print("True String: " + str(trueString) + " = " + str(bool(trueString)))
print("False String: " + str(falseString) + " = " + str(bool(falseString)))
