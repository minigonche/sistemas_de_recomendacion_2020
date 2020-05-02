//lugares js

function refrescarLugar() {
      
      // carga el JSON
      $.getJSON(locations_info_loc, function(json) {
          
          var selectBox = document.getElementById("select_lugar");
          var cs = selectBox.options[selectBox.selectedIndex].value;

          // IMG
          document.getElementById("img_location").src = img_location.replace("STATE", cs);

          //Titulo
          document.getElementById("lugar_titulo").innerHTML = json[cs]['state_name'];

          var renglon = "<strong>V1: </strong> V2 </p>";
          //Pais
          document.getElementById("lugar_pais").innerHTML = renglon.replace("V1",'Pais').replace('V2', json[cs]['country']);

          //Poblacion
          document.getElementById("lugar_poblacion").innerHTML = renglon.replace("V1",'Población').replace('V2', "".concat(json[cs]['population']," Personas"));


          //Capital
          document.getElementById("lugar_capital").innerHTML = renglon.replace("V1",'Capital').replace('V2', json[cs]['capital']);

          // Categorias
          var categorias = json[cs]['categorias'];
          var t = "";
          var linea = '<li class="list-group-item d-flex justify-content-between align-items-center"> V1 <span class="badge badge-primary badge-pill">V2</span></li>'
          
          for (var i = 0; i < categorias.length; i++){
                t += linea.replace('V1',categorias[i]['categoria']).replace('V2', categorias[i]['total'])
          }
          document.getElementById("lista_actividades").innerHTML = t;


          // Negocios
          var negocios = json[cs]['lugares'];
          var t2 = "";
  
          for (var i = 0; i < negocios.length; i++){
                t2 += linea.replace('V1',negocios[i]['lugar']).replace('V2', negocios[i]['calificacion'])
          }
          document.getElementById("lista_negocios").innerHTML = t2;

        });
      

      }