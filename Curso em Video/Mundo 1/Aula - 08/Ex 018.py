from math import radians,sin,cos,tan
x=float(input('Qual o valor do ângulo? '))
xa=radians(x)
sen=sin(xa)
cos=cos(xa)
tg=tan(xa)
print(f'O valor do seno é {sen:.2f}, do cosseno é {cos:.2f}, e da tangente é {tg:.2f}.')
