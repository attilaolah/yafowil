from yafowil.base import factory
from yafowil.utils import cssclasses

def table_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
    }
    return data.tag('table', data.rendered, **attrs)

factory.register('table',
                 factory.extractors('compound'),
                 factory.renderers('compound') + [table_renderer])

def thead_renderer(widget, data):
    return data.tag('thead', data.rendered)

factory.register('thead',
                 factory.extractors('compound'),
                 factory.renderers('compound') + [thead_renderer])

def tbody_renderer(widget, data):
    return data.tag('tbody', data.rendered)

factory.register('tbody',
                 factory.extractors('compound'),
                 factory.renderers('compound') + [tbody_renderer])

def tr_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
    }
    return data.tag('tr', data.rendered, **attrs)

factory.register('tr',
                 factory.extractors('compound'),
                 factory.renderers('compound') + [tr_renderer])

def th_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
        'colspan': widget.attrs.get('colspan'),
        'rowspan': widget.attrs.get('rowspan'),
    }
    contents = widget.attrs.get('label')
    if not contents:
        contents = data.rendered
    return data.tag('th', contents, **attrs)

factory.register('th',
                 [],
                 [th_renderer])

def td_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
        'colspan': widget.attrs.get('colspan'),
        'rowspan': widget.attrs.get('rowspan'),
    }
    return data.tag('td', data.rendered, **attrs)

factory.register('td',
                 [],
                 [td_renderer])