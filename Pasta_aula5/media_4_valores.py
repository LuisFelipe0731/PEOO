def Media_aritmetica(a,b,c,d):
    media = (a + b + c + d)/4
    print(media)
    print("Números menores que a media")
    if a < media:
        print(a)
    if b < media:
        print(b)
    if c < media:
        print(c)
    if d < media:
        print(d)
    print("Números maiores ou iguais a media")
    if a >= media:
        print(a)
    if b >=  media:
        print(b)
    if c >=  media:
        print(c)
    if d >=  media:
        print(d)

Media_aritmetica(25,9,100,4)
