$(function () {
    $('#CommentEnter form').on('submit', function (event) {
        event.preventDefault();
        event.stopImmediatePropagation();
        if (!confirm('Are you sure little fucker?')) {
            return false;
        }
        var data = $(this).serialize();
        console.log(data)
        var field = $('#comment');
        var fieldValue = field.val();
        var url = $(this).attr('action');
        console.log(url)
        var ajaxData = {
            url: url,
            data: data,
            method: 'POST',
            success: function () {
                var htmlComment = '<p>' + fieldValue + '</p>'
                $('#CommentShow').append(htmlComment);
                field.val('');
            },
        };
        $.ajax(ajaxData)
    }).on('submit', function (event) {
        alert('VANKATA NE RAZBIRA JAVASCRIPTA!');
    });

//    var counter = 0;
//    setInterval(function () {
//        console.log(counter++);
//    }, 1000)
});
