from collections import defaultdict 

class Lemma():
    '''
    methods to access and manipulate resource lemma based
    '''
    def __init__(self):
        pass
    
    def lemmas_generator(self,pos=None):
        '''
        return dict of all lemmas

        @type  pos: str
        @param pos: noun | verb. 
        Default is None, then no filtering is performed.
        '''
        lemmas = defaultdict(int)
        
        for le_obj in self.les_get_generator():
            lemma = le_obj.get_lemma()
            
            if pos:
                part_of_speech = le_obj.get_pos()
                if pos == part_of_speech:
                    lemmas[lemma] += 1
    
            else:
                lemmas[lemma] += 1
        
        return lemmas

    def lemma_get_generator(self,lemma,pos=None,ignore_case=False):
        '''
        return generator of Le class instances
        
        @type  lemma: str
        @param lemma: lemma
        
        @type  pos: str
        @param pos: noun | verb. 
        Default is None, then no filtering is performed.
        
        @rtype: list
        @return: list of Le class instances

        Added by AN:
        @param ignore_case: True | False
        @type ignore_case: bool
        Default is False. If ignore_case True returns lemmas ignoring case
        '''
        if ignore_case == False:
            
            les = []
            
            for le_obj in self.les_get_generator():
                can_lemma = le_obj.get_lemma()
                
                if can_lemma == lemma:
                    
                    if pos:
                        part_of_speech = le_obj.get_pos()
                        if pos == part_of_speech:
                            les.append(le_obj)
        
                    else:
                        les.append(le_obj)
        else:
            les = []
            for le_obj in self.les_get_generator():
                can_lemma = le_obj.get_lemma()
            
                if can_lemma.lower() == lemma.lower():
                
                    if pos:
                        part_of_speech = le_obj.get_pos()
                        if pos == part_of_speech:
                            les.append(le_obj)
        
                    else:
                        les.append(le_obj)

        return les
    
    def lemma_num_senses(self,lemma,pos=None):
        '''
        return number of senses
        
        @type  lemma: str
        @param lemma: lemma
        
        @type  pos: str
        @param pos: noun | verb. 
        Default is None, then no filtering is performed.
        
        @rtype: int
        @return: number of senses
        '''
        return len(self.lemma_get_generator(lemma, pos))
    
    
    def lemma_highest_sense_number(self,lemma,pos=None):
        '''
        return highest sense number of le instances of lemma
        
        @type  lemma: str
        @param lemma: lemma
        
        @type  pos: str
        @param pos: noun | verb. 
        Default is None, then no filtering is performed.
        
        @rtype: int
        @return: highest sense number
        '''
        highest = 0
        for le_obj in self.lemma_get_generator(lemma, pos):
            sense_id = int(le_obj.get_sense_number())
            
            if sense_id > highest:
                highest = sense_id
        
        return highest
    
