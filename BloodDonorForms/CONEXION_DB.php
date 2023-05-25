<?php 
	$servidorDB = "mysql:host=localhost;dbname=db_hospital";
	$usuario = "root";
	$password = "";
	try{
		$pdo = new PDO($servidorDB ,$usuario ,$password);
		$pdo -> exec("SET CHARACTER SET utf8");
		$pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	}catch(Exception $e)
	{
		die("ERROR en conexion en la BD".$e->getMessage());
	}
?>