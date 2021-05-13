function generateQRCode() {
	var data = document.getElementById("data").value
	eel.generate_qr(data)
}

function generateQRCodea() {
	var data = document.getElementById("data").value
	eel.generate_qra(data)
}

function generateQRCodeb() {
	var demo = document.getElementById("demo").value
	eel.generate_qrb(demo)
}

function generateQRCodec() {
	var data = document.getElementById("data").value
	eel.generate_qrc(data)
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}