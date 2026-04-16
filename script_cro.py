import os

index_html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reparación de Termotanques, Calefones y Calderas 24hs | Urgencias</title>
    <meta name="description" content="Servicio técnico 24h. Reparación urgente de termotanques, calefones y calderas. Atención inmediata en tu zona.">
    <meta name="theme-color" content="#1e3a8a">
    <meta name="keywords" content="reparación de termotanques, gasista urgente, calefones urgencia, calderas, 24 horas, servicio tecnico urgente">
    
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body>

    <!-- BOTONES FLOTANTES SIEMPRE VISIBLES -->
    <div class="floating-controls">
        <a href="https://wa.me/5491141731384?text=Hola%2C%20tengo%20una%20urgencia%20con%20el%20termotanque%2Fcalef%C3%B3n%2Fcaldera%2C%20%C2%BFpueden%20venir%20hoy%3F" class="floating-wa cro-wa" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp urgente">
            <i data-lucide="message-circle" class="wa-icon"></i>
        </a>
    </div>

    <!-- NAVEGACIÓN MOBILE MINIMALISTA -->
    <nav class="mobile-nav">
        <div class="logo-text">Servicio<strong>Técnico</strong></div>
        <a href="tel:5491141731384" class="nav-call"><i data-lucide="phone-call"></i> Llamar Directo</a>
    </nav>

    <main class="content-wrapper">
        
        <!-- 1. HERO REDISEÑADO CRO -->
        <header class="hero cro-hero" id="inicio">
            <div class="hero-content cro-hero-content">
                <div class="badge-urgency cro-badge" data-aos="fade-down" data-aos-duration="400">
                    <span class="pulse-dot"></span> 🚨 ATENCIÓN INMEDIATA • TÉCNICOS EN ESPERA
                </div>
                
                <h1 data-aos="fade-down" data-aos-duration="400" data-aos-delay="100">
                    ¿Sin agua o sin calefacción?<br>Te lo solucionamos HOY.
                </h1>
                
                <p class="hero-subtitle cro-subtitle" data-aos="fade-up" data-aos-duration="400" data-aos-delay="200">
                    Servicio técnico 24h. Respuesta rápida a tu domicilio en el día para termotanques, calefones y calderas.
                </p>
                
                <div class="cro-actions" data-aos="fade-up" data-aos-duration="400" data-aos-delay="300">
                    <a href="https://wa.me/5491141731384?text=Hola%20tengo%20una%20urgencia" class="btn-primary" target="_blank" rel="noopener noreferrer">
                        <i data-lucide="message-circle" class="icon-btn-hero"></i>
                        <div class="btn-content">
                            <span class="btn-title">ESCRIBÍ POR WHATSAPP AHORA</span>
                            <span class="btn-microcopy">En 5 min te respondemos</span>
                        </div>
                    </a>
                    <a href="tel:5491141731384" class="btn-secondary">
                        <i data-lucide="phone" class="icon-btn-hero"></i>
                        <div class="btn-content">
                            <span class="btn-title">O LLAMAR POR TELÉFONO</span>
                            <span class="btn-microcopy">Línea de emergencia prioritaria</span>
                        </div>
                    </a>
                </div>
                
                <div class="trust-indicators cro-trust" data-aos="fade-up" data-aos-duration="400" data-aos-delay="400">
                    <div class="trust-item"><i data-lucide="check-circle-2"></i> Técnicos matriculados</div>
                    <div class="trust-item"><i data-lucide="check-circle-2"></i> Llegamos rápido</div>
                    <div class="trust-item"><i data-lucide="check-circle-2"></i> Garantía Escrita</div>
                </div>
            </div>
        </header>

        <!-- 2. BLOQUE URGENCIA INMEDIATA -->
        <section class="urgency-block" data-aos="fade" data-aos-duration="300">
            <div class="urgency-container">
                <div class="urgency-left">
                    <h3>Estamos trabajando en tu zona ahora mismo.</h3>
                    <p>Últimos turnos de urgencia disponibles para HOY.</p>
                </div>
                <div class="urgency-right">
                    <a href="https://wa.me/5491141731384" class="btn-alert pulse-anim" target="_blank">Reservar Turno de Urgencia</a>
                </div>
            </div>
        </section>

        <!-- 3. SERVICIOS (Solución Rápida) -->
        <section class="services cro-services" id="soluciones">
            <div class="services-grid-fast">
                
                <article class="service-card cro-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="card-header">
                        <i data-lucide="wrench" class="icon-accent cro-icon"></i>
                        <h3>Reparación de Termotanques y Calefones</h3>
                    </div>
                    <p>Resolvemos fugas de agua, fallas de encendido o quemadores tapados sin retirar el equipo. Todo solucionado in-situ.</p>
                </article>
                
                <article class="service-card cro-card" data-aos="fade-up" data-aos-delay="200">
                    <div class="card-header">
                        <i data-lucide="thermometer" class="icon-accent cro-icon"></i>
                        <h3>Arreglo de Calderas Duales</h3>
                    </div>
                    <p>Purga de radiadores, tableros bloqueados y reestablecimiento integral de presión de agua caliente en pocas horas.</p>
                </article>

                <article class="service-card cro-card" data-aos="fade-up" data-aos-delay="300">
                    <div class="card-header">
                        <i data-lucide="shield-alert" class="icon-accent cro-icon"></i>
                        <h3>Mantenimiento Técnico</h3>
                    </div>
                    <p>Prevención de urgencias para evitar roturas costosas en invierno o fugas de gas peligrosas (CO) de inmediato.</p>
                </article>

            </div>
        </section>

        <!-- 4. SOCIAL PROOF RÁPIDA -->
        <section class="testimonials-chat" id="experiencias">
            <div class="chat-grid">
                <div class="chat-bubble left" data-aos="fade-right" data-aos-delay="100">
                    <div class="chat-stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Se me rompió el calefón un domingo nublado a las 8 AM. Llegaron en menos de 1 hora y frenaron la pérdida. Excelente trabajo."</p>
                    <span class="chat-author">- Javier A.</span>
                </div>

                <div class="chat-bubble right" data-aos="fade-left" data-aos-delay="200">
                    <div class="chat-stars"><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i><i data-lucide="star"></i></div>
                    <p>"Rápidos y limpios. Cambiaron el termostato de la caldera en el acto, sin dar mil vueltas ni llevarse nada al taller. Recomendados."</p>
                    <span class="chat-author">- Florencia G.</span>
                </div>
            </div>
        </section>

        <!-- 5. BENEFICIOS CLAVE -->
        <section class="benefits-checklist">
            <div class="checklist-grid">
                <div class="check-item-cro" data-aos="zoom-in" data-aos-delay="100">
                    <div class="icon-box-cro"><i data-lucide="zap"></i></div>
                    <div class="check-text-cro">
                        <h3>Llegamos Rápidismo</h3>
                        <p>Taller móvil equipado.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="zoom-in" data-aos-delay="200">
                    <div class="icon-box-cro"><i data-lucide="clock"></i></div>
                    <div class="check-text-cro">
                        <h3>Guardia 24hs Real</h3>
                        <p>Feriados y madrugadas incluidos.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="zoom-in" data-aos-delay="300">
                    <div class="icon-box-cro"><i data-lucide="user-check"></i></div>
                    <div class="check-text-cro">
                        <h3>Técnicos Matriculados</h3>
                        <p>No improvisamos, oficio puro.</p>
                    </div>
                </div>
                <div class="check-item-cro" data-aos="zoom-in" data-aos-delay="400">
                    <div class="icon-box-cro"><i data-lucide="award"></i></div>
                    <div class="check-text-cro">
                        <h3>Garantía Legal Escrita</h3>
                        <p>Cobertura oficial asegurada.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. PROCESO SIMPLE 3 PASOS -->
        <section class="visual-process" id="proceso">
            <div class="section-header cro-header-center" data-aos="fade-up">
                <h2 class="section-title">Solución en este orden</h2>
            </div>
            
            <div class="process-steps">
                <div class="step-cro" data-aos="fade-up" data-aos-delay="100">
                    <div class="step-num-cro">1</div>
                    <div class="step-info-cro">
                        <h3>Escribís o Llamás</h3>
                        <p>Contanos el síntoma, respondemos al instante.</p>
                    </div>
                </div>
                <div class="step-cro" data-aos="fade-up" data-aos-delay="200">
                    <div class="step-num-cro">2</div>
                    <div class="step-info-cro">
                        <h3>Diagnóstico a Domicilio</h3>
                        <p>El técnico revisa e informa el exacto presupuesto.</p>
                    </div>
                </div>
                <div class="step-cro" data-aos="fade-up" data-aos-delay="300">
                    <div class="step-num-cro">3</div>
                    <div class="step-info-cro">
                        <h3>Solución in-situ</h3>
                        <p>Arreglamos el equipo frente a ti. Vuelve el confort.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. CTA FINAL AGRESIVO -->
        <section class="cta-final-cro" id="contacto">
            <div class="cta-wrapper" data-aos="fade-up">
                <h2 class="cta-headline">No dejes que algo chico sea un desastre mayor.</h2>
                <p class="cta-sub">Resolverlo hoy es infinitamente más barato que esperar a mañana. Frená la pérdida.</p>
                <div class="cro-actions end-actions">
                    <a href="https://wa.me/5491141731384" class="btn-primary btn-huge pulse-anim" target="_blank">
                        QUIERO QUE VENGAN HOY MISMO
                    </a>
                    <a href="tel:5491141731384" class="btn-outline-white btn-huge">
                        <i data-lucide="phone"></i> O HACER LLAMADA URGENTE
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
        AOS.init({
            once: true, 
            offset: 20, 
            duration: 350,
            easing: 'ease-out-cubic'
        });
    </script>
