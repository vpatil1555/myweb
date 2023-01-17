# projects












# python manage.py makemigrations            # to create migration
# python manage.py sqlmigrate blog 0001      # migrate app with it's version
# python manage.py migrate                   # migrate all files to SQL


# ADMIN PANEL 
# python manage.py createsuperuser           

<input type="text" name="first_name" placeholder="first name">
        <input type="text" name="last_name" placeholder="last name">
        <input type="text" name="username" placeholder="username">
        <input type="email" name="email" placeholder="email">
        <input type="password" name="password1" placeholder="password">
        <input type="password" name="password2" placeholder="confirm password">
        <input type="submit">






{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  
  <title>Sign in/sign up form</title>
  <style type="text/css">
      section{
        border: 10px solid black;
        height: 90vh;
      }
      .auth-form{
        border: 10px solid gray;
        max-width: 600px;
        margin: auto;
        height: 80vh;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      hr{
        justify-items: center;
      }
  </style>
</head>

<body>
  
    <div class="auth-form">
      <form action="reg" method="post">
      {% csrf_token %}
      <div class="container">
      <h1>Register Here</h1>
      <p>Please fill in the details to create an account with us.</p>
      <hr>
      <label for="firstname"><b>First Name</b></label>
      <input type="text" placeholder="first name" name="first_name">
      <label for="lastname"><b>Last Name</b></label>
      <input type="text" placeholder="last name" name="last_name">
      <label for="username"><b>Username</b></label>
      <input type="text" placeholder="username" name="username">
      <label for="email"><b>Enter Email</b></label>
      <input type="text" placeholder="Enter Email" name="email">
      <label for="pwd"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="password1">
      <label for="confirm"><b>Confirm Password</b></label>
      <input type="password" placeholder="Confirm Password" name="password2">
      <hr>
      <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>
      <button type="submit" class="registerbtn"><strong>Register</strong></button>
      </div>
      <div class="container signin">
      <p>Already have an account? <a href="accounts/Login">Sign in</a>.</p>
      </div>
      </form>
    </div>

  

  {% for Message in messages %}
  <h3> {{Message}} </h3>
  {% endfor %}



</body>

</html>



<!-- section -->
      <section class="layout_padding">
         <div class="container">
            <div class="row">
               <div class="col-md-12">
                  <div class="full heading_s1">
                     <h3>Request A Call Back</h3>
                     <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit..</p>
                  </div>
               </div>
            </div>
         </div>
         <div class="callback">
            <form action="contact" method="post">
             {% csrf_token %}
                           <input type="text" placeholder="Your Name" name="name" ><br>
                           <input type="phone" placeholder="Phone Number" name="phone_no" ><br>
                           <input type="email" placeholder="email" name="email" ><br>
                           <textarea placeholder="Message" name="message" ></textarea>
                           <center>
                            <input type="submit" value="Send Query" id="submit">
                          </center>
                        </div>
         
      </section>
      <!-- end section -->