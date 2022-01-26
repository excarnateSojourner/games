'''
Mines of Moria

Last significant modification 2017-09-04.
Created before 2016-01-09.
This program was originally created when I was completing Python the Hard Way in highschool. I wanted to continue working on it, but I did not particularly like the Python language, so I converted it to C. Then I realized that Python is actually way better than C when you are not forced to use unnecessarily complex features of the language, so I converted it back. The structure of the code has been changed a great deal, because I have removed all classes.

The Mines of Moria is an adventure game in which you must lead a band of renegades and rangers through the massive subterranean maze that is the Mines of Moria. The goal is to reach the exit on the East side while suffering as little collateral damage as possible.
'''

from random import randint

# player's inventory
inventory = ['torch']

def main():
	
	# print epic-looking title
	print(
		' ▄▄▄█████▓ ██░ ██ ▓█████	 ███▄ ▄███▓ ██▓ ███▄	█ ▓█████   ██████	 ▒█████	█████▒	███▄ ▄███▓ ▒█████   ██▀███   ██▓ ▄▄▄	  \n',
		'▓  ██▒ ▓▒▓██░ ██▒▓█   ▀	▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▒██	▒	▒██▒  ██▒▓██   ▒	▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▒████▄	\n',
		'▒ ▓██░ ▒░▒██▀▀██░▒███	  ▓██	▓██░▒██▒▓██  ▀█ ██▒▒███   ░ ▓██▄	  ▒██░  ██▒▒████ ░	▓██	▓██░▒██░  ██▒▓██ ░▄█ ▒▒██▒▒██  ▀█▄  \n',
		'░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄	▒██	▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒   ▒██   ██░░▓█▒  ░	▒██	▒██ ▒██   ██░▒██▀▀█▄  ░██░░██▄▄▄▄██ \n',
		'  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒▒██████▒▒   ░ ████▓▒░░▒█░	   ▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██░ ▓█   ▓██▒\n',
		'  ▒ ░░	▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░   ░ ▒░▒░▒░  ▒ ░	   ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░\n',
		'	░	 ▒ ░▒░ ░ ░ ░  ░   ░  ░	  ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░	 ░ ▒ ▒░  ░		 ░  ░	  ░  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░\n',
		'  ░	   ░  ░░ ░   ░	  ░	  ░	▒ ░   ░   ░ ░	░   ░  ░  ░	 ░ ░ ░ ▒   ░ ░	   ░	  ░   ░ ░ ░ ▒	░░   ░  ▒ ░  ░   ▒   \n',
		'		  ░  ░  ░   ░  ░		  ░	░		   ░	░  ░	  ░		 ░ ░					░	   ░ ░	 ░	  ░		░  ░')
	# greet the player
	print(
		'\n\n\tWelcome to the Mines of Moria.\n',
		'As you are playing, make sure to scroll up if and when necessary, so that you don\'t miss part of the story; that would be very confusing.\n',
		'\tIn this game, you must lead a band of renegades and rangers through an infamous subterranian maze.',
		'Before we begin, you must choose a name for yourself.',
		'Make sure that it sounds either epic or hilarious (it\'s up to you).')
	username = input('==> ')
	# introduce game
	print(
		'Get comfortable. Here we go...\n'
		'\n\tYou have been selected to lead a band of adventurers on a dangerous journey to reach the land of Lothlorien.',
		'With you are Megablockless (an elf), Stanli (a dwarf), Biblio (a hobbit), and a large rodent who everyone lovingly refers to as the DLF (Dear Little Friend).',
		'It is rumored that at Lothlorien you may find the answer to life, the universe, and everything.',
		'(Obviously you have not read the Hitchhiker\'s Guide to the Galaxy.)',
		'You have travelled nigh on a fortnight, passing through forests, swamps, rivers, glens (whatever those are), dales (who knows?) and the occasional valley.',
		'The only remaining challenge that you must face is the dreaded, the lengendary, Mines of Moria.',
		'You and your fellow adventurers have heard the tales about the trecherous caverns that zig-zag their way through this mountain range.',
		'Only one thing about them is certain: no one has ever come out alive.\n',
		'\tFor the past hour or so, you and your compatriots have been searching up and down the mountain face, looking for any sign of an entrance, as the main entrance was covered up by rubble hundreds of years ago.\n',
		'\t"{}! I think I\'ve found something!" you hear Megablockless call up to you.'.format(username),
		'You walk down to where he is, and he shows you a small, rectangular slap of stone in the side of the mountain.',
		'It appears to be some sort of door.',
		'You call the group together.',
		'As a dwarf, Stanli knows the most about dwarvish history, and therefore about the Mines.',
		'He informs you that the door was likely some sort of secret exit that was used in the case of an invasion.',
		'Since it was built as an exit (with nothing to push against on the outside), it will take some time to force open.',
		'You tell him to get to work on it, and you (along with the rest of the group) head back to your base, roughly 200 metres away.\n',
		'\tSome time later, Stanli comes back to the base and reports that the door has been forced open, and the entrance way appears to be large enough for everyone to fit through.',
		'After packing up your campsite, your team enters the hole with Stanli in the lead.')
	entrance_hall('intro')
	exit(0)

