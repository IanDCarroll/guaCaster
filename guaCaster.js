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
    var jiuGua = 0, //Old situation
	yiGua = 0, //The situation which affects the change
	xinGua =0; //New situation

	for (i=0; i<6; i++) {
	    if (guaCode[i] === 3) {    //Yang changes to Yin
		jiuGua += 9 * (Math.pow(10,i));	//Yang
		yiGua += 9 * (Math.pow(10,i));	//Active
		xinGua += 6 * (Math.pow(10,i));	//Yin
	    } else if (guaCode[i] === 4) {  //Yin stays yin
		jiuGua += 6 * (Math.pow(10,i));	//Yin
		yiGua += 6 * (Math.pow(10,i));	//Passive
		xinGua += 6 * (Math.pow(10,i));	//Yin
	    } else if (guaCode[i] === 5) {  //Yang stays Yang
		jiuGua += 9 * (Math.pow(10,i));	//Yang
		yiGua += 6 * (Math.pow(10,i));	//Passive
		xinGua += 9 * (Math.pow(10,i));	//Yang
	    } else { //if (guaCode[i] === 6) { //Yin changes to Yang
		jiuGua += 6 * (Math.pow(10,i));	//Yin
		yiGua += 9 * (Math.pow(10,i));	//Active
		xinGua += 9 * (Math.pow(10,i));	//Yang
	    }
	}

	function nameGua(gua) {
		if (gua === 669669) {
			return '51';
		} else if (gua === 969669) {
			return '21';
		} else if (gua === 699669) {
			return '17';
		} else if (gua === 999669) {
			return '25. Wu Wang: Innocence |||';
		} else if (gua === 996669) {
			return '42. Yi: Increase |||';
		} else if (gua === 696669) {
			return '3';
		} else if (gua === 966669) {
			return '27. Yi: The corners of the Mouth |||';
		} else if (gua === 666669) {
			return '24. Fu: Return ||';


		} else if (gua === 669969) {
			return '55';
		} else if (gua === 969969) {
			return '30';
		} else if (gua === 699969) {
			return '49';
		} else if (gua === 999969) {
			return '13. Tong Ren: Fellowship with People |||';
		} else if (gua === 996969) {
			return '37';
		} else if (gua === 696969) {
			return '63';
		} else if (gua === 966969) {
			return '22';
		} else if (gua === 666969) {
			return '36';


		} else if (gua === 669699) {
		   return '54';
		} else if (gua === 969699) {
		    return '38';
		} else if (gua === 699699) {
		    return '58';
		} else if (gua === 999699) {
		    return '10. Lu: Treading |||';
		} else if (gua === 996699) {
		    return '61. Zhong Fu: Inner Truth |||';
		} else if (gua === 696699) {
		    return '60';
		} else if (gua === 966699) {
		    return '41. Sun: Decrease |||';
		} else if (gua === 666699) {
		    return '19. Lin: Approach ||';


		} else if (gua === 669999) {
		    return '34. Da Zhuang: The Power of the Great ||';
		} else if (gua === 969999) {
		    return '14. Da Yu: Possession in Great Measure |||';
		} else if (gua === 699999) {
		    return '43. Guai: Break-through ||';
		} else if (gua === 999999) {
		    return '1. Qian: The Creative |';
		} else if (gua === 996999) {
		    return '9. Xiao Chu: The Taming Power of the Small |||';
		} else if (gua === 696999) {
		    return '5';
		} else if (gua === 966999) {
		    return '26. Da Chu: The Taming Power of the Great |||';
		} else if (gua === 666999) {
		    return '11. Tai: Peace ||';


		} else if (gua === 669996) {
		    return '32. Heng: Duration |||';
		} else if (gua === 969996) {
		    return '50';
		} else if (gua === 699996) {
		    return '28. Da Guo: Preponderance of the Great |||';
		} else if (gua === 999996) {
		    return '44. Gou: Coming to Meet ||';
		} else if (gua === 996996) {
		    return '57';
		} else if (gua === 696996) {
		    return '48';
		} else if (gua === 966996) {
		    return '18';
		} else if (gua === 666996) {
		    return '46. Sheng: Pushing Upward |||';


		} else if (gua === 669696) {
		    return '40';
		} else if (gua === 969696) {
		    return '64';
		} else if (gua === 699696) {
		    return '47';
		} else if (gua === 999696) {
		    return '6';
		} else if (gua === 996696) {
		    return '59';
		} else if (gua === 696696) {
		    return '29';
		} else if (gua === 966696) {
		    return '4';
		} else if (gua === 666696) {
		    return '7. Shi: The Army |||';


		} else if (gua === 669966) {
		    return '62. Xiao Guo: Preponderance of the Small |||';
		} else if (gua === 969966) {
		    return '56';
		} else if (gua === 699966) {
		    return '31. Xian: Influence |||';
		} else if (gua === 999966) {
		    return '33. Dun: Retreat ||';
		} else if (gua === 996966) {
		    return '53';
		} else if (gua === 696966) {
		    return '39';
		} else if (gua === 966966) {
		    return '52';
		} else if (gua === 666966) {
		    return '15. Qian: Modesty |||';


		} else if (gua === 669666) {
		    return '16. Yu: Enthusiasm |||';
		} else if (gua === 969666) {
		    return '35';
		} else if (gua === 699666) {
		    return '45. Cui: Gathering Together |||';
		} else if (gua === 999666) {
		    return '12. Pi: Standstill ||';
		} else if (gua === 996666) {
		    return '20. Guan: Contempation ||';
		} else if (gua === 696666) {
		    return '8. Bi: Holding Together |||';
		} else if (gua === 966666) {
		    return '23. Bo: Splitting Apart ||';
		} else if (gua === 666666) {
		    return '2. Kun: The Receptive |';
		} else { return gua; }
	}
	
	return (nameGua(jiuGua) + '\n' + nameGua(yiGua) + '\n' + nameGua(xinGua));
	//return jiuGua + '\n' + yiGua + '\n' + xinGua;
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
