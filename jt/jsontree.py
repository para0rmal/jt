import json
from .themes import default
from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_LIGHT
from colr import color
from collections import OrderedDict as OD


class JSONTree(object):
    ''' Implements methods for representing JSON schema as text tree. '''
  
    def __init__(self):
        self.tr = LeftAligned(draw=BoxStyle(gfx=BOX_LIGHT, horiz_len=2))
        self.root = '●'
        self.theme = default

    @classmethod
    def __transform__(cls, d):
        r = {}
        for k, v in d:
            if type(v) in [dict, list]:
                r.update({k: OD(v)})
        return r

    def __colourise__(self, s, t):
        return color(s, fore=self.theme[t], style='bright')

    def __format__(self, d):
        r = {}
        if type(d) == dict:
            for k in d.keys():
                t = type(d[k])
                if d[k] is None:
                    r.update({self.__colourise__(k, None): {}})
                elif t == str:
                    r.update({'"{}"'.format(self.__colourise__(k, t)): {}})
                elif t in [bool, float, str, int]:
                    r.update({self.__colourise__(k, t): {}})
                elif t == dict:
                    r.update({'{{{}}}'.format(self.__colourise__(k, t)): self.__format__(d[k])})
                elif t == list:
                    r.update({'[{}]'.format(self.__colourise__(k, t)): self.__format__(d[k][0])})
        return r

    def tree(self, data, root=dict):
        dt = json.loads(json.dumps(self.__format__(data)), object_pairs_hook=self.__transform__)
        return self.tr({self.__colourise__(self.root, dict) + '┐': OD(dt)}) + '\n\n'

