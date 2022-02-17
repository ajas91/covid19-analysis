function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

var val = parseInt($('.number').text());
//Use the code in the answer above to replace the commas.
val = numberWithCommas(val);
$('.number').text(val);