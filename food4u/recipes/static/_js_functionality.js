// Functionality for Adding & Removing Input Fields

function add() {
    var new_ingredient_no = parseInt($('#total_number').val()) + 1;
    var new_input = "" +
        "<div id=ingr_form_item_" + new_ingredient_no + ">" +
            "<label for='ingredient_" + new_ingredient_no + "'>Ingredient:&nbsp</label>" +
            "<input type='text' id='ingredient_" + new_ingredient_no + "' name='ingredient_" + new_ingredient_no + "'>" +
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
