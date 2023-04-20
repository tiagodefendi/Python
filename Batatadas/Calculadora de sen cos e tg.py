import math
x=float(input('Qual o valor do ângulo? '))
xa=math.radians(x)
sen=math.sin(xa)
cos=math.cos(xa)
tg=math.tan(xa)
print(f'O valor do seno é {sen:.2f}, do cosseno é {cos:.2f}, e da tangente é {tg:.2f}.')