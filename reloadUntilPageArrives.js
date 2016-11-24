// ==UserScript==
// @name         Reload Until Page Arrives
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.coursehero.com/tutors-problems*
// @grant        none
// ==/UserScript==

window.addEventListener('load', function() {
    function reloadUntilPageArrives() {
        window.location.reload();
    }

    if ( document.title == "Page missing! | Course Hero" ) {
        reloadUntilPageArrives();
    }
});
