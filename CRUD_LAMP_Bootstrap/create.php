<?php
  
  // Copyright (C) 2017-2018 Jamil Said Jr 
     
  require 'db.php';

  if ( !empty($_POST) ) {
    // initialize validation errors
    $fnameError = null;
    $lnameError = null;
    $emailError = null;
    $phoneError = null;
     
    // save post values to variable
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
     
    // validate input
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
        $emailError = 'Please enter your email address';
        $valid = false;
    } else if ( !filter_var($email,FILTER_VALIDATE_EMAIL) ) {
        $emailError = 'Please enter a valid email address';
        $valid = false;
    }
     
    if (empty($phone)) {
        $phoneError = 'Please enter your phone number';
        $valid = false;
    }
     
    // insert data
    if ($valid) {
        $pdo = Database::connect();
        $sql = "INSERT INTO Customers (firstName,lastName,email,phone) values(?, ?, ?,?)";
        $q = $pdo->prepare($sql);
        $q->execute(array($firstName,$lastName,$email,$phone));
        Database::disconnect();
        header("Location: index.php");
    }
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
          <h3>Create a Customer</h3>
        </div>
        <form class="form-horizontal" action="create.php" method="post">
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
            <input name="lastName" type="text"  placeholder="Last Name" value="<?php echo !empty($lastName)?$lastName:'';?>">
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
            <button type="submit" class="btn btn-success">Create</button>
            <a class="btn btn-default" href="index.php">Back to Home</a>
          </div>
        </form>
      </div>
    </div> <!-- /container -->
  </body>
</html>