</body>
</html>"""

with open(r"c:\Users\Usuario\OneDrive\Desktop\rbrb\index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content)

css_append_content = """
/* ==========================================================================
   AGREGADOS CRO REDESIGN V7.3 
   Optimizaciones Mobile-First y Urgencia Visual
   ========================================================================== */

:root {
   --trust-blue: #1e3a8a;
   --trust-blue-dark: #172554;
   --urgency-red: #e63946;
   --urgency-orange: #f97316;
}

/* 0. Nav Mobile */
.mobile-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.25rem;
    background: #ffffff;
    border-bottom: 1px solid var(--border-subtle);
    position: sticky;
    top: 0;
    z-index: 999;
}
.mobile-nav .logo-text { font-size: 1.2rem; color: #111; }
.mobile-nav .nav-call {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--trust-blue);
    font-weight: 800;
    font-size: 0.95rem;
}
@media (min-width: 900px) {
    .mobile-nav { display: none; }
}

/* 1. HERO CRO */
.cro-hero { padding-top: 4rem; padding-bottom: 4rem; }
.cro-hero-content {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.cro-badge { background: rgba(230, 57, 70, 0.1); color: var(--urgency-red); border-color: rgba(230, 57, 70, 0.2); }
.cro-subtitle { text-align: center; border: none; padding: 0; margin-bottom: 2rem; }

.cro-actions {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    margin-bottom: 2.5rem;
}
@media (min-width: 900px) {
    .cro-actions { flex-direction: row; justify-content: center; }
}

/* Botones CRO Genéricos */
.btn-primary, .btn-secondary, .btn-outline-white {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    padding: 1.2rem;
    border-radius: var(--radius-pill);
    font-weight: 800;
    text-align: left;
    transition: transform 0.2s, box-shadow 0.2s;
    width: 100%;
}
@media (min-width: 900px) {
    .btn-primary, .btn-secondary, .btn-outline-white { width: auto; padding: 1.2rem 2.5rem; }
}
.btn-primary {
    background: var(--whatsapp-green);
    color: #ffffff;
    box-shadow: 0 10px 24px rgba(37, 211, 102, 0.3);
    border: none;
}
.btn-secondary {
    background: transparent;
    color: var(--text-heading);
    border: 2px solid var(--border-subtle);
}
.btn-outline-white {
    background: transparent;
    color: #ffffff;
    border: 2px solid rgba(255,255,255,0.7);
}
.btn-primary .btn-microcopy { color: rgba(255,255,255,0.9); }
.btn-secondary .btn-microcopy { color: var(--text-secondary); }

.btn-huge { padding: 1.4rem; font-size: 1.1rem; }

.cro-trust { justify-content: center; border-top: 1px solid var(--border-subtle); padding-top: 2rem; width: 100%; }

/* 2. BLOQUE URGENCIA */
.urgency-block {
    background: var(--trust-blue);
    padding: 3.5rem 1.5rem;
    width: 100%;
}
.urgency-container {
    max-width: 1280px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    align-items: center;
    text-align: center;
}
@media (min-width: 900px) {
    .urgency-container { flex-direction: row; justify-content: space-between; text-align: left; }
}
.urgency-left h3 { color: #ffffff; font-size: 1.6rem; font-weight: 800; margin-bottom: 0.5rem; }
.urgency-left p { color: rgba(255,255,255,0.8); font-size: 1.1rem; }
.btn-alert {
    background: var(--urgency-red);
    color: #ffffff;
    padding: 1.2rem 2.5rem;
    border-radius: var(--radius-pill);
    font-weight: 800;
    text-transform: uppercase;
    display: inline-block;
    box-shadow: 0 8px 24px rgba(230, 57, 70, 0.4);
    transition: transform 0.2s;
}

/* 3. SERVICIOS CONDENSADOS */
.cro-services { padding-top: 5rem; padding-bottom: 5rem; }
.services-grid-fast {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    width: 100%;
}
.cro-card {
    padding: 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.card-header { display: flex; align-items: center; gap: 1rem; }
.card-header h3 { margin: 0; font-size: 1.2rem; }
.cro-icon { margin: 0; width: 32px; height: 32px; color: var(--trust-blue); }

/* 4. CHAT TESTIMONIALS */
.testimonials-chat { padding: 4rem 1.5rem; align-items: center; background: #f0f2f5; }
.chat-grid {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    max-width: 800px;
    width: 100%;
    margin: 0 auto;
}
.chat-bubble {
    background: #ffffff;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: var(--shadow-card);
    width: 90%;
    position: relative;
    border: 1px solid var(--border-subtle);
}
.chat-bubble.left { border-bottom-left-radius: 2px; align-self: flex-start; }
.chat-bubble.right { border-bottom-right-radius: 2px; align-self: flex-end; background: #f8fafc; }
.chat-stars { display: flex; gap: 0.2rem; color: #f59e0b; margin-bottom: 0.8rem; }
.chat-stars svg { width: 16px; height: 16px; fill: #f59e0b; }
.chat-bubble p { color: var(--text-primary); font-size: 1.05rem; line-height: 1.6; font-style: italic; }
.chat-author { display: block; margin-top: 1rem; font-weight: 700; color: var(--text-secondary); font-size: 0.9rem; }

/* 5. BENEFITS GRID CHECKLIST */
.benefits-checklist { padding: 4rem 1.5rem; }
.checklist-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem 1rem;
    max-width: 1280px;
    margin: 0 auto;
}
@media (max-width: 600px) {
    .checklist-grid { grid-template-columns: 1fr; gap: 1.5rem; }
}
.check-item-cro { display: flex; align-items: center; gap: 1.2rem; }
.icon-box-cro {
    background: rgba(30,58,138,0.1);
    color: var(--trust-blue);
    padding: 1rem;
    border-radius: 12px;
    flex-shrink: 0;
}
.check-text-cro h3 { font-size: 1.15rem; font-weight: 800; margin-bottom: 0.2rem; color: var(--text-heading); }
.check-text-cro p { font-size: 0.95rem; color: var(--text-secondary); }

/* 6. PROCESO 3 PASOS */
.visual-process { padding: 5rem 1.5rem; }
.cro-header-center { text-align: center; }
.process-steps {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    max-width: 600px;
    margin: 0 auto;
    position: relative;
}
.step-cro {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    background: #ffffff;
    padding: 2rem;
    border-radius: var(--radius-card);
    box-shadow: var(--shadow-card);
    border: 1px solid var(--border-subtle);
    position: relative;
    z-index: 2;
}
.step-num-cro {
    font-size: 3rem;
    font-weight: 900;
    color: rgba(30,58,138,0.1);
    line-height: 1;
}
.step-info-cro h3 { font-size: 1.3rem; margin-bottom: 0.4rem; color: var(--text-heading); }
.step-info-cro p { color: var(--text-secondary); font-size: 1rem; }

/* 7. CTA HIGHLIGHT FINAL */
.cta-final-cro {
    background: radial-gradient(circle at 50% 50%, var(--urgency-red), #b91c1c);
    padding: 6rem 1.5rem;
    text-align: center;
}
.cta-wrapper { max-width: 800px; margin: 0 auto; }
.cta-headline { color: #ffffff; font-size: clamp(2.2rem, 5vw, 3.2rem); font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem; }
.cta-sub { color: rgba(255,255,255,0.9); font-size: 1.2rem; margin-bottom: 3rem; }
.end-actions { justify-content: center; }

/* Utils */
.pulse-anim { animation: breathing 4.5s ease-in-out infinite; }
"""

with open(r"c:\Users\Usuario\OneDrive\Desktop\rbrb\styles.css", "a", encoding="utf-8") as f:
    f.write(css_append_content)

print("HTML y CSS completamente actualizados bajo arquitectura CRO.")
