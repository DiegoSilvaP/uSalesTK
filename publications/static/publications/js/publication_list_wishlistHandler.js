var cards = document.getElementsByClassName('card card-zoom bg-light');
for (let i = 0; i < cards.length; i++) {
    if (cards[i].childElementCount == 3) {
        cards[i].innerHTML +=
            '<button name="add" class="btn btn-secondary mx-block" style="position:absolute; top:10px; right: 10px"' +
            'onclick="exe(event)"><i class="fa fa-heart-o"></i></button>'
    }
}

function exe(event) {
    var usuario = document.getElementById('user').value;
    var span = document.getElementById('wishlist_span');
    if (event.target.tagName == 'I') { // presione el icono dentro del boton
        if (event.target.parentElement.name == "delete") {
            // codigo para eliminar de la wislist

            var publicacion = event.target.parentElement.parentElement.children[2].value;
            // console.log('Eliminar user ' + usuario + ' publicacion ' + publicacion)
            $.ajax({
                url: '/wish_lists/delete/',
                data: {
                    'publication': publicacion,
                    'customer': usuario
                },
                dataType: 'json',
                success: function (data) {
                    if (data['result'] == 2) {
                        $.growl.warning({
                            title: '',
                            message: "Eliminado de favoritos 💔",
                            location: "bc"
                        });
                        event.target.className = 'fa fa-heart-o';
                        span.textContent = parseInt(span.textContent) - 1;
                        // console.log(parseInt(span.textContent)-1);

                    }
                }
            });
            event.target.className = 'fa fa-heart-o'
        } else {
            // codigo para agregar a la wishlist

            var publicacion = event.target.parentElement.parentElement.children[2].value;
            console.log('agregar user ' + usuario + ' publicacion ' + publicacion)
            $.ajax({
                url: '/wish_lists/add/',
                data: {
                    'publication': publicacion,
                    'customer': usuario
                },
                dataType: 'json',
                success: function (data) {
                    if (data['result'] == 1) {
                        $.growl.notice({
                            title: '',
                            message: "Agregado a favoritos ❤",
                            location: "bc"
                        });
                        event.target.className = 'fa fa-heart';
                        span.textContent = parseInt(span.textContent) + 1;
                        // console.log(parseInt(span.textContent)+1);
                    }
                },
                error: function () {
                    $.growl.error({
                        title: '',
                        message: "Por favor, inicia sesión para tener la mejor experiencia de compra 😎",
                        location: "bc"
                    });
                }
            });


        }
    } else {
        if (event.target.name == "delete") { // presione el boton  
            // codigo para eliminar de la wislist

            var publicacion = event.target.parentElement.children[2].value;

            $.ajax({
                url: '/wish_lists/delete/',
                data: {
                    'publication': publicacion,
                    'customer': usuario
                },
                dataType: 'json',
                success: function (data) {
                    if (data['result'] == 2) {
                        $.growl.warning({
                            title: '',
                            message: "Eliminado de favoritos 💔",
                            location: "bc"
                        });
                        event.target.children[0].className = 'fa fa-heart-o';
                        span.textContent = parseInt(span.textContent) - 1;
                        // console.log(parseInt(span.textContent)-1);
                    }
                }
            });
        } else {
            // codigo para agregar a la wishlist

            var publicacion = event.target.parentElement.children[2].value;
            $.ajax({
                url: '/wish_lists/add/',
                data: {
                    'publication': publicacion,
                    'customer': usuario
                },
                dataType: 'json',
                success: function (data) {
                    if (data['result'] == 1) {
                        $.growl.notice({
                            title: '',
                            message: "Agregado a favoritos ❤",
                            location: "bc"
                        });
                        event.target.children[0].className = 'fa fa-heart';
                        span.textContent = parseInt(span.textContent) + 1;
                        // console.log(parseInt(span.textContent)+1);
                    }
                },
                error: function () {
                    $.growl.error({
                        title: '',
                        message: "Por favor, inicia sesión para tener la mejor experiencia de compra 😎",
                        location: "bc"
                    });
                }
            });


        }
    }
}