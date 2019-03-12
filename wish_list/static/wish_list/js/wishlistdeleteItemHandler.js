var usuario = document.getElementById('user').value;

    function exe(event) {
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
                    $.growl.warning({
                        title: '',
                        message: "Eliminado de favoritos 💔",
                        location: "bc"
                    });
                    parent.style.display = 'none';
                }
            }
        });
    }