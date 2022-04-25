tup = (32, 65, 87, 22, 54)
tup
(32, 65, 87, 22, 54)
tup[1]
65

tup[1] = 55
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1] = 55
TypeError: 'tuple' object does not support item assignment

re = (43, 'ny', 4.5)
type(re)
<class 'tuple'>

s = {24,45,42,76,22}
s
{22, 24, 42, 76, 45}
s
{22, 24, 42, 76, 45}

s = {43,8,76,32,76}
s
{8, 32, 43, 76}
s
{8, 32, 43, 76}

s = {43,8,76,32,76,8}
s
{8, 32, 43, 76}

s[2]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
