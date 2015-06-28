function ajax_run() {
    $.ajax({
        url: 'http://192.168.43.48:8000/json',
        type: 'get', //this is the default though, you don't actually need to always mention it
        success: function (data) {
            values = JSON.parse(data)
            $.each(values["doors"], function (i, val) {
                $("#" + i).attr("class", val);
            });
            $.each(values["temp"], function (i, val) {
                $("#" + i).html(val + "&#x2103;");
            });
        },
        failure: function (data) {
            alert('Got an error dude');
        }
    });

}

ajax_run();
setInterval(ajax_run, 1000);