// 1. Seleciona o botão e a lista do menu através do DOM
const botaoMenu = document.querySelector('.menu-hamburger');
const listaMenu = document.querySelector('nav ul');

// 2. Cria uma função para abrir/fechar o menu
function alternarMenu() {
  botaoMenu.classList.toggle('ativo');
  listaMenu.classList.toggle('ativo');
}

// 3. Adiciona o evento de clique no botão
botaoMenu.addEventListener('click', alternarMenu);