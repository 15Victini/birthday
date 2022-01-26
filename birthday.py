from datetime import date
import random
def stealIP():
    IP = "44.553.212.452"
print("Welcome.")
for i in range(5):
    print(i)
print("Enter your birthday in MM/DD/YYYY format")
m = input("Enter your birth month: > ")
d = input("Enter your birth day: > ")
y = input("Enter your birth year: > ")
if int(y) > 2022:
    print("You are a bozo")
if int(m) > 12:
    print("You are a bozo")
if int(d) > 31:
    stealIP()
    print("You are a bozo and I have your IP address")
print("You were born on: ", m, d, y)
today = date.today()
date_arr = str(today).split('-')
yep = date
age = (int((date_arr[0])) - int(y))
if (int(date_arr[1])) < int(m):
    age = age - 1
if (int(date_arr[1])) == int(m):
    if (int(date_arr[2])) <= int(d):
        age = age - 1
print("You are", age, "year(s) old.")

role_list = [
    'Villager', 'Seer', 'Robber', 'Werewolf', 'Troublemaker', 'Insomniac'
]
player_role = "k"
cpu1_role = "k"
cpu2_role = "k"
temp = random.randrange(6)
player_role = role_list[temp]
del role_list[temp]
player_role_og = player_role
temp = random.randrange(5)
cpu1_role = role_list[temp]
del role_list[temp]
cpu1_role_og = cpu1_role
temp = random.randrange(4)
cpu2_role = role_list[temp]
del role_list[temp]
cpu2_role_og = cpu2_role
cpu1_iam = cpu1_role
cpu2_iam = cpu2_role
print('your role is: ' + player_role)
if player_role == 'Villager':
    print('You do nothing haha')
if player_role == 'Seer':
    print('You will be able to')
    print('either look at another players')
    print('card, or 2 of the center cards')
    print('1 for look at another player')
    player_seer_action = input('2 for look at center cards: ')
if player_role == 'Robber':
    print('You will steal someones card and look at your new card')
if player_role == 'Werewolf':
    print(
        'Your goal is to not die. You will also get to look at one card in the center'
    )
if player_role == 'Troublemaker':
    print('You will get to switch the other  two players cards')
if player_role == 'Insomniac':
    print('At the end of the night, you will look at your own card')
input('Enter anything to continue: ')
print('The Night will now begin')
if player_role_og == 'Werewolf':
    print('The center card is: ' + role_list[random.randrange(3)])
elif cpu1_role_og == 'Werewolf':
    cpu1_know_middle_1 = role_list[random.randrange(3)]
    fake_role1 = cpu1_know_middle_1
elif cpu2_role_og == 'Werewolf':
    cpu2_know_middle_1 = role_list[random.randrange(3)]
    fake_role2 = cpu2_know_middle_1
if player_role_og == 'Seer':
    if player_seer_action == '1':
        seer_player_see = random.randrange(2) + 1
        if seer_player_see == 1:
            seer_player_see2 = cpu1_role
        else:
            seer_player_see2 = cpu2_role
        print('You looked at cpu ' + str(seer_player_see) +
              's card and saw that they are the ' + seer_player_see2)
    if player_seer_action == '2':
        seer_player_see = role_list[random.randrange(3)]
        for x in range(100):
            seer_player_see2 = role_list[random.randrange(3)]
            if seer_player_see != seer_player_see2:
                break
        print('The center cards you saw were ' + seer_player_see + ' and ' +
              seer_player_see2)
if cpu1_role_og == 'Seer':
    seerrng = random.randrange(2)
    if seerrng == 1:
        seer_player_see = role_list[random.randrange(3)]
        for x in range(100):
            seer_player_see2 = role_list[random.randrange(3)]
            if seer_player_see != seer_player_see2:
                break
        cpu1_know_middle_1 = seer_player_see
        cpu1_know_middle_2 = seer_player_see2
    if seerrng == 2:
        seer_player_see = random.randrange(2) + 1
        if seer_player_see == 1:
            tempseer = 'Human Player'
            seer_player_see2 = player_role
        else:
            tempseer = 'cpu2'
            seer_player_see2 = cpu2_role
        cpu_know_player = seer_player_see2
        cpu_seer_look = tempseer
