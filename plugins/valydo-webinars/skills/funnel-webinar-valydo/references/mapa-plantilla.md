# Mapa de la plantilla en Systeme

Cómo está construida cada página de «PLANTILLA WEBINARS - VALYDO - IA» y cómo encontrar cada bloque cuando lees la página con `get_page_editable_content`.

- Localiza siempre por el **texto ancla** (lo que pone el bloque en la plantilla) y por el orden de las secciones. Los identificadores cambian en cada copia: usa solo los que te devuelva la lectura.
- La lectura devuelve los bloques en orden de lectura: Cuerpo → Sección → Fila → Columna → elemento. Cada sección es un hijo directo del cuerpo (`Body`).
- Los colores de texto van dentro del HTML de cada `content` (`<span style="color: rgb(…)">`). Los fondos van en `backgroundColor` de secciones y filas. Ver `branding.md`.
- **C** = lo cambia Claude con el conector. **M** = lo hace el alumno a mano en el editor.

Tipos de bloque que verás: `Section`, `Row`, `Column`, `Headline`, `Text`, `Button`, `Field` (campo del formulario), `Checkbox`, `Image`, `Video`, `Countdown`, `Popup`.

Qué NO expone el conector (siempre **M**): la imagen de un `Image`, la URL de un `Video`, el enlace de un `Button`, la fecha de un `Countdown`, la tipografía, el título SEO, la URL del paso y el nombre del funnel.

---

## Paso 1 · «Registro» (tipo sales_page) — 11 secciones

| # | Sección (fondo) | Bloque y texto ancla | Qué hacer |
|---|---|---|---|
| 1 | Barra superior (oscuro) | `Text` «🟢 CLASE GRATUITA EN DIRECTO» | C: fijo; solo colores |
| | | `Text` «[DÍA] de [MES] · [HH:MM] h 🇪🇸» | C: fecha, hora y bandera/zona |
| | | `Text` «PARA [AVATAR] · PLAZAS LIMITADAS» | C: avatar en mayúsculas |
| 2 | Hero + formulario (oscuro) | `Headline` h1 «[Promesa…] [giro…]» — 2 `span`: claro + acento en `em` | C |
| | | `Text` «En esta clase en directo vas a descubrir…» — 3 `span`: texto, autoridad en blanco y `strong`, punto final | C |
| | | `Headline` h3 «Reserva tu plaza gratis» | C: fijo; solo colores |
| | | `Text` «[HH:MM] h 🇪🇸 · en directo · plazas limitadas» | C |
| | | `Field` «Tu nombre», `Field` «Tu mejor email» | C: solo color del borde (arena) |
| | | `Checkbox` «Acepto la política de privacidad.» | C: solo colores |
| | | `Button` «QUIERO MI PLAZA →» (envía el formulario) | C: colores. No tocar su acción |
| 3 | Quizá te suene (blanco) | `Text` «QUIZÁ TE SUENE» | C: colores |
| | | `Headline` h2 centrado «¿[Situación…] y te sientes [emoción…]?» | C |
| | | `Text` con 3 párrafos «[Su día a día…]», «[Qué intenta…]», «[El momento…]» separados por `<p></p>` | C |
| | | `Text` «Y en tu cabeza no paran de sonar estas frases:» | C: colores |
| | | `Text` con 3 párrafos «[Lo que piensa 1/2/3…]» entre «» en `strong` + `em` | C |
| | | `Text` «[Cierre: cómo se queda…]» | C |
| 4 | En esta clase (crema) | `Text` «EN ESTA CLASE» | C: colores |
| | | `Headline` «Esta clase es el primer paso para [el destino que desea], de una vez por todas» | C |
| | | `Text` «Esto es lo que vas a aprender:» | C: colores |
| | | 3 columnas: `Text` «01 / [Aprendizaje 1…]» + `Text` «[Qué va a entender…]» (igual 02 y 03) | C |
| | | `Button` «QUIERO MI PLAZA →» | C: colores |
| 5 | Para quién es (blanco) | `Headline` «Esta clase es perfecta para ti si [describe a tu avatar]» | C |
| | | 3 tarjetas (`Row` con fondo crema): `Text` «[Situación N…]» + `Text` «[Qué tiene hoy + qué le falta]» | C |
| | | `Button` «QUIERO MI PLAZA →» | C: colores |
| 6 | Imparte la clase (crema) | `Image` (foto del experto, columna izquierda) | **M** |
| | | `Headline` «Imparte la clase [NOMBRE]» | C |
| | | `Text` 2 párrafos: «[Descripción corta…]» (dorado) + «[Cifra 1…] · [Cifra 2…] · [Cifra 3…]» | C |
| | | `Text` 3 párrafos: «[Credencial…]», «[Cifras exactas…]», «[Trayectoria…]» | C |
| 7 | Testimonios (crema) | `Headline` «Estas personas estaban igual que tú antes de venir a la clase» | C: fijo; colores |
| | | Tarjeta 1 (`Row` fondo de chat): `Text` «Adri de Papadri  26/5/26, 22:35» + `Text` mensaje + `Text` reacciones | C: **contenido de Valydo, sustituir** |
| | | Tarjeta 2: `Text` «Marta Calcerrada  14/12/24, 10:16» + `Text` mensaje + `Row` blanco «TOTAL HISTÒRIC / 1.101.932,06 €» + `Text` reacciones | C: **sustituir**; el `Row` blanco se borra salvo cifra real del alumno |
| | | Tarjeta 3: `Text` «Sofía García  19/3/26, 11:10» + `Text` mensaje + `Text` reacciones | C: **sustituir** |
| | | `Button` «QUIERO MI PLAZA →» | C: colores |
| 8 | Cómo será la clase (oscuro) | `Headline` «Cómo será la clase» | C: colores |
| | | `Text` «Te contamos los detalles para que puedas reservarte [la tarde].» | C |
| | | 3 tarjetas (`Row` fondo tarjeta oscura): `Text` «🗓️ / Fecha y hora» + `Text` «[Día de la semana]…»; `Text` «💻 / 100% online y en directo» + `Text` «Por [plataforma]…»; `Text` «💬 / Espacio de dudas» + `Text` fijo | C |
| 9 | Qué pasa cuando te registras (blanco) | `Headline` + `Text` «Tres pasos sencillos…» | C: colores |
| | | `Text` «PASO 1 / Rellenas el formulario» + `Text` fijo | C: colores |
| | | `Text` «PASO 2 / Entras al grupo privado de WhatsApp» + `Text` «…[material previo]…» | C |
| | | `Text` «PASO 3 / Nos vemos el [día] a las [HH:MM] h» + `Text` «Te conectas desde [dónde / cómo]…» | C |
| 10 | Cierre (oscuro) | `Headline` «¿[Listo/Lista] para [el destino que desea]?» — 3 `span`: claro + acento en `em` + claro | C |
| | | `Text` 2 párrafos: «Reserva tu plaza ahora y […]» + «[DÍA] de [MES] · [HH:MM] h · Limitado a [N] plazas…» | C |
| | | `Button` «QUIERO MI PLAZA →» | C: colores |
| 11 | Pie legal (oscuro) | `Text` legal con «[systeme.io]» y «[Política de Privacidad]» | C: quitar corchetes. Enlace **M** |
| | | `Text` «Aviso legal», `Text` «Política de privacidad» | C: colores. Enlaces **M** |
| | | `Text` «© [AÑO] [MARCA] · Todos los derechos reservados» | C |

