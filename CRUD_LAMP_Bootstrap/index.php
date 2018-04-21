<!DOCTYPE html>
<html dir="ltr" lang="en">
  <!-- Copyright (C) 2017-2018 Jamil Said Jr -->
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
      <div class="row">
        <h3>Customers -- LAMP CRUD</h3>
      </div>
      <div class="row">
        <p>
          <a href="create.php" class="btn btn-primary">Create a Customer</a>
        </p>
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Email Address</th>
              <th>Phone Number</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <?php
              require 'db.php';
              $pdo = Database::connect();
              $sql = 'SELECT * FROM Customers ORDER BY firstName ASC';
              foreach ($pdo->query($sql) as $row) {
                echo '<tr>';
                echo '<td>'. $row['firstName'] . '</td>';
                echo '<td>'. $row['lastName'] . '</td>';
                echo '<td>'. $row['email'] . '</td>';
                echo '<td>'. $row['phone'] . '</td>';
                echo '<td>';
                echo '<a class="btn btn-success" href="read.php?id='.$row['id'].'">Read</a>';
                echo ' ';
                echo '<a class="btn btn-warning" href="update.php?id='.$row['id'].'">Update</a>';
                echo ' ';
                echo '<a class="btn btn-danger" href="delete.php?id='.$row['id'].'">Delete</a>';
                echo '</td>';
                echo '</tr>';
              }
              Database::disconnect();
            ?>
          </tbody>
        </table>
      </div>
    </div> <!-- /container -->
  </body>
</html>



