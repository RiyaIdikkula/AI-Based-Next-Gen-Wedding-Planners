$(document).ready(function () {
    // Define patterns for validation
    var namePattern = /^[a-zA-Z\s]*$/;
    var phonePattern = /^[6-9]\d{9}$/;
    var pricePattern = /^[\d,]+(\.\d{2})?$/;

    // Validate name
    $("#name").keyup(function () {
        var name = $(this).val();
        if (!namePattern.test(name)) {
            $("#name-error").show();
        } else {
            $("#name-error").hide();
        }
    });

    $("#brideName").keyup(function () {
        var name = $(this).val();
        if (!namePattern.test(name)) {
            $("#brideName-error").show();
        } else {
            $("#brideName-error").hide();
        }
    });

    // Validate groom's name
    $("#groomName").keyup(function () {
        var name = $(this).val();
        if (!namePattern.test(name)) {
            $("#groomName-error").show();
        } else {
            $("#groomName-error").hide();
        }
    });

    // Validate phone number
    $("#phone").keyup(function () {
        var phone = $(this).val();
        if (!phonePattern.test(phone)) {
            $("#phone-error").show();
        } else {
            $("#phone-error").hide();
        }
    });

    // Validate price
    $("#price").keyup(function () {
        var price = $(this).val();
        if (!pricePattern.test(price)) {
            $("#price-error").show();
        } else {
            $("#price-error").hide();
        }
    });

    // Validate images
    $("#images").change(function () {
        var files = $(this).get(0).files;
        var validExtensions = ['image/jpeg', 'image/png', 'image/gif'];
        var maxSize = 5 * 1024 * 1024; // 5 MB
        var isValid = true;

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            if (!validExtensions.includes(file.type)) {
                isValid = false;
                break;
            }
            if (file.size > maxSize) {
                isValid = false;
                break;
            }
        }

        if (isValid) {
            $("#image-error").hide();
        } else {
            $("#image-error").show();
        }
    });
});
