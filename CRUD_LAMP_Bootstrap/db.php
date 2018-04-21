<?php

// Copyright (C) 2017-2018 Jamil Said Jr 

class Database
{
  private static $dbConn = null;
  
  // preventing class misuse 
  final private function __construct() {}
  final private function __clone() {}
  final private function __wakeup() {}
   
  public static function connect()
  {
      /* Using a singleton in this simple crud should be fine, but normally a 
       * dependency injection pattern should be preferrred */
      if ( null === self::$dbConn )
      {     
          try
          {
              //db credentials are stored outside of the root folder
              $dbCred = parse_ini_file('file:///home/owner/1_code_dev_linux/php/private/config.ini');
              $pwdo = $dbCred['dbUserPassword'];
              $mypwd = base64_decode($pwdo);
              
              // Create new PDO
              self::$dbConn = new PDO("mysql:host=".$dbCred['dbHost'].";"
              ."dbname=".$dbCred['dbName'].";"."charset=".$dbCred['dbCharset'],
              $dbCred['dbUsername'], $mypwd);
            
              self::$dbConn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
              self::$dbConn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); 
          }
          catch(PDOException $e)
          {
              die($e->getMessage()); 
          }
      }
      return self::$dbConn;
  }
   
  public static function disconnect()
  {
      self::$dbConn = null;
  }
}
?>
