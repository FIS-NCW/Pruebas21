from behave import *
from mazo import Mazo

@given('un mazo para jugar 21')
def implementacion(context):
    context.mazo = Mazo()

@when('el repartidor baraja el mazo')
def implementacion(context):
    context.mazo.barajar()

@then('las cartas 6 y 9 no son iguales')
def implementacion(context):
    assert not context.mazo.dar_carta(6).son_iguales(context.mazo.dar_carta(9))

@then('la catidad de cartas es 52')
def implementacion(context):
    assert  len(context.mazo.cartas) == 52