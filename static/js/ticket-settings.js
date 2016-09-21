
function getTicketElement(ticketId) {
	var el = {
			id: ticketId,
			jqE: $('#fb-'+ticketId)
	}
	el.getTitle = function(){
		return $(":nth-child(4)", this.jqE).text();
	}
	
	el.getMessage = function() {
		return $(":nth-child(5)", this.jqE).text();
	}
	
	el.getCharacterId = function() {
		return this.jqE.attr('data-charID');
	}
	el.getCharacterName = function() {
		return $(":nth-child(3)", this.jqE).text();
	}
	return el;
}

function sendTicketMail(ticketId) {
	var ticketElement = getTicketElement(ticketId);
	var title = ticketElement.getTitle();
	var message = ticketElement.getMessage();
	var charID = ticketElement.getCharacterId();
	var charName = ticketElement.getCharacterName();
	IGBW.sendMail(charID, "Answer to your Waitlist Feedback",
			"Hello "+charName+",\n"
			+ "We read your ticket:\n"
			+ "<font size=\"10\" color=\"#ffffcc00\">"
			+ $("<div>").text(title).html()+"\n\n"
			+ $("<div>").text(message).html()
			+ "</font>\n\n"
			+ "regards,\n"
			);
}