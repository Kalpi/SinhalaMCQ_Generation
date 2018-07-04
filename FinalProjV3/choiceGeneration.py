from builtins import print
from owlready2 import *


class ChoicesGeneratingQueries:

    def __init__(self):
        my_world = World()
        my_world.get_ontology("file://static\\ontology\\root-ontology.owl").load()  # path to the owl file is given here
        # sync_reasoner(my_world)  # reasoner is started and synchronized here, reasoner name: HermiT
        self.graph = my_world.as_rdflib_graph()

    def search_by_concept(self, concept, query_type):
        parents = []
        children = []
        siblings = []
        sentences = []

        # class based queries
        # find the super class of a child
        query1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>" 
                  "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
                  "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                  "SELECT ?s ?label ?supertype" 
                  "WHERE {" 
                  "?s a owl:Class."
                  "?s rdfs:subClassOf ?supertype." 
                  "?supertype rdfs:label ?label."
                  "?s rdfs:label '"+concept+"'."
                  "}")

        query1_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>" 
                    "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
                    "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                    "SELECT ?s ?label ?supertype" 
                    "WHERE {" 
                    "?s a owl:Class."
                    "?s rdfs:subClassOf ?supertype." 
                    "?supertype rdfs:label ?label."
                    "?s rdfs:label '"+concept+"'@si."
                    "}")

        # find all the child classes of a parent class
        query2 = "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                 "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> " \
                 "SELECT DISTINCT ?s ?label ?subtype" \
                 "WHERE {" \
                 "{?subtype a owl:Class}." \
                 "{?subtype rdfs:subClassOf ?s}." \
                 "{?subtype rdfs:label ?label}" \
                 "{?s rdfs:label 'ජීවින්ට පොදු ලාක්ෂණික'}." \
                 "}"

        # find all the siblings of a class
        query3 = "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                 "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> " \
                 "SELECT DISTINCT ?s ?label ?subtype ?supertype" \
                 "WHERE {" \
                 "{?s a owl:Class}." \
                 "{?s rdfs:subClassOf ?supertype}." \
                 "{?subtype rdfs:subClassOf ?supertype}." \
                 "{?subtype rdfs:label ?label}" \
                 "{?s rdfs:label '"+concept+"'}." \
                 "}"

        # object properties based queries
        query4 = "PREFIX owl: <http://www.w3.org/2002/07/owl#>" \
                 "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> " \
                 "SELECT DISTINCT ?p_label ?r_label ?domain ?range ?property" \
                 "WHERE {" \
                 "{?property rdfs:domain ?domain}." \
                 "{?property rdfs:range ?range}." \
                 "{?range rdfs:label ?r_label}" \
                 "{?property rdfs:label ?p_label}" \
                 "{?domain rdfs:label '"+concept+"'}." \
                 "}"

        query4_1 = ("PREFIX owl: <http://www.w3.org/2002/07/owl#>"
                    "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                    "SELECT DISTINCT ?p_label ?r_label ?domain ?range ?property"
                    "WHERE {"
                    "?property rdfs:domain ?domain."
                    "?property rdfs:range ?range."
                    "?range rdfs:label ?r_label."
                    "?property rdfs:label ?p_label."
                    "?domain rdfs:label '"+concept+"'@si."
                    "}")

        # to get instance values of a class
        query5 = ("prefix owl: <http://www.w3.org/2002/07/owl#> "
                  "base <http://webprotege.stanford.edu/project/C25wqZ4qamhbITLmCGstJ0> "
                  "prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> "
                  "SELECT * WHERE { ?domain rdfs:label '"+concept+"' ;"
                  "rdfs:subClassOf [ owl:hasValue ?value ; "
                  "owl:onProperty [ rdfs:label ?property ] ] }")

        # query is being run
        if query_type == 1:
            parent = self.graph.query(query1)
            for item in parent:
                label = str(item['label'].toPython())
                label = re.sub(r'.*#', "", label)

                parents.append(label)

            parent = self.graph.query(query1_1)
            for item in parent:
                label = str(item['label'].toPython())
                label = re.sub(r'.*#', "", label)

                parents.append(label)
            return parents

        elif query_type == 2:
            children_list = self.graph.query(query2)
            for item in children_list:
                label = str(item['label'].toPython())
                label = re.sub(r'.*#', "", label)

                children.append(label)
            print(children)
            return children

        elif query_type == 3:
            sibling_list = self.graph.query(query3)
            for item in sibling_list:
                label = str(item['label'].toPython())
                label = re.sub(r'.*#', "", label)

                if not concept == label:
                    siblings.append(label)
            return siblings

        elif query_type == 4:
            domain_property_range = self.graph.query(query4)
            for item in domain_property_range:
                prop_label = str(item['p_label'].toPython())
                prop_label = re.sub(r'.*#', "", prop_label)

                ran_label = str(item['r_label'].toPython())
                ran_label = re.sub(r'.*#', "", ran_label)
                sentences.append({'subject': concept, 'object': ran_label, 'predicate': prop_label})

            domain_property_range2 = self.graph.query(query4_1)
            for item in domain_property_range2:
                prop_label = str(item['p_label'].toPython())
                prop_label = re.sub(r'.*#', "", prop_label)

                ran_label = str(item['r_label'].toPython())
                ran_label = re.sub(r'.*#', "", ran_label)
                sentences.append({'subject': concept, 'object': ran_label, 'predicate': prop_label})

            domain_property_range = self.graph.query(query5)
            for item in domain_property_range:
                val_label = str(item['value'].toPython())
                val_label = re.sub(r'.*#', "", val_label)

                prop_label = str(item['property'].toPython())
                prop_label = re.sub(r'.*#', "", prop_label)
                if re.match(r'^[0-9]$', val_label):
                    sentences.append({'subject': concept, 'object': prop_label, 'predicate': val_label+"කි"})
                else:
                    sentences.append({'subject': val_label, 'object': '', 'predicate': ''})
            # print(sentences)
            return sentences

        elif query_type == 5:
            domain_property_range = self.graph.query(query5)
            for item in domain_property_range:
                prop_label = str(item['property'].toPython())
                prop_label = re.sub(r'.*#', "", prop_label)

                value = str(item['value'].toPython())
                value = re.sub(r'.*#', "", value)

                if re.match(r'^[0-9]$', value):
                    value = int(value)
                    sentences.append({'subject': concept, 'predicate': prop_label, 'value': value})
            # print(sentences)
            return sentences


generateChoices = ChoicesGeneratingQueries()
# generateChoices.search_by_concept('ඌනන විභාජනය', 4)
