"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case"""

"""Sample Test
Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )"""

def is_isogram(string):
    string=string.lower() #set lower to have same characters O is different than o for count
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True


def web_solution(string):
    return len(string) == len(set(string.lower()))
    #set cannot have same value twice