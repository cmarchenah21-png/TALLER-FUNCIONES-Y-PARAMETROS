class EventDispatcher:

    def __init__(self):
        self.listeners = {}

    
    def on(self, evento, callback, *args, **kwargs):
        if evento not in self.listeners:
            self.listeners[evento] = []

        self.listeners[evento].append((callback, args, kwargs))

    
    def limpiar_payload(self, datos):
        if isinstance(datos, dict):
            resultado = {}

            for clave, valor in datos.items():
                resultado[clave] = self.limpiar_payload(valor)

            return resultado

        elif isinstance(datos, list):
            resultado = []

            for elemento in datos:
                resultado.append(self.limpiar_payload(elemento))

            return resultado

        elif isinstance(datos, str):
            return datos.strip()

        else:
            return datos

    
    def emit(self, evento, payload=None, detener_en_error=False):

        if evento not in self.listeners:
            return

        
        payload_limpio = self.limpiar_payload(payload or {})

        for callback, args, kwargs in self.listeners[evento]:

            try:
                
                callback(*args, **payload_limpio, **kwargs)

            except Exception as error:
                print("Error en el callback:", error)

                if detener_en_error:
                    break