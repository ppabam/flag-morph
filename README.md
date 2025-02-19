# flag-morph
(❀❛ ֊ ❛„)♡ ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა (∩˃o˂∩)♡ ( ദ്ദി ˙ᗜ˙ ) ε(´｡•᎑•`)っ 💕 ദ്ദി ༎ຶ‿༎ຶ ) ᓚ₍ ^. .^₎ ≽^• ˕ • ྀི≼ ٩(ˊᗜˋ*)و  (  ≧ᗜ≦) (๑>؂•̀๑) (˶ˆᗜˆ˵) ( • ᴖ • ｡)

## Project Description  
대한민국 2024년 12월 3일 말도 안되는 계엄상황에서 탄생한 대통령 탄핵 깃발들의 문구 형태소 분석 모듈  

### English  
A morphological analysis module for the phrases on impeachment flags born in South Korea's unprecedented martial law situation on December 3, 2024.  

### Chinese (Simplified)  
针对2024年12月3日韩国史无前例的戒严状态中诞生的总统弹劾旗帜上的文字进行形态分析的模块。  

### Japanese  
2024年12月3日に韓国で発生した前代未聞の戒厳令の状況で誕生した大統領弾劾旗の文句を形態素解析するモジュール。  

### Arabic  
وحدة لتحليل الصرف للعبارات الموجودة على أعلام العزل التي ظهرت في كوريا الجنوبية خلال حالة الأحكام العرفية غير المسبوقة في 3 ديسمبر 2024.  

### Spanish  
Un módulo de análisis morfológico para las frases en las banderas de juicio político nacidas en la situación de ley marcial sin precedentes de Corea del Sur el 3 de diciembre de 2024.  

### Hindi (हिंदी)  
2024 में 3 दिसंबर को दक्षिण कोरिया की अभूतपूर्व मार्शल लॉ स्थिति में उत्पन्न राष्ट्रपति महाभियोग झंडों के नारों का रूपात्मक विश्लेषण मॉड्यूल।  
---

### French (Français)  
Un module d'analyse morphologique des phrases sur les drapeaux d'impeachment nés dans la situation de loi martiale sans précédent en Corée du Sud le 3 décembre 2024.  

### German (Deutsch)  
Ein Modul zur morphologischen Analyse der Slogans auf Amtsenthebungsfahnen, die am 3. Dezember 2024 in der beispiellosen Situation des Kriegsrechts in Südkorea entstanden sind.  

### Portuguese (Português)  
Um módulo de análise morfológica para as frases nas bandeiras de impeachment nascidas na situação de lei marcial sem precedentes da Coreia do Sul em 3 de dezembro de 2024.  

### Russian (Русский)  
Модуль морфологического анализа фраз на флагах импичмента, появившихся в Южной Корее в беспрецедентной ситуации военного положения 3 декабря 2024 года. 

### Install
```bash
$ pip install flag-morph
```
OR
```bash
$ pdm add flag-morph
```

### Use
#### command line interface
```bash
$ flag-morph "민주주의가 승리한다 내란잔당을 뿌리뽑자 - 5차 레트로 난방 탄핵버스 -" --is_print 
Extracted nouns: ['민주주의', '승리', '내란', '잔당', '뿌리', '레트로', '난방', '탄핵', '버스']


$ flag-morph       
ERROR: The function received no value for the required argument: sentence
Usage: flag-morph SENTENCE <flags>
  optional flags:        --is_print

For detailed information on this command, run:
  flag-morph --help
```
#### code
```python
from flag_morph.extract import extract_nouns

def test_extract_nouns():
    r = extract_nouns("해남대부속고등학교농구부")
    assert r == ["해남", "부속고등학교", "농구부"]

    r = extract_nouns("민주주의가 승리한다 내란잔당을 뿌리뽑자 - 5차 레트로 난방 탄핵버스 -")
    print(r)
    assert r == ['민주주의', '승리', '내란', '잔당', '뿌리', '레트로', '난방', '탄핵', '버스']
```

### Dev
```bash
$ pdm venv create
Virtualenv /home/ppabam/code/flag-morph/.venv is created successfully
$ source .venv/bin/activate
$ pdm install
```

### Ref
- https://github.com/bab2min/kiwipiepy
- https://github.com/google/python-fire

