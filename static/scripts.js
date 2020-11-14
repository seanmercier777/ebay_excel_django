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









