"""

Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

"""


def to_jaden_case(string):

    #First character make capital
    if string[0] == " ":
        jadeString = " "
    else:
        jadeString = string[0].capitalize()
    #If space make next character capital


    stringg="aaaa"
    tab=[]
    tab.append(stringg)
    print(string[0])
    print()
    return jadeString

to_jaden_case("cycki")
