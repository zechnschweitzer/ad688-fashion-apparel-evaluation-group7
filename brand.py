"""Shared chart styling for the Group 7 site.

Import this module once at the top of a page (``import brand``) and every
Plotly chart on that page picks up the site palette and typography. Pages can
also use the named colors below directly.
"""

import plotly.graph_objects as go
import plotly.io as pio

# Site palette
PLUM = "#33213B"         # Dark 1  - deep plum
WARM_WHITE = "#FFFCF7"   # Light 1 - warm white
PURPLE = "#69558E"       # Dark 2 / Accent 2 - muted purple
CREAM = "#F8F4EC"        # Light 2 - cream
MAUVE = "#79445F"        # Accent 1 - dusty mauve
LAVENDER = "#BBA7C9"     # Accent 3 - soft lavender
LILAC = "#C9ACDD"        # Accent 4 - light lilac
BERRY = "#6C3656"        # Accent 5 - dark berry
PLUM_GRAY = "#66566C"    # Accent 6 - plum gray
TINT = "#F1EAF2"         # light lilac tint for gridlines and fills
RULE = "#E2D8E6"

COLORWAY = [PURPLE, MAUVE, LAVENDER, LILAC, BERRY, PLUM_GRAY]

# Diverging scale for gaps: below target (purple) -> on target (cream) -> above target (berry)
GAP_SCALE = [[0.0, PURPLE], [0.5, CREAM], [1.0, BERRY]]
# Sequential scale for 1-5 proficiency: low (cream) -> high (purple)
PROFICIENCY_SCALE = [[0.0, CREAM], [0.5, LILAC], [1.0, PURPLE]]

FONT = "DM Sans, Helvetica Neue, Arial, sans-serif"
TITLE_FONT = "Cormorant Garamond, Georgia, serif"

pio.templates["group7"] = go.layout.Template(
    layout=dict(
        font=dict(family=FONT, color=PLUM, size=14),
        title=dict(font=dict(family=TITLE_FONT, size=24, color=PLUM)),
        colorway=COLORWAY,
        paper_bgcolor=WARM_WHITE,
        plot_bgcolor=WARM_WHITE,
        margin=dict(l=40, r=40, t=80, b=50),
        hoverlabel=dict(bgcolor=PLUM, font=dict(color=CREAM, family=FONT), bordercolor=PLUM),
        xaxis=dict(automargin=True, gridcolor=TINT, zerolinecolor=RULE, linecolor=RULE, ticks="", title=dict(font=dict(color=PLUM_GRAY))),
        yaxis=dict(automargin=True, gridcolor=TINT, zerolinecolor=RULE, linecolor=RULE, ticks="", title=dict(font=dict(color=PLUM_GRAY))),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        bargap=0.3,
    )
)
pio.templates.default = "group7"
