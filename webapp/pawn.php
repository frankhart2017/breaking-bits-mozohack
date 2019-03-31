<?php include "./includes/header.php";?>





<main>
    
  <section class="section section-stats  center">
  <div class="row">
  <div class="col s12 ">
  <div class="container">
        <div class="card-panel blue darken-3 lighten-1 white-text center">
        <i class="fab fa-facebook-square fa-10x  "></i>
        <h5>No. Of Posts</h5>
            <h3 class="count">4</h3>
          <div class="progress grey lighten-1">
            <div class="determinate white" style="width: 60%;"></div>
          </div>
    <p></p>
  </div>
  </div>
  </div>
  </section>


  


    <!-- Display customers details -->
    <section class="section section-display-user">
    <div class="container">
            <div class="row">
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-user prefix"></i>
                    <input id="name" type="text" value="Username" disabled>
                    <label for="name">Username</label>
                    </div>
                </div>
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-clipboard fa-xs prefix"></i>
                    <input id="ntweets" type="text" value="Number of Posts" disabled>
                    <label for="ntweets">Number of Posts</label>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-bullhorn prefix  "></i>
                    <input id="nbully" type="text" value="Number of bullies" disabled >
                    <label for="nbully">No. Of Bullied</label>
                    </div>
                </div>
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-hashtag prefix"></i>
                    <input id="nsafe" type="text" value="Number of safe" disabled >
                    <label for="nsafe">Number of safe</label>
                    </div>
                </div>
            </div>






            <div class="row">
                <div class = "row">
                <div class="col s12 ">
                  <h6>Profile Url (Safe)</h6>
                <ul class="collapsible sip">
                </div>

                
            </div>

            <div class = "row">
                <div class="col s12 ">
                  <h6>Profile Url (Bullied)</h6>
                <ul class="collapsible bip">
                </div>
            






            </div>

           

           
        </div>
    </section>

   

    <!-- PHP FOR CI BEGINS -->
    <?php 
        if(isset($_GET['submit'])) {
            $message = "Data Entered Successfully";
            echo "<script type='text/javascript'>alert('$message');</script>";
        }
    
    ?>


  


</main>


<script type="text/javascript" src="js/jquery3.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script type="text/javascript" src="js/materialize.min.js"></script>
<script>
// Hide Sections
$('.section').hide();
    setTimeout(function () {
      $(document).ready(function () {
        // Show Sections
        $('.section').fadeIn();

        
        var request;


    // Serialize the data in the form
    var serializedData ;
    serializedData = {
      "username" : "koshvastu@gmail.com",
      "password" : "#include<sid.h>"
    }
    console.log(serializedData);
    // Let's disable the inputs for the duration of the Ajax request.
    // Note: we disable elements AFTER the form data has been serialized.
    // Disabled form elements will not be serialized.
    swal("Processing...");
    // Fire off the request to /form.php
    request = $.ajax({
        async: true,
        url: "http://fbrest.serveo.net/info",
        type: "post",
        data: serializedData
     
    });

    // Callback handler that will be called on success
    request.done( function (response, textStatus, jqXHR){
        // Log a message to the console
        swal.close();
        console.log(response)
        console.log("Hooray, it worked!");

        $(".count").html(response.num);
        $("#name").val(response.user);
        $("#ntweets").val(response.num);
        $("#nbully").val(response.nub);
        $("#nsafe").val(response.nus);
         var content = '';
         $.each(response.bip, function( index, value ) {
            content += '<li><div class="collapsible-header"><i class="material-icons">collections</i>' + value + '</div></li>';
         });
         if(content == '')
            content = "<p style='margin-left: 10px;'>Nothing to display!</p>";
         $(".bip").html(content);

         var content = '';
         $.each(response.sip, function( index, value ) {
            content += '<li><div class="collapsible-header"><i class="material-icons">collections</i>' + value + '</div></li>';
         });
         $(".sip").html(content);

    });

    // Callback handler that will be called on failure
    request.fail(function (jqXHR, textStatus, errorThrown){
        // Log the error to the console
        console.error(
            "The following error occurred: "+
            textStatus, errorThrown
        );
    });

  


















        // Hide Preloaders
        $('.loader').fadeOut();
        Materialize.toast('Weclome to Twitter Stats', 1000);
        //Init Side nav
        $('.button-collapse').sideNav();
        // Counter
        $('.count').each(function () {
          $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
          }, {
              duration: 1000,
              easing: 'swing',
              step: function (now) {
                $(this).text(Math.ceil(now));
              }
            });
        });
        // Comments-Approve & Deny
        $('.approve').click(function (e) {
          Materialize.toast('Comment Approved', 3000);
          e.preventDefault();
        });
        $('.deny').click(function (e) {
          Materialize.toast('Comment Denied', 3000);
          e.preventDefault();
        });

      });
    }, 1000);

</script>


<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
  
</body>

</html>