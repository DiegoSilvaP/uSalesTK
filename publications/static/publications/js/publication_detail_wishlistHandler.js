var col = document.getElementById('colBtns');
var user = document.getElementById('user').value;
// if (col.childElementCount == 0) {
//     col.innerHTML =
//         '<input style="display:none" type="text" name="txtProducto" id="txtProducto" value="{{publication.id}}"><button id="btnAgregar" onclick="exe(event)" class="btn btn-secondary w-100">Agregar a deseos</button>'
//     // console.log(col.childNodes[0].id);
// }

function exe(event) {
    var action = event.target.id;
    if (action == "btnAgregar") {
        var publicacion = event.target.parentElement.childNodes[0].value;
        // console.log(user + ' va a agregar a favs el producto ' + publicacion);
        $.ajax({
            url: '/wish_lists/add/',
            data: {
                'publication': publicacion,
                'customer': user
            },
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 1) {
                    location.reload();

                    $.growl.notice({
                        title: '',
                        message: "Agregado a favoritos ❤",
                        location: "bc"
                    });

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
    } else {
        var publicacion = event.target.parentElement.childNodes[2].value;
        // console.log(user + ' va a Eliminar a favs el producto ' + publicacion);
        $.ajax({
            url: '/wish_lists/delete/',
            data: {
                'publication': publicacion,
                'customer': user
            },
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 2) {
                    location.reload();

                    $.growl.warning({
                        title: '',
                        message: "Eliminado de favoritos 💔",
                        location: "bc"
                    });

                }
            }
        });
    }
}