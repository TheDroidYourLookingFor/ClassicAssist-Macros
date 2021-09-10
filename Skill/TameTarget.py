# Name: Animal Taming training
# Description: Tames nearby animals to train Animal Taming to GM (to 90 by default) with healing, killing and basic pathfinding
# Author: Mordor
# Era: Any

from ClassicAssist.UO.Data import Direction
from ClassicAssist.UO import UOMath
import System
from Assistant import Engine
from System.Collections.Generic import List

## Script options ##
# Change to the number of followers you'd like to keep.
# The script will auto-kill the most recently tamed animal
# Set to the maximum number of times to attempt to tame a single animal. 0 == attempt until tamed
maximum_tame_attempts = 10
# Set the minimum taming difficulty to use when finding animals to tame
minimum_taming_difficulty = 30
# Set this to how you would like to heal your character if they take damage
# Options are:
# 'Magery' = uses the Heal and Greater Heal ability depending on how much health is missing
# 'None' = do not auto-heal
heal_using = 'Magery'
# True or False to track the animal being tamed
enable_follow_animal = False
# Distance to animal before start
max_distance_to_target = 3
max_search_distance = 30
# Change depending on the latency to your UO shard
journal_entry_delay_milliseconds = 500
player_stuck_timer_milliseconds = 15000
taming_attemp_timer_milliseconds = 20000
need_to_recall = 300000


def direction_to(mobile, shift_x=0, shift_y=0):
    mobile = Engine.Mobiles.GetMobile(mobile)

    if mobile == None:
        return Direction.Invalid

    return UOMath.MapDirection(Engine.Player.X, Engine.Player.Y, mobile.X + shift_x, mobile.Y + shift_y)


def fast_run(dir):
    if dir == Direction.Invalid:
        return
    Engine.Move(dir, True)


def follow_mobile(mobile, max_distance_to_target=2):
    '''
    Uses the X and Y coordinates of the animal and player to follow the animal around the map
    Returns True if player is not stuck, False if player is stuck
    '''

    global player_stuck_timer_milliseconds

    SetTimer('player_stuck_timer', 0)
    stuck_counter = 0

    while not InRange(mobile, max_distance_to_target):
        if stuck_counter > 5:
            return False

        fast_run(direction_to(mobile))
        Pause(50)

        if Timer('player_stuck_timer') > player_stuck_timer_milliseconds:
            stuck_counter += 1
            shift_x = -15
            shift_y = -15
            fast_run(direction_to(mobile, shift_x, shift_y))
            SetTimer('player_stuck_timer', 0)

    return True


def train_animal_taming():
    '''
    Trains Animal Taming to GM
    '''
    # User variables
    global maximum_tame_attempts
    global enable_follow_animal
    global journal_entry_delay_milliseconds
    global max_distance_to_target
    global max_search_distance
    global heal_using
    global taming_cap
    global need_to_recall

    if Skill('Animal Taming') == taming_cap:
        MessageBox("Done", 'You have already maxed out Animal Taming!')
        return

    # Initialize variables
    animal_being_tamed = None
    tame_handled = False
    tame_ongoing = False
    times_tried = 0
    current_followers = Followers()

    # Initialize the journal and ignore object list
    ClearJournal()
    ClearIgnoreList()

    # Toggle war mode to make sure the player isn't going to kill the animal being tamed
    if War('self'):
        WarMode('off')

    while not Dead('self'):
        # Cast heal
        if heal_using == 'Magery' and Poisoned('self'):
            Cast('Cure', 'self')
            Pause(1450)
        if heal_using == 'Magery' and DiffHits('self') > 30 and BuffExists('Protection'):
            Cast('Greater Heal', 'self')
            Pause(1450)
        if heal_using == 'Magery' and DiffHits('self') > 30 and not BuffExists('Protection'):
            Cast('Heal', 'self')
            Pause(1450)
        # If there is no animal being tamed, try to find an animal to tame
        SetTimer('need_to_recall', 0)
        while animal_being_tamed == None:
            animal_being_tamed = PromptAlias("TameTarget")
            Pause(1000)
            if Timer('need_to_recall') > need_to_recall:
                SetTimer('need_to_recall', 0)
                # recall to rune logic
                Pause(100)

        if animal_being_tamed > 0 and not tame_ongoing:
            SetTimer('need_to_recall', 0)
            HeadMsg('Found animal to tame', animal_being_tamed)

        if enable_follow_animal and animal_being_tamed > 0 and Distance(animal_being_tamed) <= max_search_distance:
            stuck = not follow_mobile(
                animal_being_tamed, max_distance_to_target)
            if stuck:
                IgnoreObject(animal_being_tamed)
                animal_being_tamed = None

        elif animal_being_tamed > 0 and Distance(animal_being_tamed) > max_search_distance:
            HeadMsg('Animal moved too far away, ignoring for now',
                    animal_being_tamed)
            animal_being_tamed = None
            continue

        # Tame the animal if a tame is not currently being attempted and enough time has passed since last using Animal Taming
        if not tame_ongoing:
            # Clear any previously selected target and the target queue
            CancelTarget()
            ClearTargetQueue()
            ClearJournal()

            # Hey, were finally using the Animal Taming skill! 'bout time!
            UseSkill('Animal Taming')
            WaitForTarget(1000)
            Target(animal_being_tamed)
            Pause(journal_entry_delay_milliseconds)

            # Check if Animal Taming was successfully triggered
            if InJournal('Tame which animal?'):
                times_tried += 1

                # Set tame_ongoing to true to start the journal checks that will handle the result of the taming
                if InJournal('*You start to tame the creature.*'):
                    tame_ongoing = True
                    SetTimer('taming_attemp_timer', 0)

                if InJournal('You have no chance of taming this creature'):
                    # Ignore the object and set to None so that another animal can be found
                    IgnoreObject(animal_being_tamed)

                    ClearJournal()
                    tame_handled = False
                    tame_ongoing = False
                    times_tried = 0
                    animal_being_tamed = None

                    ClearJournal()
                    tame_handled = False
                    tame_ongoing = False
                    times_tried = 0
                    animal_being_tamed = None
                    SetTimer('taming_attemp_timer', 0)

            else:
                continue

        if tame_ongoing:
            Pause(journal_entry_delay_milliseconds)

            if (InJournal('It seems to accept you as master.') or
                InJournal('That wasn\'t even challenging.') or
                    Followers() > current_followers):
                # Animal was successfully tamed
                tame_handled = True
            elif (InJournal('You fail to tame the creature.') or
                    InJournal('You must wait a few moments to use another skill.') or
                    InJournal('That is too far away.') or
                    InJournal('You are too far away to continue taming.') or
                    InJournal('Someone else is already taming this') or
                    InJournal('You have no chance of taming this creature') or
                    InJournal('Target cannot be seen') or
                    InJournal('You can\'t see that.') or
                    InJournal('This animal has had too many owners and is too upset for you to tame.') or
                    InJournal('That animal looks tame already.') or
                    InJournal(
                    'You do not have a clear path to the animal you are taming, and must cease your attempt.') or
                    Timer(
                        'taming_attemp_timer') > taming_attemp_timer_milliseconds
                  ):
                tame_ongoing = False
                SetTimer('taming_attemp_timer', 0)

            if tame_handled:
                ClearJournal()
                tame_handled = False
                tame_ongoing = False
                times_tried = 0
                animal_being_tamed = None
                SetTimer('taming_attemp_timer', 0)

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Pause(50)



# Start Animal Taming
train_animal_taming()