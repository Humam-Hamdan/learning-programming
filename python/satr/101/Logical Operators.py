# and
not_raining = True
not_foggy = True
is_sunny = not_raining and not_foggy
print(is_sunny)
# or
is_raining = True
is_foggy = False
not_sunny = is_raining or is_foggy
print(not_sunny)
# not
is_student = True
print(not is_student)
# and - or - not
first, second = True, False
and_result = first and second  # False
or_result = first or second  # True
not_result = not first  # False
print(and_result)
print(or_result)
print(not_result)