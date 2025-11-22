
from flask import template_rendered

from app import app, index, items


def test_index_direct_call():
    items.clear()
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        with app.test_request_context('/'):
            index()
        assert recorded, "Aucun template rendu"
        template, context = recorded[0]
        assert template.name == 'index.html'
        assert context["items"] == items
    finally:
        template_rendered.disconnect(record, app)