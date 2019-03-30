// JS QUE AGREGA EL PRODUCTO A LA LISTA DE PEDIDOS

function orderProductHandler(){
    var productId = document.getElementById('basketPublicationId').value;
    var productQuantity = 1;
    var orderTotal = document.getElementById('txtsubtotal').value;
    console.log(productId);
    console.log(orderTotal);
    $.ajax({
        url: '/orders/add/',
        data: {
            'publication': productId,
            'quantity': productQuantity,
            'subtotal':orderTotal
        },
        dataType: 'json',
        success: function (data) {
            if (data['result'] == 1) {
                console.log(data)
                window.location.replace("/orders");
            }
        }
    });
}