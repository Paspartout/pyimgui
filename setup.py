# -*- coding: utf-8 -*-
import os
import sys
from itertools import chain

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.command.develop import develop as _develop
from setuptools.command.egg_info import egg_info as _egg_info
from setuptools.command.install_egg_info import install_egg_info as _install_egg_info


try:
    from Cython.Build import cythonize
except ImportError:
    # A 'cythonize' stub is needed so that build, develop and install can
    # start before Cython is installed.
    cythonize = lambda extensions, **kwargs: extensions  # noqa
    USE_CYTHON = False
else:
    USE_CYTHON = True


_CYTHONIZE_WITH_COVERAGE = os.environ.get("_CYTHONIZE_WITH_COVERAGE", False)

if _CYTHONIZE_WITH_COVERAGE and not USE_CYTHON:
    raise RuntimeError(
        "Configured to build using Cython "
        "and coverage but Cython not available."
    )


def read(filename):
    with open(filename, 'r') as file_handle:
        return file_handle.read()


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


init = os.path.join(os.path.dirname(__file__), 'imgui', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]

VERSION = get_version(eval(version_line.split('=')[-1]))
README = os.path.join(os.path.dirname(__file__), 'README.md')


if sys.platform in ('cygwin', 'win32'):  # windows
    # note: `/FI` means forced include in VC++/VC
    # note: may be obsoleted in future if ImGui gets patched
    os_specific_flags = ['/FIpy_imconfig.h']
    # placeholder for future
    os_specific_macros = []
else:  # OS X and Linux
    # note: `-include` means forced include in GCC/clang
    # note: may be obsoleted in future if ImGui gets patched
    # placeholder for future
    os_specific_flags = ['-includeconfig-cpp/py_imconfig.h']
    os_specific_macros = []


if sys.platform in ('cygwin', 'win32'):
    os_extra_link_args = ['TODO']
    lib_extra_link_args = ['TODO']
if sys.platform == 'darwin':
    os_extra_link_args = ['-Wl,-rpath,@loader_path/../imgui.data']
    lib_extra_link_args = ['-Wl,-install_name,@loader_path/../imgui.data/libimgui.so']
else:
    os_extra_link_args = ['-Wl,-rpath,$ORIGIN/../imgui.data']
    lib_extra_link_args = []


if _CYTHONIZE_WITH_COVERAGE:
    compiler_directives = {
        'linetrace': True,
    }
    cythonize_opts = {
        'gdb_debug': True,
    }
    general_macros = [('CYTHON_TRACE_NOGIL', '1')]
else:
    compiler_directives = {}
    cythonize_opts = {}
    general_macros = []


def extension_sources(path):
    sources = ["{0}{1}".format(path, '.pyx' if USE_CYTHON else '.cpp')]

    if not USE_CYTHON:
        # note: Cython will pick these files automatically but when building
        #       a plain C++ sdist without Cython we need to explicitly mark
        #       these files for compilation and linking.
        sources += [
            'imgui-cpp/imgui.cpp',
            'imgui-cpp/imgui_draw.cpp',
            'imgui-cpp/imgui_demo.cpp',
            'imgui-cpp/imgui_widgets.cpp',
            'imgui-cpp/imgui_tables.cpp',
            'config-cpp/py_imconfig.cpp'
        ]

    return sources


def backend_extras(*requirements):
    """Construct list of requirements for backend integration.

    All built-in backends depend on PyOpenGL so add it as default requirement.
    """
    return ["PyOpenGL"] + list(requirements)


class build_ext(_build_ext):
    parent = _build_ext
    def run(self):
        print("HK build_ext >>>>")
        print("inplace:", self.inplace)
        # place the result in the ./build/temp.linux-x86_64-3.9
        self.old_build_lib, self.build_lib = self.build_lib, self.build_temp
        # make sure not to copy the result to top level folder
        self.old_inplace, self.inplace = self.inplace, 0
        # self.dump_options()

        # use our imconfig.h for the build
        self.copy_file(os.path.join('config-cpp', 'imconfig.h'), 'imgui-cpp')

        if sys.platform == 'darwin':
            from distutils import sysconfig
            vars = sysconfig.get_config_vars()
            vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-dynamiclib')

        # call the original build_ext
        self.parent.run(self)
        print("HK build_ext ####")

        orig_file = self.get_ext_fullpath('libimgui')
        target_dir = 'imgui.data'
        target_file = os.path.join(target_dir, 'libimgui.so')
        # print('stage orig_file:', orig_file)
        # create ./imgui.data/libimgui.so (used for imgui extension build and editable runtime)
        if not self.dry_run:
            self.mkpath('imgui.data')
            self.copy_file(orig_file, target_file)
            # print('develop target_file:', target_file)

            if not self.old_inplace:
                # create ./build/lib.linux-x86_64-3.9/imgui.data/libimgui.so (used for install)
                target_dir = os.path.join(self.old_build_lib, 'imgui.data')
                self.mkpath(target_dir)
                target_file = os.path.join(target_dir, 'libimgui.so')
                self.copy_file(orig_file, target_file)
                # print('install target_file:', target_file)
                for hdr in ['imconfig.h', 'imgui_internal.h', 'imstb_textedit.h',
                            'imgui.h', 'imstb_rectpack.h', 'imstb_truetype.h']:
                    header_file = os.path.join('imgui-cpp', hdr)
                    self.copy_file(header_file, target_dir)
                    # print('install header_file:', header_file)

        print("HK build_ext <<<<")


