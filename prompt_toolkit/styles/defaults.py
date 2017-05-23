"""
The default styling.
"""
from __future__ import unicode_literals, absolute_import
from .style import Style, merge_styles
from prompt_toolkit.cache import memoized

__all__ = (
    'default_style',
)

#: Default styling. Mapping from classnames to their style definition.
PROMPT_TOOLKIT_STYLE = [
    # Highlighting of search matches in document.
    ('search-match',                             'noinherit reverse'),
    ('search-match.current',                     'noinherit #ffffff bg:#448844 underline'),

    # Highlighting of select text in document.
    ('selected',                                'reverse'),

    ('cursor-column',                           'bg:#dddddd'),
    ('cursor-line',                             'underline'),
    ('color-column',                            'bg:#ccaacc'),

    # Highlighting of matching brackets.
    ('matching-bracket',                        ''),
    ('matching-bracket.other',                  '#000000 bg:#aacccc'),
    ('matching-bracket.cursor',                 '#ff8888 bg:#880000'),

    ('multiple-cursors.cursor',                 '#000000 bg:#ccccaa'),

    # Line numbers.
    ('line-number',                             '#888888'),
    ('line-number.current',                     'bold'),
    ('tilde',                                   '#8888ff'),

    # Default prompt.
    ('prompt',                                  ''),
    ('prompt.arg',                              'noinherit'),
    ('prompt.arg.text',                         ''),
    ('prompt.search',                           'noinherit'),
    ('prompt.search.text',                      ''),

    # Search toolbar.
    ('search-toolbar',                          'bold'),
    ('search-toolbar.text',                     'nobold'),

    # System toolbar
    ('system-toolbar',                          'bold'),
    ('system-toolbar.text',                     'nobold'),

    # "arg" toolbar.
    ('arg-toolbar',                             'bold'),
    ('arg-toolbar.text',                        'nobold'),

    # Validation toolbar.
    ('validation-toolbar',                      'bg:#550000 #ffffff'),
    ('window-too-small',                        'bg:#550000 #ffffff'),

    # Completions toolbar.
    ('completions-toolbar',                     'bg:#bbbbbb #000000'),
    ('completions-toolbar.arrow',               'bg:#bbbbbb #000000 bold'),
    ('completions-toolbar completion',          'bg:#bbbbbb #000000'),
    ('completions-toolbar current-completion',  'bg:#444444 #ffffff'),

    # Completions menu.
    ('completion-menu',                         'bg:#bbbbbb #000000'),
    ('completion-menu completion',              ''),
    ('completion-menu current-completion',      'bg:#888888 #ffffff'),
    ('completion-menu completion-meta',         'bg:#999999 #000000'),
    ('completion-menu completion-meta current-completion',
                                                'bg:#aaaaaa #000000'),
    ('completion-menu multi-column-completion-meta', 'bg:#aaaaaa #000000'),

    # Scrollbars.
    ('scrollbar.background',                     ''),
    ('scrollbar.button',                         'bg:#888888'),
    ('scrollbar.start',                          'underline #ffffff'),
    ('scrollbar.end',                            'underline #000000'),
    ('scrollbar.arrow',                          'noinherit bold'),

    # Auto suggestion text.
    ('auto-suggestion',                         '#666666'),

    # Trailing whitespace and tabs.
    ('trailing-whitespace',                     '#999999'),
    ('tab',                                     '#999999'),

    # When Control-C/D has been pressed. Grayed.
    ('aborting',                                '#888888'),
    ('exiting',                                 '#888888'),

    # Entering a Vi digraph.
    ('digraph',                                 '#4444ff'),

    # Default styling of HTML elements.
    ('i',                                       'italic'),
    ('u',                                       'underline'),
    ('b',                                       'bold'),
    ('em',                                      'italic'),
    ('strong',                                  'bold'),

    # Prompt bottom toolbar
    ('bottom-toolbar',                          'reverse'),
]


