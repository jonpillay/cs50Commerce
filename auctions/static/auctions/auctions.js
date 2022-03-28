/*document.addEventListener('DOMContentLoaded', () => {
    var countdown = document.getElementById("initial").innerHTML
    console.log(countdown);
    var x = setInterval(function() {

        var days = Math.floor(countdown / (60 * 60 * 24));
        var hours = Math.floor((countdown % (1000 * 60 * 60 * 24)) / (100 * 60 * 60));
        var minutes = Math.floor((countdown % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((countdown % (1000 * 60)) / 1000);

        document.getElementById("counter").innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

        function count() {
            countdown-1;
            document.querySelector('#counter').innerHTML = count;
        }

        if (countdown < 0) {
            clearInterval(x);
            document.getElementById("demo").innerHTML = "EXPIRED";
        }
    }, 1000);
}) */

document.addEventListener('DOMContentLoaded', () => {
    const set = document.querySelectorAll('.counter');
    console.log(set);
    set.forEach(function(item) {
        var endDate = Date.parse(item.dataset.enddate);
        console.log (typeof(endDate));
        console.log ("This is the enddate object " + Date.parse(item.dataset.enddate))
        console.log(endDate)
        console.log("Got here");
        console.log("This is the Date.now " + (Date.now()));
        var millisec_left = endDate - Date.now();
        console.log("This is " + parseInt(millisec_left))
        var days = Math.floor(millisec_left / (1000 * 60 * 60 * 24));
        var hours = Math.floor((millisec_left % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((millisec_left % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((millisec_left % (1000 * 60)) / 1000);
        item.innerHTML = days + " Days " + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds";
    });
    setInterval(() => {
        set.forEach(function(item, index, array) {
            var endDate = Date.parse(item.dataset.enddate);
            console.log (typeof(endDate));
            console.log ("This is the enddate object " + Date.parse(item.dataset.enddate))
            console.log(endDate)
            console.log("Got here");
            console.log("This is the Date.now " + (Date.now()));
            var millisec_left = endDate - Date.now();
            console.log("This is " + parseInt(millisec_left))
            var days = Math.floor(millisec_left / (1000 * 60 * 60 * 24));
            var hours = Math.floor((millisec_left % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((millisec_left % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((millisec_left % (1000 * 60)) / 1000);
            item.innerHTML = days + " Days " + hours + " Hours " + minutes + " Minutes " + seconds + " Seconds";
        });
    }, 1000);
});