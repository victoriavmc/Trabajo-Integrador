import re


class Validacion:

    def validarUsuario(self, usuario, contrasenia, correo):
        if len(usuario) >= 4 and len(contrasenia) >= 8:
            if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                return True
        return False
    ##############################################################
    #

    def validarMedico(self, nombre, apellido, edad, cuilCuit, telefono):
        if self.validarNumero(nombre) == False and self.validarNumero(apellido) == False:
            if self.validarNumero(edad) and self.validarNumero(cuilCuit) and self.validarNumero(telefono):
                if self.validarContarNumero(cuilCuit, 11) and self.validarContarNumero(telefono, 8):
                    return True
        return False

    def validarNumero(self, parametro):
        if parametro.isdigit():
            return True
        return False

    def validarContarNumero(self, num, cantidad):
        if len(num) == cantidad:
            return True
        return False