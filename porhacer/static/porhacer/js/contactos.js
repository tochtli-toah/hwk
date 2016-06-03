$(document).on('ready', function(){
	
	function toTitleCase(str)
	{
		return str.replace(/([^\W_]+[^\s-]*) */g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
	}
	
	$('#machacable').on('click', function(){
		$.get( "https://randomuser.me/api/", function( data ) {
		  
		  //imagen
		  $('#contactante').attr("src", data.results[0].picture.large);
		  
		  //datos de primer div
		  var importante = '<p> <strong>Nombre: </strong> ' + toTitleCase(data.results[0].name.title) + '. ' + toTitleCase(data.results[0].name.first) + ' ' + toTitleCase(data.results[0].name.last) + '</p>'; 
		  importante += '<p> <strong>Usuario: </strong> ' + toTitleCase(data.results[0].login.username) + '</p>'; 
		  importante += '<p> <strong>Contraseña: </strong> ' + toTitleCase(data.results[0].login.password) + '</p>'; 
		  if( data.results[0].email != undefined ){
		      importante += '<p> <strong>Correo electrónico: </strong> ' + data.results[0].email + '</p>'; 
	      }
	      if( data.results[0].cel != undefined ){
		      importante += '<p> <strong>Numero de celular: </strong> ' + data.results[0].cel + '</p>'; 
	      }
		  $('#importante').html(importante);
		  
		  //datos del segundo div
		  
		  var regular = '<p> <strong>Ciudad y estado: </strong> ' + toTitleCase(data.results[0].location.city) + ', ' + toTitleCase(data.results[0].location.state) + '</p>'; 
		  if( data.results[0].location.street != undefined ){
			regular += '<p> <strong>Calle: </strong> ' + toTitleCase(data.results[0].location.street) + '</p>'; 
	      }
	      if( data.results[0].location.postcode != undefined ){
			regular += '<p> <strong>Código postal: </strong> ' + data.results[0].location.postcode + '</p>'; 
	      }
		  $('#regular').html(regular);
		  
		  
		}, 'json');
	});
	
});
