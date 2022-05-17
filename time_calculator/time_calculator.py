def add_time(start, duration, start_day_week=""):
    # Separando hora de inicio
    parts = start.split()
    time = parts[0].split(":")
    time_format = parts[1]

    # Calculando el tiempo en minutos
    minutes = int(time[0]) * 60 + int(time[1])
    if time_format == "PM":
        minutes += 12 * 60  # Agregando 12 Horas del día

    # Separando duración y calculando el tiempo en minutos
    duration_time = duration.split(":")
    duration_minutes = int(duration_time[0]) * 60 + int(duration_time[1])

    # Suma de horas
    total_time_minutes = minutes + duration_minutes
    total_hours = total_time_minutes // 60
    total_minutes = total_time_minutes % 60
    total_days = total_hours // 24

    # Calcular la nueva hora
    new_hour = total_hours % 24
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Calcular AM o PM
    time_format = "AM" if total_hours % 24 < 12 else "PM"
    new_time = f"{new_hour}:{str(total_minutes).zfill(2)} {time_format}"

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day = weekdays.index(start_day_week.title()) if start_day_week else ""
    if day != "":  # Calcular el índice para buscar el día en caso de que exista
        for i in range(total_days):
            day += 1
            if day == 7:
                day = 0
        new_time += f", {weekdays[day]}"

    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    return new_time