function call_counter(url, pk) {
    window.open(url);
    $.get('YOUR_VIEW_HERE/' + pk + '/', function (data) {
        alert("counter updated!");
    });
}


function call_excel() {
    var keywords = $('#id_keyword').val();

    if (keywords === "") {
        return;
    }

    var category = $('#category').val();

    $.get({
        url: '/ajax/generate_results_table/',
        type: 'GET',
        success: function (data)
        {
            //alert("WHAT WHAT WHAT");
            window.open('data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,' + encodeURI(data));
            return data;
        }
    });
    //
    // $.ajax({
    //     url: '/ajax/generate_results_table/',
    //     data: {
    //         'keywords': keywords,
    //         'category': category,
    //     },
    //     type: 'GET',
    //     success: function (data) {
    //
    //         alert("WHAT WHAT WHAT")
    //
    //         //window.open('data:text/csv;charset=utf-8,' + encodeURIComponent(data));
    //
    //         var hiddenElement = document.createElement('a');
    //         hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(data);
    //         hiddenElement.target = '_blank';
    //         hiddenElement.download = 'people.csv';
    //
    //         hiddenElement.click();
    //
    //     },
    //     error: function (jqXHR, textStatus, errorThrown) {
    //         console.log(textStatus);
    //         console.log(errorThrown);
    //     }
    // });
}









