document.getElementById('feedback-firm').addEventListener('submit', function(event) {
    event.preventDefault();

    const inputBox = document.getElementById('user_input');
    const message = inputBox.value;
    if(message.trim() === "") return;
    
    // Lisa kasutaja sõnum
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<div class="message user"><strong>Sina:</strong> ${message}</div>`;

    // AJAX päring Flaskile
    fetch('/get_response', {
        method: 'POST',
        body: new URLSearchParams({'messages': message})
    })
    .then(response => response.json())
    .then(data => {
        messagesDiv.innerHTML += `<div class="message bot"><strong>Bot:</strong> ${data.response}</div>`;
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    });

    inputBox.value = '';
    
}