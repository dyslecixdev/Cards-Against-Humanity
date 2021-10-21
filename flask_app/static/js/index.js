import { Cah } from './Cah.js';
var MainPack = Cah[0];
var black_cards = MainPack.black;
var white_cards = MainPack.white;

console.log(MainPack.name);


var the_hand = [];
var the_text = [];

var white = document.getElementById("white")
white.addEventListener('click', white_random)
function white_random() {
    var random_w_card = white_cards[Math.floor(Math.random()*white_cards.length)];
    var WhiteCards = random_w_card.text;

    if(the_hand.length < 7){
        var hand = document.getElementById('hand')
        the_hand.push(hand.innerHTML += `<td id="hand_card" class="hand_card"><h3>${WhiteCards}<h3></td>`); 
        the_text.push(`${WhiteCards}`);
    }
}
console.log(the_text);
console.log(the_hand);


// var user_card = document.getElementById("hand_card")
// user_card.addEventListener('click', user_picks)
// function user_picks(){
    
// }

var BlackCards = black_cards[Math.floor(Math.random()*black_cards.length)];
console.log(`${BlackCards.text}`);

var black = document.getElementById("black")
black.addEventListener('click', black_random)
function black_random() {
    var BlackCards = black_cards[Math.floor(Math.random()*black_cards.length)];
    var master = document.getElementById('master')
    console.log(`${BlackCards.text}`);
    master.innerHTML = `<h1>${BlackCards.text}</h1>`
}




// for(const card of foodWhiteCards) {
//     cards.innerHTML = card `<li>${card.text}</li>`
//     myArray[Math.floor(Math.random()*myArray.length)];
// }

// var pop = document.getElementById("pop")
// // var randomBlack_card = black_cards[Math.floor(Math.random()*black_cards.length)];
// pop.innerHTML = `<h2>${}`

//slice method to remove white cards.