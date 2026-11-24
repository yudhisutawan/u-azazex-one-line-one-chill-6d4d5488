[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/yudhisutawan/u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/yudhisutawan/u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

# One Line, One Chill

One sentence of horror, under 200 characters, written to `/output/entry.txt`
by `main.py` (stdlib only, no writes to the repository itself).

> My name appeared in this morning's obituaries, and the photograph they used was taken an hour ago.

98 characters, one sentence. The dread is to the reader themself and imminent:
your death is already typeset, and someone photographed you an hour ago to
prepare it. Earned by implication, never announced — see `CANDIDATES.md` for
the full tournament (17 candidates, Hermes' 8 included; this line went 5–0
against the top 6, beating Hermes' best — the voicemail/coffin line — by
margin 2).

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -S -P main.py
cat /tmp/out/entry.txt
```

## Strategy

- Judge is pairwise on frightening > vivid > original > crafted. The winning
  line maximises the first criterion: a personal, imminent, inescapable dread
  (your own obituary, photo taken an hour ago), with concrete detail and a
  fresh turn (no mirror/doll/basement cliché), and a last phrase that lands.
- Backup if this line ever collides with a house fixed text: the runner-up in
  `CANDIDATES.md` (baby monitor / dead mother's name).
