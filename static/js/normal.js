function choice(a,b) {
    $(a).on('click',function () {
        $(this).addClass('active').siblings(b).removeClass('active');
    });
}
