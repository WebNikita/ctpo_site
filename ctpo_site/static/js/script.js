$('#robototech').click(function() {
    $('#h3_robototech').addClass('activ_h3')
    $('#h4_robototech').addClass('activ_h4')
    $('#robototech_img').addClass('activ_img')
    $('#robototech_txt').addClass('active_txt')
    $('#h3_IoT').removeClass('activ_h3')
    $('#h4_IoT').removeClass('activ_h4')
    $('#IoT_img').removeClass('activ_img')
    $('#IoT_txt').removeClass('active_txt')
});
$('#IoT').click(function() {
    $('#h3_robototech').removeClass('activ_h3')
    $('#h4_robototech').removeClass('activ_h4')
    $('#robototech_img').removeClass('activ_img')
    $('#robototech_txt').removeClass('active_txt')
    $('#h3_IoT').addClass('activ_h3')
    $('#h4_IoT').addClass('activ_h4')
    $('#IoT_img').addClass('activ_img')
    $('#IoT_txt').addClass('active_txt')
});