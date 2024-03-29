// JS que agrega un producto a la lista de deseados desde la pagina que lista todos los productos
try {
    document.getElementsByClassName('carousel-item')[0].classList.add("active");
  }
  catch(error) {
    
  }
  

  var cards = document.getElementsByName('bodyCardBasket');
  for (let i = 0; i < cards.length; i++) {
    if (cards[i].childElementCount == 3) {
      cards[i].innerHTML +=
        '<button onclick="basketListAddHandler(event)" class="btn btn-outline-primary mx-block"><i class="fa fa-shopping-cart"></i></button>'
    }
  }


var cards = document.getElementsByClassName('card card-zoom bg-light');
    for (let i = 0; i < cards.length; i++) {
        if (cards[i].childElementCount == 3) {
            cards[i].innerHTML +=
                '<button name="add" class="btn btn-secondary mx-block" style="position:absolute; top:10px; right: 10px"' +
                'onclick="wishListAddHandler(event)"><i class="fa fa-heart-o"></i></button>'
        }
    }

function wishListAddHandler(event) {
    var publicacion;
    if (event.target.tagName == 'I') {
        publicacion = event.target.parentElement.parentElement.children[2].value;
    } else {
        publicacion = event.target.parentElement.parentElement.children[0].children[2].value;
    }

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
                size:'large',
                fixed:true,
                message: "<h6>Por favor, inicia sesión para tener la mejor experiencia de compra 😎</h6>",
                // location: "bc"
            });
        }
    });
}

function wishListDeleteHandler(event) {
    var publicacion;
    if (event.target.tagName == 'I') {
        publicacion = event.target.parentElement.parentElement.children[2].value;
    } else {
        publicacion = event.target.parentElement.parentElement.children[0].children[2].value;
    }
    // console.log('Eliminar user ' + usuario + ' publicacion ' + publicacion)
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

function basketListAddHandler(event) {
    var producto;
    
    if (event.target.tagName == 'I') {
        producto = event.target.parentElement.parentElement.parentElement.children[2].value
    } else {
        producto = event.target.parentElement.parentElement.children[2].value;
    }
    $.ajax({
        url: '/shopping_basket_lists/add/',
        data: {

            'producto': producto,
            'cantidad':1
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
        },
        error: function () {
            $.growl.error({
                title: '',
                size:'large',
                fixed:true,
                message: "<h6>Por favor, inicia sesión para tener la mejor experiencia de compra 😎</h6>",
                // location: "bc"
            });
        }
    });
}

function basketListDeleteHandler(event) {

    var producto;
    if (event.target.tagName == 'I') {
        producto = event.target.parentElement.parentElement.parentElement.children[2].value
    } else {
        producto = event.target.parentElement.parentElement.children[2].value;
    }
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