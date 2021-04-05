#                    Copyright 2021 Saad Mairaj

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import threading


def _bind(cls=None, *ags, **kw):
    """Internal function.\n
    Binds and unbinds sequences with any name given as className."""
    cls = cls or kw.pop('cls', ags.pop(0))
    if ags:
        return [_bind(cls=cls, **i) for i in ags]
    classname = kw['className'] + str(cls)
    bindtags = list(cls.bindtags())
    if classname in bindtags:
        bindtags.remove(classname)
    if kw.get('func'):
        _bind(cls, className=kw['className'], sequence=kw['sequence'])
        bindtags.append(classname)
        cls.bindtags(tuple(bindtags))
        return cls.bind_class(classname, sequence=kw['sequence'],
                              func=kw['func'], add=kw.get('add', '+'))
    cls.bindtags(tuple(bindtags))
    cls.unbind_class(classname, kw['sequence'])


def threaded(fn=None, **kw):
    """To use as decorator to make a function call threaded.
    takes function as argument. To join=True pass @threaded(True)."""

    def wrapper(*args, **kwargs):
        kw['return'] = kw['function'](*args, **kwargs)

    def _threaded(fn):
        kw['function'] = fn

        def thread_func(*args, **kwargs):
            thread = threading.Thread(
                target=wrapper, args=args,
                kwargs=kwargs, daemon=kw.get('daemon', True))
            thread.start()
            if kw.get('join'):
                thread.join()
            return kw.get('return', thread)
        return thread_func

    if fn and callable(fn):
        return _threaded(fn)
    return _threaded
