//JS port of guacaster.py

function castYao() {
    var cast = 0;
    for (i=0;i<3;i++) {
	//todo) { find a way to call wheatonDice as a module
	//as an excercise in doing so. 
	cast += Math.ceil(Math.random() * 2);
    }
    return cast;
}

//This whole thing might be accomplished easier if we skip going through 
//the trigrams and just convert guaCode to 3 hex and then go through each 
//literally instead of elementally
function idGua(guaCode) {
	//Gua[0] is the upper trigram; Gua[1] is the lower trigram
    var jGua = [[],[]], //Old situation
	yGua = [[],[]], //The situation which affects the change
	xGua =[[],[]], //New situation
	
	jiuGua = '',
	yiGua = '',
	xinGua = '';

	for (i=0; i<3; i++) { //Upper Trigram
	    if (guaCode[i] === 3) {    //Yang changes to Yin
		jGua[0].push(9);	//Yang
		yGua[0].push(9);	//Active
		xGua[0].push(6);	//Yin
	    } else if (guaCode[i] === 4) {  //Yin stays yin
		jGua[0].push(6);	//Yin
		yGua[0].push(6);	//Passive
		xGua[0].push(6);	//Yin
	    } else if (guaCode[i] === 5) {  //Yang stays Yang
		jGua[0].push(9);	//Yang
		yGua[0].push(6);	//Passive
		xGua[0].push(9);	//Yang
	    } else { //if (guaCode[i] === 6) { //Yin changes to Yang
		jGua[0].push(6);	//Yin
		yGua[0].push(9);	//Active
		xGua[0].push(9);	//Yang
	    }
	}

	for (i=3; i<6; i++) { //Lower Trigram
	    if (guaCode[i] === 3) {    //Yang changes to Yin
		jGua[1].push(9);	//Yang
		yGua[1].push(9);	//Active
		xGua[1].push(6);	//Yin
	    } else if (guaCode[i] === 4) {  //Yin stays yin
		jGua[1].push(6);	//Yin
		yGua[1].push(6);	//Passive
		xGua[1].push(6);	//Yin
	    } else if (guaCode[i] === 5) {  //Yang stays Yang
		jGua[1].push(9);	//Yang
		yGua[1].push(6);	//Passive
		xGua[1].push(9);	//Yang
	    } else { //guaCode[i] ===6: //Yin changes to Yang
		jGua[1].push(6);	//Yin
		yGua[1].push(9);	//Active
		xGua[1].push(9);	//Yang
	    }
	}

	function nameGua(gua, guaName) {
		if (gua[1] === [6,6,9]) { //Lower Zhen
		    if (gua[0] === [6,6,9]) {
			guaName = '51';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '21';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '17';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '25';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '42';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '3';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '27';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '24';
		    }

		} else if (gua[1] === [9,6,9]) { //Lower Li
		    if (gua[0] === [6,6,9]) {
			guaName = '55';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '30';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '49';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '13';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '37';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '63';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '22';
		    } else { // if (gua[0] === [6,6,6]) {
			guaName = '36';
		    }

		} else if (gua[1] === [6,9,9]) {//Lower Dui
		    if (gua[0] === [6,6,9]) {
			guaName = '54';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '38';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '58';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '10';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '61';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '60';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '41';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '19';
		    }

		} else if (gua[1] === [9,9,9]) { //Lower Qian
		    if (gua[0] === [6,6,9]) {
			guaName = '34';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '14';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '43';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '1';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '9';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '5';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '26';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '11';
		    }

		} else if (gua[1] === [9,9,6]) { //Lower Xun
		    if (gua[0] === [6,6,9]) {
			guaName = '32';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '50';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '28';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '44';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '57';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '48';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '18';
		    } else { //gua[0] === [6,6,6]) {
			guaName = '46';
		    }

		} else if (gua[1] === [6,9,6]) { //Lower Kan
		    if (gua[0] === [6,6,9]) {
			guaName = '40';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '64';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '47';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '6';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '59';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '29';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '4';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '7';
		    }

		} else if (gua[1] === [9,6,6]) { //Lower Gen
		    if (gua[0] === [6,6,9]) {
			guaName = '62';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '56';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '31';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '33';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '53';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '39';
		    } else if (gua[0] === [9,6,6]) {
			guaName = '52';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '15';
		    }

		} else { //if (gua[1] === [6,6,6]) { //Lower Kun
		    if (gua[0] === [6,6,9]) {
			guaName = '16';
		    } else if (gua[0] === [9,6,9]) {
			guaName = '35';
		    } else if (gua[0] === [6,9,9]) {
			guaName = '45';
		    } else if (gua[0] === [9,9,9]) {
			guaName = '12';
		    } else if (gua[0] === [9,9,6]) {
			guaName = '20';
		    } else if (gua[0] === [6,9,6]) {
			guaName = '8';
		    } else if (gua[0] === [6,6,9]) {
			guaName = '23';
		    } else { //if (gua[0] === [6,6,6]) {
			guaName = '2';
		    }
		}
	}

	nameGua(jGua,jiuGua);
	nameGua(yGua,yiGua);
	nameGua(xGua,xinGua);

	console.log(jiuGua + '\n' + yiGua + '\n' + xinGua);
}

function castGua() {
    var guaImag = '',
	guaCode = [];
    for (j=0;j<6;j++) {
	guaCode.push(castYao());
    }
    for (k=5;k>=0;k--) {
	if (guaCode[k] === 3) {
	    guaImag += '_________  > Jiu >  ___   ___\n';
	} else if (guaCode[k] === 4) {
	    guaImag += '___   ___ |  Xin  | ___   ___\n';
	} else if (guaCode[k] === 5) {
	    guaImag += '_________ |  Xin  | _________\n';
	} else /*if (guaCode[k] === 6)*/ {
	    guaImag += '___   ___  > Jiu >  _________\n';
	}
    }
    console.log(guaImag);
    return idGua(guaCode);
}

//console.log(castYao());
console.log(castGua());
