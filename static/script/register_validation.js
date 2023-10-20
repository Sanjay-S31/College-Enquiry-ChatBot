function reg_check(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var username = document.getElementById("username").value;
        
    if (email == "" || username == "" || password == "") {
        Swal.fire({
            icon:'error',
            text:'All fields are required',
            title:'Error..',
            showConfirmButton: false
        }
        );
        return false;
    }
        
    if (!email.includes("@")) {
        Swal.fire({
            icon:'warning',
            text:'Please enter a valid email address',
            title:'Error..',
            showConfirmButton: false
        }
        );
        return false;
    }
    var alphanumeric = /^[0-9a-zA-Z]+$/;
    if (!username.match(alphanumeric)) {
        Swal.fire({
            icon:'warning',
            text:'Username should only contain alphanumeric characters',
            title:'Error..',
            showConfirmButton: false
        }
        );
        return false;
    }
        
    if (password.length < 6 || password.length > 20) {
        Swal.fire({
            icon:'warning',
            text:'Password should be between 6 and 20 characters',
            title:'Error..',
            showConfirmButton: false
        }
        );
        return false;
    }
    Swal.fire({
        icon:'success',
        text:'Welcome to College Enquiry Chatbot!',
        title:'Registration Successful !!',
        showConfirmButton: false
    }
    );
}