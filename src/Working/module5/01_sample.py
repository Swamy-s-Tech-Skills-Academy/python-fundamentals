Examining Strings Specifically
hello data science
  File "<ipython-input-31-9198726a718e>", line 1
    hello data science
          ^
SyntaxError: invalid syntax
# hello data science
type(987)
int
type("987")
str
"hello" + "data"
'hellodata'
"hello" + " data"
'hello data'
"hello" + " " + "data"
'hello data'
"hello" - " data"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-38-39f747ae0cc1> in <module>
----> 1 "hello" - " data"

TypeError: unsupported operand type(s) for -: 'str' and 'str'
"hello" * 3
'hellohellohello'
"hello" * "hello"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-41-310ddd446689> in <module>
----> 1 "hello" * "hello"

TypeError: can't multiply sequence by non-int of type 'str'
"hello" / 3
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-97438562d2ed> in <module>
----> 1 "hello" / 3

TypeError: unsupported operand type(s) for /: 'str' and 'int'
