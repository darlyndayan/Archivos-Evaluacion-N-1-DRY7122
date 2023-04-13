# Ingreso de direccion IP octeto por octeto 
octeto1 = input("Ingrese el primer octeto: ")
octeto2 = input("Ingrese el segundo octeto: ")
octeto3 = input("Ingrese el tercer octeto: ")
octeto4 = input("Ingrese el cuarto octeto: ")
# Union de los octetos para formar la ip
direccion_ip = octeto1 + "." + octeto2 + "." + octeto3 + "." + octeto4
# Determinar si es una IP privada o publica
<r direccion_ip.startswith("192.168."):
	tipo_ip = "privada"
else:
	tipo_ip = "publica"
#Mostrar la direccion IP y el tipo en pantalla
print("La direccion IP es: " + direccion_ip)
print("Siendo una direccion IP: " + tipo_ip) 
