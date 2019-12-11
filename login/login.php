<?php include("includes/header.php") ?>

<?php

	if(logged_in()) {

		redirect("admin.php");

	}


 ?>


  <?php include("includes/nav.php") ?>

	<link href="style.css" rel="stylesheet" type="text/css">
	<div class="container">
	<div>
		<div>

			<?php display_message(); ?>

			<?php validate_user_login(); ?>


		</div>
	</div>
	<div class="top">
<div class="menu float-r">
	<a href="#"><span></span></a>
	<a href="#"><span></span></a>
	<a href="#"><span></span></a>
</div>
</div>
    	<div>
			<div>
				<div class="panel panel-login" style="background-color: #333; border: none; margin: 0;">
					<div class="panel-heading" style="background-color: #333; border: none; margin: 0;">
						<div class="row">
							<div class="col-xs-6">
								<a href="login.php" class="active" id="login-form-link">Login</a>
							</div>
							<div class="col-xs-6">
								<a href="register.php" id="">Register</a>
							</div>
						</div>
						<hr>
					</div>
					<div class="panel-body">
						<div class="row">
							<div class="col-lg-12">
								<form id="login-form"  method="post" role="form" style="display: block;">
									<div class="form-group">
										<input type="text" name="email" id="email" tabindex="1" class="form-control" placeholder="Email" required>
									</div>
									<div class="form-group">
										<input type="password" name="password" id="login-
										password" tabindex="2" class="form-control" placeholder="Password" required>
									</div>
									<div class="form-group text-center">
										<input type="checkbox" tabindex="3" class="" name="remember" id="remember">
										<label for="remember" style="color: white"> Remember Me</label>
									</div>
									<div class="form-group">
										<div class="row">
											<div class="col-sm-6 col-sm-offset-3">
												<input type="submit" name="login-submit" id="login-submit" tabindex="4" class="form-control btn btn-login" value="Log In">
											</div>
										</div>
									</div>
									<div class="form-group">
										<div class="row">
											<div class="col-lg-12">
												<div class="text-center">
													<a href="recover.php" tabindex="5" class="forgot-password">Forgot Password?</a>
												</div>
											</div>
										</div>
									</div>
								</form>

							</div>
						</div>
					</div>
				</div>
			</div>

		</div>
	</div>
	<?php include("includes/footer.php") ?>
