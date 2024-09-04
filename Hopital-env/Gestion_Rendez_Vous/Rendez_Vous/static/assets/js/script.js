var lheure=setInterval(function(){Heure()}, 1000);

function Heure(){
    var obj_d=new Date();
    var temps=obj_d.toLocaleTimeString();
    document.getElementById('heure').innerHTML=temps;
}