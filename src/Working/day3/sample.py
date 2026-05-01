Performing Complex Assignment to Variables
april = 30
june = 30
september = 30
november = 30
print(april)
print(june)
print(september)
print(november)
30
30
30
30
january = march = may = july = august = october = december = 31
print(august)
31
print(december)
31
python, java = "data", "science"
print(python)
data
print(java)
science
Type Conversion
a = "september"
b = 9
c = 5.8
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
converted_b = str(b)
converted_b
'9'
print(type(converted_b))
<class 'str'>
converted_c = int(c)
converted_d = float(d)
converted_c
5
converted_d
1.0
print(type(converted_c))
print(type(converted_d))
<class 'int'>
<class 'float'>
a
'september'
converted_a = int(a)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-93-10a35ec17c61> in <module>
----> 1 converted_a = int(a)

ValueError: invalid literal for int() with base 10: 'september'
e = "8"
converted_e = int(e)
print(type(converted_e))
<class 'int'>
