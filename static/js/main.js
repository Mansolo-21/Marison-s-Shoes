window.addEventListener("load", () => {
    const card = document.getElementById("card");

    // fade in
    setTimeout(() => {
        card.classList.add("show");
    }, 200);

    // subtle mouse movement effect
    document.addEventListener("mousemove", (e) => {
        let x = (window.innerWidth / 2 - e.pageX) / 30;
        let y = (window.innerHeight / 2 - e.pageY) / 30;

        card.style.transform = `translate(${x}px, ${y}px)`;
    });
});

// Auto-hide after 7 seconds
setTimeout(() => {

    const container =
        document.getElementById(
            "messages-container"
        );

    if(container){

        container.style.transition =
            "opacity .5s ease";

        container.style.opacity = "0";

        setTimeout(() => {
            container.remove();
        }, 500);
    }

}, 7000);


// Close when X is clicked
document.querySelectorAll(
    ".close-message"
).forEach(button => {

    button.addEventListener(
        "click",
        function(){

            const message =
                this.closest(".message");

            message.style.transition =
                "opacity .3s ease";

            message.style.opacity = "0";

            setTimeout(() => {
                message.remove();
            }, 300);
        }
    );

});