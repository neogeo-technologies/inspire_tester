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

from django.contrib.gis.db import models

class WMSService(models.Model):
    name = models.CharField(max_length=200)
    uri = models.CharField(max_length=300)
    wgs84_boundingbox = models.MultiPolygonField(null=True)
    cap_cache = models.TextField(blank=True, null=True)
    cap_cache_date = models.DateTimeField(auto_now=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name
    
#class Evaluation(models.Model):
#    service = models.ForeignKey(WMSService)
#    datetime = models.DateTimeField()
#    success = models.IntegerField()
#    score = models.IntegerField()
#    report = models.URLField(max_length=200)
#    
#    def __unicode__(self):
#        return u"%s - %s" % (self.service.name, self.datetime)
