Feature: inicioJuego

    Como repartidor quiero entregar 2 cartas para iniciar el juego.

Scenario Outline: repartir dos cartas para iniciar
Given un <mazo> para jugar 21
When el repartidor reparte una <carta1> y luego otra <carta2>
Then la <mano> es correcta

Examples:

    |carta1|carta2|mano|
    |5,picas|J,treboles|2 |
    |9,corazones|A,treboles|2 |
    |3,diamantes|Q,picas)|2|
    |A,picas|A,treboles)|2 |
    |A,diamantes|J,treboles)|2 |

    


