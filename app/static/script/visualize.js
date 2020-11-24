document.getElementById("go_btn").addEventListener("click", populateData);

function populateData(){
    const input_data = document.getElementById("input_data").value;
    console.log("{{ grid_size }}")
    $.ajax({
        type: "POST",
        url: "/get_bin",
        data: { data: input_data},
        dataType: "text"
      }).done(function(res) {
        document.getElementById("decoded_data").innerHTML = res;
      });
}

