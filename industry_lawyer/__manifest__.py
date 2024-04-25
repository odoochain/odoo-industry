{
    'name': 'Lawyer',
    'version': '1.0',
    'category': 'Services',
    'description': u"""
    This module insall a configuration that preset the modules and
    configuration of a law firm.
""",
    'depends': [
        'documents_project',
        'hr_timesheet',
        'knowledge',
        'project',
        'project_enterprise',
        'sale_management',
        'sale_planning',
        'sale_timesheet_enterprise',
        'website_appointment',
        'theme_clean',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/ir_attachment_pre.xml',
        'data/documents_folder.xml',
        'data/project_project.xml',
        'data/product_template.xml',
        'data/sale_order_template.xml',
        'data/sale_order_template_line.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
        'data/appointment_type.xml',
    ],
    'demo': [
        'demo/ir_attachment_post.xml',
        'demo/res_partner.xml',
        'demo/hr_employee.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_post.xml',
        'demo/res_users.xml',
        'demo/appointment_type.xml',
        'demo/website.xml',
        'demo/website_page_views.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
    ],
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
