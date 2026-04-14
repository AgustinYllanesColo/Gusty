# Contexto del Proyecto

## Descripción
Landing page para servicio técnico especializado en reparación de termotanques, calefones y calderas.

## Objetivo Principal
Conversión rápida a contacto por WhatsApp, maximizando el CTR mediante impacto visual y sentido de urgencia en los primeros 5 segundos de visita. Estrategia Multichoice (abarca 3 niveles de mercado técnico de forma unificada).

## Público Objetivo
Hogares y comercios pequeños con urgencias, que necesitan atención rápida y garantizada.

## Zona de Cobertura
Buenos Aires (Zona Sur, CABA, Oeste, Este).

## Estilos y Diseño Visual Elevado (Capa V7 — Ultra Performance)
- Visual moderno, **Editorial-SaaS Ultra Premium con máxima fluidez (60fps)**.
- **Fondo limpio optimizado**: Se reemplazó el sistema multicapa costoso por un único gradiente súper sutil (`radial-gradient`) directamente en el background del body, eliminando `before` y noise SVG para aliviar el motor de renderizado.
- **Micro-Textura / Blur Heavy Eliminados**: Se removieron todos los `backdrop-filter` (glassmorphism en tiempo real) reemplazándolos por colores sólidos semitransparentes elegantes sobre el fondo oscuro, logrando el mismo look premium sin sobrecargar la GPU.
- **Sistema de tokens CSS (V7)**: Colores y acentos intactos (`--accent-orange`, `--accent-red`). Sombras simplificadas a una sola capa de profundidad (`box-shadow`), eliminando re-cálculos lumínicos.
- Jerarquía tipográfica intacta: `Inter`, con tracking ajustado.

## Estrategia de Fondo Visual V7 (Spotlight Thermal Puros)

### Decisión de UX Clave: Reducción de Carga Cognitiva y Foco Láser
Tras auditar el comportamiento visual en un escenario de urgencia (rotura de calefón, estrés, búsqueda rápida en móvil), se ha transformado radicalmente el enfoque del fondo:

1. **Spotlight Focal**: En lugar de animaciones de fondo, partículas o gradientes generales que flotan por la pantalla, todo el sitio recae sobre un negro absoluto (`#030305`). La única "luz" proviene de **reflectores fijos (`radial-gradients`)** colocados milimétricamente detrás de las zonas críticas de conversión: el Título Principal (Hero) y el Botón Final de WhatsApp.
2. **Cognitive Tunneling**: Al iluminar solo lo que el usuario debe leer/tocar y oscurecer el resto, creamos un "túnel cognitivo". El ojo se dirige instintivamente a la luz, evitando distracciones y fatiga visual. Esto se traduce directamente en un aumento del CTR (Click Through Rate).
3. **Toque "Thermal" Visible y Efectivo**: Tras un ajuste fino de contraste, se incrementó la opacidad de los gradientes radiales (de 0.05 a 0.15 para el tono de fuego central, rodeado de un spread de rojo cálido). Esto rescata al sitio del "negro plano aburrido" dándole una presencia volumétrica y calidez que se siente inmediatamente *premium*, guiando la vista sin competir visualmente con el texto.
4. **Performance Perfecta (Cero Core Web Vitals Override)**: Esta técnica es puramente declarativa y estática. Transmite la misma percepción estelar de un fondo hiper-iluminado, pero al prescindir por completo de animaciones, opacidades variantes y `filter: blur`, el navegador no tiene que recalcular layouts ni compositing capas durante el scroll (60 fps locked en desktop y mobile).

## Análisis de UX y Escalabilidad: Incorporación de "Calderas" (V7.1)
El diseño y su CSS Grid se plantearon modulares. Se ha inyectado el servicio avanzado de **reparación de calderas** transversalmente en el layout:
- **Indexación y SEO Global**: Modificación de etiquetas de alto impacto (`<title>`, `<meta description>`, parámetros en enlaces dinámicos de API WhatsApp, y `<H1>` de entrada). Las keywords long-tail captables se expanden drásticamente.
- **Flujo Visual Grid**: `services-grid` ahora cuenta con un número *non* (5 ítems) aprovechando `auto-fit` de CSS Grid para generar un bloque asimétrico inferior sin romper la alineación, incrementando el tiempo de retención en la lectura de la propuesta de valor.
- **Objeciones Preventivas**: Integración de nuevas FAQs referidas directamente a problemáticas del rubro de calefacción de agua dual.

### Micro-Interacciones
- `AOS.js` reducido a animaciones un 25% más rápidas (`duration: 400ms`), asegurando que la carga inicial se sienta como una app nativa, rápida y snappier.
- `VanillaTilt` restringido solo para monitores masivos (`>900px`) y con sus efectos pesados (`glare`) apagados, reduciendo significativamente la memoria de video asignada a `<canvas>` en background.
- Hover states unificados para no forzar layout trashing; todo interactúa modificando Transforms y Shadows.

## Stack Tecnológico Orgánico
- HTML5 (Semántico Puro - SEO Local Validado)
- CSS3 (Vanilla PURO - CSS animations limitadas al umbral Cero-Load)
- JavaScript (Vanilla puro - Reducido a su mínima expresión comercial)
- Google Fonts: **Inter** (peso de `400` al `900`).
- Librerías externas (CDN): AOS, VanillaTilt (Light), Lucide Icons.

## Reglas de Desarrollo Especificas
- NO usar frameworks (Tailwind, Bootstrap, React, etc.) y conservar la limpieza y velocidad extrema al momento de procesar un móvil con urgencia real de red LTE débil.
- NO incorporar animaciones basadas en propiedades que alteren Render o Layout. Solo `opacity` y `transform` son permitidos para fines decorativos.
- **Este archivo (context.md) debe servir como la memoria estricta del proyecto y actualizarse en cada iteración o cambio futuro.**
