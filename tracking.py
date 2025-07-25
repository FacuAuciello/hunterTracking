from datetime import date
import time
import msvcrt  # espera una telca determinada en mi caso enter
import json
import os

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

def option_one(): #opcion 1
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

def process_option_one(): #proceso de la opcion 1
    enter = option_one()
    if enter == "":
        duration = chronometer()
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        print(f"\nStudy session duration: {hours}h {minutes}m {seconds}s.")
        
        save_session(duration) #guarda automaticamente
    else:
        print("Paused. You must press only ENTER.")  # tiempo pausado
    

def save_session(duration): #sesiones guardadas
    archive_json = "jj.json" #nombre del archivo donde guardamos las sesiones
    if os.path.exists(archive_json): #si el archivo existe cargamos las sesiones
        with open(archive_json, "r", encoding="utf-8") as archivo:
            sessions = json.load(archivo)
    else:
        sessions = [] #else, si no existe arrancamos con una lista vacia

    new_session = { #nuevo registro de sesion
        "date":date.today().isoformat(),  #fecha actual en formato YYYY-MM-DD
        "duration":duration #duracion en segundos
    }

    sessions.append(new_session) #la nueva sesion se agrega a la lista

    with open(archive_json, "w", encoding="utf-8") as archivo: #se vuelve a guardar todo en el archivo
        json.dump(sessions, archivo, indent=4) #json.dump toma el contenido de la variable sessions y lo escribe en el json
    
    print("Session saved successfully")

def weekly_report():  # informe semanal
    archive_json = "jj.json"

    if not os.path.exists(archive_json):
        print("No study sessions found")  # no se encontraron sesiones de estudio
        return

    with open(archive_json, "r", encoding="utf-8") as archivo:
        sessions = json.load(archivo)

    days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # dias de la semana
    summary = {dia: {"count": 0, "duration": 0, "sessions": []} for dia in days_week}  # resumen

    for sesion in sessions:
        fecha_str = sesion["date"]  # "2025-07-24"
        duration = sesion["duration"]

        fecha = date.fromisoformat(fecha_str) #convertir texto en objeto tipo fecha
        name_day = fecha.strftime("%A")  # Monday, Tuesday...

        if name_day in summary: #actualizar el resumen semanal
            summary[name_day]["count"] += 1
            summary[name_day]["duration"] += duration
            summary[name_day]["sessions"].append(duration)

    print("\nWeekly Report:")

    total_duration = 0
    total_duration_habil = 0  # lunes a viernes

    for i, day in enumerate(days_week):
        count = summary[day]["count"]
        dur = summary[day]["duration"]
        sessions_detail = summary[day]["sessions"]
        hours = dur // 3600
        minutes = (dur % 3600) // 60
        print(f"- {day}: {count} sessions, {hours}h {minutes}m")

        # Detalle de cada sesión
        for idx, duracion in enumerate(sessions_detail, start=1):
            h = duracion // 3600
            m = (duracion % 3600) // 60
            s = duracion % 60
            print(f"   • Session {idx}: {h}h {m}m {s}s")

        total_duration += dur
        if i < 5:  # lunes a viernes
            total_duration_habil += dur

    # Total semanal (todos los días)
    hours_total = total_duration // 3600
    min_total = (total_duration % 3600) // 60
    print(f"\n🎯Total this week: {hours_total}h {min_total}m")

    # Total lunes a viernes (para premio)
    weekly_hours = total_duration_habil // 3600
    min_weekly = (total_duration_habil % 3600) // 60
    print(f"Time from Monday to Friday: {weekly_hours}h {min_weekly}m")

    if weekly_hours >= 10:
        print("MODO Zuckerberg ACTIVADO!(+10hs semanal)🚀\nPRIZE: GELATTO DE ITALIA PAPA!! EN ORRRRRRRRTO🍦")
    else:
        print("daleeee metele vagoneta💪. ACTIVAME EL MODO ELON🔥.")

def monthly_report():
    archive_json = "jj.json"

    if not os.path.exists(archive_json):
        print("No study sessions found")
        return

    with open(archive_json, "r", encoding="utf-8") as archivo:
        sessions = json.load(archivo)

    today = date.today()
    current_month = today.month
    current_year = today.year

    # Filtrar sesiones del mes actual
    monthly_sessions = [s for s in sessions if date.fromisoformat(s["date"]).month == current_month and date.fromisoformat(s["date"]).year == current_year]

    if not monthly_sessions:
        print("No sessions recorded this month.")
        return

    total_duration = 0
    total_sessions = 0

    # Agrupar sesiones por semanas
    from collections import defaultdict
    weekly_summary = defaultdict(int)  # clave = numero de semana, valor = duracion lunes a viernes

    for sesion in monthly_sessions:
        fecha = date.fromisoformat(sesion["date"])
        duration = sesion["duration"]
        name_day = fecha.strftime("%A")

        total_sessions += 1
        total_duration += duration

        # Solo sumar lunes a viernes para el premio
        if name_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            week_number = fecha.isocalendar().week
            weekly_summary[week_number] += duration

    # Calcular helados ganados (>=10 horas de lunes a viernes por semana)
    helados = 0
    for dur in weekly_summary.values():
        if dur >= 36000:  # 10 horas = 36000 segundos
            helados += 1

    # Mostrar reporte mensual
    total_h = total_duration // 3600
    total_m = (total_duration % 3600) // 60

    print("\nMonthly Report")
    print(f"Total sessions this month: {total_sessions}")
    print(f"Total study time: {total_h}h {total_m}m")
    print(f"Helados ganados (modo Zuckerberg activado): {helados} 🍦")

#LOGIC

greetin_and_date() 
validate_password() 

while True:
    option = menu()
    option_num = validate_menu_option(option)

    if option_num == 1:
        process_option_one()
    elif option_num == 2:
        weekly_report()
    elif option_num == 3:
        monthly_report()
    elif option_num == 4:
        print("Bye see you later") #chau hasta luego
        break
    else:
        print("Invalid option. Please enter a number between 1 and 4.")
