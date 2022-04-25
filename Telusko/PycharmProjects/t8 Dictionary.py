data = {1:'Darshil', 2:'Tejas', 3:Navin}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    data = {1:'Darshil', 2:'Tejas', 3:Navin}
NameError: name 'Navin' is not defined

data = {1:'Darshil', 2:'Tejas', 3:'Navin'}
data[4]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[4]
KeyError: 4

data[3]
'Navin'
data[1]
'Darshil'
data.get(1)
'Darshil'
data.get(3)
'Navin'
data.get(4)
print(data.get(4))
None
data.get(4,'Not Found')
'Not Found'

keys = ['Navin', 'Darshil', 'Tejas']
values = ['c', 'python', 'java']
data = dict(zip(keys, values))
data
{'Navin': 'c', 'Darshil': 'python', 'Tejas': 'java'}

data['Darshil']
'python'

data['Smit'] = 'cs'
data
{'Navin': 'c', 'Darshil': 'python', 'Tejas': 'java', 'Smit': 'cs'}

del data['Darshil']
data
{'Navin': 'c', 'Tejas': 'java', 'Smit': 'cs'}

prog = {'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'sublime'], 'java': {'jse': 'netbeans', 'jee' : 'eclipse'}}
prog
{'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'sublime'], 'java': {'jse': 'netbeans', 'jee': 'eclipse'}}
prog['js']
'atom'

prog[python]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    prog[python]
NameError: name 'python' is not defined

prog['python']
['pycharm', 'sublime']
prog['python'][1]
'sublime'

prog['java']['jse']
'netbeans'
