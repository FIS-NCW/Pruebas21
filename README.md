<h1 style="text-align:center">Juego del 21<h1>
        <h2>Integrantes: </h2>
        <ul type="square">
            <li> Andres Felipe Wilches Torres - 20172020114</li>
            <li>William Nicolas Buitrago Camacho - 20172020079</li>
            <li>Cristian Felipe Ramirez Ovalles - 20172020068</li>
        </ul>
        
  <p>En este repositorio, se encontrara el paso a paso (como un tutorial) para el juego denominado 21 y como realizar sus pruebas de aceptacion.</p>
  <h4>Nota:</h4><p>El lenguaje de programacion usado en este repositorio sera en Python, mediante el entorno Visual Studio Code y Pycharm</p>
  
  <h1> 1) ¿Que son las pruebas de aceptacion? </h1>
  <p> Las pruebas de aceptacion o UAT (por sus siglas en ingles: User Acceptance Testing), son pruebas que se hacen en las ultimas etapas previas a la liberacion del software, con el proposito de determinar si este cumple con las necesidades para el cliente. Primero se realizan las pruebas automatizadas y posterior a estas, las manuales.<br> Nuestro proposito en este repositorio, es explicar mediante el juego del 21 como funcionan dichas pruebas, por lo que este sera un tutorial, con paso a paso, de como realizarlas en este juego. Pero primero, debemos explicar como funciona el juego del 21.</p>
  
<h1> 2) ¿Que es el juego del 21?</h1>

<p>El juego del 21, o <a href="https://es.wikipedia.org/wiki/Blackjack" target="_blank" > BlackJack </a>,es un juego de cartas que usualmente se suele jugar en casinos. En si este juego de cartas cuenta con una o mas <a href="https://es.wikipedia.org/wiki/Baraja_inglesa" target="_blank">barajas inglesas</a>  de 52 cartas sin los comodines, que consiste en sumar un valor lo más próximo a 21 pero sin pasarse. Usualmente, cada jugador se enfrenta contra el repartidor o cuprier, a continuacion pasaremos la lista de reglas, valores de las cartas y un paso a paso del juego, para poder entenderlo mejor</p>
        <ol>
        <li><big><b>Reglas</b></big></li>
                <ul type="square">
                        <li>Al inicio de cada partida el jugador debe apostar.</li>
                        <li>El crupier repartirá dos cartas descubiertas a cada jugador y una a sí mismo, también visible a los jugadores.</li>
                        <li>Cada jugador decidirá si pide más cartas o se planta con las dos ya repartidas.</li>
                        <li>Luego el crupier jugará su mano.</li>
                        <li>Los jugadores que se queden más lejos de 21 que el crupier o que hayan sobrepasado este valor, pierden.</li>  
                        <li>Quienes tengan el mismo valor del crupier recuperan su apuesta pero no pierden ni ganan.</li>
                        <li> Los jugadores que saquen BlackJack (as más 10 o figura) se les paga 3×2 y aquellos que superen al crupier se les paga 1×1 según la apuesta que hayan                hecho.</li>
                 </ul> 
        <li><big><b>Valores de las cartas</b></big></li>
        <p>El As es la única carta de la baraja que tiene dos valores, 1 y 11, siendo el jugador que lo posea quien elige el valor entre ambos según le convenga. Son cartas muy        valiosas por esta virtud.Las cartas numeradas con índice del dos al diez tienen el valor correspondiente a su numeración.Por su parte, todas las figuras (Jack, Queen y King), tienen el mismo valor: 10. Importante dato para el jugador, es saber que en 52 cartas, hay 16 con un valor de 10. A continuacion se anexara una imagen para entender mejor lo escrito en esta seccion.</p>
        <li><big><b>Paso a paso del juego:</b></big></li>
             <ul type="square">
            <li>Al inicio de cada partida el jugador debe apostar.</li>
            <li>El crupier repartirá dos cartas descubiertas a cada jugador y una a sí mismo, también visible a los jugadores.</li>
            <li>Cada jugador decidirá si pide más cartas o se planta con las dos ya repartidas.</li>
            <li>Luego el crupier jugará su mano.</li>
            <li>Los jugadores que se queden más lejos de 21 que el crupier o que hayan sobrepasado este valor, pierden.</li>  
            <li>Quienes tengan el mismo valor del crupier recuperan su apuesta pero no pierden ni ganan.</li>
            <li> Los jugadores que saquen BlackJack (as más 10 o figura) se les paga 3×2 y aquellos que superen al crupier se les paga 1×1 según la apuesta que hayan hecho.</li>
        </ul>    
        </ol>
