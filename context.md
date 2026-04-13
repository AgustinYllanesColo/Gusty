# Contexto del Proyecto

## Descripción
Landing page para servicio técnico especializado en reparación de termotanques y calefones.

## Objetivo Principal
Conversión rápida a contacto por WhatsApp, maximizando el CTR mediante impacto visual y sentido de urgencia en los primeros 5 segundos de visita.

## Público Objetivo
Hogares y comercios pequeños con urgencias, que necesitan atención rápida y garantizada.

## Zona de Cobertura
Buenos Aires (Zona Sur, CABA, Oeste, Este).

## Estilos y Diseño Visual Elevado (Capa V6 — Rediseño Visual Completo)
- Visual moderno, **Editorial-SaaS Ultra Premium con alta identidad de marca**.
- Fondo negro puro (`#050508`) con sistema de **Ambient Glows animados** (drift suave via CSS keyframes) que generan una atmósfera viva sin impactar GPU.
- Acentos naranja (`#ff5e3a`) y rojo (`#e63946`) integrados mediante gradientes consistentes a lo largo de todo el diseño.
- **Sistema de tokens CSS** unificado: variables para bordes (`--border-subtle`, `--border-glass`, `--border-accent`), sombras (`--shadow-card`, `--shadow-elevated`, `--shadow-glow-orange`), radios (`--radius-card`, `--radius-pill`) y elevaciones.
- Glassmorphism refinado con `backdrop-filter: blur(16px)`, bordes cristalinos y `inset-shadows` sutiles.
- Tipografía con jerarquía ultra fuerte: `--text-heading` (#fff) para títulos, `--text-primary` (#f0f0f3) para cuerpo, `--text-secondary` (#8a8f9e) para texto de apoyo.

## Dirección Estética V6 — Decisiones de Rediseño
### Hero
- **Composición asimétrica dramática**: Línea vertical acentuada con gradiente naranja→rojo en el borde izquierdo (`::before`). Anillo decorativo geométrico animado en la esquina superior derecha (`::after`).
- **Título dominante**: `clamp(3rem, 7vw, 5.8rem)` con `font-weight: 900`, tracking ultra apretado (`-0.045em`) y text-shadow con glow naranja sutil.
- **Highlight animado**: El texto en gradiente (`.highlight`) usa `background-size: 200%` con animación `gradient-shift` suave de 6s.
- **Subtítulo con glow lateral**: Borde izquierdo naranja + pseudo-elemento con `radial-gradient` que simula difusión lumínica.
- Badge de urgencia con `backdrop-filter: blur(12px)` y tracking expandido para aspecto institucional.

### Sistema Visual Unificado
- Cada `section-title` lleva un `::after` con barra gradiente naranja→rojo de 60px como marcador visual de identidad.
- Service cards con **barra acentuada superior** (`::before`) que pasa de 50% a 100% opacidad en hover.
- Benefit items con **efecto scanner** (pseudo-elemento `::after` que barre de izquierda a derecha en hover).
- Testimonials con **comilla tipográfica decorativa** gigante (5rem) en gradiente translúcido, posicionada absolutamente.
- Coverage box con **barra animada `border-sweep`** que recorre el borde superior con movimiento pendular.
- FAQ items con **barra lateral emergente** que se expande de 0% a 60% en hover + desplazamiento del texto.

### Transiciones y Curvas
- Curva de movimiento principal: `cubic-bezier(0.34, 1.56, 0.64, 1)` — transición "spring" elástica para hover cards y botones.
- Ambient glows con `will-change: transform` y animaciones de 18-22s para movimiento imperceptible y suave.
- Todas las animaciones respetan `prefers-reduced-motion: reduce` eliminando movement y colapsando duraciones a 0.01ms.

### Mobile
- Decorativos del hero (línea vertical, anillo geométrico) se ocultan en ≤768px para mantener limpieza.
- Glows ambientales reducidos a `opacity: 0.12` y `blur(120px)` en móvil para priorizar legibilidad.
- Cards, benefits y testimonials con paddings reducidos proporcionalmente.
- CTA botones al 100% de ancho con centrado de texto.

## Stack Tecnológico Orgánico
- HTML5 (Semántico Puro - SEO Local Validado)
- CSS3 (Vanilla PURO - Animated Mesh Gradients, CSS Pseudo-element Decorators, Keyframe Animations)
- JavaScript (Vanilla puro - Rendimiento ultra alto de iteraciones lógicas)
- Google Fonts: **Inter** (peso de `400` al `900`).
- Librerías externas permitidas (CDN): AOS, VanillaTilt, tsParticles, Lucide Icons.

## Reglas de Desarrollo Especificas
- NO usar frameworks (Tailwind, Bootstrap, React, etc.) y conservar la limpieza y velocidad extrema al momento de procesar un móvil con urgencia real de red LTE débil.
- **Este archivo (context.md) debe servir como la memoria estricta del proyecto y actualizarse en cada iteración o cambio futuro.**
