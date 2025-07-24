from datetime import date
import time
import msvcrt  # espera una telca determinada en mi caso enter

# --- FUNCTIONS ---

def greetin_and_date():  # saludo y fecha
    today = date.today()
    print(f"Hello Facu SNIPER, the hunting date is {today}")  # hola facu sniper la fecha de caza es "fecha actual"

def what_do_you_wants():  # que deseas?
    question = input("¿What do you wants to hunt today? ")  # ¿Que te apetece cazar hoy?
    return question

def menu():
    option_menu = input("--Doors--\n1)new study session\n2)weekly report\n3)month report\n4)Exit\nselect an option: ")  # nueva sesion de estudio #reporte semanal #reporte mensual #salir
    return option_menu

def option_one():
    enter = input("Press ENTER to start the time. After press ENTER to end timing ")  # Apreta ENTER para iniciar el tiempo
    return enter

def validate_password():  # validación de contraseña
    key = "programming"
    while True: #se sigue imprimiendo si es falsa, con el verdadero corta el break
        program = what_do_you_wants()
        if program == key:
            print("Access confirmed\nEntering...")  # Acceso confirmado entrando
            break
        else:
            print("Mistake. Access denied.")  # Error. Acceso denegado

def validate_menu_option(option):  # validacion de opcion del menu
    if option.isdigit():
        option_num = int(option)
        if 1 <= option_num <= 4:
            return option_num
    return None

def chronometer():  # cronometro que se detiene con ENTER
    start = time.time()
    print("Timing started. Press ENTER to stop...")

    while True:
        elapsed = int(time.time() - start)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        print(f"\r⏱ {hours:02}:{minutes:02}:{seconds:02}", end="")  # \r borra la linea anterior y se sobreescribe. formateo para que los numeros tengan 2 digitos siempre. END BUENARDO NO SALTA DE LINEA
        time.sleep(1) #espera un segundo con ese 1, asi es tiempo real

        if msvcrt.kbhit():  # cortar
            key = msvcrt.getch()
            if key == b'\r':  # ENTER
                break

    end = time.time()
    duration = int(end - start)
    return duration

def process_option_one():  # logica de la opcion 1
    enter = option_one()
    if enter == "":
        duration = chronometer()
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        print(f"\nStudy session duration: {hours}h {minutes}m {seconds}s.")
    else:
        print("Paused. You must press only ENTER.")  # tiempo pausado

#LOGIC

greetin_and_date() 
validate_password() 

while True:
    option = menu()
    option_num = validate_menu_option(option)

    if option_num == 1:
        process_option_one()
    elif option_num == 2:
        print("Weekly report (coming soon).")
    elif option_num == 3:
        print("Monthly report (coming soon).")
    elif option_num == 4:
        print("Bye see you later") #chau hasta luego
        break
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
