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
        <li><b>Objetivo del juego:</b> El blackjack (modalidad americana) es un juego de cartas que consiste en sumar más puntos con tus cartas que el croupier sin pasarse de 21. Si en las 2 primeras cartas el jugador obtiene 21 puntos se consigue un “blackjack”. Las reglas en si, son las siguientes:</li>
        <li><big><b>Reglas</b></big></li>
                <ul type="square">
                        <li><b>Pedir carta:</b>  El croupier reparte una carta más al jugador. Si las cartas suman más de 21 puntos, pierde automáticamente y pasa el turno.</li>
                        <li><b>Plantarse:</b> El jugador se queda con las cartas que tiene y pasa el turno al siguiente jugador. <p><EM>Ademas el jugador posee otras opciones: </EM></p></li>
                        <li><b>Rendirse:</b> El jugador se puede rendir antes de realizar cualquier otra acción. Recupera la mitad de lo apostado.</li>
                        <li><b>Doblar:</b> Un jugador puede doblar la apuesta si tiene 9, 10 u 11 puntos. Si se dobla, el croupier reparte una carta más al jugador y termina el                turno.</li>
                        <li><b>Dividir:</b> Cuando las 2 primeras cartas valen lo mismo, se pueden dividir en 2 jugadas independientes con su propia apuesta cada una.</li> 
                        <ul type="circle">
                                <li>Si se dividen 2 ases sólo se reparte una carta a cada jugada y se termina el turno.</li>
                                <li>No se puede obtener “blackjack” después de dividir.</li>
                                <li>En esta modalidad, sólo es posible dividir una sola vez.</li>
                        </ul>
                        <li><b>Seguro:</b> Cuando la carta descubierta del croupier es un as se puede apostar a que el croupier tiene blackjack. El jugador debe realizar una apuesta adicional de la mitad de lo que ha apostado. Esta jugada se resuelve en el momento. En caso de acertar, el croupier pagará dicha apuesta 2 a 1; en caso contrario se pierde el seguro y sigue el orden normal de juego.</li>
                 </ul> 
        <li><big><b>Valores de las cartas: </b></big>El As es la única carta de la baraja que tiene dos valores, 1 y 11, siendo el jugador que lo posea quien elige el valor entre ambos según le convenga. Son cartas muy valiosas por esta virtud.Las cartas numeradas con índice del dos al diez tienen el valor correspondiente a su numeración.Por su parte, todas las figuras (Jack, Queen y King), tienen el mismo valor: 10. Importante dato para el jugador, es saber que en 52 cartas, hay 16 con un valor de 10. A continuacion se anexara una imagen para entender mejor lo escrito en esta seccion.</li>
                <img src="https://user-images.githubusercontent.com/54086394/102168238-e9c7d400-3e5d-11eb-9804-cba8c1d5b388.jpg" alt="Imagen valor cartas"/>
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
<h1>3)Historias de usuario que se definieron para este juego:</h1>
        <p>Las historias de usuario son una representación de un requisito escrito en una o dos frases utilizando el lenguaje común del usuario. en palabras mas simples: son pequeñas descripciones de los requerimientos de un cliente. <br>Para el juego del 21 o BlackJack se tuvieron en cuenta las siguientes:</p>


<h1> 4) ¿Como realizar las pruebas de aceptacion mediante (<EM><U>BEHAVE</U></EM>) comando de Python?</h1>
<p>Para realizar este tipo de pruebas, con el comando <EM>BEHAVE</EM> de python. Primero debemos seguir una lista de pasos, como primero tener instalado este lenguaje de programacion en nuestro sistema, un entorno de programacion (como Pycharm o el propio Visual Studio Code) y un administrador de paquetes que nos permitira instalar el <EM>BEHAVE</EM>, que para este caso sera el <b><EM>PIP</EM></b>.</p>
