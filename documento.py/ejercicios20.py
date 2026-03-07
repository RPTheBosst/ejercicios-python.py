#Crea una historia donde cada decisión (izquierda/derecha) lleve a una nueva pregunta anidada, hasta llegar a un final diferente según las elecciones del usuario con 6 niveles de cada pregunta.
print("Bienvenido a la aventura de las decisiones. Cada elección que hagas te llevará a un nuevo camino. ¡Buena suerte!")
print("estas explorando nuevos lugares pero te topas con dos caminos: ¿Quieres ir a la izquierda (1) o a la derecha (0)?")
decision1 = int(input())
if decision1 == 1:
    print("Has elegido ir a la izquierda. adentrarte en un bosque oscuro y encuentras una cueva. ¿Quieres entrar en la cueva (1) o seguir caminando por el bosque (0)?")
    decision2 = int(input())
    if decision2 == 1:
        print("Has entrado en la cueva pero te encuentras con un oso pero no tienes nada para defenderte. ¡Has perdido!")
        
        print("has perdido, vuelve a intentarlo")
    elif decision2 == 0:
        print("Sigues caminando por el bosque y te encuentras con un lobo, a lo lejos puedes ver una rama grande pero pesada. ¿Quieres usar la rama para defenderte (1) o correr (0)?")
        decision3 = int(input())
        if decision3 == 1:
            print("Usaste la rama para defenderte y logras ahuyentar al lobo. pero te lastimaste y no puedes seguir caminando, pero ves una cabaña a lo lejos. ¿Quieres ir a la cabaña adescansar (1) o quedarte donde estás (0)?: ")
        elif decision3 == 0:
            print("Decides correr pero el lobo te alcanza y te muerde. ¡Has perdido!")
            decision4 = int(input())
            if decision4 == 1:
                print("Has llegado a la cabaña y encuentras a un anciano amable que te ofrece comida y refugio. Pasas la noche allí y al día siguiente te sientes renovado. ya puedes seguir tu camino, pero el anciano te advierte que el bosque es peligroso. ¿Quieres seguir su consejo y salir del bosque (1) o quedarte a explorar más (0)?")
                if decision5 == int(input()):
                    if decision5 == 1:
                       print("Has decidido salir del bosque y regresar a casa. ¡Felicidades, has ganado!")
                    elif decision5 == 0:
                       print("Has decidido quedarte a explorar más el bosque. pero el anciano tenía razón, el bosque es peligroso. ¡Has perdido!")
elif decision1 == 0:
    print("Has elegido ir a la derecha. ¿Quieres cruzar el río (1) o subir la montaña (0)?")
    decision2 = int(input())
    if decision2 == 1:
        print("Has cruzado el río y encuentras un puente muy largo pero seguro estas cansado para seguir pero tienes mucha hambre y quieres saber si del otro lado hay comida. ¿Quieres cruzarlo (1) o seguir por el camino (0)?")
        decision3 = int(input())
        if decision3 == 1:
            print("Has cruzado el puente y encuentras un castillo. qué quieres hacer? Entrar (1) o seguir caminando (0)?")
        elif decision3 == 0:
            print("Decides seguir por el camino pero te encuentras con un oso y no tienes nada para defenderte. ¡Has perdido!")
            decision4 = int(input())
            if decision4 == 1:
                print("Has entrado al castillo y encuentras un dragón. ¿Quieres luchar (1) o huir (0)?")
            elif decision4 == 0:
                print("Decides huir pero te pierdes en el bosque y nunca encuentras el camino de regreso. ¡Has perdido!")
                decision5 = int(input())
                if decision5 == 1:
                    print("luchaste valientemente y derrotaste al dragón. ahora eres el nuevo rey del castillo. al fondo se ve un tesoro. ¿Quieres ir por el tesoro (1) o quedarte en el castillo (0)?")
                elif decision5 == 0:
                    print("Decides quedarte en el castillo pero el dragón te encuentra y te devora vivo. ¡Has perdido!")
                    decision6 = int(input())
                    if decision6 == 1: 
                        print("Has encontrado el tesoro, ricas comida natural y junto a el hay un mapa de regreso a tu hogar. Ademas te conviertes en la persona más rica del reino. ¡Felicidades, has ganado!")
                    else:
                        print("Decides quedarte en el castillo y vivir una vida tranquila como rey, pero te quedaste sin comida y agua, por lo que eventualmente mueres de hambre. ¡Has perdido!")
else:
    print("no puedes continuar tu aventura por otros caminos, intentalo de nuevo")