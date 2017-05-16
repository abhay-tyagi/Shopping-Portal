function reduceQty()
{
	var ddl = document.getElementById("numitem");
	var selectedValue = ddl.options[ddl.selectedIndex].value;

}


function showTime() {
	$('footer #time').text(Date());
}

$(document).ready(function() {
	setInterval(showTime, 1000);
	});