$(document).ready(function () {
    Notiflix.Loading.Init({ svgColor: "#19b46d", });

    var $ProgressBarNav = document.getElementById("ProgressBarNav")
    var $ScanningProgressBarNav = document.getElementById("ScanningProgressBarNav")

    var $UpdateProgressTitleNav = document.getElementById("UpdateProgressTitleNav")

//    if(stat == 'True'){
//        var status = true;
//    }
//    else if(stat == 'False'){
//        var status = false;
//    }

//    console.log(status);
//    updateNavScanStatus();

//    switch (stage) {
//        case 'READY_TO_UPDATE':
//            var isScan = false;
//            break;
//        default:
//            var isScan = true;
//            break;
//    }

    function updateNavScanStatus() {
        // if (navigator.userAgent.includes("Firefox")) {
        //     console.log(getCookie('csrftoken'))
        //     fetch( "/getUpdateStatus",
        //         {
        //             method: 'POST',
        //             data: JSON.stringify({
        //                 csrfmiddlewaretoken: getCookie('csrftoken')
        //             })
        //         })
        //         .then( function (data) {

        //             switch (data['stage']) {
        //                 case 'READY_TO_UPDATE':
        //                     console.log("ready to update")
        //                     $ProgressBarNav.setAttribute("style","width:1px");
        //                     $ProgressBarNav.style.visibility = "hidden";
        //                     $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
        //                     break;
        //                 case 'ERROR':
        //                     console.log("DB was not loaded")
        //                     $ProgressBarNav.setAttribute("style","width:1px");
        //                     $ProgressBarNav.style.visibility = "hidden";
        //                     $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
        //                     break;
        //                 default:
        //                     if(data['loading_percent'] == '0' && !isScan){
        //                         console.log("DB was not loaded")
        //                         $ProgressBarNav.setAttribute("style","width:1px");
        //                         $ProgressBarNav.style.visibility = "hidden";
        //                         $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
        //                         break;
        //                     }
        //                     else if(data['loading_percent'] != '100' && !isScan){
        //                         console.log("update error")
        //                         $ProgressBarNav.setAttribute("style","width:1px");
        //                         $ProgressBarNav.style.visibility = "hidden";
        //                         $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
        //                         break;
        //                     }
        //                     else{
        //                         console.log("scanning")

        //                         $UpdateProgressTitleNav.innerHTML = 'Базы обновляются: ';

        //                         $ProgressBarNav.style.visibility = "visible";
        //                         $ProgressBarNav.setAttribute("style","min-width: 150px; height: 25px");
        //                         $ScanningProgressBarNav.style.visibility = "visible";

        //                         $ScanningProgressBarNav.classList.add("progress-bar-striped", "progress-bar-animated");
        //                         $ScanningProgressBarNav.innerHTML = data['loading_percent'] + '%';
        //                         $ScanningProgressBarNav.style = 'width: ' + data['loading_percent'] + '%';

        //                         setTimeout(updateNavScanStatus, 500);
        //                         break;
        //                     }


        //             }
        //         })
        //         .catch( function (error) {
        //             console.error('updateCardUpdateStatus_AJAX_ERROR');
        //         })

        // }
        // else {
            $.ajax({
                type: 'POST',
                url: '/getUpdateStatus',
                data: {
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },
                success: function (data) {

                    switch (data['stage']) {
                        case 'READY_TO_UPDATE':
                            console.log("ready to update")
                            $ProgressBarNav.setAttribute("style","width:1px");
                            $ProgressBarNav.style.visibility = "hidden";
                            $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
                            break;
                        case 'ERROR':
                            console.log("DB was not loaded")
                            $ProgressBarNav.setAttribute("style","width:1px");
                            $ProgressBarNav.style.visibility = "hidden";
                            $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
                            break;
                        default:
                            if(data['loading_percent'] == '0' && !isScan){
                                console.log("DB was not loaded")
                                $ProgressBarNav.setAttribute("style","width:1px");
                                $ProgressBarNav.style.visibility = "hidden";
                                $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
                                break;
                            }
                            else if(data['loading_percent'] != '100' && !isScan){
                                console.log("update error")
                                $ProgressBarNav.setAttribute("style","width:1px");
                                $ProgressBarNav.style.visibility = "hidden";
                                $UpdateProgressTitleNav.innerHTML = 'Базы обновлены: '+ last_update;
                                break;
                            }
                            else{
                                console.log("scanning")

                                $UpdateProgressTitleNav.innerHTML = 'Базы обновляются: ';

                                $ProgressBarNav.style.visibility = "visible";
                                $ProgressBarNav.setAttribute("style","min-width: 150px; height: 25px");
                                $ScanningProgressBarNav.style.visibility = "visible";

                                $ScanningProgressBarNav.classList.add("progress-bar-striped", "progress-bar-animated");
                                $ScanningProgressBarNav.innerHTML = data['loading_percent'] + '%';
                                $ScanningProgressBarNav.style = 'width: ' + data['loading_percent'] + '%';

                                setTimeout(updateNavScanStatus, 500);
                                break;
                            }


                    }
                },
                error: function (error) {
                    console.error('updateCardUpdateStatus_AJAX_ERROR');
                }
            });
        // }

    }

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

});