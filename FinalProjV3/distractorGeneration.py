from builtins import print
from owlready2 import *

keywords = ['ෙසෙල', 'ෙසෙල වාදය', 'වර්ණදේහ']


class DistractorGeneratingQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("file://static\\ontology\\root-ontology.owl").load()  # path to the owl file is given here
        self.graph = my_world.as_rdflib_graph()

    def generate_distractors(self, search_word, query_type):
        distractor_phrases = []
        siblings = []

        distractor1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                       "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                       "SELECT DISTINCT ?p_label ?r_label ?domain ?range ?property"
                       "WHERE {"
                       "?property rdfs:domain ?domain."
                       "?property rdfs:range ?range."
                       "?range rdfs:label ?r_label."
                       "?property rdfs:label ?p_label."
                       "?domain rdfs:label '"+search_word+"'@si."
                       "}")

        distractor1_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                         "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                         "SELECT DISTINCT ?p_label ?r_label ?domain ?range ?property"
                         "WHERE {"
                         "?property rdfs:domain ?domain."
                         "?property rdfs:range ?range."
                         "?range rdfs:label ?r_label."
                         "?property rdfs:label ?p_label."
                         "?domain rdfs:label '"+search_word+"'."
                         "}")

        distractor2 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>" 
                       "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> " 
                       "SELECT DISTINCT ?sib_label ?p_label ?r_label ?sib_domain ?range ?property ?supertype" 
                       "WHERE {" 
                       "?domain rdfs:subClassOf ?supertype."
                       "?sib_domain rdfs:subClassOf ?supertype."
                       "?sib_domain rdfs:label ?sib_label."
                               
                       "?property rdfs:domain ?sib_domain."
                       "?property rdfs:range ?range."
                       "?range rdfs:label ?r_label." 
                       "?property rdfs:label ?p_label."
                       "?domain rdfs:label '"+search_word+"'." 
                       "}")

        distractor2_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                         "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                         "SELECT DISTINCT ?sib_label ?p_label ?r_label ?sib_domain ?range ?property ?supertype"
                         "WHERE {"
                         "?domain rdfs:subClassOf ?supertype."
                         "?sib_domain rdfs:subClassOf ?supertype."
                         "?sib_domain rdfs:label ?sib_label."
                               
                         "?property rdfs:domain ?sib_domain."
                         "?property rdfs:range ?range."
                         "?range rdfs:label ?r_label."
                         "?property rdfs:label ?p_label."
                         "?domain rdfs:label '"+search_word+"'@si."
                         "}")

        # siblings
        distractor3 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                       "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                       "SELECT DISTINCT ?s ?label ?subtype ?supertype"
                       "WHERE {"
                       "?s rdfs:subClassOf ?supertype."
                       "?subtype rdfs:subClassOf ?supertype."
                       "?subtype rdfs:label ?label."
                       "?s rdfs:label '"+search_word+"'."
                       "}")

        distractor3_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                         "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                         "SELECT DISTINCT ?s ?label ?subtype ?supertype"
                         "WHERE {"
                         "?s rdfs:subClassOf ?supertype."
                         "?subtype rdfs:subClassOf ?supertype."
                         "?subtype rdfs:label ?label."
                         "?s rdfs:label '"+search_word+"'@si."
                         "}")

        distractor4 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                       "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                       "SELECT DISTINCT ?s ?label ?subtype ?supertype"
                       "WHERE {"
                       "?s rdfs:subClassOf ?supertype."
                       "?subtype rdfs:subClassOf ?supertype."
                       "?subtype rdfs:label ?label."
                       "?s rdfs:label '"+search_word+"'."
                       "}")

        distractor4_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                         "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                         "SELECT DISTINCT ?s ?label ?subtype ?supertype"
                         "WHERE {"
                         "?s rdfs:subClassOf ?supertype."
                         "?subtype rdfs:subClassOf ?supertype."
                         "?subtype rdfs:label ?label."
                         "?s rdfs:label '"+search_word+"'@si."
                         "}")

        if query_type == 1:
            sibling_list = self.graph.query(distractor4)
            for item in sibling_list:
                label = str(item['label'].toPython())
                label = re.sub(r'.*#', "", label)

                if not search_word == label:
                    siblings.append(label)
            if not siblings:
                sibling_list = self.graph.query(distractor4_1)
                for item in sibling_list:
                    label = str(item['label'].toPython())
                    label = re.sub(r'.*#', "", label)

                    if not search_word == label:
                        siblings.append(label)
            return siblings
        else:
            domain_property_range = self.graph.query(distractor2)
            for item in domain_property_range:
                sib_label = str(item['sib_label'].toPython())
                sib_label = re.sub(r'.*#', "", sib_label)

                prop_label = str(item['p_label'].toPython())
                prop_label = re.sub(r'.*#', "", prop_label)

                ran_label = str(item['r_label'].toPython())
                ran_label = re.sub(r'.*#', "", ran_label)

                if not sib_label == search_word:
                    if ran_label == search_word:
                        distractor_phrases.append({'subject': sib_label, 'object': ran_label,
                                                   'predicate': prop_label})
                    else:
                        distractor_phrases.append({'subject': search_word, 'object': ran_label,
                                                   'predicate': prop_label})
            if not distractor_phrases:
                domain_property_range2 = self.graph.query(distractor2_1)
                for item in domain_property_range2:
                    sib_label = str(item['sib_label'].toPython())
                    sib_label = re.sub(r'.*#', "", sib_label)

                    prop_label = str(item['p_label'].toPython())
                    prop_label = re.sub(r'.*#', "", prop_label)

                    ran_label = str(item['r_label'].toPython())
                    ran_label = re.sub(r'.*#', "", ran_label)

                    if not sib_label == search_word:
                        if ran_label == search_word:
                            distractor_phrases.append({'subject': ran_label, 'object': sib_label,
                                                       'predicate': prop_label})
                        else:
                            distractor_phrases.append({'subject': search_word, 'object': ran_label,
                                                       'predicate': prop_label})
            print(distractor_phrases)
            return distractor_phrases


generateDistractors = DistractorGeneratingQueries()
# generateDistractors.generate_distractors("රළු අන්තඃප්ලාස්මීය ජාලිකා", 3)