WIDGETS_STYLE = [
    # Dialog windows.
    ('dialog',                                  'bg:#4444ff'),
    ('dialog.body',                             'bg:#ffffff #000000'),
    ('dialog.body text-area',                    'bg:#cccccc'),
    ('dialog.body text-area last-line',          'underline'),

    ('dialog frame-label',                      '#ff0000 bold'),

    # Scrollbars in dialogs.
    ('dialog.body scrollbar.background',        ''),
    ('dialog.body scrollbar.button',            'bg:#000000'),
    ('dialog.body scrollbar.arrow',             ''),
    ('dialog.body scrollbar.start',             'nounderline'),
    ('dialog.body scrollbar.end',               'nounderline'),

    # Buttons.
    ('button',                                  ''),
    ('button.arrow',                            'bold'),
    ('button focussed',                         'bg:#880000 #ffffff'),

    # Menu bars.
    ('menu-bar',                                'bg:#aaaaaa #000000'),
    ('menu-bar.selected-item',                  'bg:#ffffff #000000'),
    ('menu',                                    'bg:#888888 #ffffff'),
    ('menu.border',                             '#aaaaaa'),
    ('menu.border shadow',                      '#444444'),

    # Shadows.
    ('dialog shadow',                           'bg:#000088'),
    ('dialog.body shadow',                      'bg:#aaaaaa'),

    ('progress-bar',                             'bg:#000088'),
    ('progress-bar.used',                        'bg:#ff0000'),
]


# The default Pygments style, include this by default in case a Pygments lexer
# is used.
PYGMENTS_DEFAULT_STYLE = {
    'pygments.whitespace':                "#bbbbbb",
    'pygments.comment':                   "italic #408080",
    'pygments.comment.preproc':           "noitalic #bc7a00",

    #keyword:                   "bold #aa22ff",
    'pygments.keyword':                   "bold #008000",
    'pygments.keyword.pseudo':            "nobold",
    'pygments.keyword.type':              "nobold #b00040",

    'pygments.operator':                  "#666666",
    'pygments.operator.word':             "bold #aa22ff",

    'pygments.name.builtin':              "#008000",
    'pygments.name.function':             "#0000ff",
    'pygments.name.class':                "bold #0000ff",
    'pygments.name.namespace':            "bold #0000ff",
    'pygments.name.exception':            "bold #d2413a",
    'pygments.name.variable':             "#19177c",
    'pygments.name.constant':             "#880000",
    'pygments.name.label':                "#a0a000",
    'pygments.name.entity':               "bold #999999",
    'pygments.name.attribute':            "#7d9029",
    'pygments.name.tag':                  "bold #008000",
    'pygments.name.decorator':            "#aa22ff",

    'pygments.string':                    "#ba2121",
    'pygments.string.doc':                "italic",
    'pygments.string.interpol':           "bold #bb6688",
    'pygments.string.escape':             "bold #bb6622",
    'pygments.string.regex':              "#bb6688",
    #'pygments.string.symbol':             "#b8860b",
    'pygments.string.symbol':             "#19177c",
    'pygments.string.other':              "#008000",
    'pygments.number':                    "#666666",

    'pygments.generic.heading':           "bold #000080",
    'pygments.generic.subheading':        "bold #800080",
    'pygments.generic.deleted':           "#a00000",
    'pygments.generic.inserted':          "#00a000",
    'pygments.generic.error':             "#ff0000",
    'pygments.generic.emph':              "italic",
    'pygments.generic.strong':            "bold",
    'pygments.generic.prompt':            "bold #000080",
    'pygments.generic.output':            "#888",
    'pygments.generic.traceback':         "#04d",

    'pygments.error':                     "border:#ff0000",
}


@memoized()
def default_style():
    """
    Create a default `Style` object.
    """
    return merge_styles([
        Style(PROMPT_TOOLKIT_STYLE),
        Style(WIDGETS_STYLE),
        Style.from_dict(PYGMENTS_DEFAULT_STYLE),
    ])
