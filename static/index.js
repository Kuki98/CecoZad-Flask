$(function () {
    $('#CommentEnter form').on('submit', function (event) {
        event.preventDefault();
        event.stopImmediatePropagation();
        if (!confirm('Are you sure little fucker?')) {
            return false;
        }
        console.log('hello world');
        var data = $(this).serialize();
        var field = $('#comment');
        var fieldValue = field.val();
        var url = $(this).attr('action');
        var ajaxData = {
            url: url,
            data: data,
            method: 'POST',
            success: function () {
                $('#CommentShow').append('<p>' + fieldValue + '</p>');
                field.val('');
            },
        };
        $.ajax(ajaxData)
    }).on('submit', function (event) {
        alert('VANKATA NE RAZBIRA JAVASCRIPTA!');
    });

    var counter = 0;
    setInterval(function () {
        console.log(counter++);
    }, 1000)
});
