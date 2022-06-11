$(document).ready(function () {

    var data = [
        [
            "Tiger Nixon",
            "System Architect",
            "Edinburgh",
            "5421",
            "2011/04/25",
            "$3,120"
        ],
        [
            "Garrett Winters",
            "Director",
            "Edinburgh",
            "8422",
            "2011/07/25",
            "$5,300"
        ]
    ]


    var table = $('#table_products').DataTable({
        "language": {
            "sProcessing": "Подождите...",
            "sLengthMenu": "Показать _MENU_ продуктов",
            "sZeroRecords": "Продукция отсутствует.",
            "sInfo": "Продукция с _START_ до _END_ (всего _TOTAL_)",
            "sInfoEmpty": "",
            "sInfoFiltered": "(отфильтровано из _MAX_ продуктов)",
            "sInfoPostFix": "",
            "sSearch": "Поиск:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "Первая",
                "sPrevious": "Предыдущая",
                "sNext": "Следующая",
                "sLast": "Последняя"
            },
            "oAria": {
                "sSortAscending": ": активировать для сортировки столбца по возрастанию",
                "sSortDescending": ": активировать для сортировки столбцов по убыванию"
            }
        },
        data: data

    });
        // "ajax": function (data, callback) {
    //         $.ajax({
    //             "url": "/get_products",
    //             "dataSrc": "",
    //             "type": "POST",
    //             'data': {
    //                 project_name: project_name,
    //                 csrfmiddlewaretoken: getCookie('csrftoken')
    //             },
    //             beforeSend: function () {
    //                 // Here, manually add the loading message.
    //                 $('#vuln_table > tbody').html(
    //                     '<tr class="odd">' +
    //                     '<td valign="top" colspan="7" class="dataTables_empty">Идет загрузка&hellip;</td>' +
    //                     '</tr>'
    //                 );
    //             },
    //             success: function (data) {
    //                 callback(data)
    //                 console.log(data)
    //             },
    //             error: function (error) {
    //                 Notiflix.Notify.Failure('Ошибка загрузки таблицы через ajax')
    //             },
    //             timeout: 120000,
    //             async: true
    //         })
    //     },
    //     "deferRender": true,

    //     "columns": [
    //         { data: 'num' },
    //         { data: "packet_name" },
    //         {
    //             data: "packet_version",
    //             render: function (data) {
    //                 let field = '';
    //                 if (data) {
    //                     field += '<td style="max-width:200px;">' + data + '</td>';
    //                 }
    //                 return field;
    //             },
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;" >';
    //                 field += '<div class="row">';
    //                 field += '<div class="text-center col-sm-12">';
    //                 if (data.confirmed_critical_deb_vulnerabilities) {
    //                     field += '<a class="critical debian h6" id="tooltip1" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/confirmed_deb_critical">' + data.confirmed_critical_deb_vulnerabilities + '<span><img class="logo_base" src="/static/img/debian.png" style="max-height:20px;"></span></a>';
    //                 }

    //                 if (data.confirmed_critical_deb_vulnerabilities && data.confirmed_critical_vulnerabilities) {
    //                     field += ' + '
    //                 }

    //                 if (data.confirmed_critical_vulnerabilities) {
    //                     field += '<a class="critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/confirmed_critical">' + data.confirmed_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                 }
    //                 field += '</div></div></td>'

    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;">';
    //                 field += '<div class="row">';
    //                 field += '<div class="text-center col-sm-12">';

    //                 if (data.confirmed_non_critical_deb_vulnerabilities) {
    //                     field += '<a class="non-critical debian h6" id="tooltip1" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/confirmed_deb_non_critical">' + data.confirmed_non_critical_deb_vulnerabilities + '<span><img class="logo_base" src="/static/img/debian.png" style="max-height:20px;"></span></a>';
    //                 }

    //                 if (data.confirmed_non_critical_deb_vulnerabilities && data.confirmed_non_critical_vulnerabilities) {
    //                     field += ' + '
    //                 }

    //                 if (data.confirmed_non_critical_vulnerabilities) {
    //                     field += '<a class="non-critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/confirmed_non_critical">' + data.confirmed_non_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                 }
    //                 field += '</div></div></td>'

    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;">';
    //                 field += '<div class="row">';
    //                 field += '<div class="text-center col-sm-12">';
    //                 if (data.found_debian) {
    //                     if (data.to_analyze_critical_vulnerabilities) {
    //                         field += '<a class="critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                         if (data.packet_version) {
    //                             field += '/' + data.packet_version;
    //                         }
    //                         field += '/vulne/to_analyze_critical">' + data.to_analyze_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                     }
    //                     field += '</div></div></td>'
    //                 }
    //                 else {
    //                     field += '</div></div></td>'
    //                 }
    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;">';
    //                 field += '<div class="row">';
    //                 field += '<div class="text-center col-sm-12">';
    //                 if (data.found_debian) {
    //                     if (data.to_analyze_non_critical_vulnerabilities) {
    //                         field += '<a class="non-critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                         if (data.packet_version) {
    //                             field += '/' + data.packet_version;
    //                         }
    //                         field += '/vulne/to_analyze_non_critical">' + data.to_analyze_non_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                     }
    //                     field += '</div></div></td>'
    //                 }
    //                 else {
    //                     field += '</div></div></td>'
    //                 }
    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;">';
    //                 field += '<div class="row align-items-center">';
    //                 field += '<div class="text-center col-sm-12">';
    //                 if (data.additional_critical_vulnerabilities) {
    //                     field += '<a class="critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/additional_critical">' + data.additional_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                 }
    //                 field += '</div></div></td>'

    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '<td style="min-width:140px;">';
    //                 field += '<div class="row align-items-center">';
    //                 field += '<div class="text-center col-sm-12">';
    //                 if (data.additional_non_critical_vulnerabilities) {
    //                     field += '<a class="non-critical nist h6" id="tooltip2" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/additional_non_critical">' + data.additional_non_critical_vulnerabilities + '<span><img class="logo_base" src="/static/img/fstec.png" style="max-height:10px;"><img class="logo_base" src="/static/img/nist.png" style="max-height:10px;"></span></a>';
    //                 }
    //                 field += '</div></div></td>'

    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = "";

    //                 if (data.fixed_vulnerabilities) {
    //                     field += '<td><div class="text-center">';
    //                     field += '<a class="fixed h6" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/fixed">' + data.fixed_vulnerabilities + '</a></div></td>';
    //                 }
    //                 else {
    //                     field += '<td></td>';
    //                 }
    //                 return field;
    //             }
    //         },
    //         {
    //             data: {},
    //             render: function (data) {
    //                 let field = '';
    //                 if (data.irrelevant_vulnerabilities) {
    //                     field += '<td><div class="text-center">';
    //                     field += '<a class="irrelevant h6" href="' + project_name + '/' + data.packet_name;
    //                     if (data.packet_version) {
    //                         field += '/' + data.packet_version;
    //                     }
    //                     field += '/vulne/irrelevant">' + data.irrelevant_vulnerabilities + '</a></div></td>'
    //                 }
    //                 else {
    //                     field += '<td></td>';
    //                 }
    //                 return field;
    //             }
    //         }
    //     ],

    //     stateSave: true,
    //     searching: false,
    //     order: [[1, 'asc']],
    // });
})