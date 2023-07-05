var volume;
  var item_id;
  function openWindow1() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("new-window").style.display = "block";
}

  function closeWindow() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("new-window").style.display = "none";
}

  function openAddItemWindow() {
    closeWindow();
    document.getElementById("overlay").style.display = "block";
    document.getElementById("add-item-window").style.display = "block";
}

  function closeAddItemWindow() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("add-item-window").style.display = "none";
}

  function submitItem(event) {
    event.preventDefault();
    var form = document.getElementById('add-item-form');
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "owner_add_item", true);
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
    closeAddItemWindow();
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
  function submit_edit_item(event){
    event.preventDefault();
    var label = document.getElementById("pname_label");
    var labelValue = label.textContent;
    var form = document.getElementById('edit_item_form');
    var formData = new FormData(form);
    formData.append("pname_label", labelValue);
    formData.append("item_vol", volume);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "edit_shop_item", true);
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
  function existing_item_button(name){
    closeWindow()
    document.getElementById("overlay").style.display = "block";
    document.getElementById("existing-window").style.display = "block";
          
    var nameToFind = name; // Replace with the name you want to find
    var dataElements = document.getElementsByClassName("data");
    var plabel = document.getElementById("existing_pname_label");
    plabel.textContent=name;
    var matchingElement = Array.from(dataElements).find(function(element) {
      return element.dataset.name === nameToFind;
  });
    if (matchingElement) {
      item_id = matchingElement.dataset.id;
      console.log("Corresponding ID:", item_id);
  }
}

  function close_existing_item_window() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("existing-window").style.display = "none";
}
  function submit_existing_item(event){
    event.preventDefault();
    var form = document.getElementById('existing_item_form');
    var formData = new FormData(form);
    formData.append("item_id", item_id);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "submit_existing_item", true);
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
    close_existing_item_window();
}