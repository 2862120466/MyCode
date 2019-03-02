import re
some_text = 'a,b,,c,,,d     e'
this_text = 'foobooar'
print(re.split('[, ]+', some_text))
print(re.split('(o)',this_text))