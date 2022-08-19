Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d["name"]="abc"
>>> print(d)
{'name': 'abc'}
>>> d["roll"]="123"
>>> print(d)
{'name': 'abc', 'roll': '123'}
>>> d["roll"]=1
>>> print(d)
{'name': 'abc', 'roll': 1}
>>> d.keys()
dict_keys(['name', 'roll'])
>>> print(d.keys())
dict_keys(['name', 'roll'])
>>> d.values()
dict_values(['abc', 1])
>>> print(d.value())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(d.value())
AttributeError: 'dict' object has no attribute 'value'
>>> print(d.values())
dict_values(['abc', 1])
>>> d.items()
dict_items([('name', 'abc'), ('roll', 1)])
>>> d["num"]=99899
>>> print(d)
{'name': 'abc', 'roll': 1, 'num': 99899}
>>> del(d["name"])
>>> print(d)
{'roll': 1, 'num': 99899}
>>> d.pop("roll")
1
>>> print(d)
{'num': 99899}
>>> d.get("num")
99899
>>> 
