﻿
"""
cl = []
for i in range(0, 256): 
    cl.append(f'\x1b[38;5;{i}m')
for _ in range(0,101):
    for z in cl:
        print(f"■{z}",end='')
"""

"""
import timeit

set1 = set(range(10000))

set2 = set(range(5000, 15000))


time_intersection = timeit.timeit(lambda: set1.intersection(set2), number=10000)

time_and = timeit.timeit(lambda: set1 & set2, number=10000)


print("Время выполнения intersection():", time_intersection)

print("Время выполнения &: ", time_and)
        """

"""class Params:
    def __init__(self, peer_id, man1, man2, man1name, man2name, allow, await_state):
        self.peer_id = peer_id
        self.man1 = man1
        self.man2 = man2
        self.man1name = man1name
        self.man2name = man2name
        self.allow = allow
        self.await_state = await_state

from typing import Optional

def params_marry_control() -> Optional[Params]:
        params = {
            "peer_id": 12412412,
            "man1" : 34634634634,
            "man2": 5475745754,
            "man1name": "asfasfas",
            "man2name": "bmldslmbldsmbdfs",
            "allow": 1,
            "await_state": 0
            }
        
        if params: return Params(**params)
        else: return Params(...)

a = params_marry_control() 
print(a.peer_id)"""

import re


