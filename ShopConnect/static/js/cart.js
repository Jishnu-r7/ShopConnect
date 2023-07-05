window.addEventListener("DOMContentLoaded", function() {
  var defaultAddressRadio = document.getElementById("default-address");
  var newAddressRadio = document.getElementById("new-address");
  var houseNameInput = document.getElementById("house-name");
  var roadNameInput = document.getElementById("road-name");
  var localityInput = document.getElementById("locality");
  var districtInput = document.getElementById("district");
  var house = houseNameInput.value;
  var road= houseNameInput.value;
  var locality=localityInput.value;
  var dist=districtInput.value;
  // Disable input fields by default
  houseNameInput.readOnly = true;
  roadNameInput.readOnly = true;
  localityInput.readOnly = true;
  districtInput.readOnly = true;

  // Event listener for default address radio button
  defaultAddressRadio.addEventListener("change", function() {
    if (defaultAddressRadio.checked) {
      // Set default values from Django context variables
      houseNameInput.value = house;
      roadNameInput.value = road;
      localityInput.value = locality;
      districtInput.value = dist;

      // Disable input fields
      houseNameInput.readOnly = true;
      roadNameInput.readOnly = true;
      localityInput.readOnly = true;
      districtInput.readOnly = true;
    }
  });

  // Event listener for new address radio button
  newAddressRadio.addEventListener("change", function() {
    if (newAddressRadio.checked) {
      // Clear values
      houseNameInput.value = "";
      roadNameInput.value = "";
      localityInput.value = "";
      districtInput.value = "";

      // Enable input fields
      houseNameInput.readOnly = false;
      roadNameInput.readOnly = false;
      localityInput.readOnly = false;
      districtInput.readOnly = false;
    }
  });
});

// Get all the number divs
var numberDivs = document.getElementsByClassName('for_calc');

// Iterate over each number div
for (var i = 0; i < numberDivs.length; i++) {
  // Get the current number div
  var numberDiv = numberDivs[i];
  
  // Get the number value from the div
  var number = parseFloat(numberDiv.getElementsById('hid')[0].textContent);
  var number1 = parseFloat(numberDiv.getElementsById('count_value')[0].textContent);
  
  // Calculate the product
  var product = number * number1; // Example calculation, adjust as needed
  
  // Get the corresponding result div
  var resultDiv = document.getElementsById('result')[i];
  
  // Set the product as the text content of the result div
  resultDiv.getElementsByClassName('result')[0].textContent = product;
}

function close_edit_item_window() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("edit-window").style.display = "none";
}
function closeWindow() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("new-window").style.display = "none";
}
function close_edit_item_window() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("edit-window").style.display = "none";
}

function submit_edit_item(event){
  event.preventDefault();
  var label = document.getElementById("pname_label");
  var labelValue = label.textContent;
  var form = document.getElementById('edit_item_form');
  var formData = new FormData(form);
  formData.append("pname_label", labelValue);
  formData.append("item_vol", volume);
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "edit_user_item", true);
  xhr.onreadystatechange = function() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
      // Request completed successfully
      window.location.reload(); // Reload the page
  } else {
      // Handle any error
  }
}
};
  xhr.send(formData);
  close_edit_item_window();

}

function edititembutton(name,count,vol){
  document.getElementById("overlay").style.display = "block";
  document.getElementById("edit-window").style.display = "block";
  var plabel = document.getElementById("pname_label");
  plabel.textContent=name;
  var input = document.getElementById("qty_input");
  input.value = count;
  volume=vol;
}
function close_edit_item_window() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("edit-window").style.display = "none";
}


const defaultAddressOption = document.getElementById('default-address');
const newAddressOption = document.getElementById('new-address');
const addressForm = document.querySelector('.address-form');

// defaultAddressOption.addEventListener('change', function () {
//   addressForm.classList.remove('active');
// });

// newAddressOption.addEventListener('change', function () {
//   addressForm.classList.add('active');
// });