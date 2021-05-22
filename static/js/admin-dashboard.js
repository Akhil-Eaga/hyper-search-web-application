const userinfoBox = document.querySelector(".user-info");

function userinfoReveal(){
    userinfoBox.classList.remove("hide")
}

function userinfoHide(){
    userinfoBox.classList.add("hide")
}

function sendDeleteRequest(event){
    
    var parentId = "id" + event.target.id;
    var username = document.getElementById(parentId).querySelector(".username").innerHTML;
    console.log(username);
    console.log("Making a delete user request");
    $.ajax({
            type: "POST",
            url:"http://127.0.0.1:5000/admin_delete_user",
            data: username,
            dataType: 'json'
    }).done(function(data) { 
        console.log("reaching done func");        
    });
    document.getElementById(event.target.id).disabled = true;
    event.target.innerHTML = "Deleted";
    userinfoReveal();
}


function sendDeleteDatabaseRequest(event){
    console.log("Making a delete user request");

    if (confirm("You cannot undo this action. Please confirm.")) {
        txt = "You pressed OK!";
      
    $.ajax({
            type: "POST",
            url:"http://127.0.0.1:5000/admin_delete_database",
            data: "delete-db",
            dataType: 'json'
    }).done(function(data) { 
        console.log("Sent delete request.");        
    });
    document.getElementById(event.target.id).disabled = true;
    event.target.innerHTML = "Database Flushed!";
    } 
    else {
        alert("You have cancelled the operation.");
    }
}