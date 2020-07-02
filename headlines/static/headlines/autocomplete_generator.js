"use strict";
function open_url(textbox, url_ref) {
			var word = textbox.value;
			var new_url = url.replace("foobar", word);
			window.open(new_url);
		};