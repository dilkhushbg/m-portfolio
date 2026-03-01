document.addEventListener("DOMContentLoaded", () => {
    // GSAP Navbar Animation
    gsap.from(".navbar", {
        y: -100,
        opacity: 0,
        duration: 1,
        ease: "power3.out"
    });

    // GSAP Nav Links Iteration
    gsap.from(".nav-links li", {
        y: -20,
        opacity: 0,
        duration: 0.8,
        stagger: 0.1,
        delay: 0.5,
        ease: "power3.out"
    });

    // GSAP Footer Animation
    const footerCtx = gsap.context(() => {
        gsap.from("footer .footer-content", {
            scrollTrigger: {
                trigger: "footer",
                start: "top bottom",
            },
            y: 50,
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });
});
