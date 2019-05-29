document.getElementById('CommentEnter').addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopImmediatePropagation();
    var cnx = new XMLHttpRequest();
    var forms = document.getElementById('CommentEnter').getElementsByTagName('form')[0];
    var url = forms.getAttribute('action')
    var commentData = document.getElementById('comment').value;
    var formData = new FormData(forms);

    cnx.open('POST', url);

    cnx.onload = function(){
        document.getElementById('CommentShow').innerHTML += '<p>' + data + '</p>';
    }

    cnx.send(formData);
});
