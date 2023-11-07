$(document).ready(function() {
    // Inicialmente, oculte todos os elementos aninhados da árvore
    $("#tree ul").hide();
  
    // Adicione um evento de clique para expandir/recolher os nós de empresa e departamento
    $("#tree li.empresa").on("click", function(e) {
      e.stopPropagation(); // Evite que o clique se propague
      $(this).children("ul").slideToggle();
    });
  
    // Adicione um evento de clique para expandir/recolher os nós de funcionário
    $("#tree li.departamento").on("click", function(e) {
      e.stopPropagation(); // Evite que o clique se propague
      $(this).find("ul").slideToggle();
    });
  });
  