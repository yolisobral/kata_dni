class TablaAsignacion():
   
   # Crea la tabla de asignación de letras para el DNI
    def __init__ (self):                        
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E"
        ]

    # Devuelve la tabla de asignación de letras para el DNI
    def getTabla(self):                         
        return self.tabla
    
    # Devuelve la letra correspondiente a la posición dada, menos si esta fuera de rango, en cuyo caso devuelve un mensaje de error
    def getLetra(self, posicion):               
        try:
            return self.tabla[posicion]
        except IndexError:
            return "Posicion letra fuera de rango"

    # Devuelve el número de elementos en la tabla, que es el módulo para calcular la letra del DNI    
    def getModulo(self):                        
        return len(self.getTabla())
    
    # Calcula la letra del DNI a partir del número de DNI utilizando el módulo y la tabla de asignación
    def isLetraPermitida(self, letra):
        return letra in self.getTabla()

    # Calcula la letra del DNI a partir del número de DNI (cadena o entero)
    def calcularLetra(self, numero_dni):
        try:
            numero = int(numero_dni)
        except Exception:
            return None
        posicion = numero % self.getModulo()
        return self.getLetra(posicion)
    
    # Devuelve una representación en cadena de la tabla de asignación de letras para el DNI
    def __repr__(self): 
        return ' '.join(self.getTabla())
