/**
 * This function switches between tabs in the 'About Me' section.
 */
function opentab(contentName, title){
    /* Define variables */
    var tabLinks = document.getElementsByClassName("tab-links");
    var tabContents = document.getElementsByClassName("tab-contents");

    /* Loop through tab-links to remove any 'active-link' from class names */
    for(link of tabLinks){
        link.classList.remove("active-link");
    }
    /* Same thing but remove 'active-tab' from tab-contents' class names */
    for(content of tabContents){
        content.classList.remove("active-tab");
    }

    /* Add 'active-link' and 'active-tab' to the class names of the active tab */
    document.getElementById(title).classList.add("active-link");
    document.getElementById(contentName).classList.add("active-tab");
}