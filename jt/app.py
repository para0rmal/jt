import json
import textwrap
from colr import color
from click import echo
from .template import template


class Help:
    def __init__(self):
        self.template = template
        self.p_top = ''
        self.p_bottom = ''
        self.p_indent = ''
        self.p_bypass = False


        self.__set_format__()

    def __set_format__(self):
        try:
            self.p_bypass = self.template['theme']['padding']['bypass']
            if not self.p_bypass:
                try:
                    self.p_top = '\n' * self.template['theme']['padding']['top']
                except:
                    pass
                try:
                    self.p_bottom = '\n' * self.template['theme']['padding']['bottom']
                except:
                    pass
                try:
                    self.p_indent = ' ' * self.template['theme']['padding']['indent']
                except:
                    pass
        except:
            pass

    def display(self):
        help_str = ''
        for i in self.template['logo'].split('<n>'):
            help_str += i + '\n'

        help_str += '\n'
        help_str += self.p_indent + 'Description:\n'
        help_str += 2 * self.p_indent + self.template['description'] + '\n'

        help_str += '\n'
        help_str += self.p_indent + 'Synopsis:\n'
        help_str += 2 * self.p_indent + self.template['synopsis'] + '\n'
        
        help_str += '\n'
        help_str += self.p_indent + 'Options:\n'
        for option in self.template['sections']['Options']:
            help_str += self.p_indent * 2 + option['option'] + ': ' + option['help'] + '\n'

        help_str += '\n'
        help_str += self.p_indent + 'Examples:\n'
        for option in self.template['sections']['Examples']:
            help_str += self.p_indent * 2 + option['description'] + '\n' + 2 * self.p_indent + option['command'] + self.p_top

        help_str += self.p_indent + 'Legend:\n'
        for option in self.template['sections']['Legend']:
            help_str += self.p_indent * 2 + option['item'] + ' : ' + option['description'] + '\n'

        echo(self.__colourise__(help_str))

    def __load_template__(self):
        try:
            return json.loads(''.join([i for i in open('template.json', 'r')]))
        except Exception as e:
            pass
        
    def __colourise__(self, help_str):
        r = help_str
        for title in ['Options', 'Description', 'Examples', 'Legend', 'Synopsis']:
            r = r.replace(title, color(title, fore=self.template['theme']['colors']['titles']['fg'], style='bright'))

        for highlight in self.template['theme']['colors']['highlight']:
            r = r.replace(highlight['text'], color(highlight['text'], fore=highlight['fg'], style='bright'))
        return r

help_screen = Help()
