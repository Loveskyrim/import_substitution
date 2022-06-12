$(document).ready(function () {

    var table = $('#productsTable').DataTable({
			"language": {
				"processing": "Подождите...",
				"search": "Поиск:",
				"lengthMenu": "Показать _MENU_ записей",
				"info": "Записи с _START_ до _END_ из _TOTAL_ записей",
				"infoEmpty": "Записи с 0 до 0 из 0 записей",
				"infoFiltered": "(отфильтровано из _MAX_ записей)",
				"loadingRecords": "Загрузка записей...",
				"zeroRecords": "Записи отсутствуют.",
				"emptyTable": "В таблице отсутствуют данные",
				"paginate": {
				"first": "Первая",
				"previous": "Предыдущая",
				"next": "Следующая",
				"last": "Последняя"},},
			paging: true,
			pageLength: 15,
			lengthChange: false,
			autoWidth: true,
			searching: true,
			bInfo: true,
			bSort: true,

			"columnDefs": [
			{
				"targets": 2,
				"orderable": false
			},
		]

	});


    $('#productsTable tbody').on('click', 'tr', function () {
        // переход к проекту по нажатию на  него в строке таблицы
        var data = table.row(this).data();
        console.log(data)
        var product_publish = data[4];
        console.log(product_publish)
        var product_name = $(data[1]).text();
        console.log(product_name)

        document.location.href = "products/" + product_publish + "/" + product_name;
    });

    $(function() {
        $(window).scroll(function() {
            if($(this).scrollTop() != 0) {
                $('#toTop').fadeIn();
            } else {
                $('#toTop').fadeOut();
            }
        });

        $('#toTop').click(function() {
            $('body,html').animate({scrollTop:0},800);
        });
    });
})