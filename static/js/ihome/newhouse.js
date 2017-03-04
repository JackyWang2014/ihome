function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $.get("/api/house/area", function (data) {
       html = template("area-tmpl", {areas: data.data});
        $("#area-id").html(html)
        //console.log(html)

        // for (var i = 0; i < data.data.length; i++)
        //     $("#area-id").append('<option value="'+data.data[i].area_id+'">'+data.data[i].name+'</option>');

    })
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');


$("#form-house-info").submit(function (e) {
    e.preventDefault();
    var formData = $(this).serializeArray();
    for (var i = 0; i < formData.length; i++) {
        if (!formData[i].value) {
            $(".error-msg").show();
            return;
        }
    }
    var data = {};
    $(this).serializeArray().map(function (x) {
        data[x.name] = x.value;
    });
    var facility = []
    $("input:checkbox:checked[name=facility]").each(function (i) {
        facility[i] = this.value;
    });
    data.facility = facility;
    var jsonData = JSON.stringify(data);
    $.ajax({
        url:"/api/house/info",
        method:"POST",
        data:jsonData,
        contentType:"application/json",
        headers: {
            "X-XSRFTOKEN":getCookie("_xsrf"),
        },
        success: function (data) {
            if ("1" == data.errorcode) {
                location.href = "/login.html";
            } else if ("0" == data.errcode) {
                $("#house-id").val(data.house_id);
                $(".error-msg").hide();
                $("#form-house-info").hide();
                $("#form-house-image").show();
            }

        }
    });
})

$("#form-house-image").submit(function (e) {
    e.preventDefault();
    $('.popup_con').fadeIn('fast');
    var options = {
        url:"/api/house/image",
        method:"POST",
        headers:{
            "X-XSRFTOKEN":getCookie("_xsrf"),
        },
        success: function (data) {
            if ("4101" == data.errcode) {
                location.href = "/login.html";
            } else if ("0" == data.errcode) {
                $(".house-image-cons").append('<img src="'+ data.url +'">');
                $(".popup_con").fadeOut('fast');
            }

        }
    };
    $(this).ajaxSubmit(options);

});
})
