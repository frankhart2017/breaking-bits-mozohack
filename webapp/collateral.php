<?php include "./includes/header.php";?>





<main>
    
  <section class="section section-stats  center">
  <div class="row">
  <div class="col s12 ">
  <div class="container">
  <div class="card-panel blue lighten-1 white-text center">
  <i class="fab fa-twitter fa-10x   "></i>
            <h5>No. Of Tweets Made</h5>
            <h3 class="count">1000</h3>
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
                    <i class="fas fa-sync fa-xs prefix"></i>
                    <input id="fname" type="text" value="Number of tweets" disabled>
                    <label for="ntweets">No. Of Tweets</label>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-bullhorn prefix  "></i>
                    <input id="phone" type="text" value="Number of bullies" disabled >
                    <label for="nbully">No. Of Bullied Tweets</label>
                    </div>
                </div>
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="fas fa-hashtag prefix"></i>
                    <input id="address" type="text" value="Number of safe" disabled >
                    <label for="stweets">Safe Tweets</label>
                    </div>
                </div>
            </div>

            <div class="row">
              




                <div class="col s12 ">
                  <div class="container">
                     <div class="card">
                     
                  <div class="card-content">
                  
                     
                       
                    </div>
                  </div>
                </div>
                 
                    </div>
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


  



    <!-- <section class="section section-display-user">
        <div class="container">
            <div class="row">
                <div class="col s12 m6">
                    <div class="input-field">
                    <i class="material-icons prefix">face</i>
                    <input id="name" type="text" value="RUSHIL" disabled>
                    <label for="name">Name</label>
                    </div>
                </div>

                <div class="col s12 m6">
                    <div class="box">2</div>
                </div>
            </div>
        </div>
    </section> -->

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
      "handle" : "@sdharchou"
    }
    console.log(serializedData);
    // Let's disable the inputs for the duration of the Ajax request.
    // Note: we disable elements AFTER the form data has been serialized.
    // Disabled form elements will not be serialized.
    swal("Processing...");
    // Fire off the request to /form.php
    request = $.ajax({
        async: true,
        url: "http://twrest.serveo.net/info",
        type: "post",
        data: serializedData
     
    });

    // Callback handler that will be called on success
    request.done( function (response, textStatus, jqXHR){
        // Log a message to the console
        swal.close();
        console.log(response)
        console.log("Hooray, it worked!");

        $(".count").html(response.nut);
        $("#name").val(response.handle);
        $("#fname").val(response.nut);
        $("#phone").val(response.nub);
        $("#address").val(response.nus);
        var content = '<span class="card-title center">Bad Users</span>';
        $.each(response.bad, function( index, value ) {
          content += '<div class="chip"><img src="img/logo2.png" alt="Contact Person">' + value + '</div>'
        });
        $(".card-content").html(content);

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