"""
Feature highlights for Matplotlib 3.12.0.
"""

from functools import partial

import numpy as np
import matplotlib as mpl

import PIL

from mplslide import (
    BULLET, FONT, new_slide, slide_heading, add_qrcode, annotate_pr_author)

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


def multivariate_colormaps():
    """
    Create slide for upcoming 3.12 multivariate colormapping.
    """
    fig = new_slide()

    slide_heading(fig, '3.12: Upcoming features')

    level1 = partial(bullet_level1, fig)

    level1(0.8, f'{BULLET} Multivariate colormapping')

    with PIL.Image.open("./multivariate_colormaps.png") as im:
        code_img = np.array(im)

    ax = fig.add_axes([0.15, 0.1, 0.8, 0.6], frameon=False, xticks=[], yticks=[])
    ax.imshow(code_img)



    annotate_pr_author(fig, 'trygvrad', pr=31214)

    return fig


def alpha_blend_modes():
    """
    Create slide for Alpha Blend Modes.
    """
    fig = new_slide()

    slide_heading(fig, '3.12: Alpha Blend Modes')

    with PIL.Image.open("./blend_modes.png") as im:
        code_img = np.array(im)

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.6], frameon=False, xticks=[], yticks=[])
    ax.imshow(code_img)
    annotate_pr_author(fig, 'ayshih', pr=31163)

    return fig


def data_containers():
    """
    Create slide for 3.12 Data Containers.
    """
    fig = new_slide()

    slide_heading(fig, '3.12: Data Containers')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    level1(0.7, f'{BULLET} Unified Data Model across artists')
    level1(0.6, f'\n{BULLET} Built in support for Dynamic Data')
    level2(0.6, f'\n\n{BULLET} Pure Functions')
    level2(0.6, f'\n\n\n{BULLET} Dynamic resampling')
    level2(0.6, f'\n\n\n\n{BULLET} Live streaming data')
    
    annotate_pr_author(fig, 'ksunden', pr=30865)
    return fig



def slides():
    """
    Return slides for this section.
    """
    return (
        #multivariate_colormaps(),
        alpha_blend_modes(),
        data_containers(),
    )
