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