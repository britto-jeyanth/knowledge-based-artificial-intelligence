"""
Project 3

ADD YOUR CODE HERE

Please read project directions before importing anything
"""


class StudentAgent:
    """ADD YOUR CODE HERE"""
    global green, helpingVerbs, pronouns, determinerWords, day, prepositions, actionVerbs, synonyms, name, file, \
        language, communication, knowledge, number, percentage, conjunctions, duration, noun

    green = ['project', 'projects', 'assignment', 'assignments', 'midterm', 'final', 'course', 'announcements',
             'instructor', 'report', 'reports', 'exams', 'strategies', 'strategy', 'policy', 'peer-feedback',
             'office-days', 'content', 'communication', 'submissions', 'TA', 'component', 'code', 'policies']

    noun = ['files', 'file', 'class']

    helpingVerbs = ['will', 'be', 'is', 'doing', 'has', 'are', 'does', 'must', 'should', 'do', 'have', 'can']

    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35',
              '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
              '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69',
              '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86',
              '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']

    percentage = ['0%', '1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%',
                  '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%',
                  '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%',
                  '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%',
                  '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '69%', '70%', '71%',
                  '72%', '73%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%',
                  '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%',
                  '100%']

    pronouns = ['i', 'my']

    conjunctions = ['and', 'or']

    determinerWords = ['the', 'a', 'this', 'there', 'no']

    day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    prepositions = ['during', 'in', 'of', 'to', 'into', 'as', 'by', 'for', 'on', 'after']

    actionVerbs = ['need', 'finish', 'posted', 'turn', 'check', 'contribute', 'submit', 'close', 'occurs', 'submitted',
                   'occur', 'distributed', 'write', 'learn', 'turned', 'teach', 'released', 'get', 'preferred', 'begin',
                   'available', 'due', 'complete', 'worth', 'code']

    synonyms = {'posted':'released', 'available':'released', 'distributed':'released', 'begin':'released',
                'occur':'occurs', 'submit':'due', 'turned':'due', 'complete':'due', 'submitted':'due', 'class':'course',
                'weeks':'week', 'start':'begin', 'during':'occurs', 'get':'begin', 'turn':'due', 'weeks':'week',
                'files':'file', 'finish':'due'}

    knowledge = {}

    duration = ['week', 'weeks', 'hours']

    name = ['yaroslav', 'ashok', 'goel', 'litvak']

    file = ['pdf', 'docx', 'text', 'zip', 'gz', 'bz2']

    language = ['java', 'c++', 'python']

    communication = ['piazza', 'slack', 'canvas']



    def __init__(self, verbose):
        self._verbose = verbose
        # TODO: Add your init code here

    def removeHelpingVerb(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(helpingVerbs)):
                word = word_list[x].lower()
                hv = helpingVerbs[y].lower()
                boole = (word == hv)
                if(boole):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "helping_verb"
                    return self.removeHelpingVerb(word_list)
        return word_list

    def removeActionVerb(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(actionVerbs)):
                word = word_list[x].lower()
                hv = actionVerbs[y].lower()
                boole = (word == hv)
                if(boole):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "action_verb"
                    return self.removeActionVerb(word_list)
        return word_list

    def removeDeterminerWords(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(determinerWords)):
                if(word_list[x].lower() == determinerWords[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "determiner_word"
                    return self.removeDeterminerWords(word_list)
        return word_list

    def removePronouns(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(pronouns)):
                if(word_list[x].lower() == pronouns[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "pronoun"
                    return self.removePronouns(word_list)
        return word_list

    def removeNumber(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(number)):
                if(word_list[x].lower() == number[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "number"
                    return self.removeNumber(word_list)
        return word_list

    def removePercentage(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(percentage)):
                if(word_list[x].lower() == percentage[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "percentage"
                    return self.removePercentage(word_list)
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

    def removeConjunctions(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(conjunctions)):
                if(word_list[x].lower() == conjunctions[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "conjunctions"
                    return self.removeConjunctions(word_list)
        return word_list

    def removeGreen(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(green)):
                if(word_list[x].lower() == green[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "green"
                    return self.removeGreen(word_list)
        return word_list

    def removeNoun(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(noun)):
                if(word_list[x].lower() == noun[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "noun"
                    return self.removeNoun(word_list)
        return word_list

    def removeDuration(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(duration)):
                if(word_list[x].lower() == duration[y].lower()):
                    #print(word_list[x])
                    #word_list.remove(word_list[x])
                    word_list[x] = "duration"
                    return self.removeDuration(word_list)
        return word_list

    def getNumberGreen(self, classification_list, green_index):

        if(green_index<(len(classification_list)-1)):
            if (classification_list[green_index + 1] == 'number'):
                return green_index + 1

        return -1

    def load_green_words(self, statement, number_green_index, green_index):
        if (number_green_index != -1):
            if statement[green_index] + ' ' + statement[number_green_index] not in knowledge[statement[green_index]]:
                knowledge[statement[green_index]][statement[green_index] + ' ' + statement[number_green_index]] = {}

            if (statement[green_index].lower() == 'project'):
                if 'count' not in knowledge['project']:
                    if 'projects' not in knowledge:
                        knowledge['projects'] = {}
                    knowledge['projects']['count'] = int(statement[number_green_index])
                    knowledge['project']['count'] = int(statement[number_green_index])

                    count = int(statement[number_green_index]) - 1

                    for x in range(knowledge['project']['count']):
                        if (count > 0):
                            if statement[green_index] + ' ' + str(count) not in knowledge[
                                statement[green_index]]:
                                knowledge[statement[green_index]][
                                    statement[green_index] + ' ' + str(count)] = {}
                        count = count - 1
                elif knowledge['projects']['count'] < int(statement[number_green_index]):
                    knowledge['projects']['count'] = int(statement[number_green_index])
                    knowledge['project']['count'] = int(statement[number_green_index])

                    count = int(statement[number_green_index]) - 1

                    for x in range(knowledge['project']['count']):
                        if (count > 0):
                            if statement[green_index] + ' ' + str(count) not in knowledge[
                                statement[green_index]]:
                                knowledge[statement[green_index]][
                                    statement[green_index] + ' ' + str(count)] = {}
                        count = count - 1

            if (statement[green_index].lower() == 'assignment'):
                if 'count' not in knowledge['assignment']:
                    if 'assignments' not in knowledge:
                        knowledge['assignments'] = {}
                    knowledge['assignments']['count'] = int(statement[number_green_index])
                    knowledge['assignment']['count'] = int(statement[number_green_index])

                    count = int(statement[number_green_index]) - 1

                    for x in range(knowledge['assignment']['count']):
                        if (count > 0):
                            if statement[green_index] + ' ' + str(count) not in knowledge[
                                statement[green_index]]:
                                knowledge[statement[green_index]][
                                    statement[green_index] + ' ' + str(count)] = {}
                        count = count - 1

                elif knowledge['assignments']['count'] < int(statement[number_green_index]):
                    knowledge['assignments']['count'] = int(statement[number_green_index])
                    knowledge['assignment']['count'] = int(statement[number_green_index])

                    count = int(statement[number_green_index]) - 1

                    for x in range(knowledge['assignment']['count']):
                        if (count > 0):
                            if statement[green_index] + ' ' + str(count) not in knowledge[
                                statement[green_index]]:
                                knowledge[statement[green_index]][
                                    statement[green_index] + ' ' + str(count)] = {}
                        count = count - 1

        if (statement[green_index].lower() == 'midterm'):
            if 'exams' not in knowledge:
                knowledge['exams'] = {}
                knowledge['exams']['count'] = 1
            elif 'midterm' in knowledge and 'final' in knowledge:
                knowledge['exams']['count'] = 2


        if (statement[green_index].lower() == 'final'):
            if 'exams' not in knowledge:
                knowledge['exams'] = {}
                knowledge['exams']['count'] = 1
            elif 'midterm' in knowledge and 'final' in knowledge:
                knowledge['exams']['count'] = 2

    # actionVerbs = ['need', 'finish', 'posted', 'turn', 'check', 'contribute', 'submit', 'close', 'occurs', 'submitted',
    #     #                'occur', 'distributed', 'write', 'learn', 'turned', 'teach', 'released', 'get', 'preferred', 'begin',
    #     #                'available', 'due', 'complete']
    #     #
    #     # synonyms = {'posted': 'released', 'available': 'released', 'distributed': 'released', 'occur': 'occurs',
    #     #             'submitted': 'submit', 'turned': 'submit', 'complete': 'submit'}
    def exists(self, classification_list, word):
        for x in range(len(classification_list)):
            if(classification_list[x] == word):
                return x
        return -1

    def isFile(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(file)):
                if(word_list[x].lower() == file[y].lower()):

                    return True
        return False

    def isDuration(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(duration)):
                if(word_list[x].lower() == duration[y].lower()):

                    return True
        return False

    def isName(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(name)):
                if(word_list[x].lower() == name[y].lower()):

                    return True
        return False

    def isCommunication(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(communication)):
                if(word_list[x].lower() == communication[y].lower()):

                    return True
        return False

    def isCode(self, word_list):
        for x in range(len(word_list)):
            for y in range(len(language)):
                if(word_list[x].lower() == language[y].lower()):

                    return True
        return False

    def load_verb(self, statement, number_green_index, green_index, classification_list):
        if(number_green_index!=-1):
            green = statement[green_index]+' '+statement[number_green_index]
        else:
            green = statement[green_index]

        action_index = self.exists(classification_list,'action_verb')

        if(action_index == -1):
            copy_st = statement.copy()
            copy_cl = classification_list.copy()
            hv = self.exists(copy_cl, 'helping_verb')
            if(green_index<hv):
                if(number_green_index!=-1):
                    copy_st.pop(number_green_index)
                    copy_cl.pop(number_green_index)
                det_index = self.exists(copy_cl,'determiner_word')
                if(det_index!=-1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                green_cp_ind = self.exists(copy_cl, 'green')
                if (green_cp_ind != -1):
                    copy_st.pop(green_cp_ind)
                    copy_cl.pop(green_cp_ind)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                ni = self.exists(copy_cl, 'noun')
                if (ni != -1):
                    copy_st.pop(ni)
                    copy_cl.pop(ni)

                if(self.isDuration(copy_st)):
                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' '+copy_st[x]
                    if(number_green_index == -1):
                        knowledge[statement[green_index]]['duration'] = load
                    else:
                        knowledge[statement[green_index]][green]['duration'] = load

                elif (self.isName(copy_st)):
                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        knowledge[statement[green_index]]['name'] = load
                    else:
                        knowledge[statement[green_index]][green]['name'] = load

            else:
                if (number_green_index != -1):
                    copy_st.pop(number_green_index)
                    copy_cl.pop(number_green_index)
                det_index = self.exists(copy_cl, 'determiner_word')
                if (det_index != -1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                green_cp_ind = self.exists(copy_cl, 'green')
                if (green_cp_ind != -1):
                    copy_st.pop(green_cp_ind)
                    copy_cl.pop(green_cp_ind)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                ni = self.exists(copy_cl, 'noun')
                if (ni != -1):
                    copy_st.pop(ni)
                    copy_cl.pop(ni)

                if (self.isDuration(copy_st)):
                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        knowledge[statement[green_index]]['duration'] = load
                    else:
                        knowledge[statement[green_index]][green]['duration'] = load

                elif (self.isName(copy_st)):
                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        knowledge[statement[green_index]]['name'] = load
                    else:
                        knowledge[statement[green_index]][green]['name'] = load

        else:
            if statement[action_index] in synonyms:
                statement[action_index] = synonyms[statement[action_index]]

            if (statement[action_index] == 'occurs'):

                copy_st = statement.copy()
                copy_cl = classification_list.copy()

                if (green_index < action_index):
                    if (number_green_index != -1):
                        copy_st.pop(number_green_index)
                        copy_cl.pop(number_green_index)
                    det_index = self.exists(copy_cl, 'determiner_word')
                    if (det_index != -1):
                        copy_st.pop(det_index)
                        copy_cl.pop(det_index)

                    green_cp_ind = self.exists(copy_cl, 'green')
                    if (green_cp_ind != -1):
                        copy_st.pop(green_cp_ind)
                        copy_cl.pop(green_cp_ind)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)


                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    av = self.exists(copy_cl, 'action_verb')
                    if (av != -1):
                        copy_st.pop(av)
                        copy_cl.pop(av)

                    ni = self.exists(copy_cl, 'noun')
                    if (ni != -1):
                        copy_st.pop(ni)
                        copy_cl.pop(ni)

                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]]['occurs'] = load
                            knowledge[statement[green_index]]['release_date'] = load
                    else:
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]][green]['occurs'] = load
                            knowledge[statement[green_index]][green]['release_date'] = load

            if (statement[action_index] == 'worth'):

                copy_st = statement.copy()
                copy_cl = classification_list.copy()

                if (green_index < action_index):
                    if (number_green_index != -1):
                        copy_st.pop(number_green_index)
                        copy_cl.pop(number_green_index)
                    det_index = self.exists(copy_cl, 'determiner_word')
                    if (det_index != -1):
                        copy_st.pop(det_index)
                        copy_cl.pop(det_index)

                    green_cp_ind = self.exists(copy_cl, 'green')
                    if (green_cp_ind != -1):
                        copy_st.pop(green_cp_ind)
                        copy_cl.pop(green_cp_ind)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)


                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    av = self.exists(copy_cl, 'action_verb')
                    if (av != -1):
                        copy_st.pop(av)
                        copy_cl.pop(av)

                    ni = self.exists(copy_cl, 'noun')
                    if (ni != -1):
                        copy_st.pop(ni)
                        copy_cl.pop(ni)

                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]]['worth'] = load
                    else:
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]][green]['worth'] = load

            if (statement[action_index] == 'code'):

                copy_st = statement.copy()
                copy_cl = classification_list.copy()

                if (green_index < action_index):
                    if (number_green_index != -1):
                        copy_st.pop(number_green_index)
                        copy_cl.pop(number_green_index)
                    det_index = self.exists(copy_cl, 'determiner_word')
                    if (det_index != -1):
                        copy_st.pop(det_index)
                        copy_cl.pop(det_index)

                    green_cp_ind = self.exists(copy_cl, 'green')
                    if (green_cp_ind != -1):
                        copy_st.pop(green_cp_ind)
                        copy_cl.pop(green_cp_ind)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)


                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    av = self.exists(copy_cl, 'action_verb')
                    if (av != -1):
                        copy_st.pop(av)
                        copy_cl.pop(av)

                    ni = self.exists(copy_cl, 'noun')
                    if (ni != -1):
                        copy_st.pop(ni)
                        copy_cl.pop(ni)

                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]]['code'] = load
                    else:
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]][green]['code'] = load

            if(statement[action_index] == 'released'):
                copy_st = statement.copy()
                copy_cl = classification_list.copy()

                if (green_index < action_index):
                    if (number_green_index != -1):
                        copy_st.pop(number_green_index)
                        copy_cl.pop(number_green_index)
                    det_index = self.exists(copy_cl, 'determiner_word')
                    if (det_index != -1):
                        copy_st.pop(det_index)
                        copy_cl.pop(det_index)

                    green_cp_ind = self.exists(copy_cl, 'green')
                    if (green_cp_ind != -1):
                        copy_st.pop(green_cp_ind)
                        copy_cl.pop(green_cp_ind)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    ni = self.exists(copy_cl, 'noun')
                    if (ni != -1):
                        copy_st.pop(ni)
                        copy_cl.pop(ni)



                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    av = self.exists(copy_cl, 'action_verb')
                    if (av != -1):
                        copy_st.pop(av)
                        copy_cl.pop(av)


                    load = ''
                    copy_st = self.replace_synonyms(copy_st)
                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        if(self.isDuration(copy_st)):
                            knowledge[statement[green_index]]['release_date'] = load
                    else:
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]][green]['release_date'] = load

            if (statement[action_index] == 'due'):
                copy_st = statement.copy()
                copy_cl = classification_list.copy()

                if (green_index < action_index):
                    if (number_green_index != -1):
                        copy_st.pop(number_green_index)
                        copy_cl.pop(number_green_index)
                    det_index = self.exists(copy_cl, 'determiner_word')
                    if (det_index != -1):
                        copy_st.pop(det_index)
                        copy_cl.pop(det_index)

                    green_cp_ind = self.exists(copy_cl, 'green')
                    if (green_cp_ind != -1):
                        copy_st.pop(green_cp_ind)
                        copy_cl.pop(green_cp_ind)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)



                    hv = self.exists(copy_cl, 'helping_verb')
                    if (hv != -1):
                        copy_st.pop(hv)
                        copy_cl.pop(hv)

                    ni = self.exists(copy_cl, 'noun')
                    if (ni != -1):
                        copy_st.pop(ni)
                        copy_cl.pop(ni)

                    av = self.exists(copy_cl, 'action_verb')
                    if (av != -1):
                        copy_st.pop(av)
                        copy_cl.pop(av)

                    load = ''

                    copy_st = self.replace_synonyms(copy_st)

                    for x in range(len(copy_st)):
                        if x == 0:
                            load = copy_st[x]
                        else:
                            load = load + ' ' + copy_st[x]
                    if (number_green_index == -1):
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]]['due_date'] = load
                        elif (self.isFile(copy_st)):
                            knowledge[statement[green_index]]['file_type'] = load
                        elif (self.isCommunication(copy_st)):
                            knowledge[statement[green_index]]['submit_to'] = load
                    else:
                        if (self.isDuration(copy_st)):
                            knowledge[statement[green_index]][green]['due_date'] = load
                        elif (self.isFile(copy_st)):
                            knowledge[statement[green_index]][green]['file_type'] = load
                        elif (self.isCommunication(copy_st) ):
                            knowledge[statement[green_index]][green]['submit_to'] = load




    def load_knowledge(self, statement):
        classification_list = statement.copy()
        classification_list = self.removeHelpingVerb(classification_list)
        classification_list = self.removeActionVerb(classification_list)
        classification_list = self.removeDeterminerWords(classification_list)
        classification_list = self.removePronouns(classification_list)
        classification_list = self.removePercentage(classification_list)
        classification_list = self.removeNumber(classification_list)
        classification_list = self.removePrepositions(classification_list)
        classification_list = self.removeConjunctions(classification_list)
        classification_list = self.removeGreen(classification_list)
        classification_list = self.removeDuration(classification_list)
        classification_list = self.removeNoun(classification_list)

        green_index = self.exists(classification_list,'green')
        if(green_index!=-1):
            if statement[green_index] not in knowledge:
                knowledge[statement[green_index]] = {}
            number_green_index = self.getNumberGreen(classification_list, green_index)
            self.load_green_words(statement, number_green_index, green_index)
            self.load_verb(statement, number_green_index, green_index, classification_list)

    def infer(self):
        if('projects' in knowledge):
            if('submit_to' in knowledge['projects']):
                if 'project' in knowledge:
                    knowledge['project']['submit_to'] = knowledge['projects']['submit_to']
                    for key, value in knowledge['project'].items():
                        if type(knowledge['project'][str(key)]) is dict:
                            knowledge['project'][str(key)]['submit_to'] = knowledge['projects']['submit_to']

            if ('file_type' in knowledge['projects']):
                if 'project' in knowledge:
                    knowledge['project']['file_type'] = knowledge['projects']['file_type']
                    for key, value in knowledge['project'].items():
                        if type(knowledge['project'][str(key)]) is dict:
                            knowledge['project'][str(key)]['file_type'] = knowledge['projects']['file_type']

        if ('assignments' in knowledge):
            if ('submit_to' in knowledge['assignments']):
                if 'assignment' in knowledge:
                    knowledge['assignment']['submit_to'] = knowledge['assignments']['submit_to']
                    for key, value in knowledge['assignment'].items():
                        if type(knowledge['assignment'][str(key)]) is dict:
                            knowledge['assignment'][str(key)]['submit_to'] = knowledge['assignments']['submit_to']

            if ('file_type' in knowledge['assignments']):
                if 'assignment' in knowledge:
                    knowledge['assignment']['file_type'] = knowledge['assignments']['file_type']
                    for key, value in knowledge['assignment'].items():
                        if type(knowledge['assignment'][str(key)]) is dict:
                            knowledge['assignment'][str(key)]['file_type'] = knowledge['assignments']['file_type']

        if ('assignment' in knowledge):
            for key, value in knowledge['assignment'].items():
                if type(knowledge['assignment'][str(key)]) is dict:
                    if 'release_date' in value and 'due_date' in value:
                        rd = value['release_date'].lower().split(' ')
                        # if(rd[len(rd)-2]==' '):
                        rd = int(rd[len(rd)-1])
                        # else:
                        #rd = int(rd[len(rd) - 2]+rd[len(rd) - 2])
                        dd = value['due_date'].lower().split(' ')
                        #if (dd[len(dd) - 2] == ' '):
                        dd = int(dd[len(dd) - 1])
                        # else:
                        #     dd = int(dd[len(dd) - 2] + dd[len(dd) - 2])
                        knowledge['assignment'][str(key)]['duration'] = str(dd-rd)+' '+'week'

        if ('project' in knowledge):
            for key, value in knowledge['project'].items():
                if type(knowledge['project'][str(key)]) is dict:
                    if 'release_date' in value and 'due_date' in value:
                        rd = value['release_date'].lower().split(' ')
                        # if(rd[len(rd)-2]==' '):
                        rd = int(rd[len(rd)-1])
                        # else:
                        #rd = int(rd[len(rd) - 2]+rd[len(rd) - 2])
                        dd = value['due_date'].lower().split(' ')
                        #if (dd[len(dd) - 2] == ' '):
                        dd = int(dd[len(dd) - 1])
                        # else:
                        #     dd = int(dd[len(dd) - 2] + dd[len(dd) - 2])
                        knowledge['project'][str(key)]['duration'] = str(dd-rd)+' '+'week'



    def load_syllabus(self, list_of_list_of_statement_words):
        """Train agents from statements"""
        for _statement in list_of_list_of_statement_words:
            #print(_statement)   # for debugging
            #print(_statement.lower().split(' '))
            self.load_knowledge(_statement.lower().split(' '))
            self.infer()
        #print(knowledge)

    def replace_synonyms(self, word_list):
        for x in range(len(word_list)):
            if word_list[x] in synonyms:
                word_list[x] = synonyms[word_list[x]]
        return word_list

    def classify(self, classification_list):
        classification_list = self.removeHelpingVerb(classification_list)
        classification_list = self.removeActionVerb(classification_list)
        classification_list = self.removeDeterminerWords(classification_list)
        classification_list = self.removePronouns(classification_list)
        classification_list = self.removePercentage(classification_list)
        classification_list = self.removeNumber(classification_list)
        classification_list = self.removePrepositions(classification_list)
        classification_list = self.removeConjunctions(classification_list)
        classification_list = self.removeGreen(classification_list)
        classification_list = self.removeDuration(classification_list)
        classification_list = self.removeNoun(classification_list)
        return classification_list

    def num_of_green(self, classification_list):
        count = 0
        for x in range(len(classification_list)):
            if(classification_list[x] == 'green'):
                count = count+1
        return count

    def equivalent(self, word_list, str):
        check = False
        for x in range(len(word_list)):
            if word_list[x] in str:
                check = True
            else:
                return 'no'
        return 'yes'

    def greenIndex2(self,green_index, classification_list):
        green_index=green_index+1
        for green_index in range(green_index,len(classification_list)):
            if(classification_list[green_index] == 'green'):
                return green_index
    def input_output(self, word_list):
        """takes in list of words, returns question_object and data_requested"""

        #print(word_list) # for debugging only
        word_list = self.replace_synonyms(word_list)

        classification_list = word_list.copy()
        classification_list = self.classify(classification_list)

        #print(word_list)
        #print(classification_list)
        # TODO: Add your code here

        if(self.num_of_green(classification_list)==1):
            action_index = self.exists(classification_list, 'action_verb')
            green_index = self.exists(classification_list,'green')
            number_green_index = self.getNumberGreen(classification_list, green_index)
            if(action_index == -1):
                copy_st = word_list.copy()
                copy_cl = classification_list.copy()

                hv = self.exists(copy_cl, 'helping_verb')

                if (number_green_index != -1):
                    copy_st.pop(number_green_index)
                    copy_cl.pop(number_green_index)

                det_index = self.exists(copy_cl, 'determiner_word')
                if (det_index != -1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                det_index = self.exists(copy_cl, 'determiner_word')
                if (det_index != -1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                pro_index = self.exists(copy_cl, 'pronoun')
                if (pro_index != -1):
                    copy_st.pop(pro_index)
                    copy_cl.pop(pro_index)

                pro_index = self.exists(copy_cl, 'pronoun')
                if (pro_index != -1):
                    copy_st.pop(pro_index)
                    copy_cl.pop(pro_index)

                prep_index = self.exists(copy_cl, 'preposition')
                if (prep_index != -1):
                    copy_st.pop(prep_index)
                    copy_cl.pop(prep_index)

                green_cp_ind = self.exists(copy_cl, 'green')
                if (green_cp_ind != -1):
                    copy_st.pop(green_cp_ind)
                    copy_cl.pop(green_cp_ind)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                ni = self.exists(copy_cl, 'noun')
                if (ni != -1):
                    copy_st.pop(ni)
                    copy_cl.pop(ni)

                num_ind = self.exists(copy_cl, 'number')
                # print(copy_cl)
                #print(copy_st)


                if(self.isDuration(copy_st) and number_green_index==-1) :
                    if('duration' in knowledge[word_list[green_index]]):
                        return self.equivalent(copy_st, knowledge[word_list[green_index]]['duration'])
                elif(self.isDuration(copy_st) and number_green_index!=-1):
                    if('duration' in knowledge[word_list[green_index]][word_list[green_index]+' '+word_list[number_green_index]]):
                        return self.equivalent(copy_st, knowledge[word_list[green_index]][word_list[green_index]+' '+word_list[number_green_index]]['duration'])
                elif(num_ind!=-1 and number_green_index==-1):
                    if word_list[green_index] in knowledge:
                        if 'count' in knowledge[word_list[green_index]]:
                            if(knowledge[word_list[green_index]]['count'] == int(copy_st[num_ind])):
                                return 'yes'
                            else:
                                return 'no'
                        else:
                            return 'idk'
                    else:
                        return 'idk'
                elif (num_ind != -1 and number_green_index != -1):
                    if word_list[green_index]+' '+word_list[number_green_index] in knowledge[word_list[green_index]+' '+word_list[number_green_index]]:
                        if 'count' in knowledge[word_list[green_index]+' '+word_list[number_green_index]]:
                            if (knowledge[word_list[green_index]+' '+word_list[number_green_index]]['count'] == int(copy_st[num_ind])):
                                return 'yes'
                            else:
                                return 'no'
                        else:
                            return 'idk'
                    else:
                        return 'idk'
                elif(len(copy_st)==1):
                    if (copy_st[0] == 'many' and number_green_index == -1):
                        if word_list[green_index] in knowledge:
                            if 'count' in knowledge[word_list[green_index]]:
                                if (knowledge[word_list[green_index]]['count'] > 1):
                                    return 'yes'
                                else:
                                    return 'no'
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                    elif (copy_st[0] == 'many' and number_green_index != -1):
                        if word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index] + ' ' + word_list[number_green_index]]:
                            if 'count' in knowledge[word_list[green_index] + ' ' + word_list[number_green_index]]:
                                if (knowledge[word_list[green_index] + ' ' + word_list[number_green_index]]['count'] > 1):
                                    return 'yes'
                                else:
                                    return 'no'
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif(number_green_index==-1):
                    if(word_list[green_index] in knowledge):
                        return 'yes'
                    else:
                        return 'no'
                elif (number_green_index != -1):
                    if (word_list[green_index]+' '+word_list[number_green_index] in knowledge[word_list[green_index]]):
                        return 'yes'
                    else:
                        return 'no'
                else:
                    return 'idk'


            else:
                av = word_list[action_index]
                copy_st = word_list.copy()
                copy_cl = classification_list.copy()

                if (number_green_index != -1):
                    copy_st.pop(number_green_index)
                    copy_cl.pop(number_green_index)

                det_index = self.exists(copy_cl, 'determiner_word')
                if (det_index != -1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                det_index = self.exists(copy_cl, 'determiner_word')
                if (det_index != -1):
                    copy_st.pop(det_index)
                    copy_cl.pop(det_index)

                pro_index = self.exists(copy_cl, 'pronoun')
                if (pro_index != -1):
                    copy_st.pop(pro_index)
                    copy_cl.pop(pro_index)

                pro_index = self.exists(copy_cl, 'pronoun')
                if (pro_index != -1):
                    copy_st.pop(pro_index)
                    copy_cl.pop(pro_index)

                prep_index = self.exists(copy_cl, 'preposition')
                if (prep_index != -1):
                    copy_st.pop(prep_index)
                    copy_cl.pop(prep_index)

                green_cp_ind = self.exists(copy_cl, 'green')
                if (green_cp_ind != -1):
                    copy_st.pop(green_cp_ind)
                    copy_cl.pop(green_cp_ind)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                ni = self.exists(copy_cl, 'noun')
                if (ni != -1):
                    copy_st.pop(ni)
                    copy_cl.pop(ni)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)

                hv = self.exists(copy_cl, 'helping_verb')
                if (hv != -1):
                    copy_st.pop(hv)
                    copy_cl.pop(hv)
                av_ind = self.exists(copy_cl, 'action_verb')
                if (av_ind != -1):
                    copy_st.pop(av_ind)
                    copy_cl.pop(av_ind)
                percent_ind = self.exists(copy_cl, 'percentage')
                if(av == 'worth' and percent_ind!=-1):
                    if(number_green_index==-1):
                        if (word_list[green_index] in knowledge):
                            if('worth' in knowledge[word_list[green_index]]):
                                if(knowledge[word_list[green_index]]['worth'] == copy_st[percent_ind]):
                                    return 'yes'
                                else:
                                    return 'no'
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                    else:
                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('worth' in knowledge[word_list[green_index]][word_list[green_index] + ' ' + word_list[number_green_index]]):
                                if (knowledge[word_list[green_index]][word_list[green_index] + ' ' + word_list[number_green_index]]['worth'] == copy_st[percent_ind]):
                                    return 'yes'
                                else:
                                    return 'no'
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif(av == 'released' and self.isDuration(copy_st)):

                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            if ('release_date' in knowledge[word_list[green_index]]):
                                return self.equivalent(copy_st,knowledge[word_list[green_index]]['release_date'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('release_date' in knowledge[word_list[green_index]][
                                word_list[green_index] + ' ' + word_list[number_green_index]]):
                                #print(copy_st)
                                return self.equivalent(copy_st,knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]['release_date'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif (av == 'begin' and self.isDuration(copy_st)):

                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            if ('release_date' in knowledge[word_list[green_index]]):
                                return self.equivalent(copy_st, knowledge[word_list[green_index]]['release_date'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('release_date' in knowledge[word_list[green_index]][
                                word_list[green_index] + ' ' + word_list[number_green_index]]):
                                #print(copy_st)
                                return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]['release_date'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif (av == 'occurs' and self.isDuration(copy_st)):

                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            if ('occurs' in knowledge[word_list[green_index]]):
                                return self.equivalent(copy_st, knowledge[word_list[green_index]]['occurs'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('occurs' in knowledge[word_list[green_index]][
                                word_list[green_index] + ' ' + word_list[number_green_index]]):
                                #print(copy_st)
                                return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]['occurs'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif (av == 'due' and self.isDuration(copy_st)):

                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            dur_ind = self.exists(copy_cl, 'duration')
                            num_ind = self.exists(copy_cl, 'number')
                            if(num_ind>dur_ind):
                                if ('due_date' in knowledge[word_list[green_index]]):
                                    return self.equivalent(copy_st, knowledge[word_list[green_index]]['due_date'])
                                else:
                                    return 'idk'
                            else:
                                if ('duration' in knowledge[word_list[green_index]]):
                                    return self.equivalent(copy_st, knowledge[word_list[green_index]]['duration'])
                                else:
                                    return 'idk'
                        else:
                            return 'idk'
                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            dur_ind = self.exists(copy_cl, 'duration')
                            num_ind = self.exists(copy_cl, 'number')
                            if (num_ind > dur_ind):
                                if ('due_date' in knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]):
                                    #print(copy_st)
                                    return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                        word_list[green_index] + ' ' + word_list[number_green_index]]['due_date'])
                                else:
                                    return 'idk'
                            else:
                                if ('duration' in knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]):
                                    #print(copy_st)
                                    return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                        word_list[green_index] + ' ' + word_list[number_green_index]]['duration'])
                                else:
                                    return 'idk'
                        else:
                            return 'idk'
                elif (av == 'due' and self.isCommunication(copy_st)):
                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            if ('submit_to' in knowledge[word_list[green_index]]):
                                return self.equivalent(copy_st, knowledge[word_list[green_index]]['submit_to'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'

                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('submit_to' in knowledge[word_list[green_index]][
                                word_list[green_index] + ' ' + word_list[number_green_index]]):

                                return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]['submit_to'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
                elif (av == 'due' and self.isFile(copy_st)):
                    if (number_green_index == -1):
                        if (word_list[green_index] in knowledge):
                            if ('file_type' in knowledge[word_list[green_index]]):
                                return self.equivalent(copy_st, knowledge[word_list[green_index]]['file_type'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'

                    else:

                        if (word_list[green_index] + ' ' + word_list[number_green_index] in knowledge[
                            word_list[green_index]]):
                            if ('file_type' in knowledge[word_list[green_index]][
                                word_list[green_index] + ' ' + word_list[number_green_index]]):

                                return self.equivalent(copy_st, knowledge[word_list[green_index]][
                                    word_list[green_index] + ' ' + word_list[number_green_index]]['file_type'])
                            else:
                                return 'idk'
                        else:
                            return 'idk'
        elif (self.num_of_green(classification_list) == 2):
            action_index = self.exists(classification_list, 'action_verb')
            green_index1 = self.exists(classification_list, 'green')
            number_green_index1 = self.getNumberGreen(classification_list, green_index1)

            after = self.exists(word_list,'after')

            green_index2 = self.greenIndex2(green_index1,classification_list)

            number_green_index2 = self.getNumberGreen(classification_list, green_index2)

            # print(green_index1)
            # print(green_index2)



            if(action_index==-1):
                if(after!=-1):
                    if(number_green_index1==-1):
                        if('release_date' in knowledge[word_list[green_index1]]):
                            green_index1_release = knowledge[word_list[green_index1]]['release_date'].lower().split(' ')
                            green_index1_release = int(green_index1_release[len(green_index1_release)-1])
                            if(number_green_index2==-1):
                                if ('due_date' in knowledge[word_list[green_index2]]):
                                    green_index2_due = knowledge[word_list[green_index2]]['due_date'].lower().split(' ')
                                    green_index2_due = int(green_index2_due[len(green_index2_due) - 1])
                                    if(green_index1_release>green_index2_due):
                                        return 'yes'
                                    else:
                                        return 'no'
                                else:
                                    return 'idk'
                            else:

                                if ('due_date' in knowledge[word_list[green_index2]][word_list[green_index2]+' '+word_list[number_green_index2]]):
                                    green_index2_due = knowledge[word_list[green_index2]][word_list[green_index2]+' '+word_list[number_green_index2]]['due_date'].lower().split(' ')
                                    green_index2_due = int(green_index2_due[len(green_index2_due) - 1])
                                    if(green_index1_release>green_index2_due):
                                        return 'yes'
                                    else:
                                        return 'no'
                        else:
                            return 'idk'
                    else:
                        if ('release_date' in knowledge[word_list[green_index1]][word_list[green_index1]+' '+word_list[number_green_index1]]):
                            green_index1_release = knowledge[word_list[green_index1]][word_list[green_index1]+' '+word_list[number_green_index1]]['release_date'].lower().split(' ')
                            green_index1_release = int(green_index1_release[len(green_index1_release) - 1])
                            if (number_green_index2 == -1):
                                if ('due_date' in knowledge[word_list[green_index2]]):
                                    green_index2_due = knowledge[word_list[green_index2]]['due_date'].lower().split(' ')
                                    green_index2_due = int(green_index2_due[len(green_index2_due) - 1])
                                    if (green_index1_release > green_index2_due):
                                        return 'yes'
                                    else:
                                        return 'no'
                                else:
                                    return 'idk'
                            else:

                                if ('due_date' in knowledge[word_list[green_index2]][
                                    word_list[green_index2] + ' ' + word_list[number_green_index2]]):
                                    green_index2_due = knowledge[word_list[green_index2]][
                                        word_list[green_index2] + ' ' + word_list[number_green_index2]][
                                        'due_date'].lower().split(' ')
                                    green_index2_due = int(green_index2_due[len(green_index2_due) - 1])
                                    if (green_index1_release > green_index2_due):
                                        return 'yes'
                                    else:
                                        return 'no'
                        else:
                            return 'idk'
            if(word_list[green_index2]=='course'):
                if (number_green_index1 == -1):
                    if(word_list[green_index1] in knowledge):
                        return 'yes'
                    else:
                        return 'no'
                else:
                    if ([word_list[green_index1] + ' ' + word_list[number_green_index2]] in knowledge[word_list[green_index1]]):
                        return 'yes'
                    else:
                        return 'no'






        _answer = "idk" # NO - for debugging only, replace with your code
        #_answer = "idk"  # I do not know
        #_answer = "yes"  # YES

        return _answer
