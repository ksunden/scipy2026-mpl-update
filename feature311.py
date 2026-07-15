"""
Feature highlights for Matplotlib 3.9.0.
"""

import numpy as np
import matplotlib.pyplot as plt

from cycler import cycler

from mplslide import BULLET, FONT, new_slide, slide_heading, annotate_pr_author

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


def font_improvements():
    """
    Create slide for font improvements.
    """
    fig = new_slide()
    slide_heading(fig, '3.11: Font Improvements')

    bullet_level2(fig, 0.80, f"{BULLET} Language Support")
    text = 'Here is some رَقْم in اَلْعَرَبِيَّةُ'
    fig.text(0.5, 0.67, text, size=48, ha='center', va='center')
    bullet_level2(fig, 0.55, f"{BULLET} Ligature Support")
    text = 'f\N{Hair Space}f\N{Hair Space}i \N{Rightwards Arrow} ffi'
    fig.text(0.5, 0.44, text, size=48, ha='center', va='center')
    bullet_level2(fig, 0.33, f"{BULLET} Combining multiple or Double Width Diacritics")
    text = (
        'a\N{Combining Circumflex Accent}\N{Combining Double Tilde}'
        'c\N{Combining Diaeresis}')
    text = ' + '.join(
        c if c in 'ac' else f'\N{Dotted Circle}{c}'
        for c in text) + f' \N{Rightwards Arrow} {text}'
    fig.text(0.5, 0.21, text, size=48, ha='center', va='center',
                # Builtin DejaVu Sans doesn't support multiple diacritics.
                family=['Noto Sans', 'DejaVu Sans'])
    annotate_pr_author(fig, 'QuLogic', pr=30161)

    return fig


def accessible_cycles():
    """
    Create slide for stackplot hatching.
    """
    fig = new_slide()
    slide_heading(fig, '3.11: Accessible color cycles')

    axs = fig.subplots(ncols=3)
    color_cycles = ['petroff6', 'petroff8', 'okabe_ito']
    for ax, cc in zip(axs, color_cycles):
        ax.set_title(cc, fontsize=36)
        cc = plt.color_sequences[cc]
        ax.set(xticks=[], yticks=[])
        x = range(5)
        for i, c in enumerate(cc):
            ax.plot(x, [v*(i+1) for v in x], color=c, lw=5)
    fig.subplots_adjust(bottom=0.1, top=0.75)
    annotate_pr_author(fig, 'matthewfeickert', 'hyperphantasia', pr=30065)

    return fig


def grouped_bar():
    """
    Create slide for violinplot sides.
    """

    fig = new_slide()
    slide_heading(fig, '3.11: Grouped Bar Charts')

    np.random.seed(19680801)
    data = np.random.normal(0, 8, size=100)

    ax = fig.subplots()
    ax.set(xticks=[], yticks=[])
    ax.set_fontsize=36
    categories = ['A', 'B']
    datasets = {
        'dataset 0': [1, 11],
        'dataset 1': [3, 13],
        'dataset 2': [5, 15],
    }

    ax = fig.subplots()
    ax.grouped_bar(datasets, tick_labels=categories)
    ax.xaxis.set_tick_params(labelsize=36)
    ax.yaxis.set_tick_params(labelsize=36)
    ax.legend(fontsize=36)
    fig.subplots_adjust(bottom=0.13, top=0.8)

    annotate_pr_author(fig, 'timhoffm', pr=28560)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        grouped_bar(),
        accessible_cycles(),
        font_improvements(),
    )
