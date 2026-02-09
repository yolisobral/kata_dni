class Dni:
    LETRAS_VALIDAS = "TRWAGMYFPDXBNJZSQVHLCKE"
    LETRAS_PROHIBIDAS = set("IOUÑ") 

    def __init__(self):  
        self._dni = ""
        self._numero_sano = ""
        self._letra_sana = None

    def getDni(self): # Devuelve el DNI completo
        return self._dni

    def setDni(self, dni): # Establece el DNI completo
        self._dni = dni
        self._numero_sano = ""
        self._letra_sana = None

    def getNumeroSano(self): # Devuelve el número sano si se ha validado correctamente, sino None
        return self._numero_sano

    def getLetraSana(self): # Devuelve la letra sana si se ha validado correctamente, sino None
        return self._letra_sana

    def checkCIF(self): # Comprueba que la letra no es una de las prohibidas
        if not self._dni:
            return False
        letra = self._dni[-1].upper()
        return letra not in self.LETRAS_PROHIBIDAS

    def checkDni(self): # Comprueba que el formato del DNI es correcto y guarda el número y letra sanos
        if len(self._dni) != 9:
            return False

        numero = self._dni[:8]
        letra = self._dni[-1].upper()

        if not numero.isdigit():  # El número debe ser de 8 dígitos
            return False

        if letra not in self.LETRAS_VALIDAS:
            return False

        # Guardar valores sanos
        self._numero_sano = numero
        self._letra_sana = letra
        return True

    def checkLetra(self):  # Comprueba que la letra es correcta para el número sano
        if not self._numero_sano:
            return False

        letra_correcta = self.LETRAS_VALIDAS[int(self._numero_sano) % 23]
        return letra_correcta == self._letra_sana

    def obtenerLetra(self): # Devuelve la letra correcta para el número sano, o None si no hay número sano
        if not self._numero_sano:
            return None
        return self.LETRAS_VALIDAS[int(self._numero_sano) % 23]

    def getParteAlfabeticaDni(self): # Devuelve la letra del DNI si el formato es correcto, sino None
        if len(self._dni) == 9:
            return self._dni[-1].upper()
        return None

    def getParteNumericaDni(self): # Devuelve el número del DNI si el formato es correcto, sino None
        return self._numero_sano if self._numero_sano else None
