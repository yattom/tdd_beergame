#encoding: utf8

from beergame import *

def test_beergame():
    bd = 盤.new()
    第1週 = bd.process_week()
    小売出荷数 = 第1週.get小売出荷数()
    assert 4 == 小売出荷数


def main():
    test_beergame()


if __name__=='__main__':
    main()
