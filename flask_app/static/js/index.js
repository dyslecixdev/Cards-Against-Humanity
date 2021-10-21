import { Cah } from './Cah.js';
var foodPack = Cah[0];
var geekPack = Cah[1];
var scifiPack = Cah[2];
var black_cards = foodPack.black;
var white_cards = foodPack.white;

console.log(foodPack.name);

var show = document.getElementById("show")

show.innerHTML = `<h1> ${foodPack.name} </h1>`


var white = document.getElementById("white")
white.addEventListener('click', white_random)
function white_random() {
    var foodWhiteCards = white_cards[Math.floor(Math.random()*white_cards.length)];
    console.log(`${foodWhiteCards.text}`);
    alert(`${foodWhiteCards.text}`);
}

var white = document.getElementById("white")
white.addEventListener('click', white_random)
function black_random() {
    var foodWhiteCards = black_cards[Math.floor(Math.random()*black_cards.length)];
    console.log(`${foodBlackCards.text}`);
    var pop = document.getElementById('pop');
    pop.style.display = "block";
    pop.innerHTML = `<h2>${foodBlackCards.text}</h2>`
}


// for(const card of foodWhiteCards) {
//     cards.innerHTML = card `<li>${card.text}</li>`
//     myArray[Math.floor(Math.random()*myArray.length)];
// }

// var pop = document.getElementById("pop")
// // var randomBlack_card = black_cards[Math.floor(Math.random()*black_cards.length)];
// pop.innerHTML = `<h2>${}` 