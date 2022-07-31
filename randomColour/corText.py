import random
from sty import fg

def gerarRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return(red,green,blue)



def gerarCor(red,green,blue):
    return fg(red,green,blue)


def gerarDIff():
    red,green,blue=gerarRGB()
    colour = gerarCor(red,green,blue)
    return(colour)

print(gerarDIff(), "Texto",gerarDIff(),"Colorido")




