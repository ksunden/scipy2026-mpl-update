"""
Common functions for working with slides.
"""

import io
import pathlib
import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager
from PIL import Image
import segno


#: The blue used for Matplotlib logo.
MPL_BLUE = '#11557c'
#: The font to use for the Matplotlib logo.
LOGO_FONT = None
#: A bullet point.
BULLET = '$\N{Bullet}$'
#: The FontProperties to use, Carlito.
FONT = None
#: The size of a slide figure.
FIGSIZE = (19.2, 10.8)
#: The DPI of a slide figure.
DPI = 100
#: Syle arguments for code snippets
CODE = dict(fontfamily='monospace', fontsize=32, verticalalignment='top',
            alpha=0.7)


def bullet_level1(fig, y, text):
    """
    Create a level 1 list item.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.05, y, text,
                    fontproperties=FONT, fontsize=48, alpha=0.7,
                    verticalalignment='top')


def bullet_level2(fig, y, text, **kwargs):
    """
    Create a level 2 list item.

    This is roughly the same as level 1, but not bolded, and indented more.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.1, y, text,
                    **{'fontproperties': FONT, 'fontsize': 48, 'fontweight': 'normal',
                       'alpha': 0.7, 'verticalalignment': 'top', **kwargs})





def check_requirements():
    """
    Check requirements to create the slides.

    Currently checks whether the path to a Matplotlib repository is specified,
    and that the Carlito and/or Calibri fonts are available.
    """

    if len(sys.argv) < 2:
        sys.exit('Usage: %s <matplotlib-path>' % (sys.argv[0], ))
    fonts = pathlib.Path('fonts')
    if fonts.is_dir():
        for font in fonts.glob('*.ttf'):
            matplotlib.font_manager.fontManager.addfont(font)
    # The original font is Calibri, if that is not installed, we fall back
    # to Carlito, which is metrically equivalent.
    calibri = carlito = None
    try:
        matplotlib.font_manager.findfont('Calibri:bold', fallback_to_default=False)
    except ValueError:
        pass
    else:
        calibri = matplotlib.font_manager.FontProperties(family='Calibri',
                                                         weight='bold')
    try:
        matplotlib.font_manager.findfont('Carlito:bold', fallback_to_default=False)
    except ValueError:
        pass
    else:
        carlito = matplotlib.font_manager.FontProperties(family='Carlito',
                                                         weight='bold')
    global FONT, LOGO_FONT
    if calibri is not None:
        LOGO_FONT = calibri
        if carlito is None:
            FONT = calibri
            print('WARNING: Using Calibri for all text. '
                  'Non-logo text may not appear correct.')
        else:
            FONT = carlito
            print('Using Calibri for logo and Carlito for remaining text.')
    elif carlito is not None:
        print('WARNING: Using Carlito for all text. '
              'The logo may not appear correct.')
        LOGO_FONT = carlito
        FONT = carlito
    else:
        sys.exit('Calibri or Carlito font must be installed.')


def new_slide(plain=False, **kwargs):
    """
    Create a new slide.

    Parameters
    ----------
    plain : bool, default: False
        Whether to leave out any slide decorations (e.g., logo).
    """

    fig = plt.figure(figsize=FIGSIZE, dpi=DPI, **kwargs)
    fig.mplslide_props = {'plain': plain}
    return fig


def slide_heading(fig, text):
    """
    Add a heading to a slide, using a common style.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    text : str
        The text to place in the heading.
    """

    fig.text(0.05, 0.85, text, color='C0', fontproperties=FONT, fontsize=72)


def slide_subfig_heading(subfig, text):
    """
    Add a heading to a slide in a subfigure, using a common style.

    Parameters
    ----------
    subfig : matplotlib.figure.SubFigure
        The slide subfigure, usually from the top a Figure.
    text : str
        The text to place in the heading.
    """

    subfig.text(0.05, 0.5, text, color='C0',
                fontproperties=FONT, fontsize=72, verticalalignment='center')


def annotate_pr_author(fig, *authors, pr=None):
    """
    Annotate the Pull Request author(s) on the bottom-right corner of a slide.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    authors : list of str
        The GitHub usernames to use for the annotation.
    pr : int, optional
        The PR number on GitHub to link to.
    """

    text = 'PR by ' + ', '.join(f'@{author}' for author in authors)
    t = fig.text(0.95, 0.05, text,
                 fontproperties=FONT, fontsize=32, alpha=0.7,
                 horizontalalignment='right')
    if pr is not None:
        t.set_url(f'https://github.com/matplotlib/matplotlib/pull/{pr}')


def add_qrcode(fig, url, location):
    """
    Add a QR code on a figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The slide figure.
    url : str
        THe URL to link with the QR code.
    location : tuple of int
        A location accepted by `matplotlib.figure.Figure.add_axes` on which to place
        the QR image.
    """
    qrcode = segno.make(url)
    out = io.BytesIO()
    qrcode.save(out, kind='png', compresslevel=0, dark=MPL_BLUE)
    out.seek(0)
    img = Image.open(out).convert('RGB')
    ax = fig.add_axes(location, frameon=False, xticks=[], yticks=[])
    ax.imshow(img)


def add_quine(fig, file, location):
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import ImageFormatter

    import matplotlib.pyplot as plt
    import numpy as np
    import PIL.Image

    with open("../qcode.png", "wb") as fout, open(file) as fin:
        fout.write(
            highlight(
                fin.read(),
                PythonLexer(),
                ImageFormatter(
                    font_name="xkcd Script",
                    line_numbers=False,
                    style="dracula",
                    font_size=50,
                ),
            )
        )

    with PIL.Image.open("../qcode.png") as im:
        code_img = np.array(im)

    ax = fig.add_axes(location, frameon=False, xticks=[], yticks=[])
    ax.imshow(code_img)
