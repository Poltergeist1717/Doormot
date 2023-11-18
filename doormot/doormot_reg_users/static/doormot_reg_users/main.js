
function updateUserTypeAndSubmit(){
    var selectedUserType = document.getElementById("userTypeSelect").value;
    document.getElementById("userTypeInput").value = selectedUserType;
    return true;
    
}

// function updateUserTypeInSecondForm(){
//     var selectedUserType = updateUserTypeAndSubmit();
//     document.getElementById('userTypeInput').value = selectedUserType;
//     return true;
// }