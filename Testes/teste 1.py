def media(x, y):
    media = (x + y) / 2
    return media
    
def main():
    a = 5
    b = 7
    print(f'a: {a}, b: {b}')
    print("Media: ", media(a,b))
    print("Media: ", media(6,5))
    print("Media: ", media(6,a))

main()