def entrance_hall(previous_scene):
	if previous_scene == 'intro':
		print(
			'\tAfter walking through the darkness for a minute or so (crouching because of the limits of the passageway), you hear Stanli say, "I\'m out! I\'m in some kind of room, but I need a light."',
			'After gathering in the open area, you realize that the torch that you brought with you is quite inadequate, and does not even illuminate the ceiling, which must be at least 5 metres high.',
			'On the left side of the room, there is a large door decorated with gold, silver, and gems.',
			'The far wall in front of you is not visible through the darkness.',
			'To the right you can see a second door made of roughly hewn wood.',
			'You decide to send Megablockless (by far the fastest runner) to explore the far end of the room.',
			'When he returns, he says that there is a third door on the far wall that has (indecipherable) ancient writing on it, and a fourth small door on the right-hand wall.',
			'Your team looks to you to decide which door to try first.',
			'Do you go through the door on the LEFT, the door on the RIGHT, the door with ancient WRITING, or the SMALL door?')
	elif previous_scene == 'entrance hall':
		print(
			'\tWhat you entered was not any of the options.',
			'Type just one of the capitalized words above (then hit enter).')
	else:
		print(
			'\tYou come back into the Entrance Hall.',
			'You now have the same options as before.',
			'You may try the door on the LEFT, the door on the RIGHT, the door with ancient WRITING, or the SMALL door.')
	
	decision = input('==> ').lower()
	if decision == 'left':
		orc_hall('entrance hall')
	elif decision == 'right':
		empty_room('entrance hall')
	elif decision == 'writing':
		boss_room('entrance hall')
	elif decision == 'small':
		closet('entrance hall')
	else:
		entrance_hall('entrance hall')
def orc_hall (previous_scene):
	print(
		'\tYou burst through the well-decorated door, not sure what to expect.',
		'Immediately, about twenty orcs rush out of the darkness and attack you!',
		'Your team is taken completely off-guard, and the orcs have little trouble overcoming you.',
		'They promptly put a bag over your head, tie your hands behind your back, and drag you deeper into the room.',
		'You dropped your torch at some point in the ambush, leaving you with nothing to do but hope that the orcs don\'t kill you right away.', end = '')
	if 'torch' in inventory:
		inventory.remove('torch')
	dungeon('orc hall')

