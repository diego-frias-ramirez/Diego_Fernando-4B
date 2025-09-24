# Practcia3. Introduccion a l Polifrmismo
# Simular un sistema de cobor con multiples 
# opciones de pago

class pago_tarjeta:
    def procesar_pago(self, cantidad):  
        return f"Procecando pago de ${cantidad} con tarjeta bancaria"
    
class transferencia:
    def procesar_pago(self, cantidad):  
        return f"Procecando pago con transferencia por la cantidad de ${cantidad}"
    
class deposito:
    def procesar_pago(self, cantidad):  
        return f"Procecando pago por medio de deposito en ventanilla por ${cantidad}"
    
class paypal:
    def procesar_pago(self, cantidad):  
        return f"Procecando pago de ${cantidad} por medio de peypal"
    
#Instancia
#metodos_pago = [pago_tarjeta(), transferencia(), deposito(), paypal()]

#for m in metodos_pago:
    #print(m.procesar_pago(500))

#Actividad: procesar pago con diferentes cantidades en cada de las formas de pago 
# Ejemplo:100 con tarjeta, 500 con transferencia, 2000 con paypal, 400 con deposito 

# Instancias de cada forma de pago con la cantidad correspondiente

pagos = [
    (pago_tarjeta(), 100),
    (transferencia(), 500),
    (paypal(), 2000),
    (deposito(), 400)
]

# Procesar cada pago
for m, cantidad in pagos:
    print(m.procesar_pago(cantidad))


# Actividad 2 - Sistema de alertas multicanal

class AlertaCorreo:
    def enviar_alerta(self, contenido):
        return f"[Correo] Alerta enviada: '{contenido}'"

class AlertaSMS:
    def enviar_alerta(self, contenido):
        return f"[SMS] Alerta enviada: '{contenido}'"

class AlertaTelegram:
    def enviar_alerta(self, contenido):
        return f"[Telegram] Alerta enviada: '{contenido}'"

class AlertaNotificacionPush:
    def enviar_alerta(self, contenido):
        return f"[Push] Alerta enviada: '{contenido}'"

# Lista de canales con sus respectivos mensajes
canales_alerta = [
    (AlertaCorreo(), "Factura disponible para descargar"),
    (AlertaSMS(), "Código de verificación: 84219"),
    (AlertaTelegram(), "Tienes una nueva respuesta en el foro"),
    (AlertaNotificacionPush(), "Recordatorio: reunión en 10 minutos")
]

# Enviar alertas por cada canal
for canal, contenido in canales_alerta:
    print(canal.enviar_alerta(contenido))
