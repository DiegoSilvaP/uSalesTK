var totalProductosInputs = document.getElementsByName('quantity');
    var txtPrecioItem = document.getElementsByName('txtPrecioItem');
    var compraSubTotal = 0;
    

    for (let i = 0; i < txtPrecioItem.length; i++) {
        compraSubTotal+=parseFloat(txtPrecioItem[i].textContent);
    }


    var totalProductos= 0;

    for (let i = 0; i < totalProductosInputs.length; i++) {
        totalProductos+=parseInt(totalProductosInputs[i].value);
        
    }
    document.getElementById('txtTotalProductos').innerText = 'Productos ('+totalProductos+')';
    document.getElementById('txtcompraSubTotal').innerText = '$'+compraSubTotal.toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    document.getElementById('txtcompraTotal').innerText = '$'+compraSubTotal.toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$&,');;


    function contador(event) {
        var cantidad = event.target.value;
        var producto = event.target.parentElement.children[1].value;
        // console.log(producto);
        $.ajax({
            url: '/shopping_basket_lists/update/',
            data: {

                'producto': producto,
                'cantidad': cantidad
            },
            dataType: 'json',
            success: function (data) {
                location.reload();
            }
        });
    }

    function deleteItem(event) {
        var producto = event.target.parentElement.parentElement.parentElement.parentElement.children[1].children[0].children[
            2].children[0].value;
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