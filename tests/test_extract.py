from flag_morph.extract import extract_nouns

def test_extract_nouns():
    r = extract_nouns("해남대부속고등학교농구부")
    assert r == ["해남", "부속고등학교", "농구부"]

    r = extract_nouns("민주주의가 승리한다 내란잔당을 뿌리뽑자 - 5차 레트로 난방 탄핵버스 -")
    print(r)
    assert r == ['민주주의', '승리', '내란', '잔당', '뿌리', '레트로', '난방', '탄핵', '버스']
    