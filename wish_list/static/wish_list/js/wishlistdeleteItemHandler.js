var usuario = document.getElementById('user').value;

function deleteWishlistItemHandler(event) {
    var publicationDelete = event.target.parentElement.children[0].value;
    var parent = event.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement
        .parentElement;
    $.ajax({
        url: '/wish_lists/delete/',
        data: {
            'publication': publicationDelete,
            'customer': usuario
        },
        dataType: 'json',
        success: function (data) {
            if (data['result'] == 2) {
                location.reload();
            }
        }
    });
}

function basketListAddHandler(event) {
    var producto = event.target.parentElement.children[0].value;
    console.log(producto)
    $.ajax({
        url: '/shopping_basket_lists/add/',
        data: {

            'producto': producto,
            'cantidad': 1
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
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

function basketListDeleteHandler(event) {
    var producto = event.target.parentElement.children[0].value;
    console.log(producto)
    $.ajax({
        url: '/shopping_basket_lists/delete/',
        data: {

            'producto': producto,
            'cantidad': 1
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
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