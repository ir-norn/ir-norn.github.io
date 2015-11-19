jThree( function( j3 ) {

	$( "#loading" ).remove();
	
	j3.Trackball();
	j3.Stats();

},
function() {
	alert( "このブラウザはWebGLに対応していません。" );
} );
