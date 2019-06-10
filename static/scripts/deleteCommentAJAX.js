$(function () {
    $('#CommentShow form').on('submit', function (event) {
        event.preventDefault();
        console.log($(this))

        var url = $('#delete-button').attr('formaction')

        var deleteCommentId = $('#delete-button', this).val();

        var data = {
            delete_comment_name: deleteCommentId
        };
        var ajaxData = {
            url : url,
            data : data,
            method : "POST",
            success : function() {
                $(this).empty()
            }
        }
        $.ajax(ajaxData)
    });
});