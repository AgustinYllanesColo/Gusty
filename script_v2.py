import os

index_html_v2 = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reparación de Termotanques, Calefones y Calderas 24hs | Urgencias</title>
    <meta name="description" content="Hoy mismo volvés a tener agua caliente o calefacción. Servicio técnico 24h. Respuesta inmediata en tu zona.">
    <meta name="theme-color" content="#1e3a8a">
    <meta name="keywords" content="reparación de termotanques, gasista urgente, calefones urgencia, calderas, 24 horas, servicio tecnico urgente">
    
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body>

    <!-- BOTONES FLOTANTES SIEMPRE VISIBLES (STICKY CONTACT) -->
    <div class="floating-controls">
        <a href="https://wa.me/5491141731384?text=Hola%2C%20necesito%20un%20t%C3%A9cnico%20hoy" class="floating-wa cro-wa" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp urgente">
            <i data-lucide="message-circle" class="wa-icon"></i>
        </a>
    </div>

    <!-- NAVEGACIÓN MOBILE MINIMALISTA STICKY (OBLIGATORIO) -->
    <nav class="mobile-nav">
        <div class="logo-text">Servicio<strong>Urgente</strong></div>
        <a href="tel:5491141731384" class="nav-call pulse-anim-light"><i data-lucide="phone-call"></i> Llamar Ahora</a>
    </nav>

    <main class="content-wrapper">
        
        <!-- 1. HERO REDISEÑADO CRO V2 (RESULTADO INMEDIATO) -->
        <header class="hero cro-hero" id="inicio">
            <div class="hero-content cro-hero-content">
                <div class="badge-urgency cro-badge" data-aos="fade-up">
                    <span class="pulse-dot"></span> 🟢 ATENDIENDO AHORA EN CABA Y GBA
                </div>
                
                <h1 data-aos="fade-up" data-aos-delay="50">
                    Hoy mismo volvés a tener agua caliente o calefacción.
                </h1>
                
                <p class="hero-subtitle cro-subtitle" data-aos="fade-up" data-aos-delay="100">
                    Técnico disponible en tu zona ahora. Reparación de termotanques y calderas sin retirar el equipo.
                </p>
                
                <div class="cro-actions" data-aos="fade-up" data-aos-delay="150">
                    <a href="https://wa.me/5491141731384?text=Hola%20tengo%20una%20urgencia" class="btn-primary" target="_blank" rel="noopener noreferrer">
                        <i data-lucide="message-circle" class="icon-btn-hero"></i>
                        <div class="btn-content">
                            <span class="btn-title">ESCRIBÍ POR WHATSAPP</span>
                            <span class="btn-microcopy">Respondemos en 2 minutos</span>
                        </div>
                    </a>
                    <a href="tel:5491141731384" class="btn-secondary">
                        <i data-lucide="phone" class="icon-btn-hero"></i>
                        <div class="btn-content">
                            <span class="btn-title">O LLAMAR AL TÉCNICO</span>
                            <span class="btn-microcopy">Línea de emergencia prioritaria</span>
                        </div>
                    </a>
                </div>
                
                <!-- MICRO FAQs ADIÓS FAQs LARGAS -->
                <div class="micro-faqs" data-aos="fade-up" data-aos-delay="200">
                    <div class="mfaq-item"><i data-lucide="clock"></i> <span>¿Vienen hoy? <strong>Sí, guardia 24hs.</strong></span></div>
                    <div class="mfaq-item"><i data-lucide="shield-check"></i> <span>¿Tiene garantía? <strong>Sí, por escrito.</strong></span></div>
                </div>
            </div>
        </header>

        <!-- 2. BLOQUE URGENCIA INMEDIATA CREÍBLE -->
        <section class="urgency-block" data-aos="fade-up" data-aos-delay="50">
            <div class="urgency-container">
                <div class="urgency-left">
                    <h3>Estamos atendiendo en tu zona en este momento.</h3>
                    <p>Últimos turnos de urgencia disponibles para HOY.</p>
                </div>
                <div class="urgency-right">
                    <a href="https://wa.me/5491141731384" class="btn-alert pulse-anim" target="_blank">RESERVAR MI TURNO</a>
                </div>
            </div>
        </section>

        <!-- 3. SERVICIOS (Solución sin tecnicismos) -->
        <section class="services cro-services" id="soluciones">
            <div class="services-grid-fast">
                
                <article class="service-card cro-card" data-aos="fade-up" data-aos-delay="50">
                    <div class="card-header">
                        <i data-lucide="droplet" class="icon-accent cro-icon"></i>
                        <h3>Reparación de Termotanques y Calefones</h3>
                    </div>
                    <p>Te devolvemos el agua caliente hoy. Arreglamos fugas y falta de encendido in-situ en la primera visita.</p>
                </article>
                
                <article class="service-card cro-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="card-header">
                        <i data-lucide="thermometer" class="icon-accent cro-icon"></i>
                        <h3>Arreglo de Calderas Duales</h3>
                    </div>
                    <p>Restablecimiento de presión y temperatura en el día. Solucionamos radiadores fríos y fallas de quemador.</p>
                </article>

                <article class="service-card cro-card cro-highlight" data-aos="fade-up" data-aos-delay="150">
                    <div class="card-header">
                        <i data-lucide="award" class="icon-accent cro-icon-white"></i>
                        <h3 class="white-text">+1,200 Equipos Recuperados</h3>
                    </div>
                    <p class="white-text glow-text">Más de una década resolviendo urgencias con matriculados oficiales certificados.</p>
                </article>

            </div>
        </section>

        <!-- 4. SOCIAL PROOF (Chat real + Zonas) -->
        <section class="testimonials-chat" id="experiencias">
            <div class="chat-grid">
                <div class="chat-bubble left" data-aos="fade-up" data-aos-delay="50">
                    <div class="chat-stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Me solucionaron todo en el día. Vinieron a la hora de haber llamado y no se llevaron el equipo. Muy profesionales."</p>
                    <span class="chat-author">- Javier A. (Lomas de Zamora)</span>
                </div>

                <div class="chat-bubble right" data-aos="fade-up" data-aos-delay="100">
                    <div class="chat-stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Rápidos y limpios. Cambiaron la pieza de la caldera en el momento sin cobrar locuras. Volvió la calefacción rápido."</p>
                    <span class="chat-author">- Florencia G. (CABA)</span>
                </div>
            </div>
        </section>

        <!-- 5. BENEFICIOS CLAVE (Micro-respuestas) -->
        <section class="benefits-checklist">
            <div class="checklist-grid">
                <div class="check-item-cro" data-aos="fade-up" data-aos-delay="50">
                    <div class="icon-box-cro"><i data-lucide="zap"></i></div>
                    <div class="check-text-cro">
                        <h3>Llegamos en minutos</h3>
                        <p>Taller móvil equipado para zona Sur, CABA y Oeste.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="fade-up" data-aos-delay="100">
                    <div class="icon-box-cro"><i data-lucide="clock"></i></div>
                    <div class="check-text-cro">
                        <h3>Atención 24hs Real</h3>
                        <p>Sí, fines de semana y madrugadas feriados incluidos.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="fade-up" data-aos-delay="150">
                    <div class="icon-box-cro"><i data-lucide="user-check"></i></div>
                    <div class="check-text-cro">
                        <h3>Técnicos Matriculados</h3>
                        <p>Diagnóstico exacto y reparación en la primer visita.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="fade-up" data-aos-delay="200">
                    <div class="icon-box-cro"><i data-lucide="award"></i></div>
                    <div class="check-text-cro">
                        <h3>Garantía Escrita</h3>
                        <p>Cubre 100% mano de obra y repuestos instalados.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. PROCESO VISUAL MÍNIMO (1, 2, 3) -->
        <section class="visual-process" id="proceso">
            <div class="section-header cro-header-center" data-aos="fade-up">
                <h2 class="section-title">Contratar es así de simple</h2>
            </div>
            
            <div class="process-steps">
                <div class="step-cro" data-aos="fade-up" data-aos-delay="50">
                    <div class="step-num-cro">1</div>
                    <div class="step-info-cro">
                        <h3>Escribís</h3>
                        <p>Nos mandás WhatsApp en un click.</p>
                    </div>
                </div>
                <div class="step-cro" data-aos="fade-up" data-aos-delay="100">
                    <div class="step-num-cro">2</div>
                    <div class="step-info-cro">
                        <h3>Viajamos</h3>
                        <p>El técnico más cercano llega a tu domicilio.</p>
                    </div>
                </div>
                <div class="step-cro" data-aos="fade-up" data-aos-delay="150">
                    <div class="step-num-cro">3</div>
                    <div class="step-info-cro">
                        <h3>Funciona</h3>
                        <p>Reparación en el acto. Todo resuelto.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. CTA DE ÚLTIMO ESFUERZO (AGRESIVO) -->
        <section class="cta-final-cro" id="contacto" data-aos="fade-up">
            <div class="cta-wrapper">
                <h2 class="cta-headline">No pagues una fortuna mañana por dejarlo gotear hoy.</h2>
                <p class="cta-sub">Resolvelo rápido. Un técnico puede estar en camino a tu casa ahora mismo.</p>
                <div class="cro-actions end-actions">
                    <a href="https://wa.me/5491141731384" class="btn-primary btn-huge pulse-anim" target="_blank">
                        QUIERO SOLUCIONARLO HOY
                    </a>
                    <a href="tel:5491141731384" class="btn-outline-white btn-huge">
                        <i data-lucide="phone"></i> HACER LLAMADA URGENTE
                    </a>
                </div>
            </div>
        </section>

    </main>
    
    <footer>
        <p>&copy; 2026 Servicio Técnico Urgencias a Domicilio.</p>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>
        lucide.createIcons();
        /* REGLA CRITICA: Animaciones orientadas a conversión (200-400ms, escalonado, fade-up) */
        AOS.init({
            once: true, 
            offset: 20, 
            duration: 300, /* Obligatorio: < 400ms */
            easing: 'ease-out'
        });
    </script>
</body>
</html>"""

with open(r"c:\Users\Usuario\OneDrive\Desktop\rbrb\index.html", "w", encoding="utf-8") as f:
    f.write(index_html_v2)

css_append_content_v2 = """
/* ==========================================================================
   AGREGADOS CRO REDESIGN V2 (Micro-FAQs y Confianza)
   ========================================================================== */
.pulse-anim-light { animation: breathing 4.5s ease-in-out infinite; }
.micro-faqs {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 1.5rem;
    font-size: 0.95rem;
    color: var(--text-secondary);
}
.mfaq-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.mfaq-item i { width: 18px; height: 18px; color: var(--trust-blue); }
.mfaq-item strong { color: var(--text-heading); }

.cro-highlight {
    background: var(--trust-blue);
    border: none;
    color: white;
}
.white-text { color: white !important; }
.glow-text { color: rgba(255,255,255,0.85); }
.cro-icon-white { color: #f59e0b; }
"""

with open(r"c:\Users\Usuario\OneDrive\Desktop\rbrb\styles.css", "a", encoding="utf-8") as f:
    f.write(css_append_content_v2)

print("V2 HTML y CSS procesado para Conversión Extrema.")
