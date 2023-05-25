<?php 

	if ($_POST) {
		$nombre=$_POST['nombre_pac'];
		echo "hola ".$nombre;
	}
	
?>
<!DOCTYPE html>
<html lang="es">
 	<head>
		<title>Proyecto Profesionalizante</title>
		<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="Base de datos para distintos tipos de sangre, destinados a una organizacion de la informacion mas ordenada">
		<meta name="author" content="Facundo Alzogaray">
		<meta name="copyright" content="Derechos reservados a el grupo de estudio de ENET3139">
		<meta name="robots" content="index">
    <link rel="icon" href="medicina.ico">
    <link rel="stylesheet" type="text/css" href="estilo.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="normalize.css">
	</head>
 		<body>
 			<header>
 				<nav>
 					<ul class="enlaces">
 						<li class="enlaces__1"><a class="texto__enlace" href="Almacenamiento.html">Almacenamiento</a></li>
            <li class="enlaces__1"><a class="texto__enlace" href="Registrar_Pacientes.html">Registrar_Pacientes</a></li>
            <li class="contactar"><p class="texto__enlace_3">Whatsapp: +54 9 387 548-2380 Copyright© - Todos los derechos reservados a Facundo Alzogaray</p></li>
 					</ul>
 				</nav>
 			</header>
      <article>
        <section>
          <div class="caja_titulo">
            <h1 class="Titulo"><p>Bienvenido, por favor ingrese los datos del donante a buscar</p></h1>
          </div>
          <div class="container-flex">
            <div class="form">
             <form class="form__caja">
                 <b class="form__texto">Nombre del paciente:</b><input type="text" required="" placeholder="Nombre del paciente" class="form__Nombre">
                 <b class="form__texto">Sangre(ml):</b><input type="number" required="" class="form_LitrosSangre" name="nombre_pac">
                 <b class="form__texto">DNI:</b><input type="number" required="" class="form__DNI">
                <b class="form__texto">Fecha de emision:</b><input type="date" class="form__FechaEmision">
                <input type="submit">
              </form>
            </div>
            <div class="caja_texto">
              <p class="texto">
               Nuestro objetivo con este proyecto es ofrecer una alternativa a los registros de los donantes en documentos de texto a una pagina web, donde los datos de los pacientes quedaran organizados en base a su nombre, fecha de que se ingreso el donante, o tipo de sangre. Para iniciar con la busqueda se debera primero entrar a la pestaña de "Registrar_Paciente", alli usted ingresara los datos de un paciente. A continuacion, este se guardara en una base de datos alojada en un servidor, y estara listo para que usted pueda encontrarlo con el buscador del menu principal.
              </p> 
            </div>
          </div>
        </section>
        <section>
          
          <div>
          <p class="politica">
        Esta pagina ha sido creada con fines de educación y cualquier uso con fines de lucro de la pagina será demandada ,y luego la pagina será retirada.
          </p>
          </div>
        </section>
   </article>
   <footer>
   </footer>
 </body>
</html>
