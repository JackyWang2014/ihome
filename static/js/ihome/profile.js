function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $.get("api/profile", function (data) {
        if ("4101" == data.errcode) {
            location.href = "/login.html";
        } else if ("0" == data.errcode) {
            console.log(data)
            $("#user-name").val(data.data.name);
            if (data.data.avatar) {
                $("#user-avatar").attr("src", data.data.avatar);
            }
        }

    })

    $("#form-avatar").submit(function (e) {
        e.preventDefault();
        $('.image_uploading').fadeIn('fast');

        var options = {
            url:"/api/profile/avatar",
            method:"post",
            dataType:"json",
            headers:{
                "X-XSRFTOKEN":getCookie("_xsrf")
            },
            success:function (data) {
                if ("0" == data.errcode) {
                    $('.image_uploading').fadeOut('fast');
                    $('#user-avatar').attr("src",data.data);
                } else if ("4101" == data.errcode) {
                    location.href = "/login.html"
                }

            }
        };
        $(this).ajaxSubmit(options);

    })

    $("#form-name").submit(function (e) {
        e.preventDefault()
        var data = {};
        $(this).serializeArray().map(function (x) {
            data[x.name] = x.value;
        });
        var jsonData = JSON.stringify(data);

        $.ajax({
                url: "/api/profile/name",
                method: "post",
                data: jsonData,
                contentType: "application/json",
                headers: {
                    "X-XSRFTOKEN": getCookie("_xsrf"),
                },
                success: function (data) {
                    if ("0" == data.errcode) {
                        $(".error-msg").hide();
                    showSuccessMsg();
                } else if ("4001" == data.errcode) {
            $(".error-msg").show();

        }
        else
        if ("4101" == data.errcode) {
            location.href = "/login.html";
        }
    }
        });

    })

})

