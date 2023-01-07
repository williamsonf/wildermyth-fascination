'''
Created on Jan 6, 2023

@author: Fred
'''
import csv

class compatLists():
    def __init__(self, compat_file='friendly.csv', rivalry_file='rivalry.csv'):
        '''
        Args
        -----
        compat_file
            a csv file listing the personalities.
            each personality in this file should be adjacent to its compatible
            personalities, as we will check compatibility by just iterating
            through.
        
        rivalry_file
            a csv file. each row of the csv should begin with a personality,
            with additional entries consisting of incompatible personalities.
            for instance: "bookish","goofball","greedy"
        '''
        self.compat_list = self.read_list(compat_file)
        self.rivalries = rivalry_file
        
    def read_list(self, file):
        result = []
        
        file = open(file)
        for _ in csv.reader(file):
            for personality in _:
                result.append(personality)
                
        return result
    
    def check_compat(self, personality, personalities):
        '''
        Inputs
        ------
        personality : str
            The personality we are checking
        
        personalities : list, str
            a list of strings. the personalities we are checking against
            
        returns int
        '''
        compat_i = self.compat_list.index(personality)
        compat_score = 0
        for p in personalities:
            p = p.lower()
            if (p == self.look_ahead_compat(compat_i)) or (p == self.look_behind_compat(compat_i)) or (p == personality.lower()):
                compat_score += 1
            else:
                pass
            
        return compat_score
    
    def check_rivalry(self, personality, personalities):
        '''
        '''
        riv_score = 0
        rivalries = []
        
        for p in csv.reader(open(self.rivalries)):
            if p[0].lower() == personality.lower():
                rivalries = p[1:]
                
        for p in personalities:
            if p in rivalries:
                riv_score += 1
                
        return riv_score
        
    def look_ahead_compat(self, index):
        return self.compat_list[(index + 1) % len(self.compat_list)].lower()
    
    def look_behind_compat(self, index):
        return self.compat_list[(index - 1) % len(self.compat_list)].lower()
    
if __name__ == '__main__':
    char1 = []
    char2 = []
    checker = compatLists()
    
    u_in = 'z'
    while u_in.lower() != 'x':
        u_in = input("Please enter personalities of your hero, that are scored at 50 or higher. Type x when finished.\n")
        if u_in.lower() in checker.compat_list:
            char1.append(u_in.lower())
            print("Acknowledged. Hero is {}".format(u_in.lower()))
        elif u_in.lower() != 'x':
            print("{} is not a recognized personality. Was there a typo?".format(u_in.lower()))
        else:
            print("Moving on...")
    
    u_in = 'z'
    while u_in.lower() != 'x':
        u_in = input("Please enter the personalities of the hero to match with, that are scored at 50 or higher. Type x when finished.\n")
        if u_in.lower() in checker.compat_list:
            char2.append(u_in.lower())
            print("Acknowledged. Hero is {}".format(u_in.lower()))
        elif u_in.lower() != 'x':
            print("{} is not a recognized personality. Was there a typo?".format(u_in.lower()))
        else:
            print("Done.")
            
    print("Hero 1 is: {}".format(', '.join(char1)))
    print("Hero 2 is: {}".format(', '.join(char2)))
    print("\n")
    compat_score = 0
    for p in char1:
        compat_score += checker.check_compat(p, char2)
        compat_score -= checker.check_rivalry(p, char2)
    if compat_score > 0:
        print("Hero 1 and Hero 2 would likely make good friends.")
    elif compat_score < 0:
        print("Hero 1 and Hero 2 would likely make good rivals.")
    else:
        print("These heroes are indifferent to one another.")
    print("They have a fascination score of {}".format(str(compat_score)))