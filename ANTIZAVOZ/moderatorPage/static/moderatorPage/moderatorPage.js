$(document).ready(function () {
    var $updateDB = $('#update-db')
    var $updateProductDB = $('#update-product-db')

    $updateDB.click(function() {
        $.ajax({
            type: 'POST',
            url: '/moderate/update_database',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                console.log(data)
                // Notiflix.Notify.Success('Обновление БД запущено!');
            },
            error: function (error) {
                // Notiflix.Notify.Failure('ajax error');
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
                // Notiflix.Notify.Success('Обновление БД запущено!');
            },
            error: function (error) {
                // Notiflix.Notify.Failure('ajax error');
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