if cpu2_role_og == 'Seer':
    seerrng = random.randrange(2)
    if seerrng == 1:
        seer_player_see = role_list[random.randrange(3)]
        for x in range(100):
            seer_player_see2 = role_list[random.randrange(3)]
            if seer_player_see != seer_player_see2:
                break
        cpu2_know_middle_1 = seer_player_see
        cpu2_know_middle_2 = seer_player_see2
    if seerrng == 2:
        seer_player_see = random.randrange(2) + 1
        if seer_player_see == 1:
            tempseer = 'Human Player'
            seer_player_see2 = player_role
        else:
            tempseer = 'cpu1'
            seer_player_see2 = cpu1_role
        cpu_know_player = seer_player_see2
        cpu_seer_look = tempseer
if player_role_og == 'Robber':
    robber_take = random.randrange(2) + 1
    if robber_take == 1:
        temp = cpu1_role
        cpu1_role = player_role
        player_role = temp
        print('You stole ' + player_role + ' from cpu1')
    if robber_take == 2:
        temp = cpu2_role
        cpu2_role = player_role
        player_role = temp
        print('You stole ' + player_role + ' from cpu2')
if cpu1_role_og == 'Robber':
    robber_take = random.randrange(2) + 1
    if robber_take == 1:
        robtarget = 'Human Player'
        temp = player_role
        player_role = cpu1_role
        cpu1_role = temp
    if robber_take == 2:
        robtarget = 'cpu2'
        temp = cpu2_role
        cpu2_role = cpu1_role
        cpu1_role = temp
    cpu1_iam = cpu1_role
if cpu2_role_og == 'Robber':
    robber_take = random.randrange(2) + 1
    if robber_take == 1:
        robtarget = 'Human Player'
        temp = player_role
        player_role = cpu2_role
        cpu2_role = temp
    if robber_take == 2:
        robtarget = 'cpu1'
        temp = cpu1_role
        cpu1_role = cpu2_role
        cpu2_role = temp
    cpu2_iam = cpu2_role
if player_role_og == 'Troublemaker':
    temp = cpu1_role
    cpu1_role = cpu2_role
    cpu2_role = temp
    print('You switched the roles of cpu1 and cpu2')
if cpu1_role_og == 'Troublemaker':
    temp = player_role
    player_role = cpu2_role
    cpu2_role = temp
if cpu2_role_og == 'Troublemaker':
    temp = player_role
    player_role = cpu1_role
    cpu1_role = temp
if player_role_og == 'Insomniac':
    print('Your role is ' + player_role)
if cpu1_role_og == 'Insomniac':
    cpu1_iam = cpu1_role
if cpu2_role_og == 'Insomniac':
    cpu2_iam = cpu2_role
input('Press enter to continue')
print('It is morning')
print('It is time to discuss')
if cpu1_role_og == 'Robber':
    if cpu1_iam != 'Werewolf':
        print('Before you can ask anything, cpu1 speaks up')
        print('I was the robber, and I robbed ' + robtarget +
              '. They were the ' + cpu1_iam)
if cpu2_role_og == 'Robber':
    if cpu2_iam != 'Werewolf':
        print('Before you can ask anything, cpu2 speaks up')
        print('I was the robber, and I robbed ' + robtarget +
              '. They were the ' + cpu2_iam)
