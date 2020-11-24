function get_bin(data, grid_size = null){
    var output = "";
    if (! grid_size){
        for (var i = 0; i < data.length; i++) {
            output += data[i].charCodeAt(0).toString(2) + " ";
        }
    }
    else {
        bin = data.charCodeAt(0).toString(2);
        output += (bin.length < 8)? "0".repeat(8 - bin.length) + bin: bin;
    }
    return output
}