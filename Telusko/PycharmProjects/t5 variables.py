x = 2
x + 2
4

y = 4
x + y
6

x = 9
x + y
13
x
9

abc
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'?

x + 10
19
_ + y
23

name = 'youtube'
name
'youtube'

name + ' rocks'
'youtube rocks'

name + ' ' + 'rocks'
'youtube rocks'

name ' rocks'
SyntaxError: invalid syntax

name[0]
'y'
name[6]
'e'
name[8]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'e'
name[-2]
'b'
name[-7]
'y'
name[0:2]
'yo'
name[1:4]
'out'
name[1:]
'outube'
name[:4]
'yout'
name[3:10]
'tube'

name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment

name[0] = 'my'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name[0] = 'my'
TypeError: 'str' object does not support item assignment

'my' + name[3:]
'mytube'

myname = 'darshil jayani'
len(myname)
14
