const startBus = document.querySelector(".startBox");
var startValue = startBus.value;

const stopBus = document.querySelector(".stopBox");
var stopValue = stopBus.value;

const showTimeBtn = document.querySelector(".busInsertBtn");

const HtoS = document.querySelector(".HtoS");
const HtoHami = document.querySelector(".HtoHami");
const SintoH = document.querySelector(".SintoH");
const SouttoH = document.querySelector(".SouttoH");
const HamitoH = document.querySelector(".HamitoH");

const defaultImg = document.querySelector(".defaultImgBox");

const handleOnChange1 = (x) => {
    startValue = x.value;
    console.log(startValue);
}

const handleOnChange2 = (y) => {
    stopValue = y.value;
    console.log(stopValue);
}

const showDefaultImg = () => {
    defaultImg.style.display = "flex";
}

const HtoSshow = () => {
    HtoS.style.display = "flex";
    defaultImg.style.display = "none";
}

const HtoShide = () => {
    HtoS.style.display = "none";
}

const SintoHshow = () => {
    SintoH.style.display ="flex";
    defaultImg.style.display = "none";
}

const SintoHhide = () => {
    SintoH.style.display = "none";
}

const SouttoHshow = () => {
    SouttoH.style.display = "flex";
    defaultImg.style.display = "none";
}

const SouttoHhide = () => {
    SouttoH.style.display = "none";
}

const HamitoHHshow = () => {
    HamitoH.style.display = "flex";
    defaultImg.style.display = "none";
}

const HamitoHhide = () => {
    HamitoH.style.display = "none";
}

const HtoHamishow = () => {
    HtoHami.style.display = "flex";
    defaultImg.style.display = "none";
}

const HtoHamihide = () => {
    HtoHami.style.display = "none";
}

showTimeBtn.addEventListener("click", () => {
    // console.log(startValue);
    // console.log(stopValue);
    if(startValue == "Hanseo" && stopValue == "Seosan") {
        HtoSshow();
        SintoHhide();
        SouttoHhide();
        HamitoHhide();
        HtoHamihide();
    } else if (startValue == "SeosanIn" && stopValue == "Hanseo") {
        SintoHshow();
        HtoShide();
        SouttoHhide();
        HamitoHhide();
        HtoHamihide();
    } else if (startValue == "SeosanOut" && stopValue == "Hanseo") {
        SouttoHshow();
        HtoShide();
        SintoHhide();
        HamitoHhide();
        HtoHamihide();
    } else if (startValue == "Hami" && stopValue == "Hanseo") {
        HamitoHHshow();
        HtoShide();
        SintoHhide();
        SouttoHhide();
        HtoHamihide();
    } else if (startValue == "Hanseo" && stopValue == "Hami") {
        HtoHamishow();
        SintoHhide();
        SouttoHhide();
        HamitoHhide();
    } else {
        showDefaultImg();
        HtoShide();
        SintoHhide();
        SouttoHhide();
        HamitoHhide();
        HtoHamihide();
    }
});