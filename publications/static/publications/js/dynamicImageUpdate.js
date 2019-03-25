var user_id = document.getElementById('user').value;
document.getElementById('id_seller').value = user_id;

$("#id_picture").on("change", function () {
    readURL(this);
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgPreview')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}