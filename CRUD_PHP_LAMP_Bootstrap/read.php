<?php

  // Copyright (C) 2017-2018 Jamil Said Jr 

  require 'db.php';
  $id = null;
  if ( !empty($_GET['id']) ) {
    $id = $_GET['id'];
  }
 
  if ( null === $id ) {
    header("Location: index.php");
  } else {
    $pdo = Database::connect();
    $sql = "SELECT * FROM Customers where id = ?";
    $q = $pdo->prepare($sql);
    $q->execute(array($id));
    $data = $q->fetch(PDO::FETCH_ASSOC);
    Database::disconnect();
  }
?>

<!DOCTYPE html>
<html dir="ltr" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>CRUD LAMP</title>
    <meta name="description" content="CRUD LAMP" />
    <meta name="keywords" content= "CRUD LAMP" />
    <!-- using CDN links -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
    crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"
    integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
    crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" 
    integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" 
    crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="container">
      <div class="span10 offset1">
        <div class="row">
          <h3>Customer Information:</h3>
        </div>
      <div class="form-horizontal" >
        <div class="control-group">
          <span><label class="control-label" style="margin-right:7px;">First Name:</label><?php echo $data['firstName'];?></span>
        </div>
        <div class="control-group">
          <span><label class="control-label" style="margin-right:7px;">Last Name:</label><?php echo $data['lastName'];?></span>
        </div>
        <div class="control-group">
          <span><label class="control-label" style="margin-right:7px;">Email Address:</label><?php echo $data['email'];?></span>
        </div>
        <div class="control-group">
          <span><label class="control-label" style="margin-right:7px;">Phone Number:</label><?php echo $data['phone'];?></span>
        </div>
        <div class="form-actions">
          <a class="btn btn-default" style="margin-top:12px;" href="index.php">Back to Home</a>
        </div>

        </div>
      </div>

    </div> <!-- /container -->  
  </body>
</html>

