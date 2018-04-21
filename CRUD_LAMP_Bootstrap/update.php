<?php

  // Copyright (C) 2017-2018 Jamil Said Jr 

  require 'db.php';
  
  $id = null;
  if ( !empty($_GET['id']) ) {
    $id = $_GET['id'];
  }

  if ( null === $id ) {
    header("Location: index.php");
  }

  if ( !empty($_POST)) {
    // initialize errors to null
    $fnameError = null;
    $lnameError = null;
    $emailError = null;
    $phoneError = null;

    // save post values to variables
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];

    // validate user input
    $valid = true;
    if (empty($firstName)) {
      $fnameError = 'Please enter your first name';
      $valid = false;
    }

    if (empty($lastName)) {
      $lnameError = 'Please enter your last name';
      $valid = false;
    }

    if (empty($email)) {
      $emailError = 'Please enter email address';
      $valid = false;
    } else if ( !filter_var($email,FILTER_VALIDATE_EMAIL) ) {
      $emailError = 'Please enter a valid email address';
      $valid = false;
    }

    if (empty($phone)) {
      $phoneError = 'Please enter your phone number';
      $valid = false;
    }

    // update data
    if ($valid) {
      $pdo = Database::connect();
      $sql = "UPDATE Customers set firstName = ?, lastName = ?, email = ?, phone =? WHERE id = ?";
      $q = $pdo->prepare($sql);
      $q->execute(array($firstName,$lastName,$email,$phone,$id));
      Database::disconnect();
      header("Location: index.php");
    }
  } else {
    $pdo = Database::connect();
    $sql = "SELECT * FROM Customers where id = ?";
    $q = $pdo->prepare($sql);
    $q->execute(array($id));
    $data = $q->fetch(PDO::FETCH_ASSOC);
    $firstName = $data['firstName'];
    $lastName = $data['lastName'];
    $email = $data['email'];
    $phone = $data['phone'];
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
          <h3>Update Customer:</h3>
        </div>

        <form class="form-horizontal" action="update.php?id=<?php echo $id?>" method="post">
          <div class="control-group <?php echo !empty($fnameError)?'alert-danger':'';?>">
            <label class="control-label">First Name</label>
            <div class="controls">
              <input name="firstName" type="text"  placeholder="First Name" value="<?php echo !empty($firstName)?$firstName:'';?>">
              <?php if (!empty($fnameError)): ?>
                <span class="help-inline"><?php echo $fnameError;?></span>
              <?php endif; ?>
            </div>
          </div>
          <div class="control-group <?php echo !empty($lnameError)?'alert-danger':'';?>">
            <label class="control-label">Last Name</label>
            <div class="controls">
              <input name="lastName" type="text" placeholder="Last Name" value="<?php echo !empty($lastName)?$lastName:'';?>">
              <?php if (!empty($lnameError)): ?>
                <span class="help-inline"><?php echo $lnameError;?></span>
              <?php endif; ?>
            </div>
          </div>
          <div class="control-group <?php echo !empty($emailError)?'alert-danger':'';?>">
            <label class="control-label">Email Address</label>
            <div class="controls">
              <input name="email" type="text" placeholder="Email Address" value="<?php echo !empty($email)?$email:'';?>">
              <?php if (!empty($emailError)): ?>
                <span class="help-inline"><?php echo $emailError;?></span>
              <?php endif;?>
            </div>
          </div>
          <div class="control-group <?php echo !empty($phoneError)?'alert-danger':'';?>">
            <label class="control-label">Phone Number</label>
            <div class="controls">
              <input name="phone" type="text"  placeholder="Phone Number" value="<?php echo !empty($phone)?$phone:'';?>">
              <?php if (!empty($phoneError)): ?>
                <span class="help-inline"><?php echo $phoneError;?></span>
              <?php endif;?>
            </div>
          </div>
          <div class="form-actions" style="margin-top:12px;">
            <button type="submit" class="btn btn-warning">Update</button>
            <a class="btn btn-default" href="index.php">Back to Home</a>
          </div>
        </form>
      </div>

    </div> <!-- /container -->
  </body>
</html>



