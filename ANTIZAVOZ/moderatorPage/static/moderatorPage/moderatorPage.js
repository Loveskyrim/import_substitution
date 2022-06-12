$(document).ready(function () {
    var $updateDB = $('#update-db')
    var $updateProductDB = $('#update-product-db')
    var $updateOkvedDB = $('#update-okved')
    var $parseFabricatorDB = $('#parse-fabricator')

    $updateDB.click(function() {
        $.ajax({
            type: 'POST',
            url: '/moderate/update_database',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                console.log(data)
            },
            error: function (error) {
            }
        });
    });

    $updateProductDB.click(function() {
        $.ajax({
            type: 'POST',
            url: '/moderate/update_productsdb',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                console.log(data)
            },
            error: function (error) {
            }
        });
    });

    $updateOkvedDB.click(function() {
        $.ajax({
            type: 'POST',
            url: '/moderate/update_okveddb',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                console.log(data)
            },
            error: function (error) {
            }
        });
    });

    $parseFabricatorDB.click(function() {
        $.ajax({
            type: 'POST',
            url: '/moderate/parse_fabricatordb',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                console.log(data)
            },
            error: function (error) {
            }
        });
    });


    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }

        return cookieValue;
    }
    
})