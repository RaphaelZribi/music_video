
$('#submitButton').on('click', function(e) {
	e.preventDefault();
	console.log("form submitted!")
	addComment();

})

function addComment() {
	var videoId = $('#videoIframe').data('video-id')
	var textForm = $('#textForm').val()
	$.ajax({
		url: '/comments_app/post_comment/',
		type: 'POST',
		data: {
			'video_id': videoId, 
			'text': textForm,
		},
	})

	.done(function(data) {
		$('#addCommentForm').val('');
		if (data.code == 200) {
			var comment = data.comment;	
		}
		$('#allComments').append('<li class="list-group-item">'+ comment['username'] + ' : ' 
			+ comment['text'] +'</li>')
	})

	.fail(function(data) {
		alert('Issue adding your task')
	});



}


$(document).ready(function(){

    $(document).on('click', '#like', function(event){
        event.preventDefault();
        var videoId = $(this).data("video-id")
        likeDislike(videoId)
    })
});

function likeDislike(videoId){
    $.ajax({
        url: '/main_app/like/' + videoId + '/',
            type: 'POST',
            data: {},
        success: function(json){
            console.log(json);
            if (json.is_liked){
                $('#like').addClass('fa-thumbs-down')
                    .removeClass('fa-thumbs-up')
                    .html('Dislike');
            } else {
                $('#like').addClass('fa-thumbs-up')
                    .removeClass('fa-thumbs-down')
                    .html('Like');
            }   
                
        },
        error: function(xhr, errmsg, err){
            alert('Something is wrong')
            console.log(errmsg, err);
        }
    })
}
    


$(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});


