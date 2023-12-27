try:
   x = 5 / 0
except Exception as e:
   print( str(e) )

try:
   x = 5 / 0
except (Exception,ArithmeticError,TypeError) as e:
   print( str(e), type(e) )
