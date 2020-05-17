$(function () {
    $('.bl').on('click', '.bl__main', function (e) {
        $('.dropdown').not($(e.delegateTarget).find('.dropdown')).hide();
        $(e.delegateTarget).find('.dropdown').slideToggle()
    });
    $('.bl').on('click', '.dropdown__item', function (e) {
        $(e.delegateTarget).find('.bl__val').html($(this).html());
        $(e.delegateTarget).find('.dropdown').slideUp()

    });
    $('.btn-add-link').on('click', function () {
        $('.new-order__block_hidden').eq(0).slideDown().removeClass('new-order__block_hidden');
    });
})
