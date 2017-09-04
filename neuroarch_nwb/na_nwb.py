import nwb
from nwb.validate import validate_file
import h5py

class NWB_file(object):
    def __init__(self,filename,validate=False):
        
        self.filename = filename

        # validate if the file supplied is a valid nwb file
        if validate:
            v = validate_file( self.filename )
            assert v['errors'] == 0
            
        # open the file
        self.nwb = h5py.File(self.filename)


    def close( self ):
        self.nwb.close()

    def validate_nwb_file( self ):
        return validate_file( self.filename )  
    
    def get_metadata( self ):
        #TODO: clean up. This will only allow for a one level dictionary, with scalar values
        
        return  { k : v[()] for k,v in self.nwb['general'].iteritems() if type(v) == h5py._hl.dataset.Dataset }
    
    def get_dataset_from_path( self , path ):
        # eg ['/acquisition/timeseries']
        
        return NWB_dataset(self.nwb[path])

class NWB_dataset(object):
    # A class to hold a dataset and the required simple functions
    # TODO: Expand to non 1D arrays
    
    def __init__(self, dataset):
        """ A dataset has three keys: """
        self.dataset = dataset
        self.num_samples = self.dataset['num_samples'][()]

            
    def get_data( self ):
        """ Return the whole dataset """
        
        return  {
                    'data': self.dataset['data'][:],
                    'timestamps' : self.dataset['timestamps'][:]
                }
    
    def get_data_slice( self , steps = 1000, start = 0 ):
        """ return a slice of dataset """

        return {
                  'data': self.dataset['data'][start:steps],
                  'timestamps' : self.dataset['timestamps'][start:steps]
                }
    
    def get_data_downsampled( self , sample_length = 1000 ):
        """ return a downsampled array to fit length """

        return {
                  'data': self.dataset['data'][0:self.num_samples:self.num_samples/sample_length],
                  'timestamps' : self.dataset['timestamps'][0:self.num_samples:self.num_samples/sample_length]
                }
    
    
    
    