$(function () {
    $('#CommentShow form').on('submit', function (event) {
        event.preventDefault();

        var url = $(this).attr('action');
        var buttons = $('#CommentShow form #delete-button')


        var deleteCommentId = $('#delete-button', this).val();

        var data = {
            delete_comment_name:deleteCommentId
        };
        var ajaxData = {
            url: url,
            data: data,
            method: 'POST',
            success: function(){
                alert('Successfully deleted comment')
            },
        };
        console.log(ajaxData)
        $.ajax(ajaxData)
    });
});