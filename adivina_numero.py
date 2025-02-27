import random

print("\n🎯 ¡Bienvenido al Juego de Adivina el Número!")
print("🔢 He elegido un número del 1 al 100, ¿Podrás adivinarlo?\n")


while True:

    numero_adivinar = random.randint(1, 100)
    intentos = 0
    historial_numeros = []

    print("1. Modo Facil")
    print("2. Modo Normal")
    print("3. Modo Dificil")

    while True:
        
        opcion = input("\nElije un modo de juego (1-3): ")
        
        if opcion == '1':
            max_intentos = 20
            break
        elif opcion == '2':
            max_intentos = 10
            break
        elif opcion == '3':
            max_intentos = 5
            break
        else:
            print("❌ Opcion invalida. Intenta de nuevo")

        
    while intentos < max_intentos:

        try:
            adivinar = int(input("\n➡ Ingresa un número: "))
            intentos += 1
            historial_numeros.append(adivinar)

            if adivinar > numero_adivinar:
                print("📉 El número es menor. ¡Intenta de nuevo!")
            elif adivinar < numero_adivinar:
                print("📈 El número es mayor. ¡Intenta de nuevo!")
            else:
                print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos. 🥳")
                break 

            print(f"📜 Historial de intentos: {historial_numeros}")
            print(f"🕰  Intentos usados: {intentos}/{max_intentos}")
            print("--" * 30)

        except ValueError:
            print("❌ Número inválido, ingresa un número válido.")
            
        if intentos == max_intentos and adivinar != numero_adivinar:
            print("😢 ¡Llegaste al límite de intentos! Perdiste.")
            print(f"🔢 El número correcto era: {numero_adivinar}")
    
    jugar_otravez = input("Quieres jugar otra vez? (s/n): ").lower()
    if jugar_otravez != 's':
        print("👋 ¡Gracias por jugar! Hasta la próxima. 😊")
        break

    



