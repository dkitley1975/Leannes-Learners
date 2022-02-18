// script to auto close the alert messages
setTimeout(function () {
	if ($('#msg').length > 0) {
		$('#msg').remove();
	}
}, 2500);
