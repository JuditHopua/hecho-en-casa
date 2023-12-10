/* volver al comienzo del html clickeando la flecha */

$(document).ready(function(){
    $('.up').hide();

    $('.up').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});

	$(window).scroll(function(){
		if( $(this).scrollTop() > 0 ){
			$('.up').slideDown(1000);
		} else {
			$('.up').slideUp(1000);
		}
	});

});

/* valida el formato del email del formulario de contacto */

function valida_email(valor) {
	re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
	if(!re.exec(valor)){
		alert('Email no valido');
		document.form_contacto.email.focus();
		return(0);
	}
}

/* valida que se haya seleccionado alguna cantidad en algún producto y el formato del mail del contacto para permitir el envío del pedido */

function valida_enviar() {
	lista = document.getElementsByTagName('input')
	flag_input = 0
	for (i=0; i<lista.length; i++) {
		if (lista[i].value != 0){
			flag_input++
		}
	}
	if (flag_input == 8){
			alert('No ha seleccionado productos');
			return(0);
	} 
	valida_email(document.form_valida_pedido.email.value);
}