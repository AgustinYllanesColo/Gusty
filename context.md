# Contexto del Proyecto

## Descripción
Landing page para servicio técnico especializado en reparación de termotanques y calefones.

## Objetivo Principal
Conversión rápida a contacto por WhatsApp, maximizando el CTR mediante impacto visual y sentido de urgencia en los primeros 5 segundos de visita.

## Público Objetivo
Hogares y comercios pequeños con urgencias, que necesitan atención rápida y garantizada.

## Zona de Cobertura
Buenos Aires (Zona Sur, CABA, Oeste, Este).

## Estilos y Diseño Visual Elevado (Capa V6.1 — Polish Final)
- Visual moderno, **Editorial-SaaS Ultra Premium con identidad de marca consolidada**.
- **Fondo multicapa con profundidad atmosférica**: Se abandonó el negro plano (`#050508`) por un sistema de gradientes radiales cálidos/fríos (`radial-gradient ellipse`) posicionados estratégicamente que generan una ilusión de iluminación ambiental sin impactar rendimiento.
- **Micro-textura noise** (SVG inline como `background-image`): Overlay fijo a `opacity: 0.025` que añade rugosidad visual imperceptible pero que elimina el efecto "lavado digital" en pantallas retina. Se reduce a `0.015` en móvil.
- **Gradientes de sección**: Cada sección principal (`.services`, `.benefits`, `.testimonials`, `.faq`) tiene un `radial-gradient` propio ultra-sutil que rompe la monotonía sin crear cortes visibles.
- Acentos naranja (`#ff5e3a`) y rojo (`#e63946`) integrados mediante gradientes consistentes.
- **Sistema de tokens CSS unificado V6.1**: variables para bordes (`--border-subtle`, `--border-glass`, `--border-accent`), sombras con inset highlight (`--shadow-card`, `--shadow-elevated`), radios, y elevaciones.
- Glassmorphism refinado (`backdrop-filter: blur`) con bordes cristalinos top (`border-top` con mayor opacidad) que simulan reflejo de luz superior.
- Tipografía con jerarquía ultra fuerte: `--text-heading` (#fff), `--text-primary` (#f0f0f3), `--text-secondary` (#8a8f9e).

## Dirección Estética V6.1 — Decisiones de Rediseño

### Tratamiento del Fondo (V6.1 clave)
- **Problema resuelto**: El fondo plano `#050508` generaba una percepción de "vacío digital", haciendo que las secciones intermedias (entre cards) se sientan muertas.
- **Solución implementada**:
  1. `background-image` del `body` con 4 capas de gradientes: naranja cálido top-left, rojo cálido bottom-right, azul profundo central, gradiente lineal vertical con variación de tono.
  2. Pseudo-elemento `body::before` con SVG noise (`feTurbulence fractalNoise`) como textura fija global. Totalmente CSS, cero HTTP requests.
  3. Secciones individuales con `radial-gradient` subliminal que crea "zonas de interés visual" sin borders ni divisores explícitos.
- **Criterio de diseño**: El fondo debe sentirse vivo pero nunca competir con el contenido. Toda iluminación ambiental opera por debajo del umbral de atención consciente.

### Cards y Componentes — Refinamiento de Bordes
- Todas las cards (`.service-card`, `.benefit-item`, `.testimonial-card`, `.coverage-box`) recibieron un `border-top: 1px solid rgba(255,255,255, 0.05-0.08)` que simula un reflejo de luz superior, creando efecto de relieve/profundidad (flotan sobre el fondo).
- Sombras con `inset 0 1px 0 rgba(255,255,255,0.02)` incorporado a los tokens `--shadow-card` y `--shadow-elevated`.
- `backdrop-filter: blur()` aplicado a service cards (8px), benefits (6px) y coverage (10px) para reforzar glassmorphism contra el fondo texturizado. Desactivado en móvil (≤768px) con `backdrop-filter: none` por rendimiento GPU.

### Hero
- Composición asimétrica con línea vertical gradiente izquierda y anillo geométrico animado derecho.
- Título dominante con tracking ultra-tight y text-shadow con glow naranja sutil.
- Highlight con gradiente animado (`gradient-shift` 6s).
- Subtítulo con glow lateral radiante.

### Secciones con Alta Identidad
- Service cards con barra acentuada superior `::before`.
- Benefits con efecto scanner `::after`.
- Testimonials con comilla decorativa gigante.
- Coverage con barra animada `border-sweep`.
- FAQ con barra lateral emergente en hover.

### Transiciones y Curvas
- Curva principal: `cubic-bezier(0.34, 1.56, 0.64, 1)` — spring elástico.
- Ambient glows: 18-22s, `will-change: transform`.
- `prefers-reduced-motion: reduce` respetado globalmente.

### Mobile (≤768px)
- Decorativos del hero ocultos.
- Glows: `opacity: 0.12`, `blur(120px)`.
- Noise texture: `opacity: 0.015`.
- `backdrop-filter: none` en cards/benefits/coverage.
- CTAs al 100% width.

## Stack Tecnológico Orgánico
- HTML5 (Semántico Puro - SEO Local Validado)
- CSS3 (Vanilla PURO - Layered Radial Gradients, SVG Noise Texture, CSS Pseudo-element Decorators, Keyframe Animations)
- JavaScript (Vanilla puro - Rendimiento ultra alto)
- Google Fonts: **Inter** (peso de `400` al `900`).
- Librerías externas (CDN): AOS, VanillaTilt, tsParticles, Lucide Icons.

## Reglas de Desarrollo Especificas
- NO usar frameworks (Tailwind, Bootstrap, React, etc.) y conservar la limpieza y velocidad extrema al momento de procesar un móvil con urgencia real de red LTE débil.
- **Este archivo (context.md) debe servir como la memoria estricta del proyecto y actualizarse en cada iteración o cambio futuro.**
