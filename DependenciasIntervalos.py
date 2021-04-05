from enum import Enum
from Interval import Intervalo

class DepenEnum(Enum):
    IGUAL = 0
    ANTES = 1
    ENCUENTRA = 2
    SOLAPA = 3
    DURANTE = 4
    COMIENZA = 5
    FINALIZA = 6
    IANTES = 7
    IENCUENTRA = 8
    ISOLAPA = 9
    IDURANTE = 10
    ICOMIENZA = 11
    IFINALIZA = 12

#Declaracion de los tipos de relaciones entre intervalos
    #Cuando x > y , x ha empezado antes e y mas tarde, viceversa.

def comp_antes(entrada, comparado):
    if entrada.inicio > comparado.inicio:
        return True
    else:   
        return False
        
def comp_igual(entrada, comparado):
    if entrada.inicio == comparado.inicio:
        if entrada.fin == comparado.fin:
            return True
    return False

def comp_encuentra(entrada, comparado):
    if entrada.fin == comparado.inicio:
        return True
    return False
        
def comp_solapa(entrada, comparado):
    if entrada.inicio < comparado.inicio:
        if entrada.fin < comparado.fin:
            if entrada.fin > comparado.inicio:
                return True
    return False

def comp_durante(entrada, comparado):
        if entrada.inicio > comparado.inicio:
            if entrada.fin < comparado.fin:
                return True
        return False

def comp_comienza(entrada, comparado):
    if entrada.inicio == comparado.inicio:
        if entrada.fin < comparado.fin:
            return True
    return False
        
def comp_finaliza(entrada, comparado):
    if entrada.inicio > comparado.inicio:
        if entrada.fin == comparado.fin:
            return True
    return False