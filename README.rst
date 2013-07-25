jinja2-pluralize-filter
=======================

Simple jinja2 filter to choose correct plural form for Russian language.

You need to register filter on the template environment:

    from pluralize import pluralize
    environment.filters['pluralize'] = pluralize

Example of usage:

    {{ 42|pluralize([u'товар', u'товара', u'товаров']) }}