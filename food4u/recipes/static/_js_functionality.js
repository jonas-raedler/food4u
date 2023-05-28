// Functionality for Adding & Removing Input Fields

function add() {
    var new_ingredient_no = parseInt($('#total_number').val()) + 1;
    var new_input = "" +
        "<div id=ingr_form_item_" + new_ingredient_no + ">" +
            "<label for='ingredient_" + new_ingredient_no + "'>Ingredient:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>" +
            "<input type='text' name='quantity_" + new_ingredient_no + "' size='2' placeholder='e.g. 3' style='margin-right: 10px;'>" +
            "<input type='text' name='measurement_" + new_ingredient_no + "' size='2' placeholder='Tbsp.' style='margin-right: 10px;'>" +
            "<input type='text' name='ingredient_" + new_ingredient_no + "' id='ingredient_" + new_ingredient_no + "' size='30' placeholder='Honey'>" +
        "</div>";


    $('#ingredient_list').append(new_input);
    $('#total_number').val(new_ingredient_no);

    document.getElementById("test").innerHTML = "hahaha";
    console.log(new_ingredient_no);
}

function remove() {
    var last_ingredient_no = $('#total_number').val();

    if (last_ingredient_no > 1) {
        $('#ingr_form_item_' + last_ingredient_no).remove();
        $('#total_number').val(last_ingredient_no - 1);
    }
}


function addLineBreak() {
    var
}
