let school = document.querySelector(".school-icon-main");
let treaty = document.querySelector(".treaty-icon-main");
let contentHolderAmiskwaciy = document.querySelector(".amiskwaciy-content");
let contentHolderTreaty = document.querySelector(".treaty-content");
let titleSwapper = document.querySelector(".focus-title");

school.addEventListener("mouseover", function(){
    if(contentHolderAmiskwaciy.classList.contains('hidden')){
        contentHolderAmiskwaciy.classList.toggle('hidden');
        contentHolderTreaty.classList.toggle('hidden');
        titleSwapper.textContent = "Amiskwaciy Academy";
    }
});

treaty.addEventListener("mouseover", function(){
    if(contentHolderTreaty.classList.contains('hidden')){
        contentHolderTreaty.classList.toggle('hidden');
        contentHolderAmiskwaciy.classList.toggle('hidden');
        titleSwapper.textContent = "Treaty 6";
    }
});