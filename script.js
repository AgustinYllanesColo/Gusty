/**
 * script.js — V7 Performance Optimized
 * Stripped to essentials: Icons + AOS + Tilt (no glare)
 * Removed: tsParticles (15 dots at 30fps = wasted GPU cycles)
 */

document.addEventListener('DOMContentLoaded', () => {

    // 1. Lucide Icons
    lucide.createIcons();

    // 2. AOS — fast, once-only animations
    AOS.init({
        once: true,
        offset: 30,
        duration: 400,
        easing: 'ease-out'
    });

    // 3. Vanilla Tilt — desktop only, no glare (glare = extra <canvas> per card)
    const tiltElements = document.querySelectorAll("[data-tilt]");
    if (tiltElements.length > 0 && window.innerWidth > 900) {
        VanillaTilt.init(tiltElements, {
            max: 4,
            speed: 500,
            glare: false
        });
    }

    // tsParticles disabled — ambient glows provide sufficient atmosphere
    // The canvas engine was consuming GPU for 15 near-invisible dots

});