Además, **M**: tipografía de la página, título SEO.

## Paso 2 · «Pagina Gracias» (tipo opt_in_thank_you_page) — 2 secciones + popup

| # | Sección (fondo) | Bloque y texto ancla | Qué hacer |
|---|---|---|---|
| — | `Popup` «Crear tu cuenta gratuita» | Popup por defecto, sin uso | No tocar |
| 1 | Barra (rojo urgencia) | `Text` «⚠️ TU PLAZA AÚN NO ESTÁ CONFIRMADA · QUEDA UN ÚLTIMO PASO» | C: fijo |
| 2 | Contenido (oscuro) | `Image` (foto señalando hacia abajo) | **M** |
| | | `Headline` h2 «Para confirmar tu plaza… Tienes un regalo en la descripción 🎁» | C: adaptar el regalo si hace falta; colores |
| | | `Button` «ENTRAR AL GRUPO DE WHATSAPP» | C: colores. Enlace **M** |

El fondo general (`Body`) de esta página también es oscuro: cámbialo con la paleta. Además, **M**: título SEO.

## Paso 3 · «Replay» (tipo sales_page) — 7 secciones + popup

| # | Sección (fondo) | Bloque y texto ancla | Qué hacer |
|---|---|---|---|
| — | `Popup` «DEJA TU CORREO Y TE CONTACTAREMOS EN 24 HORAS» | Sin uso | No tocar |
| 1 | Barra (rojo urgencia) | `Text` «⏳ LA REPETICIÓN SE ELIMINA EN…» | C: fijo |
| | | `Countdown` | C: colores. Fecha **M** |
| 2 | Vídeo de la clase (oscuro) | `Text` «Repetición de la clase: cómo atraer clientes de 1.500€ a 10.000€ cada semana» — 2 `span`: acento + claro | C: **título de Valydo, sustituir** |
| | | `Text` «Mírala hasta el final: …» | C: adaptar a su oferta |
| | | `Video` (clase) | **M** |
| | | `Button` «AGENDAR MI LLAMADA DE CLARIDAD» | C: texto (si cambia el nombre de la llamada) y colores. Enlace **M** |
| 3 | Testimonios título (crema) | `Text` «Ellos ya aplican el método que has visto en la clase» | C: colores |
| 4-6 | Vídeos de testimonios (crema) | 3 secciones, cada una con una fila de 2 `Video` | **M** los vídeos. Si tiene menos de 6, C puede borrar las secciones que sobren (confirmando antes) |
| 7 | Cierre (oscuro) | `Button` «QUIERO AGENDAR MI LLAMADA DE CLARIDAD» | C: texto y colores. Enlace **M** |
| | | `Text` «© 2026 – Todos los derechos reservados» | C: año y marca |

El fondo general (`Body`) de esta página también es oscuro: cámbialo con la paleta. Además, **M**: título SEO (ahora «%TITULO%»).

---

## Ejemplo de cambio de un texto

Lectura (registro, sección 1):

```
content: <p dir="ltr"><span style="color: rgb(168, 138, 98)"><strong>PARA [AVATAR] · PLAZAS LIMITADAS</strong></span></p>
```

Cambio (avatar «coaches de pareja», secundario nuevo `rgb(201, 162, 39)`):

```
update_entity → entityType: Text, updatedProperties.content:
<p dir="ltr"><span style="color: rgb(201, 162, 39)"><strong>PARA COACHES DE PAREJA · PLAZAS LIMITADAS</strong></span></p>
```

Misma estructura, solo cambian el texto y el color.
