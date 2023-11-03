from classProfDeLaSalud import ProfDeLaSalud
from classValidacion import Validacion
import json
#-*- coding: utf-8 -*-
# Crear una instancia de la clase Validacion
validacion = Validacion()


def cargarMedico():
    """
    Carga datos de médicos desde un archivo JSON.

    Returns:
        list: Una lista de objetos ProfDeLaSalud cargados desde el archivo JSON.
    """
    try:
        with open('medicos.json', 'r') as archivo:
            medicoData = json.load(archivo)
            for data in medicoData:
                medico = ProfDeLaSalud(data['nombre'], data['apellido'], data['edad'], data['cuilCuit'],
                                       data['telefono'], data['sexo'], data['titulo'], data['especialidad'])
    except FileNotFoundError:
        pass


cargarMedico()


class Medicos:

    def __init__(self) -> None:
        pass

    def guardarMedico(self):
        data = []
        for medico in ProfDeLaSalud.listaPSalud:
            medicoData = {
                'nombre': medico.getNombre(),
                'apellido': medico.getApellido(),
                'edad': medico.getEdad(),
                'cuilCuit': medico.getCUILCUIT(),
                'telefono': medico.getTelefono(),
                'sexo': medico.getSexo(),
                'titulo': medico.getTitulo(),
                'especialidad': medico.getEspecialidad()
            }
            data.append(medicoData)

        with open('medicos.json', 'w') as archivo:
            json.dump(data, archivo, indent=4)

    def noRepetircuilCuit(self, cuilCuit):
        for profesional in ProfDeLaSalud.listaPSalud:
            if profesional.getCUILCUIT() == cuilCuit:
                return False
        return True

    def noRepetirTelefono(self, telefono):
        for profesional in ProfDeLaSalud.listaPSalud:
            if telefono == profesional.getTelefono():
                return False
        return True

    def agregarMedico(self, nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad):
        nombre = nombre.title()
        apellido = apellido.title()
        if self.noRepetircuilCuit(cuilCuit) and self.noRepetirTelefono(telefono):
            if validacion.validarMedico(nombre, apellido, edad, cuilCuit, telefono):
                medico = ProfDeLaSalud(
                    nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad)
                self.guardarMedico()
                return True
        else:
            return False

    def buscarMedico(self, cuilCuit):
        if validacion.validarContarNumero(cuilCuit, 11):
            for medico in ProfDeLaSalud.listaPSalud:
                if medico.getCUILCUIT() == cuilCuit:
                    return medico
            return None

    def modificarMedico(self, nombre, apellido, edad, cuilCuit, telefono, sexo, titulo, especialidad):
        nombre = nombre.title()
        apellido = apellido.title()
        if validacion.validarMedico(nombre, apellido, edad, cuilCuit, telefono):
            medico = self.buscarMedico(cuilCuit)
            if medico is not None:
                medico.setNombre(nombre)
                medico.setApellido(apellido)
                medico.setEdad(edad)
                medico.setTelefono(telefono)
                medico.setCUILCUIT(cuilCuit)
                medico.setSexo(sexo)
                medico.setTitulo(titulo)
                medico.setEspecialidad(especialidad)
                self.guardarMedico()
                return True
            else:
                return False
        else:
            return False

    def mostrarMedico(self, cuilCuit):
        medico = self.buscarMedico(cuilCuit)
        if medico is not None:
            return medico.mostrar()
        else:
            return False

    def eliminarMedico(self, cuilCuit):
        medico = self.buscarMedico(cuilCuit)
        if medico is not None:
            ProfDeLaSalud.listaPSalud.remove(medico)
            self.guardarMedico()
            return True
        else:
            return False