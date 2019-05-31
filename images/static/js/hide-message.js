$(document).ready(function () {
    setTimeout(function () {
        $('.messages').fadeOut('slow');
    }, 7000);
    $('.del-msg').on('click', function () {
        $('.del-msg').parent().attr('style', 'display:none;');
    })
});
