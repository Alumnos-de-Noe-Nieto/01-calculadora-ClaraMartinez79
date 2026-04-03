"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""



from calculadora.error import ExpresionInvalida
from calculadora.validaciones.alfabeto import validar_simbolos
from calculadora.validaciones.orden_descendente import validar_orden_descendente
from calculadora.validaciones.repeticiones_icxm import validar_repeticiones_icxm
from calculadora.validaciones.repeticiones_vld import validar_repeticiones_vld
from calculadora.validaciones.restas import validar_restas


def romano_a_entero(cadena: str) -> int:
    limpia = cadena.strip()

    if not validar_simbolos(limpia):
        raise ExpresionInvalida("Símbolos inválidos")
    if not validar_repeticiones_icxm(limpia):
        raise ExpresionInvalida("Repetición I/X/C/M")
    if not validar_repeticiones_vld(limpia):
        raise ExpresionInvalida("Repetición V/L/D")
    if not validar_restas(limpia):
        raise ExpresionInvalida("Resta inválida")
    if not validar_orden_descendente(limpia):
        raise ExpresionInvalida("Orden incorrecto")

    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(limpia)):
        if i + 1 < len(limpia) and valores[limpia[i]] < valores[limpia[i+1]]:
            total -= valores[limpia[i]]
        else:
            total += valores[limpia[i]]

    return total
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Examples:
        >>> romano_a_entero("I")
        1
        >>> romano_a_entero("V")
        5
        >>> romano_a_entero("IV")
        4
        >>> romano_a_entero("IX")
        9
        >>> romano_a_entero("XIV")
        14
        >>> romano_a_entero("MCMXCIV")
        1994
        >>> romano_a_entero("MMMCMXCIX")
        3999

    Raises:
        ExpresionInvalida: Si la cadena no es válida según las reglas de números romanos (símbolos inválidos, repeticiones inválidas, orden incorrecto, restas inválidas)
    """
    raise NotImplementedError()
