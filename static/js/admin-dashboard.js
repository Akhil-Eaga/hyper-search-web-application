
// ------------ Function to reveal / hide user info on admin dashboard------------//
const userinfoBox = document.querySelector(".user-info");
function userinfoReveal() { userinfoBox.classList.remove("hide") }
function userinfoHide() { userinfoBox.classList.add("hide") }


// ------------ Ajax send a delete request to Flask------------//
function sendDeleteRequest(event) {

    // Find the parent div of the event.
    var parentId = "id" + event.target.id;

    // Find the username from the parent div table.
    var username = document.getElementById(parentId).querySelector(".username").innerHTML;

    //log
    console.log(username);
    console.log("Making a delete user request");

    //Ajax request
    $.ajax({
        type: "POST",
        url: "/admin_delete_user",
        data: username,
        dataType: 'json'
    }).done(function (data) {
        console.log("User deleted");
    });

    // Disable the delete button.
    document.getElementById(event.target.id).disabled = true;
    event.target.innerHTML = "Deleted";

    // Reveal the hidden user info box
    userinfoReveal();
}

// ------------ Ajax send a delete database request to Flask ------------//
function sendDeleteDatabaseRequest(event) {
    console.log("Making a delete user request");

    // Confirm again with admin before making the actual request.
    if (confirm("You cannot undo this action. Please confirm.")) {
        // Ajax request
        $.ajax({
            type: "POST",
            url: "/admin_delete_database",
            data: "delete-db",
            dataType: 'json'
        }).done(function (data) {
            console.log("Sent delete request.");
        });

        // Disable the button
        document.getElementById(event.target.id).disabled = true;
        event.target.innerHTML = "Database Flushed!";
    }
    else {
        // Admin cancelled the action.
        alert("You have cancelled the operation.");
    }
}


// ------------ End of Admin-Dashboard JS------------//
// Last Modified: 23/05/2021 - Arjun Panicker