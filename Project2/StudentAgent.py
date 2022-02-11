"""
ADD YOUR CODE HERE

Please read project directions before importing anything
"""


import common


class StudentAgent:
    global helpingVerbs, questionWords, subjectPronouns, determinerWords, prepositions, possessivePronouns, conjuctions, \
        classifiedWords, noun, number, verb, adverb, object, adjective
    helpingVerbs = ['Be', 'am', 'is', 'are', 'was', 'Were', 'been', 'Being', 'have', 'has', 'had', 'Could', 'should', 'must',
                    'may', 'might', 'Must', 'can', 'Will', 'would', 'do', 'did', 'does']

    noun = ['ai', 'week', 'day', 'end', 'agents', 'time', 'skills', 'weeks', 'days', 'weight', 'total', 'process',
            'canvas', 'pdf', 'zip', 'file', 'report', 'specification', 'procedure', 'class', 'abilities', 'question',
            'piazza', 'forum', 'artificial', 'issues', 'log', 'times', 'goals', 'concepts', 'methods', 'discussions',
            'intelligence', 'collaboration', 'submissions', 'announcements', 'beginning', 'relationship', 'percentage',
            'human', 'cognition', 'questions']

    number = ['4', '1', 'second', '3', '2', '6', '7', 'third','8', '9', '10', '13', '4%', '15%', '20%', 'two', 'three',
              'first']

    object = ['project', 'midterm', 'final', 'assignment']

    adjective = ['specific', 'important', 'daily', 'primary', 'prominent', 'knowledge-based']

    verb = ['released', 'begin', 'design', 'start', 'occurs', 'starts', 'open', 'due', 'need', 'needed', 'turned',
            'apply', 'submit', 'turn', 'close', 'complete', 'finish', 'write', 'code', 'study', 'grade', 'worth',
            'contribute', 'contributing', 'get', 'go', 'getting', 'answering', 'use', 'possible', 'learning',
            'organized', 'teaches', 'distributed', 'download', 'submitted', 'completed', 'submitting', 'answered']

    adverb = ['not', 'know', 'available', 'working', 'much', 'there', 'long', 'many', 'regularly', 'frequently',
              'around', 'least']

    questionWords = ['What', 'When', 'How', 'Where']

    subjectPronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'you', 'they','anyone', 'anybody', 'everyone', 'everybody',
                       'someone', 'somebody']

    determinerWords = ['a', 'an', 'the', 'every', 'this', 'those', 'many', 'that']

    prepositions = ['after', 'in', 'to', 'on', 'with', 'of', 'for', 'during', 'at', 'by', 'as', 'into', 'between']

    possessivePronouns = ['my', 'mine', 'your', 'yours', 'his', 'her', 'hers', 'its', 'our', 'ours', 'your', 'yours',
                          'their', 'theirs']

    conjuctions = ['and', 'because', 'but', 'if', 'or', 'when']

    classifiedWords = ['helping verb', 'question word', 'preposition', 'determiner word', 'conjuction',
                       'possessive pronoun', 'subject pronoun', 'verb', 'adverb', 'noun', 'adjective', 'number']

    def __init__(self, verbose):
        self._verbose = verbose

        # TODO: Add your init code here
        return

    def toStringList(self, char_list):
        word_list = []
        a = 0
        #print(char_list)
        for x in range(len(char_list)):
            if char_list[x] == ' ':
                word_list.append(char_list[a:x])
                a=x+1

            if(x==len(char_list)-1):
                word_list.append(char_list[a:x+1])

        return word_list

    def removeHelpingVerb(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(helpingVerbs)):
                word = word_list[x].lower()
                hv = helpingVerbs[y].lower()
                boole = (word == hv)
                if(boole):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "helping verb"
                    return self.removeHelpingVerb(word_list)
        return word_list

    def removeQuestionWords(self, word_list):
        for y in range (len(word_list)):
            for x in range(len(questionWords)):
                if (word_list[y].lower() == questionWords[x].lower()):
                    word_list[y] = "question word"
        return word_list


    def removeSubjectPronouns(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(subjectPronouns)):
                if(word_list[x].lower() == subjectPronouns[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "subject pronoun"
                    return self.removeSubjectPronouns(word_list)
        return word_list

    def removeDeterminerWords(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(determinerWords)):
                if(word_list[x].lower() == determinerWords[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "determiner word"
                    return self.removeDeterminerWords(word_list)
        return word_list

    def removePrepositions(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(prepositions)):
                if(word_list[x].lower() == prepositions[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "preposition"
                    return self.removePrepositions(word_list)
        return word_list

    def removePossessivePronouns(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(possessivePronouns)):
                if(word_list[x].lower() == possessivePronouns[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "possessive pronoun"
                    return self.removePossessivePronouns(word_list)
        return word_list

    def removeConjuctions(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(conjuctions)):
                if(word_list[x].lower() == conjuctions[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "conjuction"
                    return self.removeConjuctions(word_list)
        return word_list

    def removeVerbs(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(verb)):
                if (word_list[x].lower() == verb[y].lower()):
                    # print(word_list[x])
                    # word_list.remove(word_list[x])
                    word_list[x] = "verb"
        return word_list

    def removeAdverbs(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(adverb)):
                if (word_list[x].lower() == adverb[y].lower()):
                    # print(word_list[x])
                    # word_list.remove(word_list[x])
                    word_list[x] = "adverb"
                    #return self.removeAdverbs(word_list)
        return word_list

    def removeAdjectives(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(adjective)):
                if (word_list[x].lower() == adjective[y].lower()):
                    # print(word_list[x])
                    # word_list.remove(word_list[x])
                    word_list[x] = "adjective"
                    #return self.removeAdjectives(word_list)
        return word_list

    def removeNouns(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(noun)):
                if (word_list[x].lower() == noun[y].lower()):
                    # print(word_list[x])
                    # word_list.remove(word_list[x])
                    word_list[x] = "noun"
                    #return self.removeNouns(word_list)
        return word_list

    def notClassified(self, word_list, index):
        for x in range(len(classifiedWords)):
            if(word_list[index].lower()==classifiedWords[x].lower()):
                return False
        return True

    def returnRemaining(self,word_list, classification_list):
        result = ''
        for x in range(len(word_list)):
            if(self.notClassified(classification_list,x)):
                if(len(result)>1):
                    result = result+' '+word_list[x]
                else:
                    result=word_list[x]
        #print(result)
        return result

    def removeJargon(self, word_list, jargon):
        for x in range(len(word_list)):
            if(self.notClassified(word_list,x)):
                for y in range(len(jargon)):
                    if(len(word_list[x])>=len(jargon[y])):
                        if(word_list[x][:len(jargon[y])]==jargon[y]):
                            word_list[x] = 'jargon'
        return word_list

    def removeBetweenQandV(self, word_list):
        hvIndex = [i for i, x in enumerate(word_list) if x == "helping verb"]
        qIndex = [j for j, x in enumerate(word_list) if x == "question word"]

        if(len(hvIndex)>0):
            for x in range(hvIndex[0]):
                if(self.notClassified(word_list, x)):
                    word_list[x] = 'not object'

        return word_list

    def removeNumbers(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(number)):
                if (word_list[x].lower() == number[y].lower()):
                    if(x>0 and x<(len(word_list)-1)):
                        check = True
                        for z in range(len(object)):
                            if(word_list[x+1].lower() == object[z].lower()):
                                check = False
                            if (word_list[x - 1].lower() == object[z].lower()):
                                check = False
                        if(check):
                            word_list[x] = 'number'
                    elif(x==0 and x<(len(word_list)-1)):
                        check = True
                        for z in range(len(object)):
                            if (word_list[x + 1].lower() == object[z].lower()):
                                check = False
                        if (check):
                            word_list[x] = 'number'

                    elif (x > 0 and x == (len(word_list) - 1)):
                        check = True
                        for z in range(len(object)):
                            if (word_list[x - 1].lower() == object[z].lower()):
                                check = False
                        if (check):
                            word_list[x] = 'number'
        return word_list

        return word_list

    def getObject(self, word_list):
        classification_list=word_list.copy()
        classification_list=self.removeHelpingVerb(classification_list)
        classification_list=self.removeQuestionWords(classification_list)
        classification_list=self.removeSubjectPronouns(classification_list)
        classification_list=self.removeDeterminerWords(classification_list)
        classification_list=self.removePrepositions(classification_list)
        classification_list=self.removeConjuctions(classification_list)
        classification_list=self.removePossessivePronouns(classification_list)
        classification_list=self.removeVerbs(classification_list)
        classification_list = self.removeAdjectives(classification_list)
        classification_list = self.removeAdverbs(classification_list)
        classification_list = self.removeNouns(classification_list)
        classification_list = self.removeNumbers(classification_list)
        # classification_list=self.removeBetweenQandV(classification_list)
        #print(word_list)

        # if(word_list[0].lower()=='when'):
        #     self.removeJargon(classification_list,['due','release','date'])
        #
        # elif(word_list[0].lower()=='where'):
        #     self.removeJargon(classification_list,['locat','specified'])
        #
        # elif (word_list[0].lower() == 'what'):
        #     self.removeJargon(classification_list, ['due','release','date', 'worth', 'percentage', 'procedure', 'process', 'locat', 'weigh', 'grade', 'specified'])
        #
        # elif (word_list[0].lower() == 'how'):
        #     self.removeJargon(classification_list, ['worth', 'weigh', 'grade'])



        #print(classification_list)
        return self.returnRemaining(word_list,classification_list)

    def hasWord(self,word_list,search_for):
        for x in range(len(word_list)):
            for y in range(len(search_for)):
                if(search_for=='1'):
                    if(search_for==word_list[x]):
                        return True
                elif(len(word_list[x])>=len(search_for[y]) and search_for != '1'):
                    if(word_list[x][:len(search_for[y])].lower()==search_for[y].lower()):
                        return True
        return False


    def getDataRequested(self,word_list):
        if(word_list[0].lower() == 'when'):
            if(self.hasWord(word_list,['due','turn', 'submit', 'complete','submissions'])):
                return 'DUEDATE'
            else:
                return 'RELEASEDATE'

        elif (word_list[0].lower() == 'where'):
            return 'PROCESS'

        elif (word_list[0].lower() == 'how'):
            if(word_list[1].lower()=='many' or word_list[1].lower()=='long' or (word_list[1].lower()=='much' and word_list[2].lower()=='time')):
                return 'DURATION'
            elif(word_list[1].lower()=='do'):
                return 'PROCESS'
            else:
                return 'WEIGHT'
        elif (word_list[0].lower() == 'what'):
            if(self.hasWord(word_list,['due','turn'])):
                return 'DUEDATE'
            elif(self.hasWord(word_list, ['release','midterm','final','start'])
                 and not self.hasWord(word_list, ['process','procedure','weigh','worth','percent'])):
                return 'RELEASEDATE'
            elif(self.hasWord(word_list, ['weigh','worth','percent'])):
                return 'WEIGHT'
            else:
                return 'PROCESS'

    def getIntent(self, question_object, data_requested, word_list):

        if(word_list[0].lower()=='what'):
            if (self.hasWord(word_list, ['project']) and self.hasWord(word_list, ['weigh', 'worth', 'percentage'])
                    and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['3','4','5'])):
                    return 26
                if (self.hasWord(word_list, ['8','9','10'])):
                    return 29
                if (self.hasWord(word_list, ['12','13','14'])):
                    return 31

            if (self.hasWord(word_list, ['assignment']) and self.hasWord(word_list,['weigh', 'worth', 'percentage'])
                    and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['2'])):
                    return 25
                if (self.hasWord(word_list, ['6'])):
                    return 27
                if (self.hasWord(word_list, ['11'])):
                    return 30

            if (self.hasWord(word_list, ['due','turn', 'submit', 'complete']) and self.hasWord(word_list, ['start','begin']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project','assignment','midterm','final'])):
                if (self.hasWord(word_list, ['3']) ):
                    return 9
                if (self.hasWord(word_list, ['7'])):
                    return 11
                if (self.hasWord(word_list, ['8'])):
                    return 12
                if (self.hasWord(word_list, ['11'])):
                    return 13
                if (self.hasWord(word_list, ['12'])):
                    return 14
                if (self.hasWord(word_list, ['15'])):
                    return 15
                if (self.hasWord(word_list, ['16'])):
                    return 16
                if (self.hasWord(word_list, ['6'])):
                    return 10
            if (self.hasWord(word_list, ['due','turn', 'submit', 'complete']) and self.hasWord(word_list, ['end']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project', 'assignment', 'midterm', 'final'])):
                if (self.hasWord(word_list, ['2']) ):
                    return 9
                if (self.hasWord(word_list, ['5'])):
                    return 10
                if (self.hasWord(word_list, ['6'])):
                    return 11
                if (self.hasWord(word_list, ['7'])):
                    return 12
                if (self.hasWord(word_list, ['10'])):
                    return 13
                if (self.hasWord(word_list, ['11'])):
                    return 14
                if (self.hasWord(word_list, ['14'])):
                    return 15
                if (self.hasWord(word_list, ['15'])):
                    return 16
            if (self.hasWord(word_list, ['release']) and self.hasWord(word_list, ['start','begin']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project','assignment','midterm','final'])):
                if (self.hasWord(word_list, ['2']) ):
                    return 1
                if (self.hasWord(word_list, ['3'])):
                    return 2
                if (self.hasWord(word_list, ['6'])):
                    return 3
                if (self.hasWord(word_list, ['7'])):
                    return 4
                if (self.hasWord(word_list, ['8'])):
                    return 5
                if (self.hasWord(word_list, ['11'])):
                    return 6
                if (self.hasWord(word_list, ['12'])):
                    return 7
                if (self.hasWord(word_list, ['15'])):
                    return 8
            if (self.hasWord(word_list, ['release']) and self.hasWord(word_list, ['end']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project','assignment','midterm','final'])):

                if (self.hasWord(word_list, ['2'])):
                    return 2
                if (self.hasWord(word_list, ['5'])):
                    return 3
                if (self.hasWord(word_list, ['6'])):
                    return 4
                if (self.hasWord(word_list, ['7'])):
                    return 5
                if (self.hasWord(word_list, ['10'])):
                    return 6
                if (self.hasWord(word_list, ['11'])):
                    return 7
                if (self.hasWord(word_list, ['14'])):
                    return 8
                if (self.hasWord(word_list, ['1']) ):
                    return 1
            if (not self.hasWord(word_list, ['release','due','turn', 'submit', 'complete']) and self.hasWord(word_list, ['start']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project','assignment','midterm','final'])):

                if (self.hasWord(word_list, ['3'])):
                    return 2
                if (self.hasWord(word_list, ['6'])):
                    return 3
                if (self.hasWord(word_list, ['7'])):
                    return 4
                if (self.hasWord(word_list, ['8'])):
                    return 5
                if (self.hasWord(word_list, ['11'])):
                    return 6
                if (self.hasWord(word_list, ['12'])):
                    return 7
                if (self.hasWord(word_list, ['15'])):
                    return 8
                if (self.hasWord(word_list, ['2']) ):
                    return 1
            if (not self.hasWord(word_list, ['release','due','turn', 'submit', 'complete']) and self.hasWord(word_list, ['end']) and self.hasWord(word_list, ['week'])
            and not self.hasWord(word_list, ['project','assignment','midterm','final'])):
                if (self.hasWord(word_list, ['2']) ):
                    return 9
                if (self.hasWord(word_list, ['6'])):
                    return 11
                if (self.hasWord(word_list, ['7'])):
                    return 12
                if (self.hasWord(word_list, ['10'])):
                    return 13
                if (self.hasWord(word_list, ['11'])):
                    return 14
                if (self.hasWord(word_list, ['14'])):
                    return 15
                if (self.hasWord(word_list, ['15'])):
                    return 16
                if (self.hasWord(word_list, ['5'])):
                    return 10
            if(self.hasWord(word_list, ['project']) and self.hasWord(word_list, ['due','turn', 'submit', 'complete'])
            and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['5'])):
                    return 10
                if (self.hasWord(word_list, ['10'])):
                    return 13
                if (self.hasWord(word_list, ['14'])):
                    return 15

            if (self.hasWord(word_list, ['assignment']) and self.hasWord(word_list, ['due', 'turn', 'submit', 'complete'])
                    and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['2'])):
                    return 9
                if (self.hasWord(word_list, ['6'])):
                    return 11
                if (self.hasWord(word_list, ['11'])):
                    return 14

            if (self.hasWord(word_list, ['project']) and self.hasWord(word_list, ['begin', 'start', 'release'])
                    and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['3'])):
                    return 2
                if (self.hasWord(word_list, ['8'])):
                    return 5
                if (self.hasWord(word_list, ['12'])):
                    return 7

            if (self.hasWord(word_list, ['assignment']) and self.hasWord(word_list,['begin', 'start', 'release'])
                    and self.hasWord(word_list, ['week'])):
                if (self.hasWord(word_list, ['2'])):
                    return 1
                if (self.hasWord(word_list, ['6'])):
                    return 3
                if (self.hasWord(word_list, ['11'])):
                    return 6



        if (data_requested.upper() == 'RELEASEDATE'):
            if(question_object.lower() == 'assignment 1' or question_object.lower() == 'first assignment' or question_object.lower() == 'assignment one'):
                return 1
            elif (question_object.lower() == 'project 1' or question_object.lower() == 'first project' or question_object.lower() == 'project one'):
                return 2
            elif (question_object.lower() == 'assignment 2' or question_object.lower() == 'second assignment' or question_object.lower() == 'assignment two'):
                return 3
            elif (question_object.lower() == 'midterm' or question_object.lower() == 'first midterm'):
                return 4
            elif (question_object.lower() == 'project 2' or question_object.lower() == 'second project' or question_object.lower() == 'project two'):
                return 5
            elif (question_object.lower() == 'assignment 3' or question_object.lower() == 'third assignment' or question_object.lower() == 'assignment three'):
                return 6
            elif (question_object.lower() == 'project 3' or question_object.lower() == 'third project' or question_object.lower() == 'project three'):
                return 7
            elif (question_object.lower() == 'final' or question_object.lower() == 'first final'):
                return 8
        if (data_requested.upper() == 'DUEDATE'):
            if (question_object.lower() == 'assignment 1' or question_object.lower() == 'first assignment' or question_object.lower() == 'assignment one'):
                return 9
            elif (question_object.lower() == 'project 1' or question_object.lower() == 'first project' or question_object.lower() == 'project one'):
                return 10
            elif (question_object.lower() == 'assignment 2' or question_object.lower() == 'second assignment' or question_object.lower() == 'assignment two'):
                return 11
            elif (question_object.lower() == 'midterm' or question_object.lower() == 'first midterm'):
                return 12
            elif (question_object.lower() == 'project 2' or question_object.lower() == 'second project' or question_object.lower() == 'project two'):
                return 13
            elif (question_object.lower() == 'assignment 3' or question_object.lower() == 'third assignment' or question_object.lower() == 'assignment three'):
                return 14
            elif (question_object.lower() == 'project 3' or question_object.lower() == 'third project' or question_object.lower() == 'project three'):
                return 15
            elif (question_object.lower() == 'final' or question_object.lower() == 'first final'):
                return 16

        if (data_requested.upper() == 'DURATION'):
            if (question_object.lower() == 'assignment 1' or question_object.lower() == 'first assignment' or question_object.lower() == 'assignment one'):
                return 17
            elif (question_object.lower() == 'project 1' or question_object.lower() == 'first project' or question_object.lower() == 'project one'):
                return 18
            elif (question_object.lower() == 'assignment 2' or question_object.lower() == 'second assignment' or question_object.lower() == 'assignment two'):
                return 19
            elif (question_object.lower() == 'midterm' or question_object.lower() == 'first midterm'):
                return 20
            elif (question_object.lower() == 'project 2' or question_object.lower() == 'second project' or question_object.lower() == 'project two'):
                return 21
            elif (question_object.lower() == 'assignment 3' or question_object.lower() == 'third assignment' or question_object.lower() == 'assignment three'):
                return 22
            elif (question_object.lower() == 'project 3' or question_object.lower() == 'third project' or question_object.lower() == 'project three'):
                return 23
            elif (question_object.lower() == 'final' or question_object.lower() == 'first final'):
                return 24

        if (data_requested.upper() == 'WEIGHT'):
            if (question_object.lower() == 'assignment 1' or question_object.lower() == 'first assignment' or question_object.lower() == 'assignment one'):
                return 25
            elif (question_object.lower() == 'project 1' or question_object.lower() == 'first project' or question_object.lower() == 'project one'):
                return 26
            elif (question_object.lower() == 'assignment 2' or question_object.lower() == 'second assignment' or question_object.lower() == 'assignment two'):
                return 27
            elif (question_object.lower() == 'midterm' or question_object.lower() == 'first midterm'):
                return 28
            elif (question_object.lower() == 'project 2' or question_object.lower() == 'second project' or question_object.lower() == 'project two'):
                return 29
            elif (question_object.lower() == 'assignment 3' or question_object.lower() == 'third assignment' or question_object.lower() == 'assignment three'):
                return 30
            elif (question_object.lower() == 'project 3' or question_object.lower() == 'third project' or question_object.lower() == 'project three'):
                return 31
            elif (question_object.lower() == 'final' or question_object.lower() == 'first final'):
                return 32

        if (data_requested.upper() == 'PROCESS'):
            if (question_object.lower() == 'assignment 1' or question_object.lower() == 'first assignment' or question_object.lower() == 'assignment one'):
                return 33
            elif (question_object.lower() == 'project 1' or question_object.lower() == 'first project' or question_object.lower() == 'project one'):
                return 34
            elif (question_object.lower() == 'assignment 2' or question_object.lower() == 'second assignment' or question_object.lower() == 'assignment two'):
                return 35
            elif (question_object.lower() == 'midterm' or question_object.lower() == 'first midterm'):
                return 36
            elif (question_object.lower() == 'project 2' or question_object.lower() == 'second project' or question_object.lower() == 'project two'):
                return 37
            elif (question_object.lower() == 'assignment 3' or question_object.lower() == 'third assignment' or question_object.lower() == 'assignment three'):
                return 38
            elif (question_object.lower() == 'project 3' or question_object.lower() == 'third project' or question_object.lower() == 'project three'):
                return 39
            elif (question_object.lower() == 'final' or question_object.lower() == 'first final'):
                return 40

        if(self.hasWord(word_list,['announcements','discussions', 'forum','collaboration','question','answer'])
                or (self.hasWord(word_list,['piazza']) and not self.hasWord(word_list,['download']))):
            return 41

        if (self.hasWord(word_list, ['class', 'learning','goals','ai','skills','knowledge-based','artificial','intelligence'])):
            return 42
        return 0

    # takes in list of words, returns question_object and data_requested
    def input_output(self, word_list):
        #word_list=self.toStringList(word_list)

        qobject = self.getObject(word_list)
        data = self.getDataRequested(word_list)
        print(qobject+' '+data)

        # TODO: Add your code here

        _intent = 0
        _intent = self.getIntent(qobject,data, word_list)

        return _intent

