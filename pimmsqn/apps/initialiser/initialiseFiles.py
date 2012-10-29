from qn.models import *
import csv
from django.conf import settings
logging=settings.LOG

def initialiseFiles():
    ''' 
    This routine initialises the database with some obvious files for 
    boundary conditoins etc 
    '''
    
    FilesCSVinfo = csv.reader(open('static/data/References/Files_CSV.csv'), 
                              delimiter=';', quotechar='|')
    
    # this is the vocab that we always use for reference types:
    v=Vocab.objects.get(name='FileFormats')
    # loop over all references in spreadsheet
    for row in FilesCSVinfo:
        # format is being read into the tuple only for convenience at the moment 
        # but is overwritten
        abbrev,name,link,filetype,description=tuple(row)
        logging.debug(name+filetype)
        # find out what file type
        #filetype='Other'
        try:
            formattype=Term.objects.filter(vocab=v).get(name=filetype)
        except:
            logging.info('Ignoring file %s'%name)
            break  # leave the loop
        # find the other things: name, description, link    
        f=DataContainer(
                    abbrev=abbrev,
                    title=name,
                    link=link,
                    description=description,
                    format=formattype)
        try:
            f.save()
        except Exception,e:
            logging.info('Unable to save file %s (%s)'%(name,e))
    
if __name__=="__main__":
    initialiseFiles()    