<?php

/*************** Helper Functions ************/

function clean($string){
  return htmlentities($string);
}

function redirect($location){
  return header("Location: {$location}");
}

function set_message($message){
  if(!empty($message)){
    $_SESSION['message'] = $message;
  }else{
    $message = "";
  }
}

function display_message(){
  if(isset($_SESSION['message'])){
    echo $_SESSION['message'];
    unset($_SESSION['message']);
  }
}

function token_generator(){
  $token = $_SESSION['token'] = md5(uniqid(mt_rand(), true));
  return $token;
}

function validation_errors($error_message){
  $error_message = <<<DELIMITER
  <div class="alert alert-danger" role="alert">$error_message</div>
DELIMITER;
  return $error_message;
}

function email_exists($email){
  // $sql = "SELECT id FROM users WHERE email='$email'";
  $sql = "SELECT id FROM users WHERE email='$email'";
  $result = query($sql);

  if(row_count($result)==1){
    return true;
  }else{
    return false;
  }
}

function username_exists($username){
  $sql = "SELECT id FROM users WHERE username='$username'";
  $result = query($sql);

  if(row_count($result)==1){
    return true;
  }else{
    return false;
  }
}

/*************** Validation Functions ************/


function validate_user_registration(){
  $errors = [];

  $min = 2;
  $max = 30;


  if($_SERVER['REQUEST_METHOD']=="POST"){
    $first_name = clean($_POST['first_name']);
    $last_name = clean($_POST['last_name']);
    $username = clean($_POST['username']);
    $email = clean($_POST['email']);
    $password = clean($_POST['password']);
    $confirm_password = clean($_POST['confirm_password']);
  }
  if(strlen($first_name)<$min) {
    $errors[] = "Your first name cannot be less than {$min} characters";
  }

  if(strlen($first_name)>$max) {
    $errors[] = "Your first name cannot be more than {$max} characters";
  }

  if(strlen($last_name)<$min) {
    $errors[] = "Your last name cannot be less than {$min} characters";
  }

  if(strlen($last_name)>$max) {
    $errors[] = "Your last name cannot be more than {$max} characters";
  }

  if(strlen($username)<$min) {
    $errors[] = "Your username cannot be less than {$min} characters";
  }

  if(strlen($username)>$max) {
    $errors[] = "Your username cannot be more than {$max} characters";
  }

  if(username_exists($username)){
    $errors[] = "Sorry that username is already taken";
  }

  if(email_exists($email)){
    $errors[] = "Sorry that email is already registered";
  }

  if(strlen($email)<$min) {
    $errors[] = "Your email cannot be less than {$min} characters";
  }

  if($password!==$confirm_password){
    $errors[] = "Your password fields do not match";
  }

  if(!empty($errors)){
    foreach ($errors as $error) {
      // Error Display
      echo validation_errors($error);
    }
  }
}



?>