def boss_room (previous_scene):
	if previous_scene == 'boss room':
		print(
			'\tWhat you entered was not any of the options.',
			'Type just one of the capitalized words above (then hit enter).')
	else:
		print(
			'\tYou try the door, and it surprisingly opens freely.',
			'The room extends about ten metres before the floor turns into a pool of boiling lava, which lights the room.',
			'There appears to be more solid ground on the other side of the lava, but you cannot tell how far it extends.',
			'(It may just be an island.)',
			'There are no ledges along the edge of the pool, making it impossible to cross.\n',
			'\tSuddenly, a massive bird-like creature flies out of the darkness, talons bared and ready to attack.',
			'There is no time to strategize.',
			'Do you FLEE from the massive bird back through the door, or do you ATTACK it and order your companions to do the same?')
	
	decision = input('==> ').lower()
	if decision == 'flee':
		print(
			'\t"Retreat!" you yell.',
			'You and your companions run back through the door.',
			'The DLF is the last one through, and closes the door behind him just in time.')
		# return to previous scene
		if previous_scene == 'entrance hall':
			entrance_hall('boss room')
		else:
			dungeon('boss room')
	   
	elif decision == 'attack':
		if 'palantri' in inventory:
			print(
				'\t"Attack!" you call.',
				'Megablockless immediately fires two arrows at the beast, but they do not hinder it in the least.',
				'You feel something moving inside your bag.',
				'You see the Palantri rise up out of your bag and begin to emit a bright light.',
				'Suddenly, the huge bird reels backward.',
				'It flies away as fast as it can.',
				'After it is out of sight, the Palantri starts to descend.',
				'You gently catch it.',
				'You and your team breath a sigh of relief.',
				'There is still no way to traverse the lava, however, so you are forced to return to the previous room.')
			# return to previous scene
			if previous_scene == 'entrance hall':
				entrance_hall('boss room')
			else:
				dungeon('boss room')
		else:
			print(
				'\t"Attack!" you call.',
				'Megablockless immediately fires two arrows at the beast, but they do not hinder it in the least.',
				'It swoops down, grabs all of you except the DLF, and flies out over the lava with you in its talons.\n',
				'\tI won\'t get into any of the gruesome details, but basically you all die.\n',
				'\tThe DLF, after grieving your deaths, would eventually leave the mines (through the path that your team took) and live out the rest of his days in the surrounding forest.\n',
				'\tThe end.')
			return
	else:
		boss_room('boss room')

def closet (previous_scene):
	print(
		'\tAll of the other doors seem a little scary to you, so you decide to try the small door.',
		'After walking in near silence for about two minutes, your team reaches the door.',
		'It has an obvious, convenient handle, and opens easily.',
		'Inside, you see that it is a closet with a few cleaning supplies.',
		'Your friends begin to laugh at you.')
	if 'palantri' not in inventory and randint(0, 9) == 9:
		print(
			'You, however, undeterred by their cackling, being to search through it.',
			'On one of the shelves, behind several rolls of quarter-ply toilet paper (dwarves have never cared much for comfort), you see something reflect the dim torch light.',
			'Reaching in, you pull out a smooth, black ball with a radius of approximately three centimetres.',
			'It is probably a gemstone.',
			'Having no idea what its value might be, you decide to put it in your bag.',
			'Just as you go to do so, however, Stanli suddenly stops laughing and says, "Wait!"',
			'You freeze, holding the ball just above the opening of your bag.',
			'"I think I know what that is," Stanli says, "and if I\'m right..."',
			'You allow him to examine it.',
			'After a minute he says, "You have found a Palantri.',
			'This ball has certain magical properties, but it is impossible to determine what they might be just by looking at it."',
			'Do you TAKE the Palantri with you, or LEAVE it, lest its magical powers work against you?')
		decision = input('==> ').lower()
		if decision == 'take':
			inventory.append('palantri')
			entrance_hall('closet')
		elif decision != 'leave':
			print(
				'\tWhat you entered was not any of the options.',
				'You drop the Palantri on the floor, and it smashes into pieces.',
				'Smooth move.',
				'A strange mist begins to rise up out of the broken pieces.',
				'Then it starts coming faster.',
				'You reflexively back away, but the mist accelerates outward and quickly surrounds the group.',
				'Everyone begins coughing as they breathe in the mist.',
				'After only a few seconds, you see that Biblio has passed out and fallen on the floor.',
				'Within a minute, everyone has passed out.',
				'You never wake up.\n',
				'\tThe end.')
			return
	else:
		entrance_hall('closet')

