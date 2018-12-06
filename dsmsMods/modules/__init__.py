import os

__all__ = list(map(lambda x: x.split('.')[0],
                   list(
                       filter(lambda x: '.py' in x and '__' not in x,
                              os.listdir(os.path.dirname(__file__)))
                   ))
               )
