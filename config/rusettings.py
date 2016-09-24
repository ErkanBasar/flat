##############################################################################
#   FoLiA Linguistic Annotation Tool (FLAT) - Settings file
#
# These are the settings for your FLAT site.
#
#---------------------------------------------------------------------------
#               PREAMBLE (don't edit this part)
#---------------------------------------------------------------------------
from django import VERSION as DJANGOVERSION
from socket import gethostname
import os.path
from os import environ
import flat


VERSION = flat.VERSION
try:
    BASE_DIR = os.path.dirname(os.path.dirname(flat.__file__)) + "/"
except:
    BASE_DIR = os.path.dirname(os.path.dirname(flat.__path__)) + "/"
hostname = gethostname()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

if hostname == 'mhysa' or hostname == 'caprica':
    WORKDIR = "/home/proycon/work/flat/tmpworkdir/"
    FOLIADOCSERVE_HOST = '127.0.0.1'
    FOLIADOCSERVE_PORT = 8080
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db',                      # Or path to database file if using sqlite3.
    }
    DEBUG = True
elif hostname[:9] == 'applejack':
    if not ('DEV' in environ) or environ['DEV'] == 'false':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'flat',                      # Or path to database file if using sqlite3.
                'USER': 'flat_admin',
                'PASSWORD': open('/www/flat/live/etc/.pw2').read().strip(),
                'HOST': 'mysql-flat.science.ru.nl',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'PORT': '',                      # Set to empty string for default.
            }
        }
        WORKDIR = "/www/flat/live/writable/docroot/"
        FOLIADOCSERVE_HOST = '127.0.0.1'
        FOLIADOCSERVE_PORT = 8023
        DEBUG = True
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'flat',                      # Or path to database file if using sqlite3.
                'USER': 'flat_admin',
                'PASSWORD': open('/www/flat/test/etc/.pw2').read().strip(),
                'HOST': 'mysql-flat.science.ru.nl',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'PORT': '',                      # Set to empty string for default.
            }
        }
        WORKDIR = "/www/flat/test/writable/docroot/"
        FOLIADOCSERVE_HOST = '127.0.0.1'
        FOLIADOCSERVE_PORT = 8024
        DEBUG = True
elif hostname[:8] == 'spitfire':
    if not ('DEV' in environ) or environ['DEV'] == 'false':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'flat',                      # Or path to database file if using sqlite3.
                'USER': 'flat_user',
                'PASSWORD': open('/var/www2/flat/live/etc/.pw').read().strip(),
                'HOST': 'mysql-flat.science.ru.nl',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'PORT': '',                      # Set to empty string for default.
            }
        }
        WORKDIR = "/var/www2/flat/live/writable/docroot/"
        FOLIADOCSERVE_HOST = 'applejack.science.ru.nl'
        FOLIADOCSERVE_PORT = 8023
        ADMIN_MEDIA_PREFIX = '/media/'
        DEBUG = True
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'flat',                      # Or path to database file if using sqlite3.
                'USER': 'flat_user',
                'PASSWORD': open('/var/www2/flat/test/etc/.pw').read().strip(),
                'HOST': 'mysql-flat.science.ru.nl',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
                'PORT': '',                      # Set to empty string for default.
            }
        }
        WORKDIR = "/var/www2/flat/test/writable/docroot/"
        FOLIADOCSERVE_HOST = 'applejack.science.ru.nl'
        FOLIADOCSERVE_PORT = 8024
        ADMIN_MEDIA_PREFIX = '/media/'
        DEBUG = True
else:
    raise Exception("I don't know where I'm running from!")



# Settings specific to FLAT

#Editor modes the user can switch between
MODES = [
    ('viewer','Viewer'),
    ('editor','Annotation Editor'),
    ('structureeditor','Structure Editor'),
    ('metadata','Metadata Editor'),
]


PERSPECTIVES = [ 'document', 'toc', 'p', 's' ]

DEFAULTMODE = 'editor'

DEFAULTCONFIGURATION = 'full'

