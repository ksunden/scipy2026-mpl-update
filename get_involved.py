from mplslide import BULLET, FONT, CODE, new_slide, slide_heading, add_qrcode, bullet_level1, bullet_level2, add_quine

from functools import partial

def get_involved():
    """
    Create slide for getting involved
    """
    fig = new_slide()

    slide_heading(fig, 'Getting Involved')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    level1(0.8, f'{BULLET} Come to Sprints!')
    level1(0.7, f'{BULLET} Tagging examples with sphinx-tags (by @melissawm)')
    level2(0.7, '\n\n.. tags:: animation, component: axes', **CODE)
    level2(0.7, '\n\n\nCome to our Sprint!')

    level1(0.4, f'{BULLET} Your Contribution?')
    t = level2(
        0.4,
        f'\n{BULLET} New Contributors Meeting\n    (first Tuesday of month)')
    t.set_url('https://scientific-python.org/calendars/')
    add_qrcode(fig, 'https://scientific-python.org/calendars/', [0.6, 0.1, 0.4, 0.4])

    return fig

def slides():
    return (get_involved(),)
