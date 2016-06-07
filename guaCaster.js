//JS port of guacaster.py

function castYao() {
    var cast = 0;
    for (i=0;i<3;i++) {
	//todo: find a way to call wheatonDice as a module
	//as an excercise in doing so. 
	cast += Math.ceil(Math.random() * 2);
    }
    return cast;
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
	} else /*if (guaCode[k] === 6))*/ {
	    guaImag += '___   ___  > Jiu >  _________\n';
	}
    }
    console.log(guaImag);
    return guaCode;
}

//console.log(castYao());
console.log(castGua());
