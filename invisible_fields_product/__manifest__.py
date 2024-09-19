# -*- coding: utf-8 -*-
{
    'name': "Invisible Campos de Producto",

    'description': """
        Carga de devolucion de Producto de parte de los Cliente, atendidos por los Vendedores
    """,

    'author': "David Bata",
    
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','account'],

    # always loaded
    'data': [
        'views/product_template.xml'
    ],
    
}
