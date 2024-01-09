var tabLinks = document.getElementsByClassName("tab-links");
var tabContents = document.getElementsByClassName("tab-contents");

function opentab(contentName, title){
    for(link of tabLinks){
        link.classList.remove("active-link");
    }
    for(content of tabContents){
        content.classList.remove("active-tab");
    }
    document.getElementById(title).classList.add("active-link");
    document.getElementById(contentName).classList.add("active-tab");
}