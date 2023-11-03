from datetime import datetime

fecha = "2023-10-03 20:10:30"
fecha_obj = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
fecha_formateada = fecha_obj.strftime("%Y-%m-%d %H:%M:%S")
print(type(fecha_formateada))
print(type(fecha_obj))