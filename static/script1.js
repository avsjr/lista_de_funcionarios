$(document).ready(function() {
  // Inicialmente, oculte todas as linhas de departamentos e funcionários
  $(".departamento-row, .funcionario-row").hide();

  // Adicione um evento de clique para expandir/recolher empresas
  $(".empresa-row .expand-button").on("click", function() {
      let button = $(this);
      let empresaRow = button.closest("tr");
      let departamentoRows = empresaRow.nextUntil(".empresa-row");
      departamentoRows.toggle();
      toggleButtonSymbol(button);
      toggleDepartmentButtons(departamentoRows);
  });

  // Adicione um evento de clique para expandir/recolher departamentos
  $(".departamento-row .expand-button").on("click", function() {
      let button = $(this);
      let departamentoRow = button.closest("tr");
      departamentoRow.nextUntil(".departamento-row").toggle();
      toggleButtonSymbol(button);
  });
});

function toggleButtonSymbol(button) {
  if (button.text() === "+") {
      button.text("-");
  } else {
      button.text("+");
  }
}

function toggleDepartmentButtons(departamentoRows) {
  let firstDepartmentRow = departamentoRows.first();
  let button = firstDepartmentRow.find(".expand-button");
  if (firstDepartmentRow.is(":visible")) {
      button.text("-");
  } else {
      button.text("+");
  }
}
