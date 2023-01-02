# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('X = '))
Y = int(input('Y = '))
Z = int(input('Z = '))
if (X == 0 or X == 1) and (Y == 0 or Y == 1) and (Z == 0 or Z == 1):
   res1 = not (X or Y or Z)
   res2 = (not X) and (not Y) and (not Z)
   result = res1 == res2
   if result:
      print('Для введенных значений предикат утверждение истинно')
   else:
      print('Для введенных значений предикат утверждение ложно')
else:
  print('Введены недопустимые значения предикат')