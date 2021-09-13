# Name: Animal Taming training
# Description: Tames nearby animals to train Animal Taming to GM (to 90 by default) with healing, killing and basic pathfinding
# Author: Mordor
# Era: Any

from ClassicAssist.UO.Data import Direction
from ClassicAssist.UO import UOMath
import System
from Assistant import Engine
from System.Collections.Generic import List

#Select bag with blank runes
FollowTarg = ''
if not FindAlias('Follow_Target'):
    HeadMsg('Select friend to follow.')
    PromptAlias('Follow_Target')
FollowTarg = GetAlias("Follow_Target")
## Script options ##
# Distance to animal before start
max_distance_to_target = 2
max_search_distance = 30
# Change depending on the latency to your UO shard
player_stuck_timer_milliseconds = 15000


def direction_to(mobile, shift_x=0, shift_y=0):
    mobile = Engine.Mobiles.GetMobile(mobile)

    if mobile == None:
        return Direction.Invalid

    return UOMath.MapDirection(Engine.Player.X, Engine.Player.Y,
                               mobile.X + shift_x, mobile.Y + shift_y)


def fast_run(dir):
    if dir == Direction.Invalid:
        return
    Engine.Move(dir, True)


def follow_mobile(mobile, max_distance_to_target=2):
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


def follow_frield():
    # User variables
    global enable_follow
    global max_distance_to_target
    global max_search_distance
    global FollowTarg

    while not Dead('self'):
        if Distance(FollowTarg) <= max_search_distance:
            stuck = not follow_mobile(FollowTarg, max_distance_to_target)
        # Wait a little bit so that the while loop doesn't consume as much CPU
        Pause(50)


follow_frield()
