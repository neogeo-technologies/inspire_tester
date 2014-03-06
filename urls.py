# -*- coding: UTF-8 -*-

#  INSPIRE_tester Copyright 2011 Benjamin Chartier, Guillaume Sueur (Neogeo Technologies) 

#  This file is part of INSPIRE_tester.
#
#  INSPIRE_tester is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  INSPIRE_tester is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with INSPIRE_tester.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        (r'^index/', include('inspire_tester.wms_tester.urls')),
        (r'^admin/', include(admin.site.urls)),
        (r'^', include('inspire_tester.wms_tester.urls')),
    )

#if settings.DEBUG:
urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
        )
