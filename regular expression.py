
#This checks if the string starts with "The" and ends with "Spain".
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes, the string matches the pattern!")
else:
    print("No match found.")

#Finds all matches in a string and returns them as a list.
import re
txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)

#Searches for the first match and returns a Match object.
#If found, you can use .group() to show the matched text.
import re

txt = "My number is 12345"
x = re.search(r"\d", txt)   # \d means any digit
print("Matched text:", x.group())
print("Position:", x.start())
#Splits the string at each match and returns a list.
import re
txt = "The rain in Spain"
x = re.split(r"\s",txt)   # \s means whitespace
print(x)
#Replaces matches with another text
import re
txt = "The rain in Spain"
x = re.sub(r"\s","45",txt)
print(x)
#[] → Matches any one character inside the brackets
import re

txt = "bat, bet, bit, but, bot"
x = re.findall("b[aeiou]t", txt)
print(x)

#Groups in Regular Expressions
import re

text = 'Amity University was established on 2014-05-12.'
#This pattern means: 4 digits - 2 digits - 2 digits
pattern = r'(\d{4})-(\d{2})-(\d{2})'
match = re.search(pattern,text)
if match :
    print('full date:',match.group(0))  # Whole match
    print('year:',match.group(1))  # First group (\d{4})
    print('Month:',match.group(2)) # second group (\d{2})
    print('Day:',match.group(3))    # third group (\d{2})
 #Named Groups
import re

text = 'Date: 2025-10-08'
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'

match = re.search(pattern, text)
if match:
    print('Year:', match.group('year'))
    print('Month:', match.group('month'))
    print('Day:', match.group('day'))
#accessing name group as dictionary\import re

text = 'Name: Vikram, Age: 30'

# Using named groups: (?P<name>pattern)
pattern = r'Name: (?P<name>\w+), Age: (?P<age>\d+)'

match = re.search(pattern, text)

if match:
    print(match.groupdict())   # Converts groups into a dictionary


