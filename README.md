# aerick-phrasing

A phrasing system for Plover.

Heavily inspired by [JadeGG's own phrasing system](https://github.com/Jade-GG/plover_phrasing). The majority of starters, middles, and ending words are from there.

This system allows you to write common phrases in one stroke, such as "I don't really even care about".

However, the actual python dictionary has practically been rewritten to accommodate for features that the original does not have.

## Changes With this System

### Grammatically incorrect phrases are less frequent

With the original system, there is space taken up by grammatically incorrect phrases. For example, "doesn't" and "don't" are separate middle words, and so stroking `KPWHOEPT` would result in "he don't want to".

With this system, the middle word represented by `OE` changes depending on the pronoun. So while `KPWHOEPT` would output "it doesn't want to", `SWROEPT` would output "I don't want to" despite using the same vowel keys.

When using no starter word, "doesn't" will be used. This is for phrases such as "Alice doesn't really need to" (`A*LS/STKPWHROEUPBTD`).

The ending "has"/"have" (`-T`) works the same.

### Plurals are automatic

With the original system, to write a phrase such as "she really cares about", one would have to stroke it as `SKWHRARBGTS` with the S pluralising the word "care". However, with this system, this is taken care of and stroking `SKWHRARBGT` is sufficient. On the other hand, using the same ending and middle word but with the pronoun "I" will not pluralise. `SWRARBGT` → "I really care about".

Currently a `❌` in the entries of the endings dictionary will prevent it from automatically being pluralised.

### The number key can be used in strokes

Currently, I'm using it for more middle words, specifically it will output the positive forms of the "non-number keyed" medials. The dictionary recognises the `AOEU` keys as `XYQN` to differentiate between when the number key has been pressed for the vowels (this is only important if you intend to change the medials).

### Final medial with the `-F` key

I've assigned this to be the word "even", so that phrases such as "I didn't even know that" are now possible. The placement of this word is always on the end of the middle words.

All of these changes have added quite a bit of space for new phrases. Currently, I am not entirely certain what I'll be using all this new space for. The dictionary may change with my usage over time. At the moment I'm thinking that the "number keyed" vowels may not be optimal ("should", "could" and "would" are all potential candidates).

## Overview of the system

**Starting words**
- `SWR`: `I`
- `KPWR`: `you`
- `KWHR`: `he`
- `SKWHR`: `she`
- `TWH`: `they`
- `TWR`: `we`
- `KPWH`: `it`
- `STKPWHR`: ` `  (nothing)
- `STWR`: ` `  (nothing, and don't plurarlise)

**Middle words**
- `OE`: `don't` or `doesn't` depending on pronoun
- `AU`: `didn't`
- `E`: `just don't` or `just doesn't` depending on pronoun
- `O`: `can't`
- `A` or `U`: `really`
- `AOEU`: ` `  (nothing yet)

With number key:
- `OE`: `do` or `does` depending on pronoun
- `AU`: `did`
- `E`: `just`
- `O`: `can`
- `A` or `U`: `really`
- `AOEU`: ` `  (nothing yet)

> NOTE: Using the A and U keys will append/prepend "really" to each middle word just like with Jade's original system. In the case of "didn't" or "did" (where AU is already taken), the O and E keys will act as the "really".

**Ending words**
- `PB`: `know`
- `PBT`: `know that`
- `*PBT`: `know the`
- `RPG`: `knew`
- `RPGT`: `knew that`
- `*RPGT`: `knew the`
- `P`: `want`
- `PT`: `want to`
- `PTD`: `wanted to`
- `*PT`: `want the`
- `*PTD`: `wanted the`
- `*P`: `wanna`
- `RPL`: `remember`
- `RPLT`: `remember that`
- `RPLTD`: `remembered that`
- `*RPLT`: `remember the`
- `*RPLTD`: `remembered the`
- `BGD`: `could`
- `*BGD`: `couldn't`
- `BL`: `believe`
- `BLT`: `believe that`
- `*BLT`: `believe the`
- `BLD`: `believed`
- `BLTD`: `believed that`
- `*BLTD`: `believed the`
- `D`: `had`
- `TD": "had to`
- `*TD": "had the`
- `T`: `have`
- `TS`: `have to`
- `*TS`: `have the`
- `S`: `was`
- `PLTS`: `must`
- `L`: `will`
- `LD`: `would`
- `PBG`: `think`
- `PBGT`: `think that`
- `*PBGT`: `think the`
- `PBLG`: `thought`
- `PBLGT`: `thought that`
- `*PBLGT`: `thought the`
- `PL`: `may`
- `PLT`: `might`
- `RB`: `shall`
- `RBD`: `should`
- `RL`: `recall`
- `RLD`: `recalled`
- `RLZ`: `realise`
- `RLZD`: `realised`
- `RP`: `were`
- `RPBT`: `were not`
- `*RPBT`: `weren't`
- `RPT`: `were the`
- `*RPT`: `were the`
- `RPBD`: `understand`
- `*RPBD`: `understood`
- `PBD`: `need`
- `PBTD`: `need to`
- `*PBTD`: `need the`
- `PBDZ`: `needed`
- `PBTSDZ`: `needed to`
- `*PBTSDZ`: `needed the`
- `LS`: `feel`
- `LGS`: `feel like`
- `LTS`: `felt`
- `LGTS`: `felt like`
- `PBL`: `mean`
- `PBLT`: `meant`
- `BLG`: `like`
- `BLGT`: `like to`
- `*BLGT`: `like the`
- `BLGD`: `liked`
- `BLGTD`: `liked to`
- `*BLGTD`: `liked the`
- `LG`: `love`
- `LGT`: `love to`
- `*LGT`: `love the`
- `LGD`: `loved`
- `LGTD`: `loved to`
- `*LGTD`: `loved the`
- `RBG`: `care`
- `RBGD`: `cared`
- `RBGT`: `care about`
- `GT`: `get`
- `*GT`: `got`
- `PLD`: `mind`
- `RG`: `forget`
- `RGT`: `forgot`
- `RBS`: `wish`
- `"RBTS`: `wish to`
- `*RBTS`: `wish the`
- `RBSZ`: `wished`
- `RBTSDZ`: `wished to`
- `*RBTSDZ`: `wished the`
- `PGT`: `expect`
- `PGTD`: `expected`
- `RPBG`: `ever`
- `B`: `be`
- `BT`: `be the`
- `*BT`: `be the`
- `BS`: `said`
- `BTS`: `said to`
- `*BTS`: `said the`
- `BZ`: `say`
- `BTZ`: `say to`
- `*BTZ`: `say the`
- `PLG`: `imagine`
- `PLGT`: `imagine that`
- `*PLGT`: `imagine the`
- `PLGD`: `imagined`
- `PLGTD`: `imagined that`
- `*PLGTD`: `imagined the`

These ending words can also be combined with other things:

**alternate starting words (with no middle words)**
- `WHA[E/U/EU]`: `what he/you/I`
- `SKPW[E/U/EU]`: `do(es)n't he/you/I`
- `STKO[E/U/EU]`: `do(es) he/you/I`
- `STKPWO[E/U/EU]`: `did he/you/I`
- `STHA[E/U/EU]`: `that he/you/I`
- `STPA[E/U/EU]`: `if he/you/I`
- `SWH[E/U/EU]`: `when he/you/I`
