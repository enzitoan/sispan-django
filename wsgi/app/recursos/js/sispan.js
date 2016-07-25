var app = {};

app.VERSION = '0.5.0';
app.AUTOR = 'Enzo Ahumada Núñez';

app.SISTEMA = {
	'valorPan': 100,
	'aPanes': {
		'1': 'Pita Blanco',
		'2': 'Pita Integral',
		'3': 'Amasado Blanco',
		'4': 'Amasado Integral'
	} 
}

app.obtenerInformacionApp = function() {
	console.log('Version: ' + this.VERSION);
	console.log('Autor  : ' + this.AUTOR);
}

app.listarTiposPan = function() {
	
}

app.validarPedido = function() {
	if ($('#txtNombre').val() == '') {
		alert('Debe ingresar campo nombre');
		return false;
	}

	if ($('#txtCorreo').val() == '') {
		alert('Debe ingresar campo correo');
		return false;
	}

	if (is.email($('#txtCorreo').val()) != true) {
		alert('Formato de correo no válido');
		return false;	
	}

	return true;
}

app.limpiarPedido = function() {

}

app.calcularTotalPedido = function(){
	var aTotPanes = [];
	var oDetalle = {
		'cantidad': 0,
		'total': 0
	};

	$.each($('.txt-pedido'), function(index, val) {
		if ($(this).prop('disabled') == false) {
			aTotPanes[index] = parseInt($(this).val());
		}		
	});

	var total = 0;
	$.each(aTotPanes,function(index, val) {
		if (isNaN(val)) {
			val = 0;
		}
	    total += val;
	});

	oDetalle.cantidad = total;
	oDetalle.total = parseInt(total) * this.SISTEMA.valorPan;

	return oDetalle;
}

app.insertarPedido = function(){
	if (this.validarPedido()) {
		alert('Enviar pedido');
	}
}

app.eventChkClick = function(checkbox) {
	if ($(checkbox).is(':checked')) {
		$('#txtPan' + $(checkbox).data('id-pan')).val(1);
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', false);
	} else {
		$('#txtPan' + $(checkbox).data('id-pan')).val('');
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', true);
	}
	this.eventTxtChange();
}

app.eventTxtChange = function() {
	var oPedido = this.calcularTotalPedido();
	$('#lblCantidad').text(oPedido.cantidad);
	$('#lblTotal').text('$ ' + oPedido.total);

	if (oPedido.total != 0) {
		$('#txtNombre').prop('disabled', false);
		$('#txtCorreo').prop('disabled', false);
		$('#btnIngresar').prop('disabled', false);
	} else {
		$('#txtNombre').prop('disabled', true);
		$('#txtCorreo').prop('disabled', true);
		$('#btnIngresar').prop('disabled', true);

		$('#txtNombre').val('');
		$('#txtCorreo').val('');
	}
}

$(document).ready(function() {
	app.obtenerInformacionApp();
	app.listarTiposPan();

	$('.chk-pedido').click(function(event) {
		app.eventChkClick($(this));
	});

	$('.txt-pedido').change(function(event) {
		app.eventTxtChange();
	});

	$('#btnIngresar').click(function(event) {
		app.insertarPedido();
	});
});