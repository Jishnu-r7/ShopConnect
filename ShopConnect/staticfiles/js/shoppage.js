document.getElementById("reload-link").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default behavior of the link
    location.reload(); // Reload the current page
});
var inputs = document.getElementsByClassName("hide");
for (var i = 0; i < inputs.length; i++) {
  inputs[i].style.display = "none";
}