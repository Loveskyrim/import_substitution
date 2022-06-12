$(document).ready(function () {
    $('#updateProductData').on('click', function() {
        var newProductName = $("#newProductName").val();
        var newProductDescription = $("#newProductDescription").val();
        
        $.ajax({
            type: "POST",
            url: "/updateProductData",
            data: {
                project: project_name,
                newprojectname: newProductName,
                newprojectdescription : newProductDescription,
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            dataType: "JSON",
            async: false,
            success: function () {
                Notiflix.Notify.Success('Данные были обновлены!');
                window.location = '/product/' + newProductName
            },
            error: function (status) {
                if (status.status == 402) { Notiflix.Notify.Failure('Проект с данным названием уже существует.') }
                else if (status.status == 405) { Notiflix.Notify.Failure("Ошибка! Символ слеша в имене проекта: " + newProjectName) }
                else { Notiflix.Notify.Failure('Ошибка при обновлении информации!') }
                
            }
        });
    });

      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';')
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i])
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                    break;
                }
            }
        }

        return cookieValue
    }
})