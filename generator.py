import random
import midiutil
from midiutil import MIDIFile
random.seed()

#Creating a list for each note's corresponding midi numbers
a_list = [21,33,45,57,69,81,93,105]
aSh_list = [22,34,46,58,70,82,94,106]
bb_list = aSh_list
b_list = [23,35,47,59,71,83,95,107]
cb_list = b_list
c_list = [24,36,48,60,72,84,96,108]
cSh_list = [25,37,49,61,73,85,97]
db_list = cSh_list
d_list = [26,38,50,62,74,86,98]
dSh_list = [27,39,51,63,75,87,99]
eb_list = dSh_list
e_list = [28,40,52,64,76,88,100]
eSh_list = [29,41,53,65,77,89,101]
f_list = eSh_list
fSh_list = [30,42,54,66,78,90,102]
gb_list = fSh_list
g_list = [31,43,55,67,79,91,103]
gSh_list = [32,44,56,68,80,92,104]
ab_list = gSh_list

#Creating a list of notes for each key's minor and major scales
A_scale = [a_list, b_list, cSh_list, d_list, e_list, fSh_list, gSh_list]
a_scale = [a_list, b_list, c_list, d_list, e_list, f_list, g_list]
Bb_scale = [bb_list, c_list, d_list, eb_list, f_list, g_list, a_list]
ASh_scale = Bb_scale
bb_scale = [bb_list, c_list, db_list, eb_list, f_list, gb_list, ab_list]
aSh_scale = bb_scale
B_scale = [b_list, cSh_list, dSh_list, e_list, fSh_list, gSh_list, aSh_list]
Cb_scale = B_scale
b_scale = [b_list, cSh_list, d_list, e_list, fSh_list, g_list, a_list]
cb_scale = b_scale
C_scale = [c_list, d_list, e_list, f_list, g_list, a_list, b_list]
c_scale = [c_list, d_list, eb_list, f_list, g_list, ab_list, bb_list]
Db_scale = [db_list, eb_list, f_list, gb_list, ab_list, bb_list, c_list]
CSh_scale = Db_scale
cSh_scale = [cSh_list, dSh_list, e_list, fSh_list, gSh_list, a_list, b_list]
db_scale = cSh_scale
D_scale = [d_list, e_list, fSh_list, g_list, a_list, b_list, cSh_list]
d_scale = [d_list, e_list, f_list, g_list, a_list, bb_list, c_list]
Eb_scale = [eb_list, f_list, g_list, ab_list, bb_list, c_list, d_list]
DSh_scale = Eb_scale
eb_scale = [eb_list, f_list, gb_list, ab_list, bb_list, cb_list, db_list]
dSh_scale = eb_scale
E_scale = [e_list, fSh_list, gSh_list, a_list, b_list, cSh_list, dSh_list]
Fb_scale = E_scale
e_scale = [e_list, fSh_list, g_list, a_list, b_list, c_list, d_list]
fb_scale = e_scale
F_scale = [f_list, g_list, a_list, bb_list, c_list, d_list, e_list]
ESh_scale = F_scale
f_scale = [f_list, g_list, ab_list, bb_list, c_list, db_list, eb_list]
eSh_scale = f_scale
Gb_scale = [gb_list, ab_list, bb_list, c_list, db_list, eb_list, f_list]
FSh_scale = Gb_scale
fSh_scale = [fSh_list, gSh_list, a_list, b_list, cSh_list, d_list, e_list]
gb_scale = fSh_scale
G_scale = [g_list, a_list, b_list, c_list, d_list, e_list, fSh_list]
g_scale = [g_list, a_list, bb_list, c_list, d_list, eb_list, f_list]
Ab_scale = [ab_list, bb_list, c_list, db_list, eb_list, f_list, g_list]
GSh_scale = Ab_scale
ab_scale = [ab_list, bb_list, cb_list, db_list, eb_list, e_list, gb_list]
gSh_scale = ab_scale