CONFIGURATIONS = {
'full':{
    'name': "Full Editor",
    'perspectives': PERSPECTIVES,
    #Automatically create namespaces for all the groups a user is in and has write permission for,
    'creategroupnamespaces': True, #boolean
    #The default annotation focus upon loading a document, set to None to start without a focus
    'annotationfocustype': None,
    'annotationfocusset': None,

    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all
    'allowedannotationfocus': True,

    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialviewannotations': True,
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowedviewannotations': True,

    'initialglobviewannotations': [],
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialeditannotations': True,
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowededitannotations': True,

    'allowaddfields': True, #boolean
    'allowdeclare': True, #boolean
    'editformdirect': True, #boolean
    'editformcorrection': True, #boolean
    'editformalternative': True, #boolean
    'editformnew': True, #boolean
    'alloweditformdirect': True, #boolean
    'alloweditformcorrection': True, #boolean
    'alloweditformalternative': True, #boolean
    'alloweditformnew': True, #boolean
    'allowupload': True, #boolean
    'allowconfidence': True,
    'modes': MODES,
},
'valkuileval':{
    'name': "Valkuil Evaluation Project - Stage 1",
    #The default annotation focus upon loading a document, set to None to start without a focus
    'annotationfocustype': 'correction',
    'annotationfocusset': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/spellingcorrection.foliaset.xml',

    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all
    'allowedannotationfocus': ('correction',),

    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialviewannotations': True,
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowedviewannotations': True,

    'initialglobviewannotations': [],
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialeditannotations': ('t',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowededitannotations': ('t',),
    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all

    'allowaddfields': False, #boolean
    'allowdeclare': False, #boolean
    'editformdirect': False, #boolean
    'editformcorrection': True, #boolean
    'editformalternative': False, #boolean
    'editformnew': False, #boolean
    'alloweditformdirect': False, #boolean
    'alloweditformcorrection': True, #boolean
    'alloweditformalternative': False, #boolean
    'alloweditformnew': False, #boolean
    'allowupload': True, #boolean
    'initialcorrectionset': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/spellingcorrection.foliaset.xml',
    'autodeclare': [('correction', 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/spellingcorrection.foliaset.xml')],
    'modes': [ ('editor','Annotation Editor')],
    'perspectives': PERSPECTIVES,
},
'ner': {
    'name': 'Named Entity Annotation Project',
    #The default annotation focus upon loading a document, set to None to start without a focus
    'annotationfocustype': 'entity',
    'annotationfocusset': 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml',

    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all
    'allowedannotationfocus': ('entity/https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml',),


    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialviewannotations': ('t','entity/https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml','correction'),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowedviewannotations': ('t','entity/https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml','correction'),

    'initialglobviewannotations': [],
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialeditannotations': ('entity/https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowededitannotations': ('entity/https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml',),
    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all

    'allowaddfields': False, #boolean
    'allowdeclare': False, #boolean
    'editformdirect': True, #boolean
    'editformcorrection': True, #boolean
    'editformalternative': False, #boolean
    'editformnew': True, #boolean
    'alloweditformdirect': True, #boolean
    'alloweditformcorrection': True, #boolean
    'alloweditformalternative': False, #boolean
    'alloweditformnew': True, #boolean
    'allowupload': True, #boolean
    'initialcorrectionset': 'https://raw.github.com/proycon/folia/master/setdefinitions/namedentitycorrection.foliaset.xml',
    'autodeclare': [
        ('correction', 'https://raw.github.com/proycon/folia/master/setdefinitions/namedentitycorrection.foliaset.xml'),
        ('entity', 'https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/namedentities.foliaset.xml')
    ],
    'modes': [ ('editor','Annotation Editor')],
    'perspectives': PERSPECTIVES,
},
'parsemedemo': {
    'name': 'PARSEME Demo',
    #The default annotation focus upon loading a document, set to None to start without a focus
    'annotationfocustype': 'entity',
    'annotationfocusset': 'https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml',

    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all
    'allowedannotationfocus': ('entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml',),


    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialviewannotations': ('t','entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml'),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowedviewannotations': ('t','entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml'),

    'initialglobviewannotations': ('entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialeditannotations': ('entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowededitannotations': ('entity/https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml',),
    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all

    'allowaddfields': False, #boolean
    'allowdeclare': False, #boolean
    'editformdirect': True, #boolean
    'editformcorrection': False, #boolean
    'editformalternative': False, #boolean
    'editformnew': True, #boolean
    'alloweditformdirect': True, #boolean
    'alloweditformcorrection': False, #boolean
    'alloweditformalternative': False, #boolean
    'alloweditformnew': True, #boolean
    'allowupload': True, #boolean
    'allowconfidence': True,
    'autodeclare': [
        ('entity', 'https://github.com/proycon/parseme-support/raw/master/parseme-mwe.foliaset.xml')
    ],
    'modes': [ ('editor','Annotation Editor')],
    'perspectives': ['s'],
    'slices': 's:100',
    'convertors': [ 
        { 'id': 'parseme_tsv',  #a unique identifier for internal use
          'module': 'tsv2folia.tsv2folia', #the python module where the converter is implemented
          'function': 'flat_convert', #the python function (in the above module) that implements the conversion hook
          'name': "PARSEME TSV", #a human readable named, to appear in the input format drop down list
          'parameter_help': 'Set <em>rtl: true</em> for right-to left languages', #human readable help for parameters
          'parameter_default': 'rtl: false', #default parameter, JSON syntax without the envelopping {}
          'inputextensions': ['tsv'], #input extensions that must be adhered to, and will be stripped for determining the output filename
        }
    ]
},
'sinfex': {
    'name': 'Sinfex Annotation Task',
    #The default annotation focus upon loading a document, set to None to start without a focus
    'annotationfocustype': 'entity',
    'annotationfocusset': 'https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml',

    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all
    'allowedannotationfocus': ('entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml',),


    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialviewannotations': ('t','entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml'),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowedviewannotations': ('t','entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml'),

    'initialglobviewannotations': ('entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'initialeditannotations': ('entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml',),
    #List of FoLiA annotation types (xml tags) that are initially enabled, set to True to enable all
    'allowededitannotations': ('entity/https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml',),
    #list of FoLiA annotation types (xml tags) that allowed as annotation focus, set to True to allow all

    'allowaddfields': False, #boolean
    'allowdeclare': False, #boolean
    'editformdirect': True, #boolean
    'editformcorrection': False, #boolean
    'editformalternative': False, #boolean
    'editformnew': True, #boolean
    'alloweditformdirect': True, #boolean
    'alloweditformcorrection': False, #boolean
    'alloweditformalternative': False, #boolean
    'alloweditformnew': True, #boolean
    'allowupload': True, #boolean
    'autodeclare': [
        ('entity', 'https://github.com/ahurriyetoglu/sinfexfolia/raw/master/sinfex-entities.foliaset.xml')
    ],
    'modes': [ ('editor','Annotation Editor')],
    'perspectives': ['event'],
    'slices': 'event:200',
}
}



#########################################


ADMINS = ( #Change to your contact details
    ('Maarten van Gompel', 'proycon@anaproy.nl'),
)

# Make this unique, and don't share it with anybody.
# IMPORTANT!!!! GENERATE A NEW SECRET KEY !!!! The default one here is *NOT*
# secret as it's publicly disclosed in the FLAT sources!
# (Use for instance http://www.miniwebtool.com/django-secret-key-generator/)
SECRET_KEY = 'ki5^nfv01@1g7(+*#l_0fmi9h&cf^_lv6bs4j9^6mpr&(%o4zk'






MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost','flat.science.ru.nl','applejack.science.ru.nl','spitfire','applejack']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = BASE_DIR + 'usermedia/' #not used

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://flat.science.ru.nl/usermedia/' #not used

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = BASE_DIR + '/flat/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

STYLE_ROOT = BASE_DIR + '/flat/style/'
STYLE_URL = '/style/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR + '/flat/style/',
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

LOGIN_URL = "/login/"


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'flat.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'flat.wsgi.application'

TEMPLATE_DIRS = [
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_DIR + 'flat/templates/'
]
for mode,_ in MODES:
    if os.path.isdir(BASE_DIR + '/modes/' + mode + '/templates/'):
        TEMPLATE_DIRS.append(BASE_DIR + '/modes/' + mode + '/templates/')

TEMPLATE_DIRS = tuple(TEMPLATE_DIRS)

if DJANGOVERSION[0] > 1 or DJANGOVERSION[1] >=8: #Django 1.8 and above
   TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': TEMPLATE_DIRS,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },]
   del TEMPLATE_DIRS
else:
    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )
    TEMPLATE_DEBUG = DEBUG



INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'flat.users'
]
for mode,_ in MODES:
    INSTALLED_APPS.append('flat.modes.' + mode)
INSTALLED_APPS = tuple(INSTALLED_APPS)


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
#}
