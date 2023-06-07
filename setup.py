try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_desc = '''Translates JavaScript to Python code. pyjs is able to translate and execute virtually any JavaScript code.

pyjs is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python.


    import pyjs

    f = pyjs.eval_js( "function $(name) {return name.length}" )

    f("Hello world")

    # returns 11

Now also supports ECMA 6 through pyjs.eval_js6(js6_code)!

More examples at: https://github.com/jo-project/pyjs
'''



# rm -rf dist build && python3 setup.py sdist bdist_wheel
# twine upload dist/*
setup(
    name='pyjs',
    version='0.1',

    packages=['pyjs', 'pyjs.utils', 'pyjs.prototypes', 'pyjs.translators',
              'pyjs.constructors', 'pyjs.host', 'pyjs.es6', 'pyjs.internals',
              'pyjs.internals.prototypes', 'pyjs.internals.constructors', 'pyjs.py_node_modules'],
    url='https://github.com/jo-project/pyjs',
    install_requires = ['tzlocal>=1.2', 'six>=1.10', 'pyjsparser>=2.5.1'],
    license='MIT',
    author='jo-project',
    author_email='jo.project.0911@gmail.com',
    description='JavaScript to Python Translator & JavaScript interpreter written in 100% pure Python.',
    long_description=long_desc
)
