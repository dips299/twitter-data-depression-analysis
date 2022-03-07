# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:07:15 2020

@author: deepa
"""

depr = ['point', 'encephalon', 'slimy', 'vexation', 'misconstrue', 'mistreat', 'abide', 'offend', 'payoff', 'fighting', 'drop_dead', 'pain_sensation', 'discomfited', 'ugly', 'ire', 'therapeutic', 'wound', 'gloominess', 'prize', 'John_L._H._Down', 'stripling', 'takings', 'putting_to_death', 'panicky', 'come_out', 'wild_blue_yonder', 'oppose', 'effect', 'blasphemous', 'involve', 'bear_upon', 'misunderstanding', 'bother', 'frustrated', 'go_through', 'juicy', 'disarray', 'release', 'support', 'unsure', 'sustain', 'tactile_sensation', 'subject', 'egress', 'confusedness', 'sorrowfulness', 'unsettled', 'lone', 'wit', 'ache', 'bring_around', 'overcome', 'wear_down', 'mistaking', 'stamp_out', 'exhausted', 'consume', 'anguish', 'unfitness', 'daunt', 'repute', 'perish', 'scared', 'scrap', 'suffer', 'excitable', 'upset', 'meet', 'tetchy', 'trouble', 'write_out', 'gentle', 'barbarous', 'finger', 'sorrow', 'brainiac', 'imprint', 'worry', 'go_forth', 'stain', 'kill', 'depressed', 'death', 'touch_sensation', 'neutrality', 'tolerate', 'ill-treatment', 'self-annihilation', 'anger', 'scratchy', 'abnormal', 'publish', 'inactivity', 'frightened', 'publication', 'horrify', 'dying', 'push_down', 'learning_ability', 'mastered', 'cut', 'injury', 'contend', 'lonely', 'mentality', 'brutal', 'alienation', 'pop', 'unhappiness', 'unsealed', 'cranky', 'shin', 'helpless', 'misconceive', 'tire', 'push', 'unequaled', 'combat', 'pour_down', 'spirit', 'cast_down', 'venerate', 'despicable', 'stick_out', 'crusade', 'inability', 'stomach', 'antidepressant', 'testy', 'misuse', 'croak', 'issue', 'perturb', 'uneasy', 'annoyance', 'outwear', 'melancholia', 'unrealized', 'bluish', 'consequence', 'insecure', 'dose', 'ill-use', 'fine-tune', 'expiry', 'ail', 'nettlesome', 'reverence', 'downwardly', 'conflict', 'drink_down', 'do_drugs', 'dog-tired', 'yield', 'skin', 'terrorise', 'agitate', 'unquiet', 'competitiveness', 'fail', 'discombobulation', 'only', 'disinterest', 'bipolar', 'cut_down', 'supply', 'inertia', 'brokenheartedness', 'campaign', 'misunderstand', 'shinny', 'contumely', 'racy', 'care', 'wipe_out', 'fagged', 'stigma', 'peckish', 'flavor', 'look_upon', 'alone', 'tone', 'unparalleled', 'genial', 'die', 'warning_device', 'isolation', 'nuisance', 'revere', 'pull_down', 'antidepressant_drug', 'wretched', 'pock', 'spent', 'Down', 'drug', 'warning_signal', 'issuing', 'cruel', 'dreary', 'clinical', 'fight_back', 'injure', 'snuff_it', 'vicious', 'uncomfortable', 'sense', 'vote_down', 'savage', 'see_red', 'downcast', 'desperation', 'be_amiss', 'choler', 'buy_the_farm', 'maltreat', 'gamy', 'belt_down', 'fatigued', 'impress', 'Great_Depression', 'petulant', 'look_on', 'pain_in_the_ass', 'choke', 'insult', 'break_down', 'alarm', 'grade', 'emergence', 'legal_separation', 'intuitive_feeling', 'trauma', 'respect', 'sadness', 'digest', 'disorder', 'take', 'refine', 'pain_in_the_neck', 'curative', 'diagnosing', 'tactual_sensation', 'bruise', "cash_in_one's_chips", 'lower', 'demise', 'maltreatment', 'blue', 'blueness', 'appal', 'aristocratical', 'disease', 'pit', 'blueing', 'admiration', 'worldly', 'dissemble', 'weakened', 'self-destruction', 'occupy', 'heartache', 'coitus_interruptus', 'disaffection', 'mental', 'techy', 'unique', 'struggle', 'experience', 'offspring', 'lugubriousness', 'pretend', 'shout', 'mental_confusion', 'unequalled', 'drug_withdrawal', 'feel', 'touch_on', 'teenager', 'fatigue', 'debilitate', 'lose', 'dispirit', 'distrait', 'devour', 'worn-out', 'panic', 'pass', 'discrimination', 'secernment', 'head', 'clinical_depression', 'degree', 'heartbreak', 'withdrawal', 'down', 'alarm_clock', 'mark', 'clapperclaw', 'dismay', 'painfulness', 'down_in_the_mouth', 'demoralise', 'brainpower', 'belief', 'uncertain', 'engagement', 'slump', 'foiled', 'scathe', 'grim', 'vex', 'affright', 'unhinge', 'suffering', 'felo-de-se', 'knock_down', 'weary', 'cark', 'bluing', 'solitary', 'solo', 'polish', 'natural_depression', 'unnatural', 'pile', 'frighten_off', 'detriment', 'appall', 'get', 'Death', 'washed-out', 'separation', 'frighten_away', 'blue_devil', 'government_issue', 'brain', 'tire_out', 'bear', 'diagnosis', 'become_flat', 'favouritism', 'risque', 'feelings', 'painful_sensation', 'favoritism', 'patrician', 'worn_out', 'unrealised', 'find', 'solely', 'regard', 'downwards', 'impression', 'bored', 'Amytal', 'scare', 'terrify', 'scare_off', 'distress', 'terrorize', 'amobarbital_sodium', 'harm', 'give_out', 'put_out', 'puritanical', 'changeable', 'vile', 'defend', 'pop_off', 'interval', 'wear_out', 'grief', 'unfulfilled', 'touch', 'have', 'secession', 'misinterpretation', 'wounded', 'pervert', 'blue_air', 'confusion', 'disorderliness', 'number', 'clamber', 'die_out', 'feeling', 'put_up', 'exclusively', 'anxiousness', 'nous', 'value', 'mind', 'inactiveness', 'fell', 'concern', 'way_out', 'end', 'aristocratic', 'scare_away', 'pulling_out', 'conk_out', 'pain', 'issuance', 'interest', 'think_of', 'scar', 'sputter', 'wrath', 'pettish', 'look', 'disappointed', 'dark', 'down_feather', 'despair', 'estrangement', 'mental_capacity', 'irritable', 'disconsolate', 'vote_out', 'cure', 'get_down', 'outcome', 'Depression', 'kick_the_bucket', 'pass_away', 'affect', 'low', 'played_out', 'vilification', 'muddiness', 'bolt_down', 'veneration', 'stage', 'gamey', 'fractious', 'alarum', 'closing_off', 'esteem', 'thwarted', 'onanism', 'naughty', 'result', 'military_issue', 'fright', 'battle', 'dash', 'torment', 'blase', 'pall', 'scramble', 'fearfulness', 'lost', 'wear', 'smart', 'topic', 'bear_on', 'gloomy', 'depression', 'land', 'upshot', 'sham', 'abuse', 'come_forth', 'blue_angel', 'adolescent', 'spicy', 'ira', 'awe', 'killing', 'defeated', 'dismal', 'mistake', 'fight_down', 'low-spirited', 'psyche', 'drab', 'inaction', 'decease', 'dispirited', 'blue-blooded', 'blue_sky', 'notion', 'anxiety', 'mix-up', 'move', 'demoralize', 'blackguard', 'downhearted', 'fag', 'mastermind', 'misapprehension', 'worthless', 'brook', 'blueish', 'flavour', 'frighten', 'go', 'dingy', 'outlet', 'Einstein', 'alarm_system', 'regard_as', 'endure', 'panic-stricken', 'misinterpret', 'revilement', 'angriness', 'event', 'roughshod', 'queasy', 'academic_degree', 'jade', 'make_out', 'impact', 'entirely', 'fear', 'feign', 'strike', 'torture', 'break', 'alert', 'bring_out', 'stand', 'ill-usage', 'distract', 'progeny', 'headache', 'prise', 'drear', 'infliction', 'withdrawal_method', 'brand', 'consternation', 'deflect', 'step', 'detachment', 'emerge', 'take_to_be', 'give_way', 'give-up_the_ghost', 'panicked', 'expire', 'destruction', 'anxious', 'toss_off', 'smell', 'press', 'remedy', 'economic_crisis', 'breakup', 'sorry', 'distracted', 'peevish', 'teen', 'down_pat', 'wear_upon', 'terrified', 'unaccompanied', 'defeat', 'obliterate', 'shoot_down', 'hurting', 'disquiet', 'go_bad', 'incapacitated', 'spite', 'conk', 'fag_out', 'incertain', 'nervous', 'depressive_disorder', 'puritanic', 'genius', 'hurt', 'deject', 'fight', 'matter', 'palpate', 'level', 'backdown', 'ill-treat', 'downward', 'unsafe', 'panic-struck', 'suicide', 'botheration', 'misapprehend', 'depress', 'dread', 'get_the_better_of', 'debilitating', 'exit', 'damage', 'proceeds', 'unworthy', 'arcdegree', 'opinion', 'return', 'heal', 'climb-down', 'enfeeble', 'dice', 'last', 'press_down', 'drain', 'terror', 'profane', 'hopeless','Fatigued', 'Detriment', 'Cure', 'Down', 'Disinterest', 'Inactivity', 'Defeated', 'Isolation', 'Hurt', 'Degree', 'Antidepressant', 'Cruel', 'Death', 'Depressed', 'Disorder', 'TiredTragic', 'Debilitating', 'Worry', 'Distracted', 'Anguish', 'Abnormal', 'Depression', 'Alarm', 'Melancholia', 'Clinical', 'Mental health', 'Esteem', 'Issues', 'Brain', 'Withdrawal', ' Aid', 'Disease', 'Kill', 'Blue', 'Affect', 'Uncertain', 'Substance abuse', 'Mental', 'Irritable', 'Drugs', 'Abuse', 'Adolescents', 'Terrified', 'Uncomfortable', 'Unfulfilled', 'Stigma', 'Bipolar', 'Misunderstanding', 'Grief', 'Panic', 'Sadness', 'Discrimination', 'Fear', 'Feelings', 'Suffer', 'Blase', 'Insecure', 'Anxiety', 'Separation', 'Diagnosis', 'Die', 'Despair', 'Hopeless', 'Suicide', 'Inability', 'Pain', 'Alone', 'Anxious', 'Worthless', 'Struggle', 'Fight', 'Anger', 'Scared', 'Helpless', 'Alienation', 'Confusion']
print(len(depr))

with open('C:/Users/deepa/Documents/Sem 6/Data Mining and Data Warehousing/Depression_Analysis_of_Twitter_Data/Depression-Words.txt', 'w') as filehandle:
    for listitem in depr:
        filehandle.write('%s\n' % listitem)