#Python Match
#match...case (новая альтернатива для if)
command = "start"

match command:
    case "start":
        print("Система запускается...")
    case "stop":
        print("Система останавливается.")
    case _:
        print("Неизвестная команда.")