def empty_room (previous_scene):
	if previous_scene == 'empty_room':
		print(
			'\tWhat you entered was not any of the options.',
			'Type just one of the capitalized words above (then hit enter).')
	# must be coming from entrance hall
	else:
		print(
			'\t"Let\'s try the door on the right," you say.',
			'Stanli helps you open the large door.',
			'You look in carefully, to find... um... nothing.',
			'The room is simple, rectangular, empty, and appears to be a dead-end.',
			'You can either EXAMINE the room to make sure that there really is not anything important in here, or you can go BACK to the first room and choose a different door.')
	
	decision = input('==> ').lower()
	if decision == 'examine':
		print(
			'\tYou tell your friends that it is probably best to examine the room before moving on.',
			'Some of them disagree, especially Stanli.',
			'"But it\'s empty! I can see that! We can\'t afford to waste time,\" he replies.',
			'You are insistent, however, and your team begins to search.\n'
			'\tAfter about five minutes, Biblio cries, "I think I\'ve found something!"',
			'You walk over to see a circular part of the wall, a few centimetres across, that has obviously been removed and replaced.',
			'It is impossible to get a grip on it, because the gap between it and the rest of the wall is only a millimetre or so.',
			'Stanli does not know what it might be, but still wants to forget about it and move on.',
			'Do you listen to him and go BACK to the main hall, or do you act stubbornly and try to MOVE it before giving up?')
		decision = input('==> ').lower()
		if decision == 'move':
			print(
				'\tSince it is impossible to pull on it, you try pushing it.',
				'It doesn\'t budge.',
				'You ask Megablockless to help you.',
				'Together you are able to push it about a centimetre into the wall.',
				'"Wow," Stanli says sarcastically, "that was impressive. I told you all that—"',
				'He is interrupted by his own surprise, as he realizes that one of the walls of the room has dissappeared.',
				'The East wall of the room simply vanished.',
				'You start to walk over slowly, dumbfounded.',
				'Suddenly, you are stopped by the loud noise of rock smashing deep in the mines below you.',
				'After pausing for a few seconds, you continue to walk towards where the wall once stood.',
				'As you approach it, you see that there is a gap in the floor, as wide as the room and approximately three decimetres long.',
				'You realize that the wall was a loose slab of rock that has now fallen out of its place.',
				'It must have been the wall itself that you heard break deep in the caverns below.',
				'Everyone is still too shocked to speak.',
				'You gesture towards the others to follow you.',
				'They begin to obey, and Megablockless picks up the DLF, as he is the only one who is unable to step across the gap.',
				'The passageway that has appeared becomes smaller as it goes on, forcing everyone except for the DLF to crawl.\n',
				'\tA few minutes pass, and everyone continues to shuffle along behind you, not saying a word.',
				'You see an end to the passageway a few metres ahead.',
				'When you reach it, you are able only to push it slightly before it gives way, and a flood of light bursts in.',
				'You see blue—the sky!',
				'You have made it out! You give a hollar of joy as you crawl out and stand up.',
				'The rest of your team gathers behind you, squinting in the bright sunlight.',
				'Stanli looks sheepish, but does not say anything.\n'
				'\tCongradulations! You won!.')
		elif decision == 'back':
			entrance_hall('empty_room')
		else:
			print(
				'\tWhat you entered was not any of the options.',
				'You stumble over your words, and Stanli makes the call for you.',
				'"We\'re trying a different way."')
			entrance_hall('empty_room')
	elif decision == 'back':
		entrance_hall('empty_room')
	else:
		empty_room('empty_room')

