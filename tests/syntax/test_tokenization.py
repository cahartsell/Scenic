
from tokenize import TokenInfo, ENCODING, NAME, OP, NUMBER, ENDMARKER

import pytest

from scenic.syntax.translator import TokenParseError, TokenTranslator
from tests.utils import compileScenic, sampleEgoFrom

templates = [
'''
ego = Object with height 2, {continuation}
{indent}with width 3, {continuation}
{indent}at 10@20
''',
'''
ego = Object with height 2, {continuation}
{indent}with width 3, at 10@20
''',
'''
ego = Object with height 2, {continuation}
{indent}#with width 2,{continuation}
{indent}with width 3
''',
'''
ego = Object with height 2, {continuation}
# with width 2,{continuation}
# blah {continuation}
{indent}with width 3
'''
]

@pytest.mark.parametrize('template', templates)
@pytest.mark.parametrize('continuation', ('', '\\', '# comment'))
@pytest.mark.parametrize('indent', ('  ', '    ', '             '))
@pytest.mark.parametrize('gap', ('', '\n', '# comment\n', '\n# comment\n'))
def test_specifier_layout(template, continuation, indent, gap):
    """Test legal specifier layouts, with and without line continuations."""
    preamble = template.format(continuation=continuation, indent=indent)
    program = preamble + gap + 'Object at 20@20'
    print('TESTING PROGRAM:', program)
    compileScenic(program)

def test_dangling_specifier_list():
    with pytest.raises(TokenParseError):
        compileScenic('ego = Object with width 4,')
    with pytest.raises(TokenParseError):
        compileScenic('ego = Object with width 4,   # comment')

def test_dangling_specifier_list_2():
    """Variant of the above test catching a quirk of the Python 3.7.0 tokenizer.

    Unlike other versions, it apparently does not insert a NEWLINE token at the
    end of a line which is terminated by EOF. Reliably reproducing the resulting
    sequence of tokens requires us to manually specify them below.
    """
    translator = TokenTranslator()
    line = 'ego = Object with width 4,'
    tokens = [
        TokenInfo(ENCODING, 'utf-8', (0, 0), (0, 0), ''),
        TokenInfo(NAME, 'ego', (1, 0), (1, 3), line),
        TokenInfo(OP, '=', (1, 4), (1, 5), line),
        TokenInfo(NAME, 'Object', (1, 6), (1, 12), line),
        TokenInfo(NAME, 'with', (1, 13), (1, 17), line),
        TokenInfo(NAME, 'width', (1, 18), (1, 23), line),
        TokenInfo(NUMBER, '4', (1, 24), (1, 25), line),
        TokenInfo(OP, ',', (1, 25), (1, 26), line),
        TokenInfo(ENDMARKER, '', (2, 0), (2, 0), '')
    ]
    with pytest.raises(TokenParseError):
        translator.translate(tokens)

def test_incipit_as_name():
    """Incipits of operators are not keywords and can be used as names.

    Here we try 'distance' from 'distance from X' and 'offset' from 'X offset by Y'.
    """
    for name in ('distance', 'offset'):
        ego = sampleEgoFrom(f'{name} = 4\n' f'ego = Object at {name} @ 0')
        assert tuple(ego.position) == (4, 0)
