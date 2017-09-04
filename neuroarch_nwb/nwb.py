import nwb

class NWB(object):
    def __init__(self):
        pass

    def validate_nwb_file( self, nl_string, user='test', format_type=None, spell_correct=True ):
        """ Process an input NL string. Attempt to translate it to NeuroArch-speak.
            The translator assumes 'morphology' is the default output format,
            but if the user inputs a specific format (i.e. outside of the NL query),
            then that setting will be considered "disambiguating" and will be used.
        """
        pass
  
