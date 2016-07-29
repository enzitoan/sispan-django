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

app.aTotPanes = [];
app.oDetalle = {};

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
	this.oDetalle = {
		'cantidad': 0,
		'total': 0
	};

	$.each($('.txt-pedido'), function(index, val) {
		var items = 0;
		if ($(this).val() != ''){
			items = $(this).val(); 
		}
		this.aTotPanes[index] = parseInt(items);		
	});

	var total = 0;
	$.each(this.aTotPanes,function(index, val) {
		if (isNaN(val)) {
			val = 0;
		}
	    total += val;
	});

	this.oDetalle.cantidad = total;
	this.oDetalle.total = parseInt(total) * this.SISTEMA.valorPan;

	$('#lblCantidad').text(this.oDetalle.cantidad);
	$('#lblTotal').text('$ ' + this.oDetalle.total);

	return oDetalle;
}

app.eventChkClick = function(checkbox) {
	if ($(checkbox).is(':checked')) {
		if (this.oDetalle.total == 0) {
			$('#txtPan' + $(checkbox).data('id-pan')).val(1);
		}
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', false);

	} else {
		if (this.oDetalle.total == 0) {
			$('#txtPan' + $(checkbox).data('id-pan')).val(0);
		}
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', true);

	}
	this.eventTxtChange();
}

app.eventTxtChange = function() {

	if (this.oDetalle.total != 0) {
		$('#txtNombre').prop('disabled', false);
		$('#txtCorreo').prop('disabled', false);
		if ($('#txtNombre').val() != '' && $('#txtCorreo').val() != '') {
			$('#btnIngresar').prop('disabled', false);
		}
		
	} else {
		$('#txtNombre').prop('disabled', true);
		$('#txtCorreo').prop('disabled', true);
		$('#btnIngresar').prop('disabled', true);
	}
}

$(document).ready(function() {
	app.obtenerInformacionApp();
	app.listarTiposPan();
	app.calcularTotalPedido();

	$('.chk-pedido').click(function(event) {
		app.eventChkClick($(this));
	});

	$('.txt-pedido').change(function(event) {
		app.eventTxtChange();
	});

	$('#pedido_form').submit(function(){
    	$("#pedido_form :disabled").removeAttr('disabled');
	});
	
});