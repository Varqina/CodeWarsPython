"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0."""

def expanded_form(num):
    number_string = str(num)
    return_string = ""
    counter = 0
    for i in range(len(number_string) - 1, 0, -1):
        if number_string[i] != "0":
            print(number_string[i])
            return_string = number_string[i] * (10 ** counter) + return_string
            if i != len(number_string) - 1:
                return_string = " + " + return_string
            counter += 1
    return return_string


print(expanded_form(12))
