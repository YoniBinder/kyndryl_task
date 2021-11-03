let list = document.getElementById("users-list");

let showItems = users =>{
    if(users.length===0){
        list.innerHTML="No users found"
        return
    }
        
    let details=''
    for (user of users){
        details += 
        `<div class="user-item">
        <div><b>First Name: </b>${user.first_name} </div>
        <div><b>Last Name: </b> ${user.last_name}</div>
        <div><b>ID: </b> ${user.user_id} </div>
        </div>`
       
    }
        list.innerHTML = details; 
}


document.getElementById("show-users-btn").addEventListener("click",()=>{
    axios.get(SERVER_URL+"/getusers")
    .then(function (response) {
    showItems(response.data);
    })
    .catch(function (error) {
        throw new Error('Error:',error)
    })
})

 