#!/usr/bin/env python3
"""Paleta de marca para la plantilla de webinar de Valydo.

Recibe 3 o 4 colores del alumno y devuelve:
- la paleta completa por papel (rol),
- la tabla de sustitución: color de la plantilla -> color nuevo,
- avisos de contraste (WCAG) en lenguaje sencillo.

Uso:
  python3 paleta.py --acento "#83f42d" --oscuro "#1b1b1b" --claro "#f4f3ec" [--secundario "#a88a62"] [--json]

Sin dependencias externas.
"""
import argparse
import json
import sys

# Colores de la plantilla (r, g, b) -> rol. Ver references/branding.md.
PLANTILLA = [
    ((27, 27, 27), "oscuro", "Fondos oscuros, fondo general de gracias y replay, titulares y textos fuertes sobre fondo claro"),
    ((38, 38, 38), "oscuro_tarjeta", "Tarjetas de «Cómo será la clase» sobre fondo oscuro"),
    ((244, 243, 236), "claro", "Fondos crema, tarjetas de «Para quién es» y titulares sobre fondo oscuro"),
    ((131, 244, 45), "acento", "Botones, parte destacada de titulares sobre oscuro, iconos, «CLASE GRATUITA»"),
    ((63, 122, 18), "acento_sobre_claro", "Frases «Y en tu cabeza…» sobre fondo blanco"),
    ((168, 138, 98), "secundario", "Etiquetas y textos de apoyo sobre fondo oscuro, casilla de privacidad, © del replay"),
    ((122, 98, 64), "secundario_sobre_claro", "Etiquetas pequeñas sobre fondo claro (QUIZÁ TE SUENE, EN ESTA CLASE, PASO 1…)"),
    ((232, 228, 218), "texto_claro_suave", "Párrafo del hero"),
    ((217, 208, 191), "arena", "Texto secundario sobre oscuro y borde de los campos del formulario"),
    ((207, 200, 184), "arena_formulario", "Línea de hora bajo «Reserva tu plaza gratis»"),
    ((154, 149, 139), "gris_legal", "Texto legal del pie"),
    ((63, 61, 56), "texto_cuerpo", "Párrafos sobre fondo claro"),
    ((74, 71, 65), "texto_cuerpo_2", "Textos de apoyo sobre fondo claro"),
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def parse_color(value):
    v = value.strip().lower()
    if v.startswith("rgb"):
        nums = v[v.index("(") + 1 : v.index(")")].split(",")
        return tuple(int(float(n)) for n in nums[:3])
    v = v.lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    try:
        if len(v) != 6:
            raise ValueError
        return tuple(int(v[i : i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError(f"Color no válido: {value}. Usa un código hex como #83f42d.") from None


def to_hex(c):
    return "#{:02x}{:02x}{:02x}".format(*c)


def to_rgb(c):
    return "rgb({}, {}, {})".format(*c)


def mix(a, b, t):
    """Mezcla a hacia b en proporción t (0 = a, 1 = b)."""
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def luminance(c):
    def ch(x):
        x = x / 255
        return x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4

    r, g, b = (ch(x) for x in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def push_until(color, toward, against, target):
    """Mueve `color` hacia `toward` hasta que contraste >= target con todos los de `against`."""
    for step in range(0, 101, 2):
        c = mix(color, toward, step / 100)
        if all(contrast(c, x) >= target for x in against):
            return c
    return mix(color, toward, 1)


def build(acento, oscuro, claro, secundario=None):
    avisos = []
    roles = {}

    if luminance(oscuro) > 0.2:
        avisos.append("El color oscuro no es muy oscuro: los textos claros encima pueden leerse mal. Mejor un tono más profundo.")
    if luminance(claro) < 0.6:
        avisos.append("El color claro no es muy claro: los textos oscuros encima pueden leerse mal. Mejor un tono más suave.")
    if contrast(claro, WHITE) < 1.04:
        avisos.append(
            "Tu color claro es casi blanco: las secciones crema y las blancas se verán iguales. "
            "Si quieres que se distingan, usa un claro con un toque de color (por ejemplo, un crema o un gris muy suave)."
        )

    roles["oscuro"] = oscuro
    roles["oscuro_tarjeta"] = mix(oscuro, WHITE, 0.05)
    roles["claro"] = claro
    roles["acento"] = acento
    roles["acento_sobre_claro"] = push_until(acento, BLACK, [WHITE, claro], 4.5)

    if secundario is None:
        secundario = mix(claro, oscuro, 0.35)
    roles["secundario"] = push_until(secundario, WHITE, [oscuro], 4.5)
    if roles["secundario"] != secundario:
        avisos.append("He aclarado un poco el color secundario para que se lea bien sobre el fondo oscuro.")
    roles["secundario_sobre_claro"] = push_until(secundario, BLACK, [WHITE, claro], 4.5)

    roles["texto_claro_suave"] = mix(claro, oscuro, 0.05)
    roles["arena"] = mix(claro, oscuro, 0.12)
    roles["arena_formulario"] = mix(claro, oscuro, 0.17)
    roles["gris_legal"] = push_until(mix(claro, oscuro, 0.42), claro, [oscuro], 4.5)
    roles["texto_cuerpo"] = mix(oscuro, claro, 0.15)
    roles["texto_cuerpo_2"] = mix(oscuro, claro, 0.22)

    # Texto de los botones (y de cualquier texto sobre el color de acento)
    c_osc, c_bla = contrast(oscuro, acento), contrast(WHITE, acento)
    if c_osc >= 4.5:
        roles["texto_boton"] = oscuro
    elif c_bla >= 4.5:
        roles["texto_boton"] = WHITE
        avisos.append("El texto de los botones irá en blanco: sobre tu color de acento se lee mejor que el oscuro.")
    else:
        roles["texto_boton"] = oscuro if c_osc >= c_bla else WHITE
        avisos.append(
            "Ni el texto oscuro ni el blanco se leen bien sobre tu color de acento "
            f"(contraste {max(c_osc, c_bla):.1f}, recomendado 4,5). Plantéate un acento más claro o más oscuro."
        )

    # Comprobaciones de lectura
    checks = [
        ("claro", "oscuro", 4.5, "Los titulares claros sobre fondo oscuro"),
        ("arena", "oscuro", 4.5, "Los textos secundarios sobre fondo oscuro"),
        ("texto_cuerpo", "claro", 4.5, "Los párrafos sobre fondo crema"),
        ("oscuro", "claro", 4.5, "Los titulares oscuros sobre fondo crema"),
    ]
    for a, b, target, label in checks:
        ratio = contrast(roles[a], roles[b])
        if ratio < target:
            avisos.append(f"{label} tienen poco contraste ({ratio:.1f}, recomendado {target}).")
    ratio = contrast(acento, oscuro)
    if ratio < 3:
        avisos.append(
            f"Tu color de acento se ve poco sobre el fondo oscuro (contraste {ratio:.1f}). "
            "Las partes destacadas de los titulares y los botones perderán fuerza."
        )

    sustituciones = []
    for rgb, rol, donde in PLANTILLA:
        nuevo = roles[rol]
        sustituciones.append(
            {
                "plantilla": to_rgb(rgb),
                "plantilla_hex": to_hex(rgb),
                "nuevo": to_rgb(nuevo),
                "nuevo_hex": to_hex(nuevo),
                "rol": rol,
                "donde": donde,
            }
        )

    return {
        "roles": {k: {"hex": to_hex(v), "rgb": to_rgb(v)} for k, v in roles.items()},
        "sustituciones": sustituciones,
        "excepcion_botones": {
            "regla": "En botones, textColor y mobileTextColor usan texto_boton, no oscuro, aunque en la plantilla ambos sean rgb(27, 27, 27).",
            "texto_boton": to_rgb(roles["texto_boton"]),
        },
        "se_mantienen": [
            "rgb(255, 255, 255) blanco (fondos blancos, campos del formulario, textos sobre barras rojas)",
            "rgb(217, 48, 37) y rgb(255, 228, 224) urgencia (barras rojas y etiquetas de la cuenta atrás)",
            "Colores de las tarjetas de testimonios tipo chat",
            "Colores de los popups sin uso",
            "Colores con transparencia total (alfa 0)",
        ],
        "avisos": avisos,
    }


def as_markdown(result):
    lines = ["| Rol | Plantilla | Nuevo | Dónde |", "|---|---|---|---|"]
    for s in result["sustituciones"]:
        lines.append(f"| {s['rol']} | {s['plantilla_hex']} | {s['nuevo_hex']} | {s['donde']} |")
    lines.append(f"| texto_boton | #1b1b1b (solo botones) | {result['roles']['texto_boton']['hex']} | Texto de los botones |")
    lines.append("")
    lines.append("Se mantienen: " + "; ".join(result["se_mantienen"]) + ".")
    if result["avisos"]:
        lines.append("")
        lines.append("Avisos:")
        lines.extend(f"- {a}" for a in result["avisos"])
    else:
        lines.append("")
        lines.append("Sin avisos de contraste.")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Paleta de marca para la plantilla de webinar de Valydo")
    p.add_argument("--acento", required=True, help="Color de acento (botones y destacados), p. ej. #83f42d")
    p.add_argument("--oscuro", required=True, help="Color oscuro (fondos oscuros y textos), p. ej. #1b1b1b")
    p.add_argument("--claro", required=True, help="Color claro (fondos claros), p. ej. #f4f3ec")
    p.add_argument("--secundario", help="Opcional: color de etiquetas pequeñas, p. ej. #a88a62")
    p.add_argument("--json", action="store_true", help="Salida en JSON")
    a = p.parse_args()
    try:
        result = build(
            parse_color(a.acento),
            parse_color(a.oscuro),
            parse_color(a.claro),
            parse_color(a.secundario) if a.secundario else None,
        )
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2) if a.json else as_markdown(result))


if __name__ == "__main__":
    main()
