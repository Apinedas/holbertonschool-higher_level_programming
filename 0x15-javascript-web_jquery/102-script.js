
$(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(() => {
    const apiUrl = (url + $('INPUT#language_code').val());
    $.getJSON(apiUrl, data => {
      $('DIV#hello').text(data.hello);
    });
  });
});
