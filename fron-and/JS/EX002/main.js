const numero = document.getElementById("n")
const botao = document.getElementById('botao')
botao.addEventListener('click',function(){
    let valor = Number(numero.value)
    let numeroaleatorio = Math.random()
    console.log(numeroaleatorio)

})