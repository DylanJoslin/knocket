let school = document.querySelector(".school-icon-main");
let treaty = document.querySelector(".treaty-icon-main");
let Majorville = document.querySelector(".majorville-icon-main");
let LacSteAnne = document.querySelector(".lacsteanne-icon-main");
let headsmashed = document.querySelector(".headsmashed-icon-main");
let ribstones = document.querySelector(".ribstones-icon-main");
let writingstone = document.querySelector(".writingstone-icon-main");
let medicinelake  = document.querySelector(".medicinelake-icon-main");

let contentHolderAmiskwaciy = document.querySelector(".amiskwaciy-content");
let contentHolderTreaty = document.querySelector(".treaty-content");
let contentHolderMajorville = document.querySelector(".extra-content-majorville");
let contentHolderLacsteanne = document.querySelector(".extra-content-lacsteanne");
let contentHolderHeadsmashed = document.querySelector(".extra-content-headsmashed");
let contentHolderRibstones = document.querySelector(".extra-content-ribstones");
let contentHolderWritingstone = document.querySelector(".extra-content-writingstone");
let contentHolderMedicinelake = document.querySelector(".extra-content-medicinelake");

let titleSwapper = document.querySelector(".focus-title");

school.addEventListener("click", function(){
    if(contentHolderAmiskwaciy.classList.contains('hidden')){
        contentHolderAmiskwaciy.classList.remove('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "amiskwaciy Academy";
    }
});

treaty.addEventListener("click", function(){
    if(contentHolderTreaty.classList.contains('hidden')){
        contentHolderTreaty.classList.remove('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Treaty 6";
    }
});

Majorville.addEventListener("click", function(){
    if(contentHolderMajorville.classList.contains('hidden')){
        contentHolderMajorville.classList.remove('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Majorville Cairn and Medicine Wheel";
    }
});

LacSteAnne.addEventListener("click", function(){
    if(contentHolderLacsteanne.classList.contains('hidden')){
        contentHolderLacsteanne.classList.remove('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Lac Ste. Anne";
    }
});

headsmashed.addEventListener("click", function(){
    if(contentHolderHeadsmashed.classList.contains('hidden')){
        contentHolderHeadsmashed.classList.remove('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Head Smashed in Buffalo Jump";
    }
});

ribstones.addEventListener("click", function(){
    if(contentHolderHeadsmashed.classList.contains('hidden')){
        contentHolderRibstones.classList.remove('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Viking Ribstones";
    }
});

writingstone.addEventListener("click", function(){
    if(contentHolderWritingstone.classList.contains('hidden')){
        contentHolderWritingstone.classList.remove('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        contentHolderMedicinelake.classList.add('hidden');
        titleSwapper.textContent = "Writing-On-Stone";
    }
});

medicinelake.addEventListener("click", function(){
    if(contentHolderMedicinelake.classList.contains('hidden')){
        contentHolderMedicinelake.classList.remove('hidden');
        contentHolderWritingstone.classList.add('hidden');
        contentHolderRibstones.classList.add('hidden');
        contentHolderHeadsmashed.classList.add('hidden');
        contentHolderLacsteanne.classList.add('hidden');
        contentHolderMajorville.classList.add('hidden');
        contentHolderTreaty.classList.add('hidden');
        contentHolderAmiskwaciy.classList.add('hidden');
        titleSwapper.textContent = "Medicine Lake";
    }
});