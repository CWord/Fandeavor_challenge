$(function() {

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        run_search();
    });

    function run_search() {
        // console.log("run_search working")
        $.ajax({
            url : "run_search/",
            type : "POST",
            data : { search_value : $('#us').val() },
            
            success : function(json) {
                $('#result_list').empty();
                $('#notable_list').empty();
                $('#image-holder').empty();
                $('#results').empty();
                // console.log(json['Success']);
                if (json['Success'] === 'true'){
                    key_list = ['Image source', 'full name', 'Notable facts', 'date of birth', 'place of birth', 'date of death', 'place of death']
                    pretty_list = ['Image source', 'Full Name', 'Notable facts', 'Date of Birth', 'Place of Birth', 'Date of Death', 'Place of Death']
                    for (key in key_list){
                        // console.log(key_list[key]);
                        if (key_list[key] === 'Image source'){
                            $("#image-holder").append("<img class='img-responsive' style='float: right;' src="+json['Image source']+">")
                        }
                        else if (key_list[key] === 'Notable facts'){
                            for (var item in json['Notable facts']){
                                $("#notable_list").append("<li>"+json['Notable facts'][item]+"</li>");
                            }
                            $("#notable_list").prepend("<li style='list-style-type: none; font-size: 20px;'><strong>Notable Facts:</strong></li>");
                        }
                        else if (key_list[key] in json){
                            $("#result_list").append("<li><strong>"+pretty_list[key]+":</strong> "+json[key_list[key]]+"</li>");                          
                        }
                    }
                }
                else {
                    $("#result_list").append("Search not found")
                }
            },

            error : function(xhr,errmsg,err) {
                $('#result_list').empty();
                $('#notable_list').empty();
                $('#image-holder').empty();
                $('#results').empty();                
                $('#results').html("<div>Error</div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});