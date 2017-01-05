#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'DIANA HEP'
SITENAME = u'DIANA HEP'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
			('Team','/pages/team.html'),
      ('Activities','/pages/activities.html'),
			('DIANA Fellows','/pages/fellows.html'),
            ('Blog','/category/blog.html')
			)

# Blogroll
LINKS =  (('ROOT', 'https://root.cern.ch/drupal/'),
		  ('NSF SI2','http://www.nsf.gov/funding/pgm_summ.jsp?pims_id=504817'),
		  ('S2I2-HEP','http://s2i2-hep.org/'),
		  ('Jetscape','http://jetscape.wayne.edu/'),
		  ('rootpy','http://www.rootpy.org'),
		  ('scikit-learn','http://scikit-learn.org/stable/'),
		  ('RooStats','https://twiki.cern.ch/twiki/bin/view/RooStats/WebHome'),
		  )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/diana_hep'),
          ('github', 'http://github.com/diana-hep'),
          ('Indico', 'https://indico.cern.ch/category/7192/'),
          ('Google Group', 'https://groups.google.com/forum/#!forum/diana-hep'),
          ('Vidyo Room', 'https://vidyoportal.cern.ch/flex.html?roomdirect.html&key=g24IFWEdhejzHVy851PztEh82e4'),)

CC_LICENSE="CC-BY"


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False


DISPLAY_TAGS_ON_SIDEBAR=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True


THEME = 'pelican-bootstrap3'
#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+

#For pelican-ootstrap3
BOOTSTRAP_THEME='simplex'
#BOOTSTRAP_THEME='yeti'
#BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
BOOTSTRAP_THEME='cosmo'
#BOOTSTRAP_THEME='paper'
DISPLAY_BREADCRUMBS=False

BOOTSTRAP_NAVBAR_INVERSE =True
BANNER="images/diana-hep-06-banner.png"
BANNER_TITLE=None
BANNER_SUBTITLE = None
BANNER_ALL_PAGES = False



#custom CSS
CUSTOM_CSS = 'static/custom.css'


#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')

PATH = 'content'
ARTICLE_PATHS = ['blog']

STATIC_PATHS = ['images','css', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'pages/projects', 'favicon.png']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'static/custom.css'}
}

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
FAVICON= "images/favicon.ico"

PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
#			'liquid_tags.youtube', 'render_math',
#           'liquid_tags.include_code', 'liquid_tags.notebook',
#           'liquid_tags.literal', 'tipue_search']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
			'liquid_tags.youtube', 'render_math',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


# comments
DISQUS_SITENAME="diana-hep"

''' For reference, this code
<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 'diana-hep';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
'''

