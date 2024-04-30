var cover = document.querySelector(".itemCoverImgSection");
var resImg = document.querySelector(".itemImgSection");
var ex = document.querySelector(".itemExSection");

var getBtn = document.querySelector(".getBtn");
var reGetBtn = document.querySelector(".reGetBtn");
var seeMenuBtn = document.querySelector(".seeMenuBtn");

const getMenu = () => {
    cover.style.display = "none"
    resImg.style.display = "flex"
    ex.style.display = "flex"
    getBtn.style.display = "none"
    reGetBtn.style.display = "flex"
    seeMenuBtn.style.display = "flex"
}

getBtn.addEventListener("click", () => {
    getMenu();
})