def dungeon (previous_scene):
	if previous_scene == 'dungeon':
		print(
			'\tWhat you entered was not any of the options.',
			'You trip over one of the head bags in the darkness and hit your head on the wall.',
			'You still have the same options: FIRST or SECOND?')
	elif previous_scene == 'orc hall':
		print(
			# the omission of the \t below is intentional
			'They continue to take you through several passageways (it\'s impossible to know just how many) and eventually stop, throwing you on the ground.',
			'You hear your compatriots come in, their voices muffled by the bags on their heads.',
			'You hear the orcs leave, and begin to work your way out of the rope around your wrists.',
			'This does not take long, as orcs are terrible at tying knots.',
			'Even after you take the bag off of your head you cannot see anything, as there are no lights in the room.',
			'After you free yourself (and help your companions to do the same), you talk to them and decide to feel your way around the room in the darkness, looking for any doors or other escape routes.',
			'You are quite certain of where the door was that you were brought in through, and you are able to find it without much searching.',
			'Biblio also finds a second door in one of the other walls of the room, though there is no way of knowing what might be on the other side.',
			'You know that both doors are probably locked, but orcs occasionally forget to think of important things like that, so you might as well try them.',
			'Which door do you try first: the FIRST door that you came in through, or the SECOND door that Biblio found?')
	# must be coming from the boss room
	else:
		print(
			'\tWell, that was a bad call.',
			'Now you have no choice but to try to get out through the door that the orcs brought you in by.',
			'Since (out of those on your team that has hands) he is the best at sneaking, Biblio is elected to try to open the door discretely.',
			'It opens a crack without any hindrance, and he whispers to the rest of you that there are two orcs guarding the entrance.',
			'Your team groups around the door and prepares to burst out.',
			'You lead the charge, but resist the urge to yell "Charge!", as this might alert other orcs in the vicinity of your jailbreak.',
			'When you burst out you find that there were actually many more orcs that Biblio was not able to see through the crack.',
			'They quickly overtake you and you are all soon unceremoniously executed, except for the DLF.',
			'Because they see him as harmless, they set him free outside and he lives out the rest of his days in the surrounding forest.')
		return
	
	decision = input('==> ').lower()
	if decision == 'first':
		print(
			'\tSince (out of those on your team that has hands) he is the best at sneaking, Biblio is elected to try to open the door discretely.',
			'It opens a crack without any hindrance, and he whispers to the rest of you that there are two orcs guarding the entrance.',
			'Your team groups around the door and prepares to burst out.',
			'You lead the charge, but resist the urge to yell "Charge!", as this might alert other orcs in the vicinity of your jailbreak.',
			'The orcs seem like they must have been daydreaming, and their reflexes could be compared to those of a dead cat.',
			'You immediately overtake them.',
			'You then turn your attention to your surroundings.',
			'There are two chests against the walls on either side of the room.',
			'There are two doors besides the one that you came in through.',
			'And—wait—is that sunlight?',
			'Yes, the other door has a window with light streaming through it!',
			'Do you immediately RUN towards the door screaming (because it feels like years since you have seen the sun), or do you calmly INFORM your comrades and let them talk?')
			
		decision = input('==> ').lower()
		if decision == 'run':
			print(
				'\t"Freedom!" you yell, as you sprint towards the door.',
				'Your team follows you quickly, and Stanli, the last one to make it out, closes the door behind him.',
				'You breath deeply and take a moment to appreciate the view.',
				'You then remember the chests in the room.',
				'Is it possible that there was treasure in them?',
				'Stanli comfirms your suspicision.',
				'You try the door.',
				'Nope.',
				'It\'s locked.',
				'The window in the door is not large enough for any of you to fit through.',
				'So much for that.\n',
				'\tCongradulations, you won (though not in the best way).')
		elif decision == 'inform':
			print(
				'\t"We can get out!" you say in a reasonable tone, pointing.',
				'A few of your comrades start to walk towards the door.',
				'"Wait," Biblio says, "what do you think is in these chests?"',
				'"Oh, this is wonderful!" says Stanli. "These are old dwarvish treasure chests—"',
				'"Quiet! Do you hear that?" Megablockless interupts.',
				'You hear heavy footsteps approaching.',
				'"We have to get out of here."',
				'All of you rush towards the door.',
				'Stanli, thinking quickly—which he does not do very often—grabs the chest, heaves it up onto his shoulder, and follows behind the group.',
				'Everyone gathers outside, and you quickly close the door behind Stanli.',
				'You made it out, and everyone gets treasure!\n',
				'\tCongradulations, you won!')
	elif decision == 'second':
		boss_room('dungeon')
	else:
		dungeon('dungeon')

if __name__ == '__main__':
	main()
