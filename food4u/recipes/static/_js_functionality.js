// Functionality for Adding & Removing Input Fields

    $('.add').on('click', add);
    $('.remove').on('click', remove);

function add() {
  var new_ingredient_no = parseInt($('#total_number').val()) + 1;
  var new_input = "<label for='ingredient" + new_ingredient_no + "'>Ingredient:</label><input type='text' id='ingredient" + new_ingredient_no + "' name='ingredient" + new_ingredient_no + "'>";

  $('#ingredient_list').append(new_input);
  $('#total_number').val(new_chq_no);
  console.log(3);
}

function remove() {
  var last_ingredient_no = $('#total_number').val();

  if (last_ingredient_no > 1) {
    $('#ingredient_' + last_chq_no).remove();
    $('#total_number').val(last_chq_no - 1);
  }
}
