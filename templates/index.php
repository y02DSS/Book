<?php
$serverName = "DSS";
$connectionInfo = array("Database"=>"localhost\Goods", "UID"=>"", "PWD"=>"");
$conn = sqlsrv_connect( $serverName, $connectionInfo);
 
if( $conn === false ) {
     die( print_r( sqlsrv_errors(), true));
     
}
 
$sql = "INSERT INTO Goods (Name, Adress) VALUES (?, ?)";
$params = array("$_POST[name]", "$_POST[adress]");
 
$stmt = sqlsrv_query( $conn, $sql, $params);
 
if( $stmt === false ) {
     die( print_r( sqlsrv_errors(), true)); 
}else{
     echo "";
}
?>