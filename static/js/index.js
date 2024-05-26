

/*javascript of navbar*/
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const navbar = document.getElementById('navbar');

    menuToggle.addEventListener('click', function() {
        // Toggle the 'open' class to show/hide the navbar
        navbar.classList.toggle('open');
    });
});


function checkLink(event, url) {
    if (!url) {  // If the URL is empty or undefined
        event.preventDefault();  // Prevent the default action (navigation)
        alert("No link is provided.");  // Display an alert message
    }
}



/*models.py */

// myapp/static/myapp/js/item_admin.js
/*var $ = jQuery.noConflict();
(function($) {
    $(document).ready(function() {
        $('#id_dept').change(function() {
            var dept_id = $(this).val(); 
            var url = '/admin/home/role/ajax/' + dept_id + '/';  // get the url of the `load_subcategories` view
            $.get(url, function(data) {
                var subCategorySelect = $('#id_role');
                subCategorySelect.empty();
                $.each(data, function(key, value) {
                    subCategorySelect.append($('<option></option>').attr('value', key).text(value));
                });
            });
        });
    });
})(jQuery);*/

/*uh */

var $ = jQuery.noConflict();
$(document).ready(function() {
    $('#id_dept1').change(function() {
        var deptId = $(this).val();
        if (deptId) {
            $.ajax({
                url: '/home/role/ajax/' + deptId + '/',
                type: 'GET',
                success: function(data) {
                    $('#id_role1').empty();
                    $('#id_role1').append($('<option></option>').attr('value', '').text('---------'));
                    $.each(data, function(key, value) {
                        $('#id_role1').append($('<option></option>').attr('value', value.id).text(value.name));
                    });
                },
                error: function(xhr, status, error) {
                    console.error("AJAX error:", status, error);
                }
            });
        } else {
            $('#id_role1').empty();
            $('#id_role1').append($('<option></option>').attr('value', '').text('---------'));
        }
    });
});

