let firstName = document.getElementById("firstName");
let lastName = document.getElementById("lastName");
let userId = document.getElementById("userId");
let message= document.getElementById("message");


const nameString = /^[A-Z][a-z]*$/;
const idNumber= /^[0-9]+$/


function messageShow(msg,status){
    message.setAttribute("class",status)
    message.innerHTML=msg
}


document.getElementById("add-user-btn").addEventListener("click",()=>{
 
    if(!nameString.test(firstName.value))
        messageShow("First name must contain capital letter and then letters","fail")
    else if(!nameString.test(lastName.value))
        messageShow("Last name must contain capital letter and then letters","fail")
    else if(!idNumber.test(userId.value))
        messageShow("ID must contain one digit or more","fail")
    else
        axios.post(SERVER_URL+"/adduser",{
            first_name:firstName.value,
            last_name:lastName.value,
            user_id:userId.value
        })
        .then(function (response) {
            messageShow(response.data,"success")
        })
        .catch(function (error) {
            throw new Error('Error:',error)
        })
})