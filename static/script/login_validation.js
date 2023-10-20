function check(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
        
    if (email == "" || password == "") {
        Swal.fire({
            icon:'error',
            text:'Both fields are required',
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
        title:'Login Successful !!',
        showConfirmButton: false
    }
    );
}