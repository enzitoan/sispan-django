var app = {};

app.VERSION = '1.0';
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
	app.oDetalle = {
		'cantidad': 0,
		'total': 0
	};

	$.each($('.txt-pedido'), function(index, val) {
		var items = 0;
		if ($(this).val() != ''){
			items = $(this).val(); 
		}
		app.aTotPanes[index] = parseInt(items);		
	});

	var total = 0;
	$.each(app.aTotPanes,function(index, val) {
		if (isNaN(val)) {
			val = 0;
		}
	    total += val;
	});

	app.oDetalle.cantidad = total;
	app.oDetalle.total = parseInt(total) * this.SISTEMA.valorPan;

	$('#lblCantidad').text(app.oDetalle.cantidad);
	$('#lblTotal').text('$ ' + app.oDetalle.total);

	if (app.oDetalle.cantidad > 0) {
		if ($('#txtNombre').val() != '' && $('#txtCorreo').val() != '') {
			$('#btnIngresar').prop('disabled', false);
		}
	}
}

app.eventChkClick = function(checkbox) {
	if ($(checkbox).is(':checked')) {
		if($('#isEdit').val() != 'S') {
			$('#txtPan' + $(checkbox).data('id-pan')).val(1);			
		}
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', false);
	} else {
		if($('#isEdit').val() != 'S') {
			$('#txtPan' + $(checkbox).data('id-pan')).val(0);
		}		
		$('#txtPan' + $(checkbox).data('id-pan')).prop('disabled', true);
	}
	this.eventTxtChange();
}

app.eventTxtChange = function() {
	app.calcularTotalPedido();

	if($('#isEdit').val() != 'S') {
		if (app.oDetalle.total != 0) {
			$('#txtNombre').prop('disabled', false);
			$('#txtCorreo').prop('disabled', false);
			$('#btnIngresar').prop('disabled', false);		
		} else {
			$('#txtNombre').prop('disabled', true);
			$('#txtCorreo').prop('disabled', true);
			$('#btnIngresar').prop('disabled', true);
		}
	}
}

$(document).ready(function() {
	app.obtenerInformacionApp();
	app.listarTiposPan();

	if($('#isEdit').val() == 'S') {
		$('#txtNombre').prop('disabled', true);
		$('#txtCorreo').prop('disabled', true);
		$('#btnIngresar').prop('disabled', false);
	}

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