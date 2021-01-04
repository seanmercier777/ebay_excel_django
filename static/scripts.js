function call_excel() {

    var keywords = $('#id_keyword').val();

        if (keywords === "") {
        return;
    }

    var store = $('#id_store').val();

    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        var a, today;
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            a = document.createElement('a');
            a.href = window.URL.createObjectURL(xhttp.response);
            today = new Date();
            a.download = "ebay_output_" + keywords + "_" + today.toDateString().split(" ").join("_") +".xlsx"
            a.style.display = 'none';
            document.body.appendChild(a);
            return a.click();
        }
    };

    xhttp.open("GET", `/generate_results_table?keywords=${keywords}&store=${store}`, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.responseType = 'blob';
    xhttp.send(keywords);
}

function call_player() {

    var startDate = $('#startdate').val();
    var endDate = $('#enddate').val();
    var file = $('#file1');
    var fileContent = $('#file1').content;
    var fileContents = $('#file1').contents;

    var keywords = $('#id_keyword').val();

        if (keywords === "") {
        return;
    }

    var store = $('#id_store').val();

    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        var a, today;
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            a = document.createElement('a');
            a.href = window.URL.createObjectURL(xhttp.response);
            today = new Date();
            a.download = "ebay_output_" + "KEY" + "_" + today.toDateString().split(" ").join("_") +".xlsx"
            a.style.display = 'none';
            document.body.appendChild(a);
            return a.click();
        }
    };

    xhttp.open("GET", `/player_import?startdate=${startDate}&enddate=${endDate}&file=${file}`, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.responseType = 'blob';
    xhttp.send(keywords);
}








$('.datepicker').datepicker({
    format: 'mm/dd/yyyy',
    startDate: '-3d'
});



function downloadFile(fileName, urlData) {

    var aLink = document.createElement('a');
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("click");
    aLink.download = fileName;
    aLink.href = urlData;
    aLink.dispatchEvent(evt);
}




