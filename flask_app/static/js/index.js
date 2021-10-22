import { Cah } from './Cah.js';

var MainPack = Cah[0];
var black_cards = MainPack.black;
var white_cards = MainPack.white;

console.log(MainPack.name);

// Rules as an alert box when black deck is clicked.
var black = document.getElementById("black");
black.addEventListener('click', rules);
function rules() {
    alert("1. The text in the black box is the black card you have to complete." + "2. Clicking on the white deck adds a white card to your hand, and you can have up to seven cards!" + "3. Clicking on one of the white cards in your hand submits it as your answer, and removes the card from your hand." + "4. Out of the three white cards in the black box (your card and two cards from computer players), click the one you think is the funniest." + "5. Click the Next Round button to begin the next round!" + "6. After 5 rounds the game ends!");
}

// Generates the text from a random black card in the black box.
var master = document.getElementById('master');
var BlackCards = black_cards[Math.floor(Math.random()*black_cards.length)];
master.innerHTML = `<h1>${BlackCards.text}</h1>`;
console.log(`${BlackCards.text}`);

// var black = document.getElementById("black");
// black.addEventListener('click', black_random);

// function black_random() {
//     var BlackCards = black_cards[Math.floor(Math.random()*black_cards.length)];
//     var master = document.getElementById('master');
//     console.log(`${BlackCards.text}`);
//     master.innerHTML = `<h1>${BlackCards.text}</h1>`;
// }

// Adds a white card to your hand with a maximum limit of 7.
var the_hand = [];
var num = 0;

var white = document.getElementById("white");
white.addEventListener('click', white_random);

function white_random() {
    var random_w_card = white_cards[Math.floor(Math.random()*white_cards.length)];
    var WhiteCards = random_w_card.text;

    if(the_hand.length < 7){
        var hand = document.getElementById('hand');
        the_hand.push(hand.innerHTML += `<td id="hand_card ${num}" class="hand_card"><h3>${WhiteCards}<h3></td>`); 
        num++;
        console.log(num);
    }
}

console.log(the_hand);

// Removes a card and adds its text to the black box on click.
var the_user = [];
var user_card = document.getElementById("hand");
user_card.addEventListener('click', user_picks/* && computer_card*/);
function user_picks(e){
    // console.log(e);
    console.log(e.target);
    var the_card = e.target;

    var master_display = document.getElementById("display_row");
    master_display.innerHTML = `<td id="hand_card ${num}" class="hand_card"><h3>${the_card.innerText}<h3></td>`;
    the_user.push(the_card.innerText);
    console.log(master_display.innerHTML);
    the_card.parentNode.removeChild(the_card);
    setTimeout(addCard, 1000);
    setTimeout(addCard, 2000);
    // var random_w_card = white_cards[Math.floor(Math.random()*white_cards.length)];
    // var WhiteCards = random_w_card.text;
    // console.log(WhiteCards);
    // display_row.innerHTML += `<td id="hand_card ${num}" class="hand_card"><h3>${WhiteCards}<h3></td>`;
}

console.log(the_user);

// Adds the computer player's cards
function addCard(){
    var random_w_card = white_cards[Math.floor(Math.random()*white_cards.length)];
    var WhiteCards = random_w_card.text;
    console.log(WhiteCards);
    display_row.innerHTML += `<td id="hand_card ${num}" class="hand_card"><h3>${WhiteCards}<h3></td>`;
}

// Fun extra features Flynn included.
var chosen_one = document.getElementById('display_row');
chosen_one.addEventListener('click', choose);
function choose(e){
    var chosen = e.target.innerText;
    console.log(chosen);
    var alert_user = document.getElementById('pop-it');
    if(chosen == the_user[0]){
        alert_user.innerHTML= '<div class="notify"><iframe src="https://giphy.com/embed/7b4FwtEI6W9yg" width="480" height="366" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><h2>I guess you won this round.</h2></div>';
    } else{
        alert_user.innerHTML= `<div class="notify" style='text-align: center;'><h2 style='width:400px;'>Wow you think the computer is funnier? I respect the honesty. You deserve an Oscar.</h2><iframe src="https://giphy.com/embed/jU9m03NG7bw88rwzok" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>`;
    }
}

var count = 0;

var restart_button = document.getElementById('next_game');
restart_button.addEventListener('click', restart);
function restart(){
    //PROBLEM CHILD: deletes whole <tr>
    var display_row = document.getElementById('display_row'); // Problem child!
    display_row.remove();

    var master = document.getElementById('master');
    var BlackCards = black_cards[Math.floor(Math.random()*black_cards.length)];
    master.innerHTML = `<h1>${BlackCards.text}</h1>`;
    console.log(`${BlackCards.text}`);
    count++;
}

// var chosen_two = document.getElementById('display_row');
// chosen_two.addEventListener('click', reset);
// function reset() {
//     document.getElementById("display_row").reset();

// function computer_card() {
//     var random_w_card = white_cards[Math.floor(Math.random()*white_cards.length)];
//     var WhiteCards = random_w_card.text;
//     console.log(WhiteCards);
//     display.innerHTML += `<td id="hand_card ${num}" class="hand_card"><h3>${WhiteCards}<h3></td>`;
// }

// for(const card of foodWhiteCards) {
//     cards.innerHTML = card `<li>${card.text}</li>`
//     myArray[Math.floor(Math.random()*myArray.length)];
// }

// var pop = document.getElementById("pop")
// // var randomBlack_card = black_cards[Math.floor(Math.random()*black_cards.length)];
// pop.innerHTML = `<h2>${}`