/**
 * script.js - Orquestación de lógica Frontend
 * Refinado V3: Performance + Equilibrio UX
 */

document.addEventListener('DOMContentLoaded', () => {

    // 1. Inicialización de Lucide Icons
    lucide.createIcons();

    // 2. Inicialización de AOS (Animate on Scroll)
    // Refinado: animaciones más breves y sutiles para no molestar la lectura.
    AOS.init({
        once: true,           
        offset: 30,           
        duration: 500,        // Rapidez: animaciones más breves (antes 800)
        easing: 'ease-out-quad' // Curva de aceleración limpia y predecible
    });

    // 3. Inicialización de Vanilla Tilt
    // Refinado: Solo se activa en monitores grandes. Se reduce la inclinación radicalmente.
    const tiltElements = document.querySelectorAll("[data-tilt]");
    if (tiltElements.length > 0 && window.innerWidth > 768) {
        VanillaTilt.init(tiltElements, {
            max: 5,               // Inclinación muy sutil, transmite elegancia
            speed: 600,           // Retorno suave
            glare: true,          
            "max-glare": 0.05     // Brillo apenas perceptible
        });
    }

    // 4. Inicialización de tsParticles
    // Refinado: Límite a 30fps, anulación de retina. Menos partículas, más lentas.
    tsParticles.load({
        id: "tsparticles",
        options: {
            fpsLimit: 30, // Ahorro tajante de recursos
            particles: {
                color: {
                    value: ["#ff6b35", "#e23e3e"] 
                },
                links: {
                    enable: false 
                },
                move: {
                    enable: true,
                    speed: { min: 0.1, max: 0.5 }, // Movimiento hiper-sutil ambiental
                    direction: "top", 
                    outModes: {
                        default: "out"
                    }
                },
                number: {
                    density: {
                        enable: true,             
                        width: 800,
                        height: 800
                    },
                    value: 15                     // Reducción del 60% en cantidad de partículas
                },
                opacity: {
                    value: { min: 0.05, max: 0.15 } // Extra-opacas para evitar robos de foco
                },
                shape: {
                    type: "circle"                
                },
                size: {
                    value: { min: 1, max: 2 }     // Tamaños mínimos
                }
            },
            detectRetina: false // Apagado intencional: libera tarjeta de video en móviles modernos
        }
    });

});
