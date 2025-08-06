let pessoa = 'kayk';
const numero = 2;
function falar() {
    console.log('nome:');
}
falar()
if (numero < 1){
    console.log('menor que 1');
}
else{
    console.log('numero e maior que 1')
}
for (let i = 1; i <= 5; i++){
    console.log('numero:' + i);
}
const input = document.getElementById('input')
const botao = document.getElementById('butao')
botao.addEventListener('click', function() {
    const valor = Number(input.value);
    console.log('Você digitou:', valor);

    if (valor < 2) {
        console.log('Seu número não é primo');
        return;
    }

    const resultado = primo(valor);

    if (resultado) {
        console.log('É primo');
    } else {
        console.log('Não é primo');
    }
});
function primo(numero){
    for ( let i = 2; i <= Math.sqrt(numero);i++){
        if (numero % i === 0){
            return false
        }
    }
    return true   }



/*(|| == ou ) (&& todas tem que ser verdadeiras) */
/* % restp */

