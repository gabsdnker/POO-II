function addCampo() {
    var form = document.querySelector('form[action="/cadastrar"]');
    var campo = document.createElement('input');
    campo.type = 'text';
    campo.name = 'campo';
    campo.placeholder = 'Nome do campo';
    var valor = document.createElement('input');
    valor.type = 'text';
    valor.name = 'valor';
    valor.placeholder = 'Valor do campo';
    var botao = document.createElement('button');
    botao.type = 'button';
    botao.innerText = '-';
    botao.onclick = function() {
        form.removeChild(campo);
        form.removeChild(valor);
        form.removeChild(botao);
    }
    form.insertBefore(campo, form.lastElementChild);
    form.insertBefore(valor, form.lastElementChild);
    form.insertBefore(botao, form.lastElementChild);
}


// menu
function addField() {
    var fieldContainer = document.createElement("div");
    fieldContainer.innerHTML = `
        <label for="campo">Field Name:</label>
        <input type="text" name="campo[]" required>
        <label for="valor">Field Value:</label>
        <input type="text" name="valor[]" required><br>`;
    document.querySelector("form").appendChild(fieldContainer);
}

function adicionarCampo() {
    var campoInput = document.createElement('input');
    campoInput.type = 'text';
    campoInput.name = 'campo[]';
    campoInput.required = true;

    var valorInput = document.createElement('input');
    valorInput.type = 'text';
    valorInput.name = 'valor[]';
    valorInput.required = true;

    var br = document.createElement('br');

    var form = document.getElementsByTagName('form')[0];
    form.insertBefore(campoInput, form.lastElementChild);
    form.insertBefore(valorInput, form.lastElementChild);
    form.insertBefore(br, form.lastElementChild);
}