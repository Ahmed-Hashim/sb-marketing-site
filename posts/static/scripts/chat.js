

id = JSON.parse(document.getElementById('json-username').textContent);
message_username = JSON.parse(document.getElementById('json-message-username').textContent);
receiver = JSON.parse(document.getElementById('json-username-receiver').textContent);
link = 'wss://'+ window.location.host+ '/ws/'+ id + '/'
socket = new WebSocket(link);
sound = new Audio(product_detail_url);




socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    
    
    if(data.username == message_username){
        document.querySelector('#messages_ul').innerHTML += `
                                                            <li class="clearfix admin_chat">
                                                                <div class="chat-body clearfix">
                                                                    <p>
                                                                    ${data.message}
                                                                    </p>
                                                                    <div class="chat_time">Just Now</div>
                                                                </div>
                                                            </li>
                                                            `
    } else {
        sound.play()
        document.querySelector('#messages_ul').innerHTML += `
                                                            <li class="clearfix user2_chat">                                                         
                                                                <div class="chat-body clearfix">
                                                                    <p>
                                                                    ${data.message}
                                                                    </p>
                                                                    <div class="chat_time">Just Now</div>
                                                                </div>
                                                            </li>
                                                                `
    }
}
function scrollToBottom() {
    
        let chatBox = $("#messages");
    chatBox.mCustomScrollbar("scrollTo", "bottom", {
        scrollEasing: "easeOut"
      });
    

}
$("#id_content").keydown(function(event) {
    const textareaValue = $("#id_content").val().trim();
    // Check if Enter key is pressed (keyCode 13)
    let message_input = document.querySelector('#id_content');
    let message = message_input.value;
    let chatBox = $("#messages");
    if (event.keyCode === 13) {
        if (event.shiftKey) {
            // Allow a new line (Shift+Enter), do not prevent default
        } else {
            // Prevent the default Enter key behavior (line break)
            event.preventDefault();
            // Check if the textarea is not empty
            if (textareaValue !== "") {
                // Trigger the HTMX POST request on the button click
               
                socket.send(JSON.stringify({
                    'message':message,
                    'username':message_username,
                    'receiver':receiver
                }));
            
                message_input.value = '';
                setInterval(scrollToBottom, 50);

                
            }
        }
    }
});
$("#send_message").click(function(event) {
    const textareaValue = $("#id_content").val().trim();
    // Check if Enter key is pressed (keyCode 13)
    let message_input = document.querySelector('#id_content');
    let message = message_input.value;
    let chatBox = $("#messages");
    if (textareaValue !== "") {
            // Trigger the HTMX POST request on the button click
            socket.send(JSON.stringify({
                'message':message,
                'username':message_username,
                'receiver':receiver
            }));
        
            message_input.value = '';
            chatBox.mCustomScrollbar("scrollTo", "bottom", {
                scrollEasing: "easeOut"
            });
            chatBox.mCustomScrollbar("scrollTo", "bottom", {
                scrollEasing: "easeOut"
            });
            
        }
}); 
htmx.on("htmx:afterRequest", function(event) {
    socket.close()
});