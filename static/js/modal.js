const btn = document.getElementById('help');
const modal = document.getElementById('modalbox');
const closing = document.getElementById('close');

btn.onclick = function() {
    modal.style.display = "block";   
}

closing.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}