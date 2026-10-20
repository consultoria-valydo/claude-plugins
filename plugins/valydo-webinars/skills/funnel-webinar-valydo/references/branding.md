# Branding: colores de la plantilla y cómo sustituirlos

La plantilla usa la paleta de Valydo. Cada color tiene un **papel** (rol). Al personalizar, se cambia el color pero se mantiene el papel: lo que era fondo oscuro sigue siendo fondo oscuro, con el oscuro del alumno.

## 1. Calcula la paleta

```
python3 scripts/paleta.py --acento "#hex" --oscuro "#hex" --claro "#hex" [--secundario "#hex"] [--json]
```

- `--acento`: color principal de botones y destacados.
- `--oscuro`: fondo de las secciones oscuras y texto fuerte sobre claro. Debe ser muy oscuro.
- `--claro`: fondo de las secciones crema y titulares sobre oscuro. Debe ser muy claro.
- `--secundario` (opcional): etiquetas pequeñas. Si no lo da, el script usa un neutro a medio camino entre su claro y su oscuro.

El script devuelve la tabla «color de la plantilla → color nuevo», el color del texto de los botones y avisos de contraste. Usa `--json` para trabajar tú con los valores exactos.

## 2. Colores de la plantilla por papel

| Rol | Plantilla | Dónde aparece |
|---|---|---|
| oscuro | rgb(27, 27, 27) · #1b1b1b | Fondos de secciones oscuras; fondo general (`Body`) de gracias y replay; titulares y textos fuertes sobre fondo claro |
| oscuro_tarjeta | rgb(38, 38, 38) · #262626 | Tarjetas de «Cómo será la clase» |
| claro | rgb(244, 243, 236) · #f4f3ec | Fondos crema; tarjetas de «Para quién es»; titulares sobre fondo oscuro |
| acento | rgb(131, 244, 45) · #83f42d | Fondo y borde de botones; parte destacada en cursiva de titulares; iconos de tarjetas; «CLASE GRATUITA EN DIRECTO»; «Repetición de la clase:» |
| acento_sobre_claro | rgb(63, 122, 18) · #3f7a12 | Las 3 frases «Y en tu cabeza…» (sobre blanco) |
| secundario | rgb(168, 138, 98) · #a88a62 | «PARA [AVATAR]…», casilla de privacidad, fecha del cierre, © del replay |
| secundario_sobre_claro | rgb(122, 98, 64) · #7a6240 | Etiquetas sobre fondo claro: QUIZÁ TE SUENE, EN ESTA CLASE, 01/02/03, PASO 1/2/3, descripción del experto |
| texto_claro_suave | rgb(232, 228, 218) | Párrafo del hero |
| arena | rgb(217, 208, 191) y rgba(217, 208, 191, 1) | Textos secundarios sobre oscuro; borde de los campos del formulario |
| arena_formulario | rgb(207, 200, 184) | Línea de hora bajo «Reserva tu plaza gratis» |
| gris_legal | rgb(154, 149, 139) | Pie legal |
| texto_cuerpo | rgb(63, 61, 56) | Párrafos sobre fondo claro |
| texto_cuerpo_2 | rgb(74, 71, 65) | Textos de apoyo sobre fondo claro |
| texto_boton | rgb(27, 27, 27) **solo en botones** | `textColor` y `mobileTextColor` de los botones |

## 3. Se mantienen (salvo que el alumno pida cambiarlos)

- **Blanco** rgb(255, 255, 255) / rgba(255, 255, 255, 1): secciones blancas, campos del formulario, texto de las barras rojas, autoridad del hero.
- **Urgencia** rgb(217, 48, 37) y rgb(255, 228, 224): barras rojas de gracias y replay y etiquetas de la cuenta atrás. El rojo funciona por urgencia; cámbialo solo si choca mucho con su marca.
- **Tarjetas de testimonios tipo chat**: rgb(30, 31, 34), rgb(43, 45, 49), rgb(242, 243, 245), rgb(219, 222, 225), rgb(201, 205, 251), rgb(181, 186, 193), rgb(148, 155, 164) y los colores de los nombres (rgb(233, 185, 73), rgb(231, 95, 76)). Imitan una captura de Discord. Si los testimonios del alumno son de WhatsApp y quiere que se parezcan, puedes proponerle cambiarlos, pero no es necesario.
- **Popups sin uso** y cualquier color con transparencia total (alfa 0).
- `subTextColor` de los botones (no se usa).

## 4. Cómo aplicar la sustitución

1. Compara siempre por los 3 números (r, g, b). Da igual si en la lectura aparece como `rgb(…)` o `rgba(…, 1)`: conserva el formato original y, en `rgba`, conserva el alfa.
2. Dónde están los colores:
   - Dentro del HTML de `content` (textos, titulares, casilla): en `<span style="color: rgb(…)">`. Reescribe el `content` completo con el texto nuevo y los colores nuevos.
   - `backgroundColor` y `mobileBackgroundColor` de `Body`, `Section` y `Row`.
   - Botones: `background`, `mobileBackground`, `border.color` → acento; `textColor`, `mobileTextColor` → texto_boton. Si un botón tiene `mobileTextColor` o `mobileBackground` distinto al de escritorio, respeta el papel de cada uno.
   - Campos (`Field`): `border.color` → arena. El fondo blanco se mantiene.
   - Cuenta atrás (`Countdown`): `timeStyles` y `labelStyles` están en blanco y rosa claro sobre la barra roja; se mantienen si la barra sigue roja.
3. rgb(27, 27, 27) tiene dos papeles: en botones es **texto_boton**; en todo lo demás es **oscuro**.
4. Un color que no esté en esta tabla y no esté en «Se mantienen» no lo cambies; si te parece un error, coméntaselo al alumno.

## 5. Tipografía

La plantilla usa Montserrat. El conector no cambia la fuente: si su marca usa otra, el alumno la cambia a mano en la configuración de la página (fase 5). Mantén negrita en titulares y mayúsculas en botones y etiquetas.
