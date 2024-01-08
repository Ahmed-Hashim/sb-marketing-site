const loggedin_user = JSON.parse(document.getElementById('json-message-username').textContent);
const online_status = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/'
    + 'status/'
)

online_status.onopen = function(e){
    online_status.send(JSON.stringify({
        'username':loggedin_user,
        'type':'open'
    }))
}

window.addEventListener("beforeunload", function(e){
    online_status.send(JSON.stringify({
        'username':loggedin_user,
        'type':'offline'
    }))
})


online_status.onmessage = function(e){
    var data = JSON.parse(e.data)
    if (data.username != loggedin_user) {
        var user_to_change = document.getElementById(`${data.username}_status`)
        var user_to_change1 = document.getElementById(`${data.username}_status1`)
        var small_status_to_change = document.getElementById(`${data.username}_small`)
        var small_status_to_change1 = document.getElementById(`${data.username}_small1`)
        if(data.online_status == true){
            user_to_change.style.color = 'green'
            small_status_to_change.textContent = 'Online'
            user_to_change1.style.color = 'green'
            small_status_to_change1.textContent = 'Online'
        }else{
            user_to_change.style.color = 'grey'
            small_status_to_change.textContent = 'Offline'
            user_to_change1.style.color = 'grey'
            small_status_to_change1.textContent = 'Offline'
        }
    }
}