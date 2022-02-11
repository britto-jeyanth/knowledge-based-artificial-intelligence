"""
ADD YOUR CODE HERE

Please read project directions before importing anything
"""


import common


class StudentAgent:
    global helpingVerbs, questionWords, subjectPronouns, determinerWords, prepositions, possessivePronouns, conjuctions, classifiedWords
    helpingVerbs = ['Be', 'am', 'is', 'are', 'was', 'Were', 'been', 'Being', 'have', 'has', 'had', 'Could', 'should', 'must',
                    'may', 'might', 'Must', 'can', 'Will', 'would', 'do', 'did', 'does']

    questionWords = ['How much', 'How long', 'How many', 'What', 'When', 'How', 'Where']

    subjectPronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'you', 'they','anyone', 'anybody', 'everyone', 'everybody',
                       'someone', 'somebody']

    determinerWords = ['a', 'an', 'the', 'every', 'this', 'those', 'many']

    prepositions = ['after', 'in', 'to', 'on', 'with', 'of', 'for']

    possessivePronouns = ['my', 'mine', 'your', 'yours', 'his', 'her', 'hers', 'its', 'our', 'ours', 'your', 'yours',
                          'their', 'theirs']

    conjuctions = ['and', 'because', 'but', 'if', 'or', 'when']

    classifiedWords = ['helping verb', 'question word', 'preposition', 'determiner word', 'conjuction',
                       'possessive pronoun', 'subject pronoun', 'verb', 'jargon', 'not object']

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
                    qword = self.toStringList(questionWords[x])
                    if(len(qword)>1):
                        if ((word_list[y].lower() == qword[0].lower()) and y+1<len(word_list)):
                            if(word_list[y+1].lower() == qword[1].lower()):
                                #word_list.remove(qword[0].lower())
                                word_list[y] = "question word"
                                #word_list.remove(qword[1].lower())
                                word_list[y+1] = "question word"
                                return self.removeQuestionWords(word_list)
                    else:
                        if(word_list[y].lower() == questionWords[x].lower()):
                            #word_list.remove(word_list[y])
                            word_list[y] = "question word"
                            return self.removeQuestionWords(word_list)
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

    def removeVerbs(self, word_list, list):
        hvIndex = [i for i, x in enumerate(word_list) if x == "helping verb"]
        spIndex = [j for j, x in enumerate(word_list) if x == "subject pronoun"]
        prepIndex = [k for k, x in enumerate(word_list) if x == "preposition"]
        # print('helping verb index: ',hvIndex)
        for x in range(len(hvIndex)):
            if (hvIndex[x] == (len(word_list) - 2)):
                if (self.notClassified(word_list, hvIndex[x] + 1)):
                    word_list[hvIndex[x] + 1] = 'verb'

            if (hvIndex[x] <= (len(word_list) - 3)):
                if ((word_list[hvIndex[x] + 2] == 'preposition') and self.notClassified(word_list, hvIndex[x] + 1)):
                    word_list[hvIndex[x] + 1] = 'verb'

        for x in range(len(spIndex)):
            if (spIndex[x] <= (len(word_list) - 3)):
                if ((word_list[spIndex[x] + 2] == 'preposition') and self.notClassified(word_list, spIndex[x] + 1)):
                    word_list[spIndex[x] + 1] = 'verb'
                if ((word_list[spIndex[x] + 2] == 'determiner word') and self.notClassified(word_list, spIndex[x] + 1)):
                    word_list[spIndex[x] + 1] = 'verb'


            if (spIndex[x] <= (len(word_list) - 4)):
                if (word_list[spIndex[x] + 3] == 'preposition'):
                    if((word_list[spIndex[x] + 2][-2:]=='ed') or (word_list[spIndex[x] + 2][-3:]=='ing')):
                        word_list[spIndex[x] + 1] = 'verb'
                        word_list[spIndex[x] + 2] = 'verb'

            if (spIndex[x] <= (len(word_list) - 2)):
                if (self.notClassified(word_list, spIndex[x] + 1)):
                    word_list[spIndex[x] + 1] = 'verb'


        for x in range(len(prepIndex)):
            if ((prepIndex[x] <= (len(word_list) - 3)) and self.notClassified(word_list, prepIndex[x] + 1)):
                if (word_list[prepIndex[x] + 2] == 'determiner word'):
                    word_list[prepIndex[x] + 1] = 'verb'

            if ((prepIndex[x] <= (len(word_list) - 3)) and self.notClassified(word_list, prepIndex[x] + 1)):
                if (word_list[prepIndex[x] + 2] == 'preposition'):
                    word_list[prepIndex[x] + 1] = 'verb'

            if ((prepIndex[x] <= (len(word_list) - 3)) and self.notClassified(word_list, prepIndex[x] + 1)):
                if (word_list[prepIndex[x] + 1][-3:]=='ing'):
                    word_list[prepIndex[x] + 1] = 'verb'

            if ((list[prepIndex[x]].lower() == 'to') and self.notClassified(word_list, prepIndex[x] + 1)):
                word_list[prepIndex[x]+1] = 'verb'

            if ((list[prepIndex[x]].lower() == 'to') and self.notClassified(word_list, prepIndex[x] - 1)):
                word_list[prepIndex[x]-1] = 'verb'


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

    def getObject(self, word_list):
        classification_list=word_list.copy()
        classification_list=self.removeHelpingVerb(classification_list)
        classification_list=self.removeQuestionWords(classification_list)
        classification_list=self.removeSubjectPronouns(classification_list)
        classification_list=self.removeDeterminerWords(classification_list)
        classification_list=self.removePrepositions(classification_list)
        classification_list=self.removeConjuctions(classification_list)
        classification_list=self.removePossessivePronouns(classification_list)
        classification_list=self.removeVerbs(classification_list, word_list)
        classification_list=self.removeBetweenQandV(classification_list)
        #print(word_list)

        if(word_list[0].lower()=='when'):
            self.removeJargon(classification_list,['due','release','date'])

        elif(word_list[0].lower()=='where'):
            self.removeJargon(classification_list,['locat','specified'])

        elif (word_list[0].lower() == 'what'):
            self.removeJargon(classification_list, ['due','release','date', 'worth', 'percentage', 'procedure', 'process', 'locat', 'weigh', 'grade', 'specified'])

        elif (word_list[0].lower() == 'how'):
            self.removeJargon(classification_list, ['worth', 'weigh', 'grade'])

        #print(classification_list)
        return self.returnRemaining(word_list,classification_list)

    def hasWord(self,word_list,search_for):
        for x in range(len(word_list)):
            for y in range(len(search_for)):
                if(len(word_list[x])>=len(search_for[y])):
                    if(word_list[x][:len(search_for[y])].lower()==search_for[y].lower()):
                        return True
        return False

    
    def getDataRequested(self,word_list):
        if(word_list[0].lower() == 'when'):
            if(self.hasWord(word_list,['due','turn'])):
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
        else:
            if(self.hasWord(word_list,['due','turn'])):
                return 'DUEDATE'
            elif(self.hasWord(word_list, ['release'])):
                return 'RELEASEDATE'
            elif(self.hasWord(word_list, ['weigh','worth','percent'])):
                return 'WEIGHT'
            else:
                return 'PROCESS'


    # takes in list of words, returns question_object and data_requested
    def input_output(self, word_list):
        #word_list=self.toStringList(word_list)

        qobject = self.getObject(word_list)
        data = self.getDataRequested(word_list)

        # TODO: Add your code here

        _question_object = qobject # for debugging only, replace with your code
        _data_requested = data   # for debugging only, replace with your code

        return _question_object, _data_requested

