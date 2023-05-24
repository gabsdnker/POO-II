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


const dropdowns = document.querySelectorAll('.dropdown');   // Seleciona todos os elementos com a classe "dropdown"      
dropdowns.forEach((dropdown) => {                           // Adiciona um evento de clique para cada elemento com a classe "dropdown"
    const dropdownContent = dropdown.nextElementSibling;    // Seleciona o elemento com a classe "dropdown-content"
    dropdown.addEventListener('click', () => {              // Adiciona um evento de clique ao elemento com a classe "dropdown"
        dropdownContent.classList.toggle('show');           // Adiciona ou remove a classe "show" do elemento com a classe "dropdown-content"
    });
   
});


//Script para veririficar estado das imagem do botão dropdown
function trocarImagem(elemento) {
    var imagem = elemento.querySelector("img");
    if (imagem.src.indexOf("seta-direita.png") != -1) {
      imagem.src = "../static/img/seta-para-baixo.png";
    } else {
      imagem.src = "../static/img/seta-direita.png";
    }
}