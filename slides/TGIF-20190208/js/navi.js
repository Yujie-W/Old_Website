// This the navigation function
document.onkeyup = function(event) {
    var x = event.which || event.keyCode;
    if (x==32){
        var curr_div = 0;
        // get current div
        var x = document.getElementsByClassName("sfigure");
        for (i = 0; i < x.length; i++) {
            if (x[i].style.display == "block") {
                curr_div = i+1;
            }
        }
        showDivs(slideIndex = curr_div+1);
    }
    else if (x==16){
        var curr_div = 0;
        // get current div
        var x = document.getElementsByClassName("sfigure");
        for (i = 0; i < x.length; i++) {
            if (x[i].style.display == "block") {
                curr_div = i+1;
            }
        }
        showDivs(slideIndex = curr_div-1);
    }
}




function currentDiv(n) {
    showDivs(slideIndex = n);
}




function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("sfigure");
    var dots = document.getElementsByClassName("demo");
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" w3-red", "");
    }
    x[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " w3-red";
}
