
    function orderProductHandler(event) {
        var productQuantity = event.target.parentElement.parentElement.parentElement.parentElement.children[1].children[
            0].children[0].children[0].value;
        var productId = event.target.parentElement.parentElement.parentElement.parentElement.children[1].children[0]
            .children[2].children[0].value;
        var orderTotal = event.target.parentElement.parentElement.parentElement.parentElement.children[2].children[0].children[0].children[1].textContent;
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