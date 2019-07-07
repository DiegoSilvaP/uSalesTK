// JS que agrega un producto a lista de deseados desde la pagina del producto

function wishListAddHandler(event) {
        var publicacion = event.target.parentElement.childNodes[0].value;
        // console.log(user + ' va a agregar a favs el producto ' + publicacion);
        $.ajax({
            url: '/wish_lists/add/',
            data: {
                'publication': publicacion,
            },
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 1) {
                    location.reload();
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
    function wishListDeleteHandler(event) {
        var publicacion = event.target.parentElement.childNodes[2].value;
        $.ajax({
            url: '/wish_lists/delete/',
            data: {
                'publication': publicacion,
            },
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 2) {
                    location.reload();
                }
            }
        });
    }


function basketListDeleteItemHandler(event){
    var producto = event.target.parentElement.children[0].value;
    $.ajax({
        url: '/shopping_basket_lists/delete/',
        data: {
            
            'producto': producto,
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
        }
    });
}

function basketListAddItemHandler(event){
    var producto = event.target.parentElement.children[0].value;
    $.ajax({
        url: '/shopping_basket_lists/add/',
        data: {
            'producto': producto,
            'cantidad': 1
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
        }
    });
}