import random

numero_adivinar = random.randint(1, 100)
intentos = 0
historial_numeros = []
max_intentos = 10

print("--" * 30)
print("🎯 ¡Bienvenido al Juego de Adivina el Número!")
print("🔢 He elegido un número del 1 al 100, ¿Podrás adivinarlo?")
print("--" * 30)

while intentos < max_intentos:
    try:
        adivinar = int(input("➡ Ingresa un número: "))
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


