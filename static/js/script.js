const messageDiv = document.createElement('div');
messageDiv.textContent = 'Sinu vastus salvestatud';
messageDiv.classList.add('fade-message');
document.body.appendChild(messageDiv);
setTimeout(()=> messageDiv.remove(), 2000);

const input = document.querySelector('input[name="q1"]');
const counter = document.getElementById('char-count');
input.addEventListener('input', () => {
    counter.textContent = '${input.value.length} tähemärki';