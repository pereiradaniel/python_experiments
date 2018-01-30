# not is evaluated first
# and is evaluated next
# or is evaluated last

# bool_one analyzed
bool_one = False or not True and True
# bool_one evaluates to False
bool_one_not = not True
# bool_one_not evaluates to False
bool_one_and = False and True
# bool_one_and evaluates to False
bool_one_or = False or False
# bool_one_or evaluates to False
# Final value for total equation is False

# bool_two analyzed
bool_two = False and not True or True
# bool_two evaluates to True
bool_two_not = not True
# bool_two_not evaluates to False
bool_two_and = False and not True
# bool_two_and evaluates to False
bool_two_or = False or True
# bool_two_or evaluates to True
# Final value for equation is True