#Defining chromatic scales
#                   0        1        2       3        4        5       6        7       8        9        10       11
a_chrom_scale = [[a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], 
                 [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh']]
bb_chrom_scale = [[bb_list, 'Bb', 'bb'], [b_list, 'B', 'b'], [c_list, 'C', 'c'], [db_list, 'Db', 'db'], [d_list, 'D', 'd'],
                  [eb_list, 'Eb', 'eb'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [gb_list, 'Gb', 'gb'], [g_list, 'G', 'g'], 
                  [ab_list, 'Ab', 'ab'], [a_list, 'A', 'a']]
aSh_chrom_scale = bb_chrom_scale
b_chrom_scale = [[b_list, 'B', 'b'], [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], 
                 [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh']]
cb_chrom_scale = b_chrom_scale
c_chrom_scale = [[c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], 
                 [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b']]
db_chrom_scale = [[cSh_list, 'CSh', 'cSh'], 
                 [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c']]
cSh_chrom_scale = db_chrom_scale
d_chrom_scale = [[d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh']]
eb_chrom_scale = [[dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd']]
dSh_chrom_scale = eb_chrom_scale
e_chrom_scale = [[e_list, 'E', 'e'], [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh']]
fb_chrom_scale = e_chrom_scale
f_chrom_scale = [[f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e']]
gb_chrom_scale = [[fSh_list, 'FSh', 'fSh'], 
                 [g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], [f_list, 'F', 'f']]
fSh_chrom_scale = gb_chrom_scale
g_chrom_scale = [[g_list, 'G', 'g'], [gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], 
                 [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh']]
ab_chrom_scale = [[gSh_list, 'GSh', 'gSh'], [a_list, 'A', 'a'], [aSh_list, 'ASh', 'aSh'], [b_list, 'B', 'b'], 
                 [c_list, 'C', 'c'], [cSh_list, 'CSh', 'cSh'], [d_list, 'D', 'd'], [dSh_list, 'DSh', 'dSh'], [e_list, 'E', 'e'], 
                 [f_list, 'F', 'f'], [fSh_list, 'FSh', 'fSh'], [g_list, 'G', 'g']]
gSh_chrom_scale = ab_chrom_scale

#Defining scale dict
scale_dict = {'A':A_scale, 'a':a_scale, 'Bb':Bb_scale, 'ASh':ASh_scale,
              'bb':bb_scale, 'aSh':aSh_scale, 'B':B_scale, 'Cb':Cb_scale,
              'b':b_scale, 'cb':cb_scale, 'C':C_scale, 'c':c_scale,
              'Db':Db_scale, 'db':db_scale, 'CSh':CSh_scale, 'cSh':cSh_scale,
              'D':D_scale, 'd':d_scale, 'Eb':eb_scale, 'eb':eb_scale, 
              'DSh':DSh_scale, 'dSh':dSh_scale, 'E':E_scale, 'e':e_scale,
              'Fb':Fb_scale, 'fb':fb_scale, 'F':F_scale, 'f':f_scale,
              'ESh':ESh_scale, 'eSh':eSh_scale, 'Gb':Gb_scale, 'gb':gb_scale,
              'FSh':FSh_scale, 'fSh':fSh_scale, 'G':G_scale, 'g':g_scale,
              'Ab':Ab_scale, 'ab':ab_scale, 'GSh':GSh_scale, 'gSh':gSh_scale}

#Defining chord generation dict:
chord_dict = {'a':a_chrom_scale, 'bb':bb_chrom_scale, 'aSh':aSh_chrom_scale, 'b':b_chrom_scale,
              'cb':cb_chrom_scale, 'c':c_chrom_scale, 'db':db_chrom_scale, 'cSh':cSh_chrom_scale,
              'd':d_chrom_scale, 'eb':eb_chrom_scale, 'dSh':dSh_chrom_scale, 'e':e_chrom_scale,
              'fb':fb_chrom_scale, 'f':f_chrom_scale, 'gb':gb_chrom_scale, 'fSh':fSh_chrom_scale,
              'g':g_chrom_scale, 'ab':ab_chrom_scale, 'gSh':gSh_chrom_scale}

#Chord probability arrays
chord_prob_minor = [[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0], #i
              [0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],[0,3,7,2,0],
              [7,2,10,2,14],[7,2,10,2,14],[7,2,10,2,14],                              #v
              [8,3,0,1,17],[8,3,0,1,17],[8,3,0,1,17],                                 #VI
              [10,5,2,1,20],[10,5,2,1,20],[10,5,2,1,20],                              #VII
              [7,11,2,1,23],[7,11,2,1,24],[7,11,2,1,25],                              #V
              [3,7,10,1,26],[3,7,10,1,27],[3,7,10,1,28],                              #III
              [5,0,8,2,29],[5,0,8,2,30,],[5,0,8,2,31],                                 #iv
              [2,5,9,2,32],[2,5,9,2,33],[2,5,9,2,34],                                 #ii
              [1,5,8,1,35],                                                 #bII
              [6,1,9,2,36],                                                 ##iv
              [9,4,1,1,37],                                                 ##VI
              [1,4,8,2,38],                                                 #bii
              [5,0,9,1,39],                                                 #IV
              [8,3,11,2,40],                                                #vi
              [10,5,1,2,41],                                                #vii
              [2,6,9,1,42],                                                 #II
              [3,6,10,2,43],                                                #iii
              [6,1,10,1,44],                                                ##IV
              [4,8,11,1,45],                                                ##III
              [4,7,11,2,46],                                                ##iii
              [9,4,0,2,47],                                                 ##vi
              [11,6,3,1,48],                                                ##VII
              [11,6,2,2,49]                                                 ##vii
             ]

chord_prob_major = [[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0], #I
              [0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],[0,4,7,2,0],
              [7,11,2,1,23],[7,11,2,1,24],[7,11,2,1,25],                              #V
              [5,0,9,1,39],[5,0,9,1,39],[5,0,9,1,39],                                 #IV
              [2,5,9,2,32],[2,5,9,2,33],[2,5,9,2,34],                                 #ii
              [10,5,1,2,41],[10,5,1,2,41],[10,5,1,2,41],                              #vii
              [8,3,11,2,40],[8,3,11,2,40],[8,3,11,2,40],                              #vi
              [3,6,10,2,43],[3,6,10,2,43],[3,6,10,2,43],                              #iii
              [5,0,8,2,29],[5,0,8,2,30,],[5,0,8,2,31],                                #iv
              [1,5,8,1,35],                                                 #bII
              [6,1,9,2,36],                                                 ##iv
              [9,4,1,1,37],                                                 ##VI
              [1,4,8,2,38],                                                 #bii
              [8,3,0,1,17],                                                 #VI
              [10,5,2,1,20],                                                #VII
              [2,6,9,1,42],                                                 #II
              [3,7,10,1,26],                                                #III
              [6,1,10,1,44],                                                ##IV
              [4,8,11,1,45],                                                ##III
              [4,7,11,2,46],                                                ##iii
              [9,4,0,2,47],                                                 ##vi
              [11,6,3,1,48],                                                ##VII
              [11,6,2,2,49],                                                 ##vii
              [7,2,10,2,14]                                                 #v
             ]


def find_nearest(num, inp_list):
    '''Finds the nearest number to an input from an input list and returns that number.
    If the inp_list contains num, returns num'''
    
    dif = (1, 200)
    for i in inp_list:
        if num > i:
            test = num - i
        elif num < i:
            test = i - num
        else:
            return num
        
        if test < dif[1]:
            dif = (i, test)
    
    return dif[0]

def generate_chord_progression(key, length): #Key of the progression, midi_time to write progression to
    total_length = 0
    num_chords = length // 4
    has_i = False
    chord_progression = [] #Tuples: chord, duration
    for i in range(num_chords):
        if i == num_chords-1: #Determining chord duration
            duration = length - total_length
        elif total_length >= length-4:
            duration = random.randint(2,6)/2
        elif total_length >= length-8:
            duration = random.randint(2,8)/2
        else:
            duration = random.randint(2,16)/2
        total_length += duration
        
        if i == num_chords-1:
            if has_i == False:
                pitch_array = chord_prob[0]
            else:
                chord = random.randint(0,49)
                pitch_array = chord_prob[chord]
        else:
            chord = random.randint(0,49)
            pitch_array = chord_prob[chord]
            if has_i == False:    
                if chord < 14:
                    has_i == True
        
        chord_name = chord_dict[key.lower()][pitch_array[0]][pitch_array[3]]
        chord_progression.append((chord_name, duration, pitch_array[4]))      
    return chord_progression

wchord_type_array = ['sustained', 'eigths', 'sixteens', 'eights_arp', '8pings', '16pings'] #index = 0-5
def write_chord_progression(chord_progression, midi_file_location, type = 'sustained'):
    if type == 'sustained':
        track = random.randint(1,8)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            duration = i[1]
            for j in range(3):
                pitch = chord_dict[key.lower()][pitch_array[j]][0][3]
                output.addNote(track, channel, pitch, midi_file_location, duration, volume)
            midi_file_location += duration
    elif type == 'eigths':
        track = random.randint(1,8)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            total_duration = i[1]
            phrase_duration = 0
            while phrase_duration < total_duration:
                for j in range(3):
                    pitch = chord_dict[key.lower()][pitch_array[j]][0][3]
                    output.addNote(track, channel, pitch, midi_file_location, .4, volume)
                midi_file_location += .5
                phrase_duration += .5
    elif type == 'sixteens':
        track = random.randint(1,9)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            total_duration = i[1]
            phrase_duration = 0
            last_pitch = 0
            while phrase_duration < total_duration:
                while True:
                    pitch = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0][3]
                    if pitch != last_pitch:
                        break
                last_pitch = pitch
                output.addNote(track, channel, pitch, midi_file_location, .25, volume)
                midi_file_location += .25
                phrase_duration += .25
    elif type == 'eigths_arp':
        track = random.randint(1,9)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            total_duration = i[1]
            phrase_duration = 0
            last_pitch = 0
            while phrase_duration < total_duration:
                while True:
                    pitch = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0][3]
                    if pitch != last_pitch:
                        break
                last_pitch = pitch
                output.addNote(track, channel, pitch, midi_file_location, .5, volume)
                midi_file_location += .5
                phrase_duration += .5
    elif type == '8pings':
        track = random.randint(9,11)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            total_duration = i[1]
            phrase_duration = 0
            while phrase_duration < total_duration:
                pitch = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0][3]
                output.addNote(track, channel, pitch, midi_file_location, .25, volume)
                midi_file_location += .5
                phrase_duration += .5
    elif type == '16pings':
        track = random.randint(9,11)
        for i in chord_progression:
            pitch_array = chord_prob[i[2]]
            total_duration = i[1]
            phrase_duration = 0
            while phrase_duration < total_duration:
                pitch = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0][3]
                output.addNote(track, channel, pitch, midi_file_location, .125, volume)
                midi_file_location += .25
                phrase_duration += .25
                
            
        
        
def generate_melody(chord_progression,key):
    melody_data = []
    pitch = c_list[4]
    for i in chord_progression:
        first = 1
        chord_duration = i[1] #Finding duration
        phrase_duration = 0
        thresh = chord_duration - 2
        while phrase_duration < chord_duration:
            rest_chance = random.randint(1, 10)
            if rest_chance == 10: #chance for a rest
                if phrase_duration >= thresh:
                    duration = chord_duration - phrase_duration
                    melody_data.append((0, duration))
                    phrase_duration += duration
                else:
                    duration = random.randint(1,8)/4
                    melody_data.append((0,duration))
                    phrase_duration += duration
                continue
            if phrase_duration >= thresh:
                duration = chord_duration - phrase_duration
            else:
                duration = random.randint(1, 8)/4
            
            phrase_duration += duration
            melody_pitch_roll = random.randint(1,6)
            if first == 1:
                pitch_array = chord_prob[i[2]]
                pitch_class = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0]
                pitch = find_nearest(pitch, pitch_class)
                first = 0
            elif melody_pitch_roll == 1:
                pitch_index = random.randint(0, 6)
                pitch_class = scale_dict[i[0]][pitch_index]
                pitch = find_nearest(pitch, pitch_class)
            elif melody_pitch_roll < 4:
                pitch_index = random.randint(0, 6)
                pitch_class = scale_dict[key][pitch_index]
                pitch = find_nearest(pitch, pitch_class)
            else:
                pitch_array = chord_prob[i[2]]
                pitch_class = chord_dict[key.lower()][pitch_array[random.randint(0,2)]][0]
                pitch = find_nearest(pitch, pitch_class)
            if pitch < 72:
                pitch += 12
            elif pitch > 108:
                pitch -= 12
            melody_data.append((pitch,duration))   
            
    return melody_data

def write_melody(melody_data, midi_file_location):
    if melody_data == None:
        return 0
    
    track = random.randint(13,18)
    for i in melody_data:
        if i[0] == 0:
            midi_file_location += i[1]
            continue
        pitch = i[0]
        duration = i[1]
        output.addNote(track, channel, pitch, midi_file_location, duration, volume)
        midi_file_location += duration

bassline_type_array = ['complex', 'sustained'] #index = 0-1
def generate_bassline(chord_progression,type = 'complex'): #Complex: Djenty, Sustained: One held note
    bassline_data = []
    for i in chord_progression:
        pitch = scale_dict[i[0]][0][2]
        if type == 'complex':
            phrase_duration = 0
            chord_duration = i[1]
            thresh = chord_duration - .5
            while phrase_duration < chord_duration:
                rest_chance = random.randint(1, 2)
                if rest_chance == 1: #chance for a rest
                    if phrase_duration >= thresh:
                        duration = chord_duration - phrase_duration
                        bassline_data.append((0, duration))
                        phrase_duration += duration
                    else:
                        duration = random.randint(1,2)/4
                        bassline_data.append((0,duration))
                        phrase_duration += duration
                else:
                    if phrase_duration >= thresh:
                        duration = chord_duration - phrase_duration
                    else:
                        duration_roll = random.randint(1,3)
                        if duration_roll == 1:
                            duration = .5
                        else:
                            duration = .25
                    phrase_duration += duration
                    bassline_data.append((pitch, duration))
        elif type == 'sustained':
            duration = i[1]
            bassline_data.append((pitch,duration))
    return bassline_data

def write_bassline(bassline_data, midi_file_location):
    if bassline_data == None:
        return 0
    
    for i in bassline_data:
        if i[0] == 0:
            midi_file_location += i[1]
            continue
        pitch = i[0]
        duration = i[1]
        output.addNote(20, channel, pitch, midi_file_location, duration, volume)
        output.addNote(21, channel, pitch, midi_file_location, duration, volume)
        midi_file_location += duration

kick_type_array = ['complex', 'pattern'] # index = 0-1    
def generate_kick_pattern(length, type = 'complex'):
    kick_data = []
    if type == 'complex':
        total_duration = length
        phrase_duration = 0
        thresh = length - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            kick_data.append(duration)
        return kick_data
    elif type == 'pattern':
        pattern = []
        total_duration = length / 4
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            pattern.append(duration)
        for i in range(4):
            for j in pattern:
                kick_data.append(j)
        return kick_data

wkick_type_array = ['complex', 'bassline', 'quarters', 'halves', 'data']        
def write_kick(data, chord_progression, midi_file_location,length, type = 'complex'):
    if data == None:
        return 0
    
    if type == 'bassline': #matches a bassline
        for i in chord_progression:
            pitch = 36
            if i[0] == 0:
                midi_file_location += i[1]
                continue
            duration = i[1]
            output.addNote(23, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += duration
    elif type == 'quarters': #note every beat
        for i in range(int(length)):
            pitch = 36
            output.addNote(23, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += 1
    elif type == 'halves': #Note every two beats
        for i in range(int(length//2)):
            pitch = 36
            output.addNote(23, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += 2
    elif type == 'data': #uses generate_kick_pattern data
        pitch = 36
        for i in data:
            output.addNote(23, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += i

snare_type_array = ['complex', 'simple', 'pattern']             
def generate_snare_pattern(length, type = 'complex'):
    snare_data = []
    if type == 'complex':
        total_duration = length
        phrase_duration = 0
        thresh = length - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            snare_data.append(duration)
        return snare_data
    elif type == 'simple':
        total_duration = length
        phrase_duration = 0
        thresh = length - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            snare_data.append(duration)
        return snare_data
    elif type == 'pattern':
        pattern = []
        total_duration = length / 4
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            pattern.append(duration)
        for i in range(4):
            for j in pattern:
                snare_data.append(j)
        return snare_data

wsnare_type_array = ['data', 'backbeat', 'offbeats']   
def write_snare(snare_data, midi_file_location,length, type ='data'):
    if snare_data == None:
        return 0
    pitch = 38
    if type == 'data': #uses complex, simple, or pattern snare_data
        for i in snare_data:
            duration = i
            output.addNote(24, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += duration
    elif type == 'backbeat':
        for i in range(int(length//2)):
            midi_file_location += 1
            output.addNote(24, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += 1
    elif type == 'offbeats':
        for i in range(int(length)):
            midi_file_location += .5
            output.addNote(24, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += .5

cymbal_type_array = ['simple', 'pattern']            
def generate_cymbal_pattern(length, type = 'simple'):
    cymbal_data = []
    if type == 'simple':
        total_duration = length
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            cymbal_data.append(duration)
        return cymbal_data
    elif type == 'pattern':
        pattern = []
        total_duration = length / 4
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            pattern.append(duration)
        for i in range(4):
            for j in pattern:
                cymbal_data.append(j)
        return cymbal_data
    
wcymbal_type_array = ['data', 'backbeat', 'offbeats', 'onbeats']            
def write_cymbal(data, midi_file_location,length, type = 'data'):
    if data == None:
        return 0
    
    pitch = 37
    if type == 'backbeat':
        for i in range(int(length//2)):
            midi_file_location += 1
            output.addNote(25, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += 1
    elif type == 'offbeats':
        for i in range(int(length)):
            midi_file_location += .5
            output.addNote(25, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += .5
    elif type == 'onbeats':
        for i in range(int(length)):
            output.addNote(25, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += 1
    elif type == 'data':
        for i in data:
            duration = i
            output.addNote(25, channel, pitch, midi_file_location, perc_dur, volume)
            midi_file_location += duration

hihat_type_array = ['complex', 'simple', 'pattern']           
def generate_hihat_pattern(length, type = 'complex'):
    hihat_data = []
    pitch_array = [42,46]
    if type == 'complex':
        total_duration = length
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            if duration == .5:
                pitch = pitch_array[random.randint(0,1)]
            elif duration == 1:
                pitch = 46
            else:
                pitch = 42
            hihat_data.append((pitch, duration))
        return hihat_data
    elif type == 'simple':
        total_duration = length
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            if duration == 1:
                pitch = 46
            else:
                pitch = 42
            hihat_data.append((pitch, duration)) 
        return hihat_data
    elif type == 'pattern':
        pattern = []
        total_duration = length / 4
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            if duration == .5:
                pitch = pitch_array[random.randint(0,1)]
            elif duration == 1:
                pitch = 46
            else:
                pitch = 42
            pattern.append((pitch, duration))
        for i in range(4):
            for j in pattern:
                hihat_data.append(j)
        return hihat_data
    
def write_hihat(data, midi_file_location):
    if data == None:
        return 0
    
    for i in data:
        pitch = i[0]
        duration = i[1]
        output.addNote(26, channel, pitch, midi_file_location, perc_dur, volume)
        midi_file_location += duration

toms_type_array = ['complex', 'simple', 'pattern']        
def generate_toms_pattern(length, type = 'complex'):
    toms_data = []
    pitch_array = [43,45,47]
    if type == 'complex':
        total_duration = length
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            pitch = pitch_array[random.randint(0,2)]
            toms_data.append((pitch, duration))
        return toms_data
    elif type == 'simple':
        total_duration = length
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,2)/2
            phrase_duration += duration
            pitch = pitch_array[random.randint(0,2)]
            toms_data.append((pitch, duration)) 
        return toms_data
    elif type == 'pattern':
        pattern = []
        total_duration = length / 4
        phrase_duration = 0
        thresh = total_duration - 1
        while phrase_duration < total_duration:
            if phrase_duration >= thresh:
                duration = total_duration - phrase_duration
            else:
                duration = random.randint(1,4)/4
            phrase_duration += duration
            pitch = pitch_array[random.randint(0,2)]
            pattern.append((pitch, duration))
        for i in range(4):
            for j in pattern:
                toms_data.append(j)
        return toms_data
    
def write_toms(data, midi_file_location):
    if data == None:
        return 0
    
    for i in data:
        pitch = i[0]
        duration = i[1]
        output.addNote(27, channel, pitch, midi_file_location, perc_dur, volume)
        midi_file_location += duration
        
def generate_section(key,length): #Format of output list:                                      0: chord progression
    section_data = []                                                                         #1: chord type 
                                                                                              #2: melody data
    chord_progression = generate_chord_progression(key,length) #chord progression and type     3: bass_data
    chord_type = wchord_type_array[random.randint(0,5)]                                       #4: kick_data
    section_data.append(chord_progression)                                                    #5: kick_type
    section_data.append(chord_type)                                                           #6: snare_data
                                                                                              #7: snare_type
    melody_chance = random.randint(1,4) #melody                                               #8: cymbal_data
    if melody_chance == 4:                                                                    #9: cymbal_type
        melody_data = None                                                                    #10: hihat_data
    else:                                                                                     #11: toms_data
        melody_data = generate_melody(chord_progression,key)                                  #12: length
    section_data.append(melody_data)
    
    bass_chance = random.randint(1,10) #Bassline
    if bass_chance == 10:
        bass_data = None
        bass_type = 0
    else:
        bass_type = bassline_type_array[random.randint(0,1)]
        bass_data = generate_bassline(chord_progression, bass_type)
    section_data.append(bass_data)
    
    kick_chance = random.randint(1,15) #kick
    if kick_chance == 15:
        kick_data = None
        kick_type = 0
    else:
        kick_data = generate_kick_pattern(length, kick_type_array[random.randint(0,1)])
        if bass_type == 'complex':
            kick_mirror_chance = random.randint(1,4)
            if kick_mirror_chance > 1:
                kick_type = wkick_type_array[4]
            else:
                kick_type = wkick_type_array[random.randint(0,3)]
        else:
            kick_type = wkick_type_array[random.randint(0,3)]
    section_data.append(kick_data)
    section_data.append(kick_type)
    
    snare_chance = random.randint(1,5) #snare
    if snare_chance == 5:
        snare_data = None
        snare_type = 0
    else:
        snare_data = generate_snare_pattern(length, snare_type_array[random.randint(0,2)])
        snare_chance = random.randint(1,2)
        if snare_chance == 2:
            snare_type = wsnare_type_array[0]
        else:
            snare_type = wsnare_type_array[random.randint(1,2)]
    section_data.append(snare_data)
    section_data.append(snare_type)
    
    cymbal_chance = random.randint(1,5) # cymbal
    if cymbal_chance == 5:
        cymbal_data = None
        cymbal_type = 0
    else:
        cymbal_data = generate_cymbal_pattern(length, cymbal_type_array[random.randint(0,1)])
        cymbal_chance = random.randint(1,2)
        if cymbal_chance == 2:
            cymbal_type = wcymbal_type_array[0]
        else:
            cymbal_type = wcymbal_type_array[random.randint(1,3)]
    section_data.append(cymbal_data)
    section_data.append(cymbal_type)
    
    hihat_chance = random.randint(1,3)
    if hihat_chance == 3:
        hihat_data = None
    else:
        hihat_data = generate_hihat_pattern(length, hihat_type_array[random.randint(0,2)])
    section_data.append(hihat_data)    
    
    toms_chance = random.randint(1,2)
    if toms_chance == 2:
        toms_data = None
    else:
        toms_data = generate_toms_pattern(length, toms_type_array[random.randint(0,2)])
    section_data.append(toms_data)
    
    section_data.append(length)
    
    return section_data


def write_section(section_data, midi_file_location):
    write_chord_progression(section_data[0], midi_file_location,section_data[1])
    extra_roll = random.randint(1,2)
    while extra_roll == 1:
        write_chord_progression(section_data[0], midi_file_location,wchord_type_array[random.randint(0,5)])
        extra_roll = random.randint(1,3)
    write_melody(section_data[2], midi_file_location)
    write_bassline(section_data[3], midi_file_location)
    write_kick(section_data[4], section_data[0], midi_file_location,section_data[12], section_data[5])
    write_snare(section_data[6], midi_file_location, section_data[12], section_data[7])
    write_cymbal(section_data[8], midi_file_location,section_data[12], section_data[9])
    write_hihat(section_data[10], midi_file_location)
    write_toms(section_data[11], midi_file_location)
    midi_file_location += section_data[12]
    return midi_file_location
    
def stinger_ending(key, midi_file_location):
    stinger_duration = random.randint(2,4)/4
    chord_chance = random.randint(1,4)
    if chord_chance < 4:
        chord_pitch_array= chord_prob[0]
        track = random.randint(1,8)
        for j in range(3):
            pitch = chord_dict[key.lower()][chord_pitch_array[j]][0][3]
            output.addNote(track, channel, pitch, midi_file_location, stinger_duration, volume)
    
    bass_chance = random.randint(1,10)
    if bass_chance < 10:
        pitch = scale_dict[key][0][2]
        output.addNote(20, channel, pitch, midi_file_location, stinger_duration, volume)
        output.addNote(21, channel, pitch, midi_file_location, stinger_duration, volume)
    
    output.addNote(23, channel, 36, midi_file_location, perc_dur, volume)
    
    snare_chance = random.randint(1,3)
    if snare_chance < 3:
        output.addNote(24, channel, 38, midi_file_location, perc_dur, volume)
    
    cymbal_chance = random.randint(1,3)
    if cymbal_chance < 3:
        output.addNote(25, channel, 37, midi_file_location, perc_dur, volume)
        
    hihat_chance = random.randint(1,3)
    if hihat_chance < 3:
        pitch_array = [46,44,42]
        pitch = pitch_array[random.randint(0,2)]
        output.addNote(26, channel, pitch, midi_file_location, perc_dur, volume)
        
    toms_chance = random.randint(1,3)
    if toms_chance < 3:
        pitch_array = [36,43,45,47]
        pitch = pitch_array[random.randint(0,3)]
        output.addNote(27, channel, 38, midi_file_location, perc_dur, volume)
        
def change_tempo(tempo, midi_file_location):
    tempo_change = random.randint(-15,15)
    tempo = tempo + tempo_change
    for i in range(tracks):
        output.addTempo(i, midi_time, tempo)
        
    
    
    

        
        

#Setting up output midi file
track    = 0  #Guide: 0: Chords Bus, 1-8: Chords, 9-11: Pings, 12: Melody Buss, 13-18: Leads,
channel  = 0         #19: Bass Bus, 20-21: Basses, 22: Drums Bus, 23: Kick, 24: Snare, 25: Cymbal, 26: hihat, 27: Toms
midi_time = 0   # In beats
duration = 1   # In beats
tempo    = 120  # In BPM
volume   = 96 # 0-127, as per the MIDI standard
perc_dur = .1

#Must add tempo to each track
tracks = 28
output = MIDIFile(tracks)

key = input('Enter Key: ')
if key[0].isupper() == True:
    chord_prob = chord_prob_major
else:
    chord_prob = chord_prob_minor
section_number = input('Enter number of unique sections: ')
section_number = int(section_number)
tempo = input('Enter starting tempo: ')
tempo = int(tempo)
for i in range(tracks):
    output.addTempo(i, midi_time, tempo)
    
section_data_master = []


for i in range(section_number):
    len_roll = random.randint(1,6)
    if len_roll == 1:
        sec_len = 16
    elif len_roll == 2:
        sec_len = 24
    elif len_roll == 3:
        sec_len = 32
    else:
        sec_len = random.randint(16,32)
    section_data = generate_section(key,sec_len)
    section_data_master.append(section_data)

section_tracker = []
while True:
    index = random.randint(0, section_number-1)
    if index in section_tracker:
        reroll_chance = random.randint(1,4)
        if reroll_chance == 4:
            continue
        midi_time = write_section(section_data_master[index], midi_time)
        repeat_chance = random.randint(1,4)
        if repeat_chance < 4:
            midi_time = write_section(section_data_master[index], midi_time)
        tempo_roll = random.randint(1,20)
        if tempo_roll == 20:
            change_tempo(tempo, midi_time)
    else:
        section_tracker.append(index)
        midi_time = write_section(section_data_master[index], midi_time)
        repeat_chance = random.randint(1,4)
        if repeat_chance < 4:
            midi_time = write_section(section_data_master[index], midi_time)
        tempo_roll = random.randint(1,20)
        if tempo_roll == 20:
            change_tempo(tempo, midi_time)
    if len(section_tracker) == section_number:
        break


ending_type = random.randint(1,2)
if ending_type == 1:
    for i in range(4):
        midi_time = write_section(section_data_master[index], midi_time)
else:
    stinger_ending(key, midi_time)




with open("output.mid", "wb") as output_file:
    output.writeFile(output_file)

print("Finished.")
    

    


