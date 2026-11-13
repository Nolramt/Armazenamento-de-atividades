const abaAtividade = document.getElementById("aba-atividade");
const abaTrabalho = document.getElementById("aba-trabalho");

const painelAtividade = document.getElementById("painel-atividade");
const painelTrabalho = document.getElementById("painel-trabalho");

abaAtividade.addEventListener("click", function() {

    painelAtividade.hidden = false;
    painelTrabalho.hidden = true;

    abaAtividade.classList.add("ativa");
    abaTrabalho.classList.remove("ativa");

});

abaTrabalho.addEventListener("click", function() {

    painelTrabalho.hidden = false;
    painelAtividade.hidden = true;

    abaTrabalho.classList.add("ativa");
    abaAtividade.classList.remove("ativa");

});