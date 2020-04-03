//Button Hover Title Changer
let blockHolder = document.querySelectorAll(".blocky");
let province = document.getElementById("province-hover");
let alberta = document.querySelector(".alberta");

alberta.addEventListener("mouseover", function(){
    province.innerHTML = "Alberta";
    alberta.addEventListener("mouseout", function(){
        province.innerHTML = "Select A Province";
    });
}); // End Alberta Hover Tile Changer

//Mobile Map Slideshow
let images = ["static/img/bc-final.png", "static/img/alberta-final.png", "static/img/sk-final.png", "static/img/mb-final.png", "static/img/on-final.png", "static/img/qc-final.png", "static/img/nl-final.png", "static/img/nb-final.png", "static/img/ns-final.png"];
let currentImg = 0;

document.querySelector(".next").addEventListener("click", function(){
    if (currentImg < images.length - 1) {
        currentImg += 1;
    } else {
        currentImg = 0;
    }
    document.querySelector(".holder-mobile>div>img").src = images[currentImg];

    if(currentImg == 0){
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "British Columbia";
    } else if (currentImg == 1){
        document.querySelector(".mobile-local-button").href = "province/ab";
        document.querySelector(".mobile-provice-name").innerHTML = "Alberta";
    } else if (currentImg == 2){
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Saskatchewan";
    } else if (currentImg == 3) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Manitoba";
    } else if (currentImg == 4) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Ontario";
    } else if (currentImg == 5) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Quebec";
    } else if (currentImg == 6) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Newfoundland & Labrador";
    } else if (currentImg == 7) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "New Brunswick";
    } else if (currentImg == 8) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Nova Scotia & Prince Edward Island";
    }
})

document.querySelector(".prev").addEventListener("click", function(){
    if (currentImg > 0) {
        currentImg -= 1;
    } else {
        currentImg = images.length - 1;
    }
    document.querySelector(".holder-mobile>div>img").src = images[currentImg];

    if(currentImg == 0){
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "British Columbia";
    } else if (currentImg == 1){
        document.querySelector(".mobile-local-button").href = "province/ab";
        document.querySelector(".mobile-provice-name").innerHTML = "Alberta";
    } else if (currentImg == 2){
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Saskatchewan";
    } else  if (currentImg == 3){
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Manitoba";
    } else if (currentImg == 4) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Ontario";
    } else if (currentImg == 5) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Quebec";
    } else if (currentImg == 6) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Newfoundland & Labrador";
    } else if (currentImg == 7) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "New Brunswick";
    } else if (currentImg == 8) {
        document.querySelector(".mobile-local-button").href = "#";
        document.querySelector(".mobile-provice-name").innerHTML = "Nova Scotia & Prince Edward Island";
    }
})
