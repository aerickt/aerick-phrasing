# aerick-phrasing

A phrasing system for Plover.

Heavily inspired by [JadeGG's own phrasing system](https://github.com/Jade-GG/plover_phrasing). The majority of starters, middles, and ending words are from there.

This system allows you to write common phrases in one stroke, such as "I don't really even care about".

However, the actual [python dictionary](https://pypi.org/project/plover-python-dictionary/) has practically been rewritten to accommodate for features that the original does not have.

## Changes With this System

### "doesn't" and "don't" use the same keys

With the original system, `E` is used for `doesn't` while `OE` is used for `don't`. This means that there is space taken up by grammatically incorrect phrases such as `he don't want to` (`KWHROEPT`).

With this system, the middle word represented by `OE` changes depending on the pronoun. So while `KPWHOEPT` would output `it doesn't want to`, `SWROEPT` would result in `I don't want to` despite using the same vowel keys.

### Plurals are automatic

With the original system, to write a phrase such as `she really cares about`, one would have to stroke it as `SKWHRARBGTS` with the S pluralising the word `care`. However, with this system, this is taken care of and stroking `SKWHRARBGT` is sufficient. On the other hand, using the same ending and middle word but with the pronoun `I` will not pluralise. `SWRARBGT` → `I really care about`.

Currently a `❌` in the entries of the endings dictionary will prevent it from automatically being pluralised.

### The number key can be used in strokes

Currently, I'm using it for more middle words, specifically it will output the positive forms of the "non-number keyed" medials. The dictionary recognises the `AOEU` keys as `XYQN` to differentiate between when the number key has been pressed for the vowels (this is only important if you intend to change the medials).

### Final medial with the `-F` key

I've assigned this to be the word `even`, so that phrases such as `I didn't even know that` are now possible. The placement of this word is always on the end of the middle words.

All of these changes have added quite a bit of space for new phrases. Currently, I am not entirely certain what I'll be using all this new space for. The dictionary may change with my usage over time. At the moment I'm thinking that the "number keyed" vowels may not be optimal (`should`, `could` and `would` are all potential candidates).

## Overview of the system

**Starting words**
- `SWR`: `I`
- `KPWR`: `you`
- `KWHR`: `he`
- `SKWHR`: `she`
- `TWH`: `they`
- `TWR`: `we`
- `KPWH`: `it`
- `STKPWHR`: ` ` (nothing)
  - Plural form of phrases (e.g. `STKPWHRPT`: `wants to`)
  - `STKPWHROE`: `doesn't`
  - `#STKPWHROE`: `does`
- `STWR`: ` ` (nothing)
  - Singular form of phrases (e.g. `STWRPT`: `want to`)
  - `STKPWHROE`: `don't`
  - `#STKPWHROE`: `do`

**Middle words**
- `A`: `really`
- `O`: `can't`
- `OE`: `don't`/`doesn't` (depends on pronoun)
- `E`: `just`
- `U`: `really`
- `-F`: `even`
- `AU`: `didn't`
- `AEU`: `didn't really`
- `AOU`: `really didn't`
- `AOEU`: `kinda`
- `AOEUF`: `kind of`

> NOTE: When using `A` and `U` with `O`, `OE`, and `E`, the word `really` can be either appended or prepended to the middle word (e.g., `AOE` → `don't really`, `AE` → `really just`).

> NOTE: `E` can be added in for the word `even`. It is always at the end of the middle words (e.g., `OUF` → `can't really even`).

> Memorisation tip: as for `really didn't` and `didn't really`, the side with two keys represents `really` (I think of the word `didn't` as one syllable, and therefore gets one key while `really` - having two syllables - gets two).

**With number key**
- `A`: `have`
- `AO`: `haven't`
- `OU`: `haven't really`
- `O`: `can`
- `AOE`: `really do`
- `OE`: `do`
- `OEU`: `do really`
- `AE`: `really just didn't`
- `E`: `just didn't`
- `EU`: `just didn't really`
- `U`: `really`
- `AOU`: `really did`
- `AU`: `did`
- `AEU`: `did really`
- `AOEU`: `ever`
- `AOEUF`: `ever just`
- `F`: `even`

**Ending words**

All ending words comprise of a "root" word (`know`, `find`, `see`, etc) which `-T` can be added onto. What exactly this last word is depends on the ending word, but is usually `to` or `that`. Using the asterisk `*T` will result in other last words (usually `the`).

To get the past tense of an ending word, `-D` is used. For example `-PB` → `know`, and `-PBD` → `knew`. This can also be used together with the `-T` (`-PBTD` → `knew that`).

For root words that end in `-S` (e.g., `-RBS` → wish, `-RPLS` → matter) the pattern is different. `-T` is still used to get the final word (`-RBTS` → `wish to`) but since pressing `-D` would require a shift, `-Z` is used for past tense (`-RBSZ` → `wished`). Similarly, since pressing `-TZ` would require a shift, `-TSDZ` is used for past tense in combination with a final word (`-RBTSDZ` → `wished to`).

While there aren't many words that currently use this exception, `-S` is free to be used with many more ending words since it has been freed up by the automatic pluralising functionality.

> With Jade's system, `-S` would be used to pluralise, and wasn't available for use in root words.

- `PB`: `know`
- `PBT`: `know that`
- `*PBT`: `know the`
- `PBD`: `knew`
- `PBTD`: `knew that`
- `*PBTD`: `knew the`
- `P`: `want`
- `PT`: `want to`
- `PTD`: `wanted to`
- `*PT`: `want the`
- `*PTD`: `wanted the`
- `*P`: `wanna`
- `RPBL`: `make`
- `RPBLT`: `make that`
- `*RPBLT`: `make the`
- `RPBLD`: `made`
- `RPBLTD`: `made that`
- `*RPBLTD`: `made the`
- `RPL`: `remember`
- `RPLT`: `remember that`
- `RPLTD`: `remembered that`
- `*RPLT`: `remember the`
- `*RPLTD`: `remembered the`
- `RPLS`: `matter`
- `RPLTS`: `matter to`
- `*RPLTS`: `matter to`
- `RPLSZ`: `mattered`
- `RPLTSDZ`: `mattered to`
- `*RPLTSDZ`: `mattered to`
- `RBL`: `see`
- `RBLT`: `see that`
- `*RBLT`: `see the`
- `RBLD`: `saw`
- `RBLTD`: `saw that`
- `*RBLTD`: `saw the`
- `BG`: `can`
- `BGT`: `cannot`
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
- `T`: `have` (`T`, `TS`, and `*TS` all depend on the pronoun)
- `TS`: `have to`
- `*TS`: `have the`
- `S`: `was`
- `SZ`: `was not`
- `*SZ`: `wasn't`
- `PLTS`: `must`
- `L`: `will`
- `LD`: `would`
- `PBG`: `think`
- `PBGT`: `think that`
- `*PBGT`: `think the`
- `PBGD`: `thought`
- `PBGTD`: `thought that`
- `*PBGTD`: `thought the`
- `PBLG`: `find`
- `PBLGT`: `find that`
- `*PBLGT`: `find the`
- `PBLGD`: `found`
- `PBLGTD`: `found that`
- `*PBLGTD`: `found the`
- `PL`: `may`
- `PLS`: `seem`
- `PLTS`: `seem to`
- `PLSZ`: `seemed`
- `PLTSDZ`: `seemed to`
- `PLT`: `might`
- `RB`: `shall`
- `RBD`: `should`
- `RBLG`: `try`
- `RBLGT`: `try to`
- `*RBLGT`: `try the`
- `RBLGD`: `tried`
- `RBLGTD`: `tried to`
- `*RBLGTD`: `tried the`
- `RPBLG`: `look`
- `RPBLGT`: `look like`
- `*RPBLGT`: `look at`
- `RPBLGD`: `looked`
- `RPBLGTD`: `looked like`
- `*RPBLGTD`: `looked at`
- `RL`: `recall`
- `RLD`: `recalled`
- `RLS`: `realise`
- `RLTS`: `realise that`
- `*RLTS`: `realise the`
- `RLSZ`: `realised`
- `RLTSDZ`: `realised that`
- `*RLTSDZ`: `realised the`
- `RP`: `were`
- `RPBT`: `were not`
- `*RPBT`: `weren't`
- `RPT`: `were the`
- `*RPT`: `were the`
- `RPB`: `understand`
- `RPBD`: `understood`
- `RPG`: `need`
- `RPGT`: `need to`
- `*RPGT`: `need the`
- `RPGD`: `needed`
- `RPGTD`: `needed to`
- `*RPGTD`: `needed the`
- `LS`: `feel`
- `LTS`: `feel like`
- `LSZ`: `felt`
- `LTSDZ`: `felt like`
- `PBL`: `mean`
- `PBLT`: `mean that`
- `*PBLT`: `mean the`
- `PBLD`: `meant`
- `PBLTD`: `meant that`
- `*PBLTD`: `meant the`
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
- `GTD`: `got`
- `PLD`: `mind`
- `RG`: `forget`
- `RGD`: `forgot`
- `RGT`: `forget to`
- `RGTD`: `forgot to`
- `RBS`: `wish`
- `RBTS`: `wish to`
- `*RBTS`: `wish the`
- `RBSZ`: `wished`
- `RBTSDZ`: `wished to`
- `*RBTSDZ`: `wished the`
- `PGS`: `expect`
- `PGTS`: `expect to`
- `*PGTS`: `expect the`
- `PGSZ`: `expected`
- `PGTSDZ`: `expected to`
- `*PGTSDZ`: `expected the`
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

**Alternate starting words (no middle words)**
- `WHA[E/U/EU]`: `what he/you/I`
- `SKPW[E/U/EU]`: `do(es)n't he/you/I`
- `STKO[E/U/EU]`: `do(es) he/you/I`
- `STKPWO[E/U/EU]`: `did he/you/I`
- `STHA[E/U/EU]`: `that he/you/I`
- `STPA[E/U/EU]`: `if he/you/I`
- `SWH[E/U/EU]`: `when he/you/I`