class develop(_develop):
    parent = _develop
    def run(self):
        print("HK develop >>>>")
        self.reinitialize_command('build_ext', inplace=1)
        self.run_command('build_ext')
        print("HK develop <<<<")


class egg_info(_egg_info):
    parent = _egg_info
    def run(self):
        pass


class install_egg_info(_install_egg_info):
    parent = _install_egg_info
    def run(self):
        pass


EXTRAS_REQUIRE = {
    'Cython':  ['Cython>=0.24,<0.30'],
    'cocos2d': backend_extras(
        "cocos2d",
        "pyglet>=1.5.6; sys_platform == 'darwin'",
    ),
    'sdl2': backend_extras('PySDL2'),
    'glfw': backend_extras('glfw'),
    'pygame': backend_extras('pygame'),
    'opengl': backend_extras(),
    'pyglet': backend_extras(
        "pyglet; sys_platform != 'darwin'",
        "pyglet>=1.5.6; sys_platform == 'darwin'",
    )
}

# construct special 'full' extra that adds requirements for all built-in
# backend integrations and additional extra features.
EXTRAS_REQUIRE['full'] = list(set(chain(*EXTRAS_REQUIRE.values())))

EXTENSIONS = [
    Extension(
        "imgui.core", extension_sources("imgui/core"),
        extra_compile_args=os_specific_flags,
        extra_link_args=os_extra_link_args,
        define_macros=[
            # note: for raising custom exceptions directly in ImGui code
            ('PYIMGUI_CUSTOM_EXCEPTION', None)
        ] + os_specific_macros + general_macros,
        include_dirs=['imgui', 'config-cpp', 'imgui-cpp', 'ansifeed-cpp'],
        library_dirs=["imgui.data"],
        libraries=["imgui"],
    ),
    Extension(
        "imgui.internal", extension_sources("imgui/internal"),
        extra_compile_args=os_specific_flags,
        extra_link_args=os_extra_link_args,
        define_macros=[
            # note: for raising custom exceptions directly in ImGui code
            ('PYIMGUI_CUSTOM_EXCEPTION', None)
        ] + os_specific_macros + general_macros,
        include_dirs=['imgui', 'config-cpp', 'imgui-cpp', 'ansifeed-cpp'],
        library_dirs=["imgui.data"],
        libraries=["imgui"],
    ),
]


setup(
    name='libimgui',

    cmdclass = {'build_ext': build_ext,
                'develop': develop,
                'egg_info': egg_info,
                'install_egg_info': install_egg_info
                },

    ext_modules=[
        Extension(
            "libimgui",
            sources=[
                'imgui-cpp/imgui.cpp',
                'imgui-cpp/imgui_draw.cpp',
                'imgui-cpp/imgui_demo.cpp',
                'imgui-cpp/imgui_widgets.cpp',
                'imgui-cpp/imgui_tables.cpp',
            ],
            language="c++",
            extra_link_args=lib_extra_link_args,
        ),
    ]
)


setup(
    name='imgui',
    version=VERSION,
    packages=find_packages('.'),

    author=u'Michał Jaworski',
    author_email='swistakm@gmail.com',

    description="Cython-based Python bindings for dear imgui",
    long_description=read(README),
    long_description_content_type="text/markdown",

    url="https://github.com/swistakm/pyimgui",

    ext_modules=cythonize(
        EXTENSIONS,
        compiler_directives=compiler_directives, **cythonize_opts
    ),
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,

    license='BSD',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Cython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Cython',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',

        'Topic :: Games/Entertainment',
    ],
)
