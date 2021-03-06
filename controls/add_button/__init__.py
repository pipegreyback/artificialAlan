import src


class AddButtonControl(src.boiler_ui_module.BoilerUIModule):
    conf = {
        'static_url_prefix': '/add_button/',
        'static_path': './controls/add_button/static',
        'css_files': ['add_button.css'],
        'js_files': [],
    }

    def render(self, id_):
        return self.render_string(
            '../controls/add_button/add_button.html',
            id_=id_)
