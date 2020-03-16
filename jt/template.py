import json

template = {
    'logo': '    ●<n>    ║ <n>    ╠══╦══<n>  ══╝  ║<n>       ║',
    'description': 'jt, a command line utility for visualising JSON schemas as text trees',
    'synopsis': 'jt FILENAME [-h] [-s] [-u] [-y]',
    'sections': {
        'Options': [
            {
                'option': '-h',
                'help': 'show this message and exit'
            },
            {
                'option': '-s',
                'help': 'Read JSON from stream'
            },
            {
                'option': '-y',
                'help': 'Read YAML from stream'
            },
            {
                'option': '-u',
                'help': 'Read JSON from HTTP GET request',
            }
        ],
        'Examples': [
            {
                'description': 'Read JSON from HTTP GET request ',
                'command': '$ jt -u https://api.github.com/users/para0rmal/repos'
            },
            {
                'description': 'Read JSON from file ',
                'command': '$ jt file.json'
            },
            {
                'description': 'Read YAML from stream ',
                'command': '$ cat file.yml | jt -y'
            },
            {
                'description': 'Read JSON from HTTP GET request ',
                'command': '$ jt -u https://api.github.com/users/para0rmal/repos'
            },
            {
                'description': 'Read JSON from stream',
                'command': '$ echo \'{"0": {"00": [{"000": "", "001": [""]}]}, "1": {"10": [""]}}\' | jt -s'
            }
        ],
        'Legend': [
            {
                'item': '{n_obj} ',
                'description': 'object'
            },
            {
                'item': '[n_arr] ',
                'description': 'array'
            },
            {
                'item': '"n_str" ',
                'description': 'string'
            },
            {
                'item': 'n_bool  ',
                'description': 'bool'
            },
            {
                'item': 'n_null  ',
                'description': 'null'
            },
            {
                'item': 'n_int   ',
                'description': 'integer'
            },
            {
                'item': 'n_float ',
                'description': 'float'
            },
        ],
    },
    'theme': {
        'padding': {
            'bypass': False,
            'top': 2,
            'bottom': 2,
            'indent': 2
        },
        'colors': {
            'text': {
                'bypass': True,
                'fg': 'white',
                'bg': 'default'
            },
            'titles': {
                'bypass': True,
                'fg': 'orange',
                'bg': 'default'
            },
            'highlight': [
                {
                    'text': 'JSON',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': 'YAML',
                    'fg': 'cyan',
                    'bg': 'default'
                },
                {
                    'text': 'stream',
                    'fg': 'magenta',
                    'bg': 'default'
                },
                {
                    'text': 'FILENAME',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'HTTP GET request',
                    'fg': 'blue',
                    'bg': 'default'
                },
                {
                    'text': 'file ',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'filename',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'URL',
                    'fg': 'blue',
                    'bg': 'default'
                },
                {
                    'text': 'file.json',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'file.yml',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'n_obj',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': 'n_arr',
                    'fg': 'blue',
                    'bg': 'default'
                },
                {
                    'text': 'n_str',
                    'fg': 'green',
                    'bg': 'default'
                },
                {
                    'text': 'n_bool',
                    'fg': 'magenta',
                    'bg': 'default'
                },
                {
                    'text': 'n_null',
                    'fg': 'grey',
                    'bg': 'default'
                },
                {
                    'text': 'n_int',
                    'fg': 'cyan',
                    'bg': 'default'
                },
                {
                    'text': 'n_float',
                    'fg': 'red',
                    'bg': 'default'
                },
                {
                    'text': '●',
                    'fg': 'orange',
                    'bg': 'default'
                },
                {
                    'text': '$',
                    'fg': 'green',
                    'bg': 'default'
                }
            ]
        }
    }
}
