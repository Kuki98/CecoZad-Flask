document.getElementById('CommentEnter').addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopImmediatePropagation();
    var cnx = new XMLHttpRequest();
    var forms = document.getElementById('CommentEnter').getElementsByTagName('form')[0];
    var url = forms.getAttribute('action')
    var data = document.getElementById('comment').value;

    cnx.open('POST', url);
    cnx.onload = function(){
        document.getElementById('CommentShow').innerHTML += '<p>' + data + '</p>';
    }

    cnx.send();
});
