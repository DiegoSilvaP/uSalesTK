var selectedCategory;
var subcategory = document.getElementById('id_subcategory');
getSubCategory(this);

function getSubCategory(event) {
    if (event.target == undefined) {
        selectedCategory = document.getElementById('id_category').value;
    } else {
        selectedCategory = event.target.value;
    }
    $.ajax({
        url: '/get_sub_category/',
        data: {
            'category': selectedCategory,
        },
        dataType: 'json',
        success: function (data) {
            
            var JsonData = JSON.parse(JSON.stringify(JSON.parse(data), null, 2));
            subcategory.innerHTML = '<option value="" selected="">---------</option>';
            if (JsonData.length > 0) {
                for (let i = 0; i < JsonData.length; i++) {
                    subcategory.innerHTML += '<option value="' + JsonData[i].pk + '" >' + JsonData[i].fields.name + '</option>';
                }
            } else {
                subcategory.innerHTML = '<option value="" selected="">---------</option>';
            }

        }
    });

}