const webSocket = new WebSocket('ws://' + window.location.host + '/ws/clicker/' + parseInt(window.location.pathname.split('/')[2]));


webSocket.onmessage = function(e) {
	// console.log(e)
	const data = JSON.parse(e.data);
	document.querySelector('#score').innerText = data.score
	// chat.innerHTML += '<div class="msg">' + data.message + '</div>'
};


function clicker() {
	score = document.querySelector('#score').innerText;
	document.querySelector('#score').innerText = parseInt(score) + 1;

	webSocket.send(JSON.stringify({
		'room_id': window.location.pathname.split('/')[2],
		'score': document.querySelector('#score').innerText,
	}));
}