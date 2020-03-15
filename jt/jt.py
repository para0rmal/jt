import sys
import json
import yaml
import requests
from click import command, argument, option, echo
from colr import color
from .jsontree import *
from .app import help_screen

CONTEXT_SETTINGS = dict(help_option_names=[])


@command(context_settings=CONTEXT_SETTINGS)
@argument('filename', required=False)
@option('-u', help='Perform HTTP GET request on the specified endpoint and echo JSON response as tree.')
@option('-s', is_flag=True, help='Read JSON from stream.')
@option('-y', is_flag=True, help='Read YAML from stream.')
@option('-h', is_flag=True, help='Show help.')
def run(filename, u, s, y, h):
    j = JSONTree()

    if u:
        r = None
        try:
            r = requests.get(u)
            if r.status_code != 200:
                echo('Response code: {}'.format(color(r.status_code.__str__(), 'red')))
                sys.exit(0)
        except Exception as e:
            echo('Request failed: {}'.format(color(e, 'red')))
            sys.exit(0)

        r = json.loads(r.text)

        if type(r) == list:
            echo(j.tree(r[0]))
        else:
            echo(j.tree(r))

        sys.exit(0)

    elif s:
        input_buffer = None
        r = None

        try:
            input_buffer = ''.join([l for l in sys.stdin])
            r = json.loads(input_buffer)
        except Exception as e:
            echo('Error: expecting {} format. Got: {}'.format(color('JSON', 'yellow'), color(input_buffer, 'red')))
            sys.exit(0)

        if type(r) == list:
            echo(j.tree(r[0]))
        else:
            echo(j.tree(r))

        sys.exit(0)
        
    elif y:
        input_buffer = None
        r = None

        try:
            input_buffer = ''.join([l for l in sys.stdin])
            r = yaml.load(input_buffer, Loader=yaml.FullLoader)
        except Exception as e:
            echo('Error: expecting {} format. Got: {}'.format(color('JSON', 'yellow'), color(input_buffer, 'red')))
            echo(e)
            sys.exit(0)

        if type(r) == list:
            echo(j.tree(r[0]))
        else:
            echo(j.tree(r))

        sys.exit(0)

    elif filename:
        r = None

        try:
            r = ''.join([i for i in open(filename, 'r')])
        except Exception as e:
            echo('Exception: {}'.format(color(e, 'red')))
            sys.exit(0)

        try:
            r = json.loads(r)
        except Exception as e:
            echo('Error: expecting {} format. Got: {}'.format(color('JSON', 'yellow'), color(input_buffer, 'red')))
            sys.exit(0)

        if type(r) == list:
            echo(j.tree(r[0]))
        else:
            echo(j.tree(r))

        sys.exit(0)

    else:
        help_screen.display()
