""" Compile app styles """
import sass


def compile_sass():
    """ Compile and compress sass file 'main.scss'"""
    with open('src/assets/css/main.css', 'w') as main_css:
        main_css.write(sass.compile(
            filename='src/styles/scss/main.scss', output_style='compressed'))


# Launch with python
if __name__ == '__main__':
    compile_sass()
