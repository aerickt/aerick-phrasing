import re

LONGEST_KEY = 1

starters = {
                "SWR":"I",
                "KPWR":"you",
                "KWHR":"he",
                "SKWHR":"she",
                "TWH":"they",
                "TWR":"we",
                "KPWH":"it",
                "STKPWHR":"",
                "STWR": ""
}

are = {
            "SWR":"am",
            "KPWR":"are",
            "KWHR":"is",
            "SKWHR":"is",
            "TWH":"are",
            "TWR":"are",
            "KPWH":"is",
            "STKPWHR":"are",
            "WHAE":"is",
            "WHAU":"are",
            "WHAEU":"am",

            "SKPWE":"is",
            "SKPWU":"are",
            "SKPWEU":"am",

            "STKOE":"is",
            "STKOU":"are",
            "STKOEU":"am",

            "STKPWOE":"is",
            "STKPWOU":"are",
            "STKPWOEU":"am",

            "STHAE":"is",
            "STHAU":"are",
            "STHAEU":"am",

            "STPAE":"is",
            "STPAU":"are",
            "STPAEU":"am",

            "SWHE":"is",
            "SWHU":"are",
            "SWHEU":"am"
}

middles = {
            "A":"really",
            "U":"really",
            "O":"can't",
            "OE":"don't",
            "E":"just don't",
            "AU":"didn't",
            "AEU":"didn't really",
            "AOU":"really didn't",
            "X": "really",
            "N": "really",
            "Y": "can",
            "YQ": "do",
            "Q": "just",
            "XYN": "really did",
            "XQN": "did really",
            "XN": "did",
            "F": "even",
            "":""
}

what = {
            "WHAE":"what he",
            "WHAU":"what you",
            "WHAEU":"what I",

            "SKPWE":"doesn't he",
            "SKPWU":"don't you",
            "SKPWEU":"don't I",

            "STKOE":"does he",
            "STKOU":"do you",
            "STKOEU":"do I",

            "STKPWOE":"did he",
            "STKPWOU":"did you",
            "STKPWOEU":"did I",

            "STHAE":"that he",
            "STHAU":"that you",
            "STHAEU":"that I",

            "STPAE":"if he",
            "STPAU":"if you",
            "STPAEU":"if I",

            "SWHE":"when he",
            "SWHU":"when you",
            "SWHEU":"when I"
}

ends = {
            "PB":"know",
            "PBT":"know that",
            "*PBT":"know the",
            "RPG":"knew❌",
            "RPGT":"knew that❌",
            "*RPGT":"knew the❌",
            "P":"want",
            "PT":"want to",
            "PTD":"wanted to❌",
            "*PT":"want the",
            "*PTD":"wanted the❌",
            "*P":"wanna❌",
            "RPL":"remember",
            "RPLT":"remember that",
            "RPLTD":"remembered that❌",
            "*RPLT":"remember the",
            "*RPLTD":"remembered the❌",
            "BGD":"could❌",
            "*BGD":"couldn't❌",
            "BL":"believe",
            "BLT":"believe that",
            "*BLT":"believe the",
            "BLD":"believed❌",
            "BLTD":"believed that❌",
            "*BLTD":"believed the❌",
            "D":"had❌",
            "TD": "had to❌",
            "*TD": "had the❌",
            "T":"have❌",
            "TS":"have to❌",
            "*TS":"have the❌",
            "S":"was❌",
            "PLTS":"must❌",
            "L":"will❌",
            "LD":"would❌",
            "PBG":"think",
            "PBGT":"think that",
            "*PBGT":"think the",
            "PBLG":"thought",
            "PBLGT":"thought that❌",
            "*PBLGT":"thought the❌",
            "PL":"may❌",
            "PLT":"might❌",
            "RB":"shall❌",
            "RBD":"should❌",
            "RL":"recall",
            "RLD":"recalled❌",
            "RLZ":"realise",
            "RLZD":"realised❌",
            "RP":"were❌",
            "RPBT":"were not❌",
            "*RPBT":"weren't❌",
            "RPT":"were the❌",
            "*RPT":"were the❌",
            "RPBD":"understand",
            "*RPBD":"understood❌",
            "PBD":"need",
            "PBTD":"need to",
            "*PBTD":"need the",
            "PBDZ":"needed❌",
            "PBTSDZ":"needed to❌",
            "*PBTSDZ":"needed the❌",
            "LS":"feel",
            "LGS":"feel like",
            "LTS":"felt❌",
            "LGTS":"felt like❌",
            "PBL":"mean",
            "PBLT":"meant❌",
            "BLG":"like",
            "BLGT":"like to",
            "*BLGT":"like the",
            "BLGD":"liked❌",
            "BLGTD":"liked to❌",
            "*BLGTD":"liked the❌",
            "LG":"love",
            "LGT":"love to",
            "*LGT":"love the",
            "LGD":"loved❌",
            "LGTD":"loved to❌",
            "*LGTD":"loved the❌",
            "RBG":"care",
            "RBGD":"cared❌",
            "RBGT":"care about",
            "GT":"get",
            "*GT":"got❌",
            "PLD":"mind❌",
            "RG":"forget",
            "RGT":"forgot❌",
            "RBS":"wish",
            "RBTS":"wish to",
            "*RBTS":"wish the",
            "RBSZ":"wished❌",
            "RBTSDZ":"wished to❌",
            "*RBTSDZ":"wished the❌",
            "PGT":"expect",
            "PGTD":"expected❌",
            "RPBG":"ever❌",
            "B":"be❌",
            "BT":"be the",
            "*BT":"be the",
            "BS":"said❌",
            "BTS":"said to❌",
            "*BTS":"said the❌",
            "BZ":"say",
            "BTZ":"say to",
            "*BTZ":"say the",
            "PLG":"imagine",
            "PLGT":"imagine that",
            "*PLGT":"imagine the",
            "PLGD":"imagined❌",
            "PLGTD":"imagined that❌",
            "*PLGTD":"imagined the",
            "":""
}

