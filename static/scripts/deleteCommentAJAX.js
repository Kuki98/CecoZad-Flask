$(function () {
    $('#CommentShow form').on('submit', function (event) {
        event.preventDefault();

        var url = $(this).attr('action');

        var deleteCommentId = $('#delete-button', this).val();

//        var comment = $('#comment_id').text().trim()

        var data = {
            delete_comment_name:deleteCommentId
        };
        var ajaxData = {
            url: url,
            data: data,
            method: 'POST',
            success: function(){
                alert('Successfully deleted comment: ')

            },
        };
        console.log(ajaxData)
        $.ajax(ajaxData)
    });
});