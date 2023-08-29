class NetworkLayerSimulation:
    def __init__(self):
        self.apps = {'whatsapp': '01', 'telegram': '10', 'facebook': '11'} # atributo de apps
        self.devices = {'PC1': '0001', 'PC2': '0010', 'Router': '0100'} # atributo de dispositivos

    def capa_5(self, message):
        print("\nEstamos en la capa 5, imprimiendo datos.")
        print("Mensaje:", message)
        return message

    def capa_4(self, message, app):
        print("\nEstamos en capa 4, imprimiendo mensaje.")
        header = f"Aplicación: {app}, Mensaje: {message}"
        print(header)
        return header

    def capa_3(self, header, app):
        print("\nEstamos en capa 3, imprimiendo segmento.")
        code = self.apps[app]
        segment = f"Código: {code}, {header}"
        print(segment)
        return segment

    def capa_2(self, segment, source, destination):
        print("\nEstamos en capa 2, imprimiendo datagrama.")
        src_code = self.devices[source]
        dest_code = self.devices[destination]
        datagram = f"Emisor: {src_code}, Receptor: {dest_code}, {segment}"
        print(datagram)
        return datagram

    def capa_1(self, datagram, source):
        print("\nEstamos en capa 1, imprimiendo trama en", source)
        src_device = source
        frame = f"Dispositivo: {src_device}, {datagram}"
        print(frame)
        return frame

    def simulate_send(self, message, app, source, destination):
        msg = self.capa_5(message)
        hdr = self.capa_4(msg, app)
        segment = self.capa_3(hdr, app)
        datagram = self.capa_2(segment, source, destination)
        frame = self.capa_1(datagram, source)
        return frame

    
    def simulate_receive(self, frame, destination):
        print("\n------ Recibiendo en", destination, "------")
        
        # Capa 1: Interpretar el dispositivo del frame
        _, datagram = frame.split("Dispositivo: ", 1)
        print("\nEstamos en capa 1, interpretando trama desde", frame.split(",")[0].split(":")[1].strip())
        
        # Capa 2: Interpretar el datagrama
        _, segment = datagram.split(", Receptor: ", 1)
        src_code = datagram.split(", Emisor: ")[1].split(",")[0].strip()
        dest_code = datagram.split(", Receptor: ")[1].split(",")[0].strip()
    
        segment_parts = segment.split(", ")
        app_code = segment_parts[1].split(": ")[1].strip()
        app_name = segment_parts[2].split(": ")[1].strip()
        msg = segment_parts[3].split(": ")[1].strip()
        
        print("\nEstamos en capa 2, imprimiendo datagrama.")
        print(f"Mensaje: {msg}, Aplicación: {app_name}, Código de aplicación: {app_code}, Emisor: {src_code}, Receptor:{dest_code}")
        
        # Capa 3: Interpretar el segmento
        print("\nEstamos en capa 3, imprimiendo segmento.")
        print(f"Mensaje: {msg}, Encabezado de aplicación: {app_name}, Código: {app_code}")
        
        # Capa 4: Interpretar el encabezado y el mensaje
        print("\nEstamos en capa 4, imprimiendo mensaje.")
        print("Encabezado:", app_name)
        print("Mensaje:", msg)
    
        print("\nMensaje transmitido, simulación terminada.")


    

def main():
    sim = NetworkLayerSimulation()
    print("Simulador de Red basado en Tanenbaum")
    source = input("\nDesde qué PC enviarás (PC1/PC2): ")
    destination = 'PC2' if source == 'PC1' else 'PC1'
    message = input("Escribe el mensaje a enviar: ")
    app = input("A través de qué aplicación (whatsapp/telegram/facebook): ")

    print(f"\n------ Transmitiendo desde {source} a {destination} ------")
    frame = sim.simulate_send(message, app, source, destination)

    print("\n------ Enrutador ------\nEnrutando trama desde", source, "a", destination)

    sim.simulate_receive(frame, destination)


if __name__ == "__main__":
    main()