def lookup(key):
    assert len(key) <= LONGEST_KEY

    if key[0] == "WHAEUL": return "whale"

    dict = {
        '1': 'S',
        '2': 'T',
        '3': 'P',
        '4': 'H',
        '5': 'X',
        '6': 'F',
        '7': 'P',
        '8': 'L',
        '9': 'T',
        '0': 'Y',
        'E': 'Q',
        'U': 'N'
    }

    stroke = key[0]

    if '#' in stroke or any(char.isdigit() for char in stroke):
        for (i, j) in dict.items():
            stroke = stroke.replace(i, j)

    mk = ''
    mw = ''
    ek = ''
    ew = ''

    sk = stroke

    midPtrn = ['A', 'O', 'E', 'U', 'X', 'Y', 'Q', 'N', 'F', '-', '*']

    for x in midPtrn:
        sk = sk.split(x)[0]
        if x in stroke and not x in '-*':
            mk += x

    ek = ek + stroke.replace(sk, '').replace(mk, '').replace('-', '')

    wk = sk + mk

    if sk in starters:
        sw = starters[sk]

        midList = []

        if mk != '':
            while mk != '':
                midLen = 0
                for i in middles:
                    if i in mk and len(i) > midLen:
                        midLen = len(i)
                        base = i
                midList.append(base)
                mk = mk.replace(base, '')

            for i in midList:
                mw += ' ' + middles[i]

            " ".join(mw)

    elif wk in what:
        sw = what[wk]
        sk = wk
        mw = ''
    else:
        raise KeyError

    if ek in ["R", "RT", "*RT"]:
        if ek == "R":
            ew = are[sk] + " ❌"
        elif ek == "RT":
            ew = are[sk] + " not❌"
        elif ek == "*RT":
            ew = are[sk] + "n't❌"
    else: ew = ends[ek]

    if sw in ['he', 'she', 'it', '', 'what he']:
        mw += " "
        if "do " in mw:
            mw = mw.replace("do ", "does ")
        elif "don't " in mw:
            mw = mw.replace("don't ","doesn't ")
        mw = mw[:-1]

        if 'have' in ew: ew = ew.replace('have', 'has')

        if not any(x in mw for x in ['does', 'did', 'can']) and not '❌' in ew and sk != 'STWR':
            for i in [' to', ' the', ' about', ' that', ' like']:
                lastWord = ""
                if i in ew:
                    lastWord = i
                    ew = ew.split(i)[0]
                    break
            ew += "s" + lastWord

    stm = sw + mw

    ret = stm + " " + ew.replace('❌', '')

    return " ".join(ret.split())
