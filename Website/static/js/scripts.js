var selectedValue;

function reduceQty()
{
	var ddl = document.getElementById("numitem");
	selectedValue = ddl.options[ddl.selectedIndex].text;
}

function showTotal()
{
	var ddl = document.getElementById("numitem");
	var vale = ddl.options[ddl.selectedIndex].text;
	
	$("#totalc").text(vale);
}


function showTime() {
	$('footer #time').text(Date());
}

$(document).ready(function() {
	setInterval(showTime, 1000);
	});