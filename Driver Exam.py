import json

#Correct answers
exam_key_ans = {}

# drivers answers
drvr_ans = {'1': None, '2': None, '3': None, '4': None, '5': None,
            '6': None, '7': None, '8': None, '9': None, '10': None,
            '11': None, '12': None, '13': None, '14': None, '15': None,
            '16': None, '17': None, '18': None, '19': None, '20': None}

# correct answers
drvr_correct = ''

# incorrect answers
drvr_wrong = ''

#clear screen
def wipe():
    print('\n'*49)
   
# Checks if the user input only one character
def ans_lmt():
    while True:
        if len(pick) > 1:
            print('Please enter one \'Letter\'!\n',
                  'Any character input other than the choices given can result in an incorrect answer.')
            return pick
        else:
            break

# Checks the answer given with the ans_key to add to the wrong or correct list
def drvr_check():
    r = 0 
    w = 0
    for ans_key, ans_value in exam_key_ans.items():
        drvr_value = drvr_ans[ans_key]
        if drvr_value == ans_value:
            r += 1
        else:
            w += 1
    return r, w

# generates a pass or fail based on wrong and correct lists
def fail_pass():
    if drvr_wrong >= 6:
        print('You failed your drivers exam.\n',
              'Your drivers license has been revoked!\n',
              'Please find your designated driver.\n',
              'You are NOT permited to drive until you return in six (6) weeks to try again.')
    else:
        print('Congratulations, you passed your drivers exam!') 

# Retrieve Answer Key
def read_file_ans():
    with open('answerkey.txt', 'r') as f:
        python_object = json.load(f)
        return python_object

# The driver's exam program
while True:
    print('Welcome! The driver exam is multiple choice.',
          '\nYou must correctly answer 15 out of 20 questions to receive a passing score.\n',
          'Any character input other than \'A, B, C, or D\' will result in an incorrect answer.'
          '\nGood luck!')
    input('Press Enter to begin!:')
    wipe()
    print('[1] How fast should you drive in neighborhoods?')
    print('\nA: 20 MPH',
          '\nB: 30 MPH',
          '\nC: 25 MPH',
          '\nD: 40 MPH')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['1'] = pick
    print('_'*50)
    print('[2] What is the exit ramp called?')
    print('\nA: Public roadway merger',
          '\nB: The only way off the freeway',
          '\nC: The exit ramp',
          '\nD: Deceleration Lane')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['2'] = pick
    print('_'*50)
    print('[3] What does the \'P\' with a green circle mean?')
    print('\nA: You can park',
          '\nB: Limited parking',
          '\nC: Two hour parking',
          '\nD: Metered parking')
    pick = input('Enter Answer: ').capitalize()     
    ans_lmt()
    drvr_ans['3'] = pick
    print('_'*50)
    print('[4] What does the stop light color yellow mean?')
    print('\nA: Precede with caution',
          '\nB: Hurry up and get through',
          '\nC: Slow down and stop',
          '\nD: The choice is yours, just don\'t wrap around the signal pole')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['4'] = pick
    print('_'*50)
    print('[5] How do you know to use caution while driving?')
    print('\nA: Look for the blinking yellow light in school zones',
          '\nB: Look for yellow diamond shaped signs with instructions',
          '\nC: If the signal light is green',
          '\nD: Just drive cautiously')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['5'] = pick
    print('_'*50)
    print('[6] If you missed the MPH sign, what should you do?')
    print('A: Drive at the speed you last saw\n',
          'B: Look around, if no businesses drive 55 MPH\n',
          'C: Look around, if no buildings drive 65 - 75 MPH',
          '\nD: Look around, and figure it out')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['6'] = pick
    print('_'*50)
    print('[7] What does MPH mean?')
    print('\nA: Maple Peanut Hour',
          '\nB: Miles Per Hour',
          '\nC: Megabites Per Hour',
          '\nD: \'Missions Per Hour')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['7'] = pick
    print('_'*50)
    print('[8] What color is the stop sign')
    print('\nA: Red',
          '\nB: Blue',
          '\nC: Yellow',
          '\nD: Orange')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['8'] = pick
    print('_'*50)
    print('[9] What should you do first before you drive?')
    print('\nA: Check your mirrors',
          '\nB: Put the gear in Drive',
          '\nC: Put on your seatbelt',
          '\nD: Put the gear in Reverse')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['9'] = pick
    print('_'*50)
    print('[10] What color is the pedestrian crossing sign?')
    print('\nA: Orange',
          '\nB: Yellow',
          '\nC: Blue',
          '\nD: White')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['10'] = pick
    print('_'*50)
    print('[11] What is the sequence of the letters on the gear shift?')
    print('\nA: P, R, D, N, 1, 2',
          '\nB: P, R, N, D, 2, 1',
          '\nC: P, D, R, 2, 1',
          '\nD: D, R, 2, N, 1, P')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['11'] = pick
    print('_'*50)
    print('[12] What should you do if you see Police lights?')
    print('\nA: Slow down but keep driving until they pass',
          '\nB: Floor it, they are trying to catch you!',
          '\nC: Pull over slowly to a safe area and turn off the ignition',
          '\nD: Get ready for Grand Theft Auto and Go Live!')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['12'] = pick
    print('_'*50)
    print('[13] What do you do if there is a vehicle in the auxillary lane?')
    print('\nA: Stay where you are if the door is not open',
          '\nB: Play Chicken',
          '\nC: Use the car as a ramp and get Tony Hawk points',
          '\nD: Switch lanes or slow down')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['13'] = pick
    print('_'*50)
    print('[14] What does a double solid yellow line mean?')
    print('\nA: No passing the car in front of you',
          '\nB: Pass with caution',
          '\nC: Drive close to the car ahead of you to make them speed up',
          '\nD: Your choice')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['14'] = pick
    print('_'*50)
    print('[15] What symbol tells drivers to watch for pedestrians at a red light?')
    print('\nA: A pedestrian on the corner',
          '\nB: A yellow hand and white man',
          '\nC: The red light',
          '\nD: A white man and yellow hand')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['15'] = pick
    print('_'*50)
    print('[16] What does no turn on red mean?')
    print('\nA: You must stop completely, then you can turn',
          '\nB: As long as there are no pedestrians, you can turn',
          '\nC: You can only turn right on green',
          '\nD: That sign is only for busses')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['16'] = pick
    print('_'*50)
    print('[17] What does a solid line and a dotted line on a 2-way lane mean?')
    print('\nA: Do not pass the car in front of you',
          '\nB: Drive really close to the car in front of you to make them speed up',
          '\nC: Use caution to pass the car in front of you',
          '\nD: Honk your horn to make them pull over')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['17'] = pick
    print('_'*50)
    print('[18] What does the sign \'13ft 8in\' mean on underpasses?')
    print('\nA: The place for the towns to hang festival banners',
          '\nB: A vehicle carrying a load to safely travel under the bridge',
          '\nC: They are just decoration to make the bridge not look plain',
          '\nD: A leftover sign the contractors forgot to remove')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['18'] = pick
    print('_'*50)
    print('[19] What is the outer lane that begins at an on-ramp,and ends at the off-ramp called?')
    print('\nA: On-coming traffic',
          '\nB: Exiting traffic',
          '\nC: The lane to use to go around slow drivers',
          '\nD: Auxiliary Lane')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['19'] = pick
    print('_'*50)
    print('[20] What is the speed limit on the highway?')
    print('\nA: 70',
          '\nB: 65',
          '\nC: 55',
          '\nD: 75')
    pick = input('Enter Answer: ').capitalize()
    ans_lmt()
    drvr_ans['20'] = pick
    exam_key_ans = read_file_ans()
    drvr_correct, drvr_wrong = drvr_check()      
    print('\t', '_'*25)
    print('_'*50)
    print('\t', '_'*25)
    print('You have finished taking the test!\n')
    input('Press any key to view your results\n')
    wipe()
    print('You answered', drvr_correct, 'questions correctly.')
    print('You answered', drvr_wrong, 'questions incorrectly.')
    print('\t', '_'*25)
    print('_'*50)
    print('\t', '_'*25)
    print()
    fail_pass()
    break 

         