iii = {'count': 37, 'items': [{'id': 288958605, 'owner_id': 388145277, 'size': 1617, 'title': 'сохранки 2022', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1671447796, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457301050, 'thumb_is_last': 1, 'updated': 1672588062}, {'id': 288957831, 'owner_id': 388145277, 'size': 27, 'title': 'сигнатуры', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1671446966, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457306468, 'thumb_is_last': 1, 'updated': 1679213170}, {'id': 279113124, 'owner_id': 388145277, 'size': 2611, 'title': 'сохранки 2021', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1625846233, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457272817, 'thumb_is_last': 1, 'updated': 1671897490}, {'id': 269327874, 'owner_id': 388145277, 'size': 2, 'title': 'рисунки знакомых', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1581770722, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457254024, 'thumb_is_last': 
1, 'updated': 1581770744}, {'id': 269323119, 'owner_id': 388145277, 'size': 72, 'title': 'WAR MEMES', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1581756029, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457270812, 'thumb_is_last': 1, 'updated': 1622213357}, {'id': 269320590, 'owner_id': 388145277, 'size': 4, 'title': 'music bingo ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1581746050, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': 
[], 'privacy_view': [], 'thumb_id': 457253944, 'thumb_is_last': 1, 'updated': 1581746445}, {'id': 269320266, 'owner_id': 388145277, 'size': 54, 'title': 
'ШИТЛЕСС', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1581743867, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457253654, 'thumb_is_last': 1, 'updated': 1581754237}, {'id': 269128242, 'owner_id': 388145277, 'size': 68, 'title': 'шиза', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1580992523, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457310385, 'thumb_is_last': 1, 'updated': 1687570778}, {'id': 
269125192, 'owner_id': 388145277, 'size': 45, 'title': 'благородные мемы', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1580984140, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457253960, 'thumb_is_last': 1, 'updated': 1581746927}, {'id': 269008427, 'owner_id': 388145277, 'size': 4, 'title': 'дурка', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1580553833, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457264380, 'thumb_is_last': 1, 'updated': 1696019052}, {'id': 263854904, 'owner_id': 388145277, 'size': 66, 'title': 'всратый mail.ru', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1564499759, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457250990, 'thumb_is_last': 1, 'updated': 1571824096}, {'id': 263854228, 'owner_id': 388145277, 'size': 300, 'title': 'на переговоры', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1564498188, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457308517, 'thumb_is_last': 1, 'updated': 1683295065}, {'id': 260853472, 'owner_id': 388145277, 'size': 72, 'title': 'пизданутый coding', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1554044117, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457313743, 'thumb_is_last': 1, 'updated': 1690765572}, {'id': 259899655, 'owner_id': 388145277, 'size': 254, 'title': 'всратые кошаки', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1550871458, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457299030, 'thumb_is_last': 1, 'updated': 1670234979}, {'id': 259899598, 'owner_id': 388145277, 'size': 28, 'title': 'смысл', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1550871219, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456245079, 'thumb_is_last': 1, 'updated': 1550871219}, {'id': 259899417, 'owner_id': 388145277, 'size': 31, 'title': 'хуйня с валакасом', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1550870474, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457253968, 'thumb_is_last': 1, 'updated': 1581747741}, {'id': 255335197, 'owner_id': 388145277, 'size': 18, 'title': 'серьезные ебальники', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1535266527, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457253887, 'thumb_is_last': 1, 'updated': 1581744141}, {'id': 255335144, 'owner_id': 388145277, 'size': 283, 'title': 'бред и хуйня', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1535266340, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457316743, 'thumb_is_last': 1, 'updated': 1696019171}, {'id': 253483761, 'owner_id': 388145277, 'size': 197, 'title': '©.        ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1527600725, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457306844, 'thumb_is_last': 1, 'updated': 1680175188}, {'id': 253483579, 'owner_id': 388145277, 'size': 25, 'title': 'словарь', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1527600143, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456248111, 'thumb_is_last': 1, 'updated': 1559451152}, {'id': 252656056, 'owner_id': 388145277, 'size': 44, 'title': 'опросники долбоеба ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1524225534, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457295315, 'thumb_is_last': 1, 'updated': 1662731363}, {'id': 
252552230, 'owner_id': 388145277, 'size': 138, 'title': 'stalker', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1523805462, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457295513, 'thumb_is_last': 1, 'updated': 1663261301}, {'id': 252503999, 'owner_id': 388145277, 'size': 137, 'title': 'переговоры (н;п;к)', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1523615916, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456247792, 'thumb_is_last': 1, 'updated': 1558208638}, {'id': 252503934, 'owner_id': 388145277, 'size': 136, 'title': 'переговоры ( ат)', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1523615753, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457296438, 'thumb_is_last': 1, 'updated': 1665600720}, {'id': 252503891, 'owner_id': 388145277, 'size': 24, 'title': 'переговоры (зл)', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1523615614, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456245473, 'thumb_is_last': 1, 'updated': 1551156494}, {'id': 252503829, 'owner_id': 388145277, 'size': 45, 'title': 'переговоры ( ухмыл)', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1523615427, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456247146, 'thumb_is_last': 1, 'updated': 1560365785}, {'id': 252093341, 'owner_id': 388145277, 'size': 44, 'title': 'личное ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1522081354, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457313689, 'thumb_is_last': 1, 'updated': 1690713897}, {'id': 252093278, 'owner_id': 388145277, 'size': 25, 'title': 'логотип NOD', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1522081186, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456244949, 'thumb_is_last': 1, 'updated': 1542647162}, {'id': 251944567, 'owner_id': 388145277, 'size': 105, 'title': 'arts', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521553261, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457311440, 'thumb_is_last': 1, 'updated': 1688322060}, {'id': 251944495, 'owner_id': 388145277, 'size': 1264, 'title': 'mems', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521553089, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457316673, 'thumb_is_last': 1, 'updated': 1695837559}, {'id': 251944468, 'owner_id': 388145277, 'size': 107, 'title': 'мудрёная хуйня ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521553011, 'description': '', 'can_delete': True, 'can_include_to_feed': True, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457311438, 'thumb_is_last': 1, 'updated': 1688315328}, {'id': 251944431, 'owner_id': 388145277, 'size': 16, 'title': 'USSR', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521552911, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456247258, 'thumb_is_last': 1, 'updated': 1557600013}, {'id': 251944407, 'owner_id': 388145277, 'size': 32, 'title': 'Kane . Knyaz.', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521552852, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456243840, 'thumb_is_last': 1, 'updated': 1535265704}, {'id': 251944323, 'owner_id': 388145277, 'size': 13, 'title': 'deus vult', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521552666, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 456247253, 'thumb_is_last': 1, 'updated': 1556542035}, {'id': 251944244, 'owner_id': 388145277, 'size': 41, 'title': '            ', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521552481, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457249307, 'thumb_is_last': 1, 'updated': 1576819742}, {'id': 251944105, 'owner_id': 388145277, 'size': 128, 'title': 'brotherhood NOD', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521552080, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457249652, 'thumb_is_last': 1, 'updated': 1567429300}, {'id': 251944065, 'owner_id': 388145277, 'size': 4, 'title': 'переговорная', 'feed_disabled': 0, 'feed_has_pinned': 0, 'created': 1521551952, 'description': '', 'can_delete': True, 'can_include_to_feed': False, 'is_locked': True, 'privacy_comment': [], 'privacy_view': [], 'thumb_id': 457254626, 'thumb_is_last': 1, 'updated': 1584339741}]}


