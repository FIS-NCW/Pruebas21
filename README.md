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
        <p>Las historias de usuario son una representación de un requisito escrito en una o dos frases utilizando el lenguaje común del usuario. en palabras mas simples: son pequeñas descripciones de los requerimientos de un cliente. <br>Teniendo en cuenta las reglas descritas anteriormente y su paso a paso, se tuvieron en cuenta las siguientes, por simplicidad del proyecto:</p>
        <ul type="circle">
            <li>Como repartidor quiero barajar.</li>
            <li>Como repartidor quiero entregar 2 cartas para iniciar el juego.</li>
            <li>Como jugador quiero determinar el valor de una carta para determinar el valor de la mano.</li>
            <li>Como jugador quiero determinar el valor de la mano para seguir jugando.</li>
            <li>Como jugador quiero solicitar una carta adicional para seguir jugando.</li>
            <li>Como jugador quiero plantarme para finalizar el turno.</li>
            <li>Como repartidor quiero saber el valor de las manos para determinar quién gana.</li>
        </ul>  

<h1> 4) ¿Como realizar las pruebas de aceptacion mediante (<EM><U>BEHAVE</U></EM>) comando de Python?</h1>
<p>Para realizar este tipo de pruebas, con el comando <EM>BEHAVE</EM> de python. Primero debemos seguir una lista de pasos, como primero tener instalado este <a href="https://www.youtube.com/watch?v=-IyA_Yvs8IQ" target="_blank" >lenguaje de programacion</a> en nuestro sistema, un entorno de programacion (como <a href="https://www.youtube.com/watch?v=kJP7f7cU03M">Pycharm</a> o el propio <a href="https://www.youtube.com/watch?v=HVzFLw5r2EM">Visual Estudio Code</a>) y un administrador de paquetes que nos permitira instalar el <EM>BEHAVE</EM>, que para este caso sera el <b><EM>PIP</EM></b>.</p>
        <ol>
        <li>Instalacion del administrador de paquetes <b>PIP</b>:<br><p>Una vez que tengamos instalado el lenguaje de programacion Python y un entorno de nuestro gusto, debemos instalar el PIP en nuestro sistema (esta parte viene mas dada para las personas que no tienen el comando <pip> en su sistema, y a continuacion se mostrara como agregarlo a las variables 'path' del sistema).<br> Para agregar el comando PIP, a nuestras variables de entorno de nuestro sistema, lo que tenemos que hacer es oprimir las teclas Windows + R:</p> <img src="https://user-images.githubusercontent.com/54086394/102171700-2c40df00-3e65-11eb-9bd9-c921c3604d2a.jpg" alt="Imagen W+R"/><p>Al realizar esto, se nos abrira el programa 'ejecutar' del sistema, alli deberemos poner el comando '<EM>sysdm.cpl</EM>':</p> <img src="https://user-images.githubusercontent.com/54086394/102171798-598d8d00-3e65-11eb-9d1d-2ea4a0dba5e0.jpeg"/><p>Este comando, nos permitira abrir las propiedades del sistema. Una vez alli dentro nos vamos a la pestaña de  opciones avanzadas y clicamos el boton de 'variables de entorno', esto con el proposito de añadir PIP a nuestra variable PATH: </p> <img src="https://user-images.githubusercontent.com/54086394/102171799-598d8d00-3e65-11eb-8b84-1e1b786a9c60.jpeg"/><p>Una vez clicado, seleccionamos la variable PATH, tal como se ve en la siguiente imagen y le damos al boton de  'editar': </p><img src="https://user-images.githubusercontent.com/54086394/102171794-585c6000-3e65-11eb-8387-bd9201a3c328.jpeg"/><p>Una vez se abra la ventana, le daremos al boton de nuevo y agergaremos la ruta donde tenemos instalado el PIP de nuestro Python. En nuestro caso la ruta es: <samp>C:\Users\Cristian Ovalles\AppData\Local\Programs\Python\Python39\Scripts</samp> </p><img src="https://user-images.githubusercontent.com/54086394/102171795-58f4f680-3e65-11eb-9008-013ecc4e47a7.jpeg"/><p>Una vez hecho todo lo anterior, ya tendremos instalado nuestro PIP en el sistema</p></li>
            <li>Instalar Behave</li>
        <p>Para instalar el Behave es tan sencillo como abrir la terminal en nuestro Visual Studio Code y poner lo siguiente <samp>PIP install behave</samp></p><img src="https://user-images.githubusercontent.com/54086394/102171797-58f4f680-3e65-11eb-89b3-22fed63b6888.jpeg"/>
        </ol>
        
<h1> 5) Realizar pruebas de aceptacion</h1>
        <p>Las pruebas de usuario estan compuestas por dos tipos de archivo: El <em>STEPS</em> y el <em>Feature</em>.</br>Usamos los features donde creamos la test suite para verificar un requerimiento determinado. El archivo feature contiene escenarios donde definimos los pasos Given->When->Then para verificar los criterios de aceptación de la funcionalidad en desarrollo. </br> Entonces, vamos a tener muchos archivos features con criterios de aceptación que describen los comportamientos de la aplicación y una gran cantidad de código que ejercita la aplicación linkeado a los Given->When->Then que son llamados desde los escenarios en los features.</br> Los STEPS, son los pasos que sigue el programa, por lo que lo que hace behave es comparar los features, que vienen dados por los scenarios y unos valores conocidos, con los steps. Si no suelta errores, el programa tendria sus pruebas de aceptacion validas</br></br>A continuacion mostraremos imagenes de los steps y Features para cada historia de usuario.</p>
       <ol>
            <li><b>Como repartidor quiero barajar.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>barajar</em>. Revuelve las cartas.</p>
                <h4>Feature</h4>
                <p>En este caso, el feature tiene el escenario de barajar, dado un mazo de 52 cartas para jugar al 21. Esta accion se da cuando el repartidor baraja (revuelve) el mazo, luego de esto se comprueba que las cartas no sean iguales</p>
                <img src="https://user-images.githubusercontent.com/54086394/102276520-eb90a680-3ef4-11eb-85f2-79d259124c7a.png"/>
                <h4>STEPS</h4>
        <p>En los steps, vemos la implementacion mediante <SAMP>Def</SAMP> de los <SAMP>@Given, @When y @Then</SAMP> dos veces, ya que tambien toca corroborar la cantidad de cartas, que es 52.</p>
                <img src="https://user-images.githubusercontent.com/54086394/102276525-ed5a6a00-3ef4-11eb-809d-a5dd3f0cc13f.png"/>
            <li><b>Como repartidor quiero entregar 2 cartas para iniciar el juego.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>InicioJuego</em>. Sirve para empezar el juego</p>
                <h4>Feature</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
                <h4>STEPS</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
            <li><b>Como jugador quiero determinar el valor de una carta para determinar el valor de la mano.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>Carta</em>. Sirve para que el jugador pueda determinar el valor de las cartas</p>
                <h4>Feature</h4>
                <p>En este caso, el feature tiene el escenario outline de determinar el valor de la carta, se da, para una carta de modo que el jugador desee conocer su valor, luego se corrobora que el valor de dicha carta es correcto (corresponde al valor de las cartas conocidas).</br> Ademas se agrega los <samp>Examples</samp> o ejemplos conocidos y ciertos.</p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
                <h4>STEPS</h4>
                <p>En los steps, vemos la implementacion mediante <SAMP>Def</SAMP> de los <SAMP>@Given, @When y @Then</SAMP>, Esto hace que el programa: Dada una carta, cuando el jugador quiere saber el valor de esta, corrobora que su valor sea correcto.</p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
            <li><b>Como jugador quiero determinar el valor de la mano para seguir jugando.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>Mano</em>. Sirve para que el jugador pueda determinar de su mano y de esta forma pueda escoger otras opciones.</p>
                <h4>Feature</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
                <h4>STEPS</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
            <li><b>Como jugador quiero solicitar una carta adicional para seguir jugando.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>SolicitarCarta</em>. Sirve para que el jugador obtenga una nueva carta dada por el repartidor</p>
                <h4>Feature</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
                <h4>STEPS</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
            <li><b>Como jugador quiero plantarme para finalizar el turno.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>Plantar</em>. Sirve para terminar el juego, no se reciben mas cartas por parte del jugador</p>
                <h4>Feature</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
            <li><b>Como repartidor quiero saber el valor de las manos para determinar quién gana.</b></li>
                <p>Esta historia de usuario, hace alusion a las pruebas de aceptacion <em>ValorManos</em>. Sirve para que el repartidor sepa el valor de las manos de los jugadores y asi determina quien gana</p>
                <h4>Feature</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273465-5c818f80-3ef0-11eb-8fb5-be9fbb44c685.png"/>
                <h4>STEPS</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
       </ol>
<h1> 6)Resultado pruebas</h1>
        <p>Al ejecutar el comando behave en la raiz de la ubicacion de nuestro programa, se obtuvieron los siguientes resultados:</p>
        <h4>Al ejecutar el comando BEHAVE</h4>
                <p></p>
                <img src="https://user-images.githubusercontent.com/54086394/102273468-5d1a2600-3ef0-11eb-898d-f8661cae59b4.png"/>