cpu1_interview = False
cpu2_interview = False
for x in range(10):
    print('Who would you like to ask for their story?')
    askwhom = input('1 for cpu1, 2 for cpu2: ')
    if askwhom == '1':
        cpu1_interview = True
        if cpu1_role_og == 'Robber':
            if cpu1_iam != 'Werewolf':
                print('I was the robber, and I robbed ' + robtarget +
                      '. They were the ' + cpu1_iam)
            else:
                robWolf = random.randrange(3)
                if robWolf == 0:
                    print('I was the Villager')
                elif robWolf == 1:
                    print(
                        'I was the Insomniac, at the end of the night, I was the Insomniac'
                    )
                else:
                    print(
                        'I was the Seer. I saw cpu2s card and they were the Werewolf'
                    )
        if cpu1_role_og == 'Villager':
            print('I was the Villager')
        if cpu1_role_og == 'Troublemaker':
            print('I was the Troublemaker')
        if cpu1_role_og == 'Insomniac':
            if cpu1_iam != 'Werewolf':
                print(
                    'I was the Insomniac, at the end of the night I was the ' +
                    cpu1_iam)
            else:
                insWolf = random.randrange(2)
                if insWolf == 1:
                    print('I was the Villager')
                else:
                    print('I was the Troublemaker')
        if cpu1_role_og == 'Seer':
            if seerrng == 1:
                print('I was the seer and looked in the middle, I saw ' +
                      cpu1_know_middle_1 + ' and ' + cpu1_know_middle_2)
            if seerrng == 2:
                print('I was the seer and looked at ' + tempseer +
                      's card. They are the ' + cpu_know_player)
    if askwhom == '2':
        if cpu2_role_og == 'Robber':
            if cpu2_iam != 'Werewolf':
                print('I was the robber, and I robbed ' + robtarget +
                      '. They were the ' + cpu2_iam)
            else:
                robWolf = random.randrange(3)
                if robWolf == 0:
                    print('I was the villager')
                elif robWolf == 1:
                    print(
                        'I was the Insomniac, at the end of the night, I was the Insomniac'
                    )
                else:
                    print(
                        'I was the Seer. I saw cpu1s card and they were the Werewolf'
                    )
        if cpu2_role_og == 'Villager':
            print('I was the Villager')
        if cpu2_role_og == 'Troublemaker':
            print('I was the Troublemaker')
        if cpu2_role_og == 'Insomniac':
            if cpu2_iam != 'Werewolf':
                print(
                    'I was the Insomniac, at the end of the night I was the ' +
                    cpu2_iam)
            else:
                insWolf = random.randrange(2)
                if insWolf == 1:
                    print('I was the Villager')
                else:
                    print('I was the Troublemaker')
        if cpu2_role_og == 'Seer':
            if seerrng == 1:
                print('I was the seer and looked in the middle, I saw ' +
                      cpu2_know_middle_1 + ' and ' + cpu2_know_middle_2)
            if seerrng == 2:
                print('I was the seer and looked at ' + tempseer +
                      's card. They are the ' + cpu_know_player)
        cpu2_interview = True
    if cpu1_interview == True:
        if cpu2_interview == True:
            break

print('Vote for who you think is the werewolf')
vote = int(input('1 for cpu1, 2 for cpu2, 3 for nobody: '))
print('Your role was: ' + player_role)
print('cpu1s role was: ' + cpu1_role)
print('cpu2s role was: ' + cpu2_role)
if 'Werewolf' in role_list:
    if vote == 1 or vote == 2:
        print('There were no werewolves, you lose')
    elif vote == 3:
        print('There were no werewolves, you win')
if player_role == 'Werewolf':
    print('This is a flawed game, you are a werewolf, you win')
if cpu1_role == 'Werewolf':
    if vote == 1:
        print('cpu1 was indeed the werewolf, you win')
    elif vote == 2 or vote == 3:
        print('cpu1 was the werewolf, you lose')
if cpu2_role == 'Werewolf':
    if vote == 2:
        print('cpu2 was indeed the werewolf, you win')
    elif vote == 1 or vote == 3:
        print('cpu2 was the werewolf, you lose')
print('Run again to play again')
