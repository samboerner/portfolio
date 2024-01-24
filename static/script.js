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

/**
 * These functions open and close the side menu on smaller screens;
 */
var menu = document.getElementById("menu");

function openmenu(){
    menu.style.right = "0";
}
function closemenu(){
    menu.style.right = "-200px";
}

/**
 *  The following code handles the contact form submission
 *  posting to the flask app.
 */
var form = document.getElementById("contact-form");
var msg = document.getElementById("msg");

function submitForm(event) {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/',
        data: $('form').serialize(),
        success: function() {
           $('#name').val('');
           $('#email').val('');
           $('#message').val('');
           msg.innerHTML = "Your message has been sent!";
            setTimeout(function(){
                msg.innerHTML = ""
            }, 5000);
            form.reset();
        }
    });
}

form.addEventListener('submit', submitForm);
