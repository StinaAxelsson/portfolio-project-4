/**codesnippet from django I think therefore i blog
 * Fade the messages away automatic.
 * */
setTimeout(function () {
    let messages = document.getElementById('msg-box');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);