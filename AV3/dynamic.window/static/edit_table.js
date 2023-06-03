function updateCell(event) {
  event.preventDefault(); // Evita o envio do formulário

  // Obtém os elementos do formulário
  var addForm = event.target.closest(".cell");
  var deleteForm = addForm.nextElementSibling;

  // Exibe o botão "Excluir" e oculta o botão "Add"
  addForm.style.display = "none";
  deleteForm.querySelector(".delete-button").style.display = "inline";

  // Obtém o valor da célula
  var cellValue = addForm.querySelector("input[name='value']").value;

  // Cria um elemento para exibir o valor da célula
  var cellValueElement = document.createElement("span");
  cellValueElement.textContent = cellValue;

  // Insere o elemento na célula
  addForm.parentNode.insertBefore(cellValueElement, addForm);
}
