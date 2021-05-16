// JS code to add user input validation in the quiz form submission

$(document).ready(function () {

    // the min_max_lengths array is used to set the minlength and maxlength attributes of the input elements
    // first element in the array is a dummy value as index 0 corresponds to the form.hidden_tag() element.
    // that is why the looping starts from 1 and ends at 10 instead of 0-9
    var min_max_lengths = [1000, 1, 11, 11, 19, 24, 21, 19, 2, 13, 13];

    // grabbing all the input elements present on the quiz page
    var input_elements = document.querySelectorAll("input");

    // looping over all the input elements except the first one which is the form.hidden_tag()
    for (i = 1; i < 11; i++) {
        // setting the required attribute to true
        input_elements[i].setAttribute("required", "true");

        // setting the minlength attribute to the corresponding value in the min_max_lengths array
        input_elements[i].setAttribute("minlength", String(min_max_lengths[i]));

        // setting the maxlength attribute to the corresponding value in the min_max_lengths array
        input_elements[i].setAttribute("maxlength", String(min_max_lengths[i]));
    }
});