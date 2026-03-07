#Recomienda géneros de películas según edad y dinero disponible para gastar en el cine.
print("Recomienda géneros de películas según edad y dinero disponible para gastar en el cine.")
print("ingresa tu edad: ")
edad = int(input())
print("ingresa el dinero disponible para gastar en el cine")
dinero = float(input())
if edad < 13:
    if dinero < 5:
        print("Te recomendamos ver películas de animación o comed   ía infantil.")
    else:
        print("Puedes disfrutar de películas de animación, comedia infantil o incluso algunas películas de aventuras.")
elif 13 <= edad < 18:
    if dinero < 5:
        print("Te recomendamos ver películas de comedia adolescente o acción ligera.")
    else:
        print("Puedes disfrutar de películas de comedia adolescente, acción, aventura o incluso algunas películas de ciencia ficción.")
else:
        print("Puedes disfrutar de una amplia variedad de géneros, incluyendo comedia, drama, acción, ciencia ficción, terror y más.")
