//Button Hover Title Changer
let blockHolder = document.querySelectorAll(".blocky");
let province = document.getElementById("province-hover");
let alberta = document.querySelector(".alberta");

document.querySelector(".bc").addEventListener("mouseover", function(){
    province.innerHTML = "British Columbia (Coming Soon)";
    document.querySelector(".bc").addEventListener("mouseout", function(){
        province.innerHTML = "Select A Province";
    });
}); // End BC Hover Tile Changer

alberta.addEventListener("mouseover", function(){
    province.innerHTML = "Alberta";
    alberta.addEventListener("mouseout", function(){
        province.innerHTML = "Select A Province";
    });
}); // End Alberta Hover Tile Changer

document.querySelector(".sask").addEventListener("mouseover", function(){
    province.innerHTML = "Saskatchewan (Coming Soon)";
    document.querySelector(".sask").addEventListener("mouseout", function(){
        province.innerHTML = "Select A Province";
    });
}); // End Saskatchewan Hover Tile Changer

document.querySelector(".manitoba").addEventListener("mouseover", function(){
    province.innerHTML = "Manitoba (Coming Soon)";
    document.querySelector(".manitoba").addEventListener("mouseout", function(){
        province.innerHTML = "Select A Province";
    });
}); // End Manitoba Hover Tile Changer

//Mobile Map Slideshow
let images = ["img/bc.svg", "img/alberta.svg", "img/saskatchewan.svg", "img/manitoba.svg"];
let currentImg = 0;

document.querySelector(".next").addEventListener("click", function(){
    if (currentImg < images.length - 1) {
        currentImg += 1;
    } else {
        currentImg = 0;
    }
    document.querySelector(".holder-mobile>div>img").src = images[currentImg];

    if(currentImg == 0){
        document.querySelector(".mobile-local-button").href = "local-bc.html";
        document.querySelector(".mobile-provice-name").innerHTML = "British Columbia";
    } else if (currentImg == 1){
        document.querySelector(".mobile-local-button").href = "local-alberta.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Alberta";
    } else if (currentImg == 2){
        document.querySelector(".mobile-local-button").href = "local-sask.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Saskatchewan";
    } else {
        document.querySelector(".mobile-local-button").href = "local-manitoba.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Manitoba";
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
        document.querySelector(".mobile-local-button").href = "local-bc.html";
        document.querySelector(".mobile-provice-name").innerHTML = "British Columbia";
    } else if (currentImg == 1){
        document.querySelector(".mobile-local-button").href = "local-alberta.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Alberta";
    } else if (currentImg == 2){
        document.querySelector(".mobile-local-button").href = "local-sask.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Saskatchewan";
    } else {
        document.querySelector(".mobile-local-button").href = "local-manitoba.html";
        document.querySelector(".mobile-provice-name").innerHTML = "Manitoba";
    }
})
