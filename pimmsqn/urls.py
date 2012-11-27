# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pimmsqn.apps.qn.feeds import DocFeed

# this is not actually correct, since strictly we need hexadecimal following this pattern
uuid='\w\w\w\w\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w-\w\w\w\w\w\w\w\w\w\w\w\w'

urlpatterns = patterns('',
    # Example:
    # (r'^pimmsqn/', include('pimmsqn.foo.urls')),
    (r'^$','pimmsqn.apps.qn.views.centres'),
    (r'^cmip5/$','pimmsqn.apps.qn.views.centres'),
    (r'^cmip5/centres/$','pimmsqn.apps.qn.views.centres'),
    (r'^cmip5/(?P<centre_id>\d+)/$','pimmsqn.apps.qn.views.centre'),
    # 
    url(r'^cmip5/authz/$','pimmsqn.apps.qn.views.authorisation',name='security'),
    #        
    # ajax vocabulary handler
    url(r'^ajax/vocabs/(?P<vocabName>\D+)/$','pimmsqn.apps.qn.views.completionHelper', 
                                                name='ajax_value'),
    url(r'^ajax/autocomplete/modelname/$', 'pimmsqn.apps.qn.views.autocomplete_model', 
                                                name='autocomplete_model'),
    #
    # generic document handling
    # 
    (r'^cmip5/(?P<cid>\d+)/(?P<docType>\D+)/doc/(?P<pkid>\d+)/(?P<method>\D+)/$','pimmsqn.apps.qn.views.genericDoc'),  
    (r'^cmip5/(?P<docType>\D+)/(?P<uri>%s)/$'%uuid,'pimmsqn.apps.qn.views.persistedDoc'),
    (r'^cmip5/(?P<docType>\D+)/(?P<uri>%s)/(?P<version>\d+)/$'%uuid,'pimmsqn.apps.qn.views.persistedDoc'),                     
    # 
    # COMPONENTS:
    #   
    (r'^cmip5/(?P<centre_id>\d+)/component/add/$','pimmsqn.apps.qn.views.componentAdd'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/edit/$','pimmsqn.apps.qn.views.componentEdit'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/addsub/$','pimmsqn.apps.qn.views.componentSub'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/refs/$','pimmsqn.apps.qn.views.componentRefs'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/coupling/$','pimmsqn.apps.qn.views.componentCup'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/Inputs/$','pimmsqn.apps.qn.views.componentInp'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/copy/$','pimmsqn.apps.qn.views.componentCopy'),
    (r'^cmip5/(?P<centre_id>\d+)/component/(?P<component_id>\d+)/text/$','pimmsqn.apps.qn.views.componentTxt'),
    #
    # SIMULATIONS
    #
    (r'^cmip5/(?P<centre_id>\d+)/simulation/list/$',
                'pimmsqn.apps.qn.views.simulationList'),  
    (r'^cmip5/(?P<centre_id>\d+)/simulation/add/(?P<experiment_id>\d+)/$',
                'pimmsqn.apps.qn.views.simulationAdd'),
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/edit/$',
                'pimmsqn.apps.qn.views.simulationEdit'),  
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/coupling/$',
                'pimmsqn.apps.qn.views.simulationCup'), 
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/coupling/(?P<coupling_id>\d+)/(?P<ctype>\D+)/$',
                'pimmsqn.apps.qn.views.simulationCup'),  
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/conformance/$',
                'pimmsqn.apps.qn.views.conformanceMain'),  
    (r'^cmip5/(?P<centre_id>\d+)/simulation/copy/$',
                'pimmsqn.apps.qn.views.simulationCopy'),
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/copyind/$',
                'pimmsqn.apps.qn.views.simulationCopyInd'),
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/resetCouplings/$',
                'pimmsqn.apps.qn.views.simulationCupReset'), 
    (r'^cmip5/(?P<centre_id>\d+)/simulation/(?P<simulation_id>\d+)/delete/$',
                'pimmsqn.apps.qn.views.simulationDel'),
    # 
    # GRIDS:
    #   
    (r'^cmip5/(?P<centre_id>\d+)/grid/add/$','pimmsqn.apps.qn.views.gridAdd'),
    (r'^cmip5/(?P<centre_id>\d+)/grid/(?P<grid_id>\d+)/copy/$','pimmsqn.apps.qn.views.gridCopy'),
    (r'^cmip5/(?P<centre_id>\d+)/grid/(?P<grid_id>\d+)/edit/$','pimmsqn.apps.qn.views.gridEdit'),
    (r'^cmip5/(?P<centre_id>\d+)/grid/(?P<grid_id>\d+)/refs/$','pimmsqn.apps.qn.views.gridRefs'),             
    #           
    # platforms/add/centre_id
    # platforms/edit/platform_id
    #
    (r'^cmip5/(?P<centre_id>\d+)/platform/add/$',
            'pimmsqn.apps.qn.views.platformEdit'),
    (r'^cmip5/(?P<centre_id>\d+)/platform/(?P<platform_id>\d+)/edit/$',
            'pimmsqn.apps.qn.views.platformEdit'),
    #
    # experiment/view/experiment_id
    (r'^cmip5/(?P<cen_id>\d+)/experiment/(?P<experiment_id>\d+)/$',
            'pimmsqn.apps.qn.views.viewExperiment'),
    
    # cmip5/conformance/centre_id/simulation_id/requirement_id/$
    (r'^cmip5/conformance/(?P<cen_id>\d+)/(?P<sim_id>\d+)/(?P<req_id>\d+)/$',
            'pimmsqn.apps.qn.views.conformanceEdit'),  
                     
    # help, intro, about, vn history
    (r'^cmip5/(?P<cen_id>\d+)/help/$',
            'pimmsqn.apps.qn.views.help'),
    (r'^cmip5/(?P<cen_id>\d+)/vnhist/$',
            'pimmsqn.apps.qn.views.vnhist'),
    (r'^cmip5/(?P<cen_id>\d+)/trans/$',
            'pimmsqn.apps.qn.views.trans'),              
    (r'^cmip5/(?P<cen_id>\d+)/about/$',
            'pimmsqn.apps.qn.views.about'),     
    (r'^cmip5/(?P<cen_id>\d+)/intro/$',
            'pimmsqn.apps.qn.views.intro'),                       
    # ensembles ...
    (r'^cmip5/(?P<cen_id>\d+)/(?P<sim_id>\d+)/ensemble/$',
            'pimmsqn.apps.qn.views.ensemble'),
    (r'^cmip5/(?P<cen_id>\d+)/(?P<sim_id>\d+)/ensemble/(?P<ens_id>\d+)/$',
            'pimmsqn.apps.qn.views.ensemble'),                                               
                          
    #### generic simple views
    # DELETE
    (r'^cmip5/(?P<cen_id>\d+)/delete/(?P<resourceType>\D+)/(?P<resource_id>\d+)/(?P<returnType>\D+)/$',
            'pimmsqn.apps.qn.views.delete'),
    (r'^cmip5/(?P<cen_id>\d+)/delete/(?P<resourceType>\D+)/(?P<resource_id>\d+)/(?P<targetType>\D+)/(?P<target_id>\d+)/(?P<returnType>\D+)/$',
            'pimmsqn.apps.qn.views.delete'),      
    # EDIT
    # pimmsqn/centre_id/edit/resourceType/resourceID/returnType  (resourceID=0, blank form)
    (r'^cmip5/(?P<cen_id>\d+)/edit/(?P<resourceType>\D+)/(?P<resource_id>\d+)/(?P<returnType>\D+)/$',
            'pimmsqn.apps.qn.views.edit'),
    # pimmsqn/centre_id/edit/resourceType/resourceID/targetType/targetID/returnType  
        #(resourceID=0, blank form)
    (r'^cmip5/(?P<cen_id>\d+)/edit/(?P<resourceType>\D+)/(?P<resource_id>\d+)/(?P<targetType>\D+)/(?P<target_id>\d+)/(?P<returnType>\D+)/$',
            'pimmsqn.apps.qn.views.edit'),
    # LIST
    (r'^cmip5/(?P<cen_id>\d+)/list/(?P<resourceType>\D+)/$',
            'pimmsqn.apps.qn.views.list'),
    (r'^cmip5/(?P<cen_id>\d+)/list/(?P<resourceType>\D+)/(?P<targetType>\D+)/(?P<target_id>\d+)$',
            'pimmsqn.apps.qn.views.list'),
    (r'^cmip5/(?P<cen_id>\d+)/filterlist/(?P<resourceType>\D+)$',
            'pimmsqn.apps.qn.views.filterlist'),
    # ASSIGN            
    (r'^cmip5/(?P<cen_id>\d+)/assign/(?P<resourceType>\D+)/(?P<targetType>\D+)/(?P<target_id>\d+)/$',
            'pimmsqn.apps.qn.views.assign'),       
            
    # export files to CMIP5
    (r'^cmip5/(?P<cen_id>\d+)/exportFiles/$','pimmsqn.apps.qn.views.exportFiles'), 
    (r'^cmip5/testFile/(?P<fname>.+)$','pimmsqn.apps.qn.views.testFile'),
        
            # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
    # Vocabs
    url(r'^cmip5/vocab/$','pimmsqn.apps.qn.vocab.list',name="vocab_display"),
    (r'^cmip5/vocab/(?P<vocabID>\d+)/$','pimmsqn.apps.qn.vocab.show'),
    #(r'^cmip5/vocab/(?P<docID>\d+)/(?P<valID>\d+)/$','pimmsqn.apps.qn.vocab.list'),
        
    # Atom Feeds
    (r'^feeds/(.*)/$', "django.contrib.syndication.views.feed", {
        "feed_dict": {"cmip5": DocFeed,}
        }
    ),

    # Admin
    (r'', include('pimmsqn.apps.qn.admin.urls')),
    #(r'^admin/qn/component/copy/$', 'pimmsqn.apps.qn.admin.admin_views.modelcopy'),
    (r'^cmip5/admin/', include(admin.site.urls)),

)


# now add the common document url methods
#for doc in ['experiment','platform','component','simulation']:
#    for key in ['validate','view','xml','html','export']:
#        urlpatterns+=patterns('',(r'^cmip5/(?P<centre_id>\d+)/%s/(?P<%s_id>\d+)/%s/$'%(doc,doc,key),'pimmsqn.apps.qn.views.doc'))
                    
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True }),
    (r'^media/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),
    )

