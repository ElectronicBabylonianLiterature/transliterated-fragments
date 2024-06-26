# Transliterated Fragments from [eBL](https://www.ebl.lmu.de/)
Code to fetch and parse Data from Paper: <br>
[Transliterated Cuneiform Tablets of the Electronic Babylonian Library Platform](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.148) <br>
Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10018951.svg)](https://doi.org/10.5281/zenodo.10018951)  <br>
For a details and overview of contributors please refer to paper. To cite see below.  <br>
<br>
This repository contains code to download all publicly available transliterations using our public api (specified in `example.py`) and parse it using our [atf-parser](https://github.com/ElectronicBabylonianLiterature/generic-documentation/wiki/eBL-ATF-and-other-ATF-flavors). The atf parser has been manually extracted from our [api](https://github.com/ElectronicBabylonianLiterature/ebl-api). It has to be kept up to date manually, please open an issue in case there are any problems. You can always use the JSON provided in Zenodo. This JSON contains all fragments from the 1st of September 2023 and has been created using this code therefore should be compatible with the parser.
The atf-parser that is used in [production](https://www.ebl.lmu.de/)  verifies all signs using our sign database. The parser in this repository is not checking against a sign list. It is just validating the syntax and parsing the atf-string.



# Install

```
python >= 3.9.0

pip install poetry

poetry install
```
# Usage
Run `example.py` file

`get_first_batch_fragments` function does download 1000 Fragments from Api and saves them as json.

`get_all_fragments` function does download all > 25000 Fragments from Api and saves them as json. May Take 20 -30 minutes.

`get_some_fragments_and_parse` function does download 1000 Fragments from Api and parses the atf and saves them as json. 

ATF is a string in our flavor of ASCII-Transliteration Format (uses unicode is a legacy name)

ATF can be parsed using `parse_atf_lark` see in `example.py`.

Our ATF Parser details in https://github.com/ElectronicBabylonianLiterature/ebl-api/blob/master/docs/ebl-atf.md

# Tests
Run tests (with pytest) in `ebl/test` folder

# Example Fragment 
https://www.ebl.lmu.de/fragmentarium/1868%2C0523.2

```javascript

{
  "fragments": [
    {
      "_id": "1868,0523.2",
      "museumNumber": {
        "prefix": "1868,0523",
        "number": "2",
        "suffix": ""
      },
      "accession": "",
      "editedInOraccProject": "",
      "publication": "Edition by NinMed",
      "description": "Clay tablet, 20 + 19 lines of inscription, Neo-Assyrian.",
      "collection": "Kuyunjik",
      "museum": "The British Museum",
      "width": {
        "value": 8.25,
        "note": ""
      },
      "length": {
        "value": 8.25,
        "note": ""
      },
      "thickness": {},
      "joins": [],
      "record": [
        {
          "user": "Jiménez",
          "type": "Transliteration",
          "date": "2021-06-22T08:48:05.538589"
        },
        {
          "user": "Jiménez",
          "type": "Revision",
          "date": "2021-06-22T08:49:05.433443"
        },
        {
          "user": "Stadhouders",
          "type": "Revision",
          "date": "2021-06-26T11:39:08.314521"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T18:42:45.892870"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T20:58:39.646671"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:41:20.159908"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:42:10.881671"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:44:29.059411"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:47:01.920545"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:51:14.982451"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T21:58:04.358044"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:02:35.247136"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:07:48.755570"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:08:12.799157"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:08:52.401307"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:09:43.752966"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:15:43.211047"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:20:27.744949"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:27:13.596656"
        },
        {
          "user": "Simkó",
          "type": "Revision",
          "date": "2023-08-22T22:29:08.906415"
        }
      ],
      "signs": "X X X X X X X X X X X ABZ215 ABZ13 ABZ554 ABZ536 ABZ535 ABZ1 ABZ7\nX X X X X ABZ318 ABZ328 ABZ70 ABZ318 ABZ481 ABZ15 ABZ579 ABZ128 ABZ5 ABZ215 ABZ13 ABZ74 ABZ50 ABZ411 ABZ554\nX X X ABZ318 ABZ97 ABZ381 ABZ229 ABZ61 ABZ586 ABZ381 ABZ562 ABZ13 ABZ579 LAGAB×HAL ABZ318 ABZ330 ABZ49 ABZ537 ABZ72 ABZ296 ABZ214 ABZ231\nX X X X ABZ396 ABZ396 ABZ461 ABZ579 ABZ13 ABZ579 LAGAB×HAL ABZ201 ABZ296 ABZ342 ABZ75 ABZ480 ABZ411 ABZ411 ABZ83 ABZ1 ABZ69 ABZ296 ABZ541 ABZ396 ABZ396 ABZ411 ABZ411 ABZ411 ABZ533 ABZ7 ABZ342 ABZ73\nX X X X ABZ576 ABZ537 ABZ7 ABZ201 ABZ318 ABZ589 ABZ229 ABZ61 ABZ586 ABZ13 ABZ74 ABZ229 ABZ393 ABZ231 |GIŠ%GIŠ| ABZ381 ABZ1 ABZ7\nABZ480 ABZ461 ABZ570 ABZ579 ABZ86 ABZ579 ABZ330 ABZ1 ABZ539 ABZ314 ABZ483 ABZ483 ABZ411 ABZ1 ABZ106 ABZ545 ABZ597 ABZ13\nABZ480 ABZ70 ABZ354 ABZ576 ABZ342 ABZ537 ABZ7 ABZ229 ABZ61 ABZ586 ABZ215 ABZ13 ABZ74 ABZ461 ABZ579 ABZ13 ABZ579 LAGAB×HAL ABZ15 ABZ579 ABZ128 ABZ5 ABZ318 ABZ481\nABZ231 ABZ69 ABZ332 ABZ167 ABZ324 ABZ13 ABZ437 ABZ381 ABZ597 ABZ332 ABZ411 ABZ88 ABZ598b ABZ318 ABZ396 ABZ579 ABZ13 ABZ75 ABZ94 ABZ73 ABZ461\nABZ480 ABZ411 ABZ411 ABZ83 ABZ1 ABZ231 ABZ296 ABZ544 ABZ533 ABZ7 ABZ342 ABZ465 ABZ381 ABZ366 ABZ12\nABZ480 ABZ70 ABZ576 ABZ537 ABZ7 ABZ480 ABZ465 ABZ545 ABZ536 ABZ53 ABZ536 ABZ575 ABZ536 ABZ536 ABZ575 ABZ74 ABZ328 ABZ536 ABZ355 ABZ579 ABZ579 ABZ597 ABZ597 ABZ74 ABZ230\nABZ318 ABZ366 ABZ328 ABZ165 ABZ112 ABZ112 ABZ100+063 ABZ74 ABZ461 ABZ579 ABZ13 ABZ579 LAGAB×HAL ABZ536 ABZ306 ABZ328\nABZ444 ABZ469 ABZ206 ABZ79 ABZ330 ABZ49 ABZ537 ABZ536 ABZ597 ABZ535 ABZ354 ABZ482 ABZ1 ABZ172 ABZ58 ABZ354 ABZ12 ABZ545\nABZ480 ABZ70 ABZ354 ABZ576 ABZ342 ABZ537 ABZ7 ABZ215 ABZ59 ABZ461 ABZ579 ABZ13 ABZ579 LAGAB×HAL ABZ480 ABZ411 ABZ411 ABZ192 ABZ79 ABZ1 ABZ231 ABZ537 ABZ400 ABZ76 ABZ50 ABZ396 ABZ396\nABZ1 ABZ7 ABZ101 ABZ69 ABZ296 ABZ541 ABZ449 ABZ544 ABZ537 ABZ115 ABZ206 ABZ7 ABZ537 ABZ106 ABZ7 ABZ481 ABZ342 ABZ73 ABZ381\nABZ215 ABZ362 ABZ362 ABZ215 ABZ59 ABZ252 ABZ331e+152i ABZ461 ABZ579 ABZ13 ABZ579 LAGAB×HAL ABZ536 ABZ446 ABZ15 ABZ579 ABZ128 ABZ5 ABZ60 ABZ598b ABZ318 ABZ396 ABZ579\nABZ192 ABZ79 ABZ1 ABZ579 ABZ252 ABZ331e+152i ABZ12 ABZ3 ABZ1 ABZ536 ABZ396 ABZ579 ABZ101 ABZ86 ABZ115 ABZ206 ABZ7 ABZ481 ABZ334\nX ABZ215 X X X ABZ215 ABZ396 ABZ579 X X",
      "notes": {
        "text": "BabMed Team, 2013–2018.",
        "parts": [
          {
            "text": "BabMed Team, 2013–2018.",
            "type": "StringPart"
          }
        ]
      },
      "genres": [
        {
          "category": [
            "CANONICAL",
            "Technical",
            "Medicine",
            "Therapeutic"
          ],
          "uncertain": false
        }
      ],
      "introduction": {
        "text": "",
        "parts": []
      },
      "script": {
        "period": "Neo-Assyrian",
        "periodModifier": "None",
        "uncertain": false,
        "sortKey": 14
      },
      "externalNumbers": {
        "cdliNumber": "P451784",
        "bmIdNumber": "W_1868-0523-2",
        "archibabNumber": "",
        "bdtnsNumber": "",
        "urOnlineNumber": "",
        "hilprechtJenaNumber": "",
        "hilprechtHeidelbergNumber": ""
      },
      "projects": [],
      "traditional_reference": [],
      "datesInText": [],
      "atf": "1'. [x x x x x x x x x x (x) {šim}{d}]nin#-urta [ina] KUŠ\n#note: Ln. 1' // BAM 470 ln. 21'.\n#tr.en: If DITTO, @i{mūṣu}-stone, @i{parzillu} ('iron') . . . (and) @i{nikiptu}-aromatic ('spurge') in a leather bag.\n$ single ruling\n2'. [x x x x x u₂?-r]a?-na {u₂}LAL KA A.AB.BA {šim}{d}MAŠ NITA₂ u MUNUS\n#note: Ln. 2'-4' // KAR 56 ln. 5-11 // BAM 9 47-50.\n3'. [x x x {u₂}]ak?#-tam?# {na₄}mu-ṣa UH₂.{d}ID₂ {u₂}LU₂.U₁₈.LU NUMUN {giš}bi-ni\n4'. [x x x x] HI.HI PIŠ₁₀.{d}ID₂ SUHUŠ {giš}MA.NU DIŠ-niš SUD₂ ina MUD₂ {giš}EREN HI.HI EŠ-MEŠ-su-ma TI\n#tr.en: If a man has been seized by a ghost: you parch (and) mix @i{urânu} ('anise'), @i{ašqulālu}-plant, @i{imbûʾ tâmti} ('sea algae'), male and female @i{nikiptu}-aromatic ('spurge'), @i{qan šalāli} (a kind of reed), @i{aktam}-plant, @i{mūṣu}-stone, @i{ruʾtītu} (a kind of sulphur), @i{amīlānu}-plant ('man-like' plant), seed from @i{bīnu}-tree ('tamarisk') (and) ox horn, (then) you pound @i{kibrītu} (a kind of sulphur) (and) root from @i{ēru}-tree together, you mix them in blood from @i{erēnu}-tree ('cedar'), you keep anointing him (with the mixture), and then he will recover.\n$ single ruling\n5'. [x x x x G]IDIM DAB-su SUHUŠ {u₂}KU₆ {na₄}mu-ṣa AN.BAR {na₄}ZALAG₂ ni-kip-ta₅ ina KUŠ\n#note: Ln. 5' // BAM 470 ln. 22' // K.2492 ln. 2'-3'.\n#tr.en: Poultice for (the case when) a man has been seized by a ghost: root from @i{urânu}-plant ('anise'), @i{mūṣu}-stone, @i{parzillu} ('iron'), @i{zalāqu}-stone ('shiny' stone) (and) @i{nikiptu} ('spurge') in a leather bag.\n$ single ruling\n6'. [DIŠ KIMIN A.RI].A# LU₂ ina {sig₂}AKA₃ NIGIN u# ina GU₂-šu₂ GAR-an\n#note: Ln. 6' // BAM 470 ln. 23' // K.2492 ln. 4'.\n#tr.en: If DITTO, you wrap human seed in tuft of wool and you put it on his neck.\n$ single ruling\n7'. DIŠ# NA# ŠU#.GIDIM#.MA DAB-su {na₄}mu-ṣa {šim}{d}MAŠ PIŠ₁₀.{d}ID₂ KA A.AB.BA {u₂}LAL\n#note: Ln. 7'-9' // K.2492 ln. 5'-7'.\n8'. I₃# SUMUN ZAG.DU₈ E₂ {d}AMAR.UTU ša₂ ZAG u GUB₃ 6 U₂-HI.A an-nu-ti₃ TI-qe₂\n9'. DIŠ-niš SUD₂ ina I₃.GIŠ ŠEŠ₂-MEŠ-su-ma DIN-uṭ lat-kut\n#tr.en: If a man has been seized by 'hand-of-ghost': @i{mūṣu}-stone, @i{nikiptu}-aromatic ('spurge'), @i{kibrītu} (a kind of sulphur), @i{imbûʾ tâmti} ('sea algae'), @i{urânu}-plant ('anise') (and) old grease from the right and left doorjambs of the Marduk temple - you take these six drugs, you pound them together, you keep anointing him with them in oil, and then he will recover. Tested (remedy).\n$ single ruling\n10'. DIŠ NA GIDIM DAB-su ana DIN-šu₂ ŠE₁₀ ŠAH ŠE₁₀ UR.GI₇ ŠE₁₀ UR.BAR.RA ŠE₁₀ KA₅.A A.GAR.GAR MAŠ.DA₃\n#note: Ln. 10'-12' // K.2492 ln. 8'-10'.\n11'. {u₂}KUR.RA NAGA.SI SI DARA₃.MAŠ PIŠ₁₀.{d}ID₂ ku-up-ra\n12'. GIR₃.PAD.DU NAM.LU₂.U₁₈.LU {tug₂}NIG₂.DARA₂.ŠU.LAL₂ ina NE tu-qat-tar-šu₂\n#tr.en: If a man has been seized by a ghost: in order to heal him, you fumigate him with pig dung, dog dung, wolf dung, fox dung, gazelle droppings, @i{nīnû}-plant ('mint'), @i{uḫūlu qarnānû} ('horned alkali'), stag horn, @i{kibrītu} (a kind of sulphur), @i{kupru} ('bitumen'), human bone (and) soiled rag over fire.\n$ single ruling\n13'. DIŠ NA ŠU.GIDIM.MA DAB-su {šim}LI PIŠ₁₀.{d}ID₂ DIŠ-niš GAZ SIM ina I₃.UDU ELLAG₂ MAŠ₂.NITA₂! HI.HI\n#note: Ln. 13'-14' // K.2492 ln. 11'-13'.\n14'. ina KUŠ SUR MUD₂ {giš}EREN IGI ŠEŠ₂ lu SAG.DU-su lu GU₂-su LAL-ma TI-uṭ\n#tr.en: If a man has been seized by 'hand-of-ghost': you crush (and) sift @i{burāšu}-aromatic (a kind of juniper) (and) @i{kibrītu} (a kind of sulphur) together, you mix them in fat from the kidney of a male goat, you smear (the mixture) on a piece of leather, you rub blood from @i{erēnu}-tree ('cedar') on it, you bandage either his head or his neck, and then he will recover.\n$ single ruling\n15'. {šim}GUR₂.GUR₂ {šim}LI GAZI{sar} PIŠ₁₀.{d}ID₂ ZI₃ GIB₃ KA A.AB.BA PAP 6 U₂-HI.A\n#note: Ln. 15'-16' // K.2492 ln. 14'-15' // BAM 9 ln. 64-65.\n16'. GAZ SIM ina A GAZI{sar} tara-muk ina TUG₂-HI.A SUR-ri SAG.DU-su LAL-id\n#tr.en: @i{kukru}-aromatic, @i{burāšu}-aromatic (a kind of juniper), @i{kasû}-herb ('tamarind'), @i{kibrītu} (a kind of sulphur), flour from @i{kibtu} ('wheat') (and) @i{imbûʾ tâmti} ('sea algae') - altogether six drugs, you crush (and) sift them, you soak them in juice from @i{kasû}-herb ('tamarind'), you smear (the mixture) on a piece of fabric (and) you bandage his head with it.\n$ single ruling\n17'. [x] {šim#}x x (x) ŠIM-HI.A x x [...]\n#tr.en: . . . aromatics . . ."
    }
  ]
}
```

# Cite
```
@article{Cobanoglu-2024,
 abstract = {This work presents a corpus of transliterated cuneiform tablets from the Electronic Babylonian Library (eBL) platform, including a public API endpoint to download the latest version of the data, and a Python library to parse the transliterations in ATF format. As of the time of writing, the constantly growing dataset contains around 25,000 tablets with over 350,000 lines of transliterated text. This dataset is a sizeable addition to open-source cuneiform data and a major milestone for research within the fields of cuneiform studies and NLP.},
 author = {Cobanoglu, Yunus and Laasonen, Jussi and Simonjetz, Fabian and Khait, Ilya and Cohen, Sophie and Földi, Zsombor and Hätinen, Aino and Heinrich, Adrian and Mitto, Tonio and Rozzi, Geraldina and Sáenz, Luis and Jiménez, Enrique},
 doi = {10.5334/johd.148},
 journal = {Journal of Open Humanities Data},
 keyword = {en_US},
 month = {Feb},
 title = {Transliterated Cuneiform Tablets of the Electronic Babylonian Library Platform},
 year = {2024}
}
```

