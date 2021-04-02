import util


class CHARA:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None
        self.power = None
        self.level = None
        self.cost = None
        self.soul = None
        self.feature = None
        self.status = None
        self.counter = False
        self.appendEffect = None  # util.AppendEffect()
        self.attackLimit = False
        self.useCardLimit = None


class EVENT:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None
        self.level = None
        self.cost = None
        self.counter = False
        self.useCardLimit = None

    def autoEffect(self, player1, player2):
        pass


class CX:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None


class S51_001(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�I���E�X�e�[�W�A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃^�[�����A���̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y�N�z �W�� �m�@ ���Ȃ��̃L������2�����X�g����n ���Ȃ��͎����̎R�D�̏ォ��4�����߂���A�T�����ɒu���B�����̃J�[�h�̃N���C�}�b�N�X1���ɂ��A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    def permanentEffect(self, player1, player2, position):
        if player1.turnPlayer is True:
            pass

    def startUpEffect(self, player1, player2, position):
        player1.useCost(1)
        self.status = util.Status.REST
        search_count = player1.cardEffect.CharaEffect.concentration( player1, player2, position )
        if search_count != 0:
            pass # TODO �T�[�`


class S51_002(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̖񑩃A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��2�����A�T�����ɒu���B�����̃J�[�h�ɃN���C�}�b�N�X������Ȃ�A���̃^�[�����A���̃J�[�h�̃\�E�����{2�B
�y���z�m���Ȃ��̃X�g�b�N�̏ォ��1�����N���b�N�u��ɒu���A���̃J�[�h���v���o�ɂ���n �o�g�����̂��̃J�[�h�����o�[�X�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����̃J�[�h���Ɂu�L���g�v���u�A�X�i�v���u���C�v���܂ރL������1���I�сA��D�ɖ߂��B
'''
    

class S51_003(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���|�̍����A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B
�y���zCX�R���{�m��D��2���T�����ɒu���n ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�s�}�U�[�Y�E���U���I�t�v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�̏ォ��11�����A�T�����ɒu���A����ɂw�_���[�W��^���A���̃^�[�����A���̃J�[�h�̃p���[���{3000�B�w�͂����̃J�[�h�̃g���K�[�A�C�R���̃\�E���}�[�N�̍��v�ɓ������B�i�_���[�W�L�����Z���͔�������j
'''
    

class S51_004(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����f�[�g������"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{1500�B
�y���z �J�^�u�g�A�g�U���h�L���g�v �m��D��1���T�����ɒu���n �i���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�g�A�g�U���h�L���g�v��1���I�сA��D�ɖ߂��j
'''
    

class S51_005(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�L���g�̗��l�A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̃J�[�h�̓T�C�h�A�^�b�N�ł��Ȃ��B
�y���zCX�R���{�m���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��̃N���C�}�b�N�X�u��Ɂu�ς��Ȃ��C�����v������Ȃ�A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    

class S51_006(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����^�C��������"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{�w�B�w�͂��̃L�����̃��x���~500�ɓ������B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1500���A���̔\�͂�^����B�w�y�i�z ���̃J�[�h�͑���̌��ʂɑI�΂�Ȃ��B�x
'''
    

class S51_007(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�M���t�A�X�i&amp;�s���̌��m�t�L���g"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃N���b�N�u��Ɂu�g�{�C�ɂȂ鎞�h�L���g�v������Ȃ�A���Ȃ��̎�D�̂��̃J�[�h�̃��x�����|1�B
�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ���1���܂ň����A�����̎�D�̃R�X�g1�ȉ��̃L������1���܂őI�сA����̍D���Șg�ɒu���B
'''
    

class S51_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h�A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h���A�^�b�N�������A���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{1500�B
�y���z ���̃J�[�h���u�g�A�g�U���h�L���g�v�́y���z�̌��ʂŕ���ɒu���ꂽ���A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA�X�g�b�N�u��ɒu���Ă悢�B
'''
    

class S51_009(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�҂��������񑩂̓��A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̂��̃J�[�h�̃��x�����|1�B
�y���z �o�g�����̂��̃J�[�h�����o�[�X�������A���̃J�[�h���R�D�̉��ɒu���B
'''
    

class S51_010(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�񑩂����ɃA�X�i&amp;�L���g"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z �L�� ���Ȃ��̎v���o�u��Ɂu�����̖� �A�X�i�v������Ȃ�A���̃J�[�h�̃p���[���{5000���A�\�E�����{1�B
'''
    

class S51_011(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "������MVP�A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ���1�������A�����̎�D��1���I�сA�T�����ɒu���B
�y���z ���̃J�[�h�����o�[�X�������A���̃J�[�h�̃o�g������̃��x��������̃��x����荂���Ȃ�A���Ȃ��͂��̃L�������X�g�b�N�u��ɒu���Ă悢�B����������A���Ȃ��͑���̃X�g�b�N�̉�����1�����A�T�����ɒu���B
'''
    

class S51_012(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���f�̏��A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m��D�́s�A�o�^�[�t���s�l�b�g�t�̃L������1���T�����ɒu���n���Ȃ��̃L�����̃g���K�[�`�F�b�N�ŃN���C�}�b�N�X���ł����A���̃J�[�h�̃g���K�[�A�C�R�����\�E���~2�Ȃ�A�R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D���ォ��2���܂Ō��āA�J�[�h��1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���B
�y�N�z�m�@���̃J�[�h�����X�g����n���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ��D�ɉ�����B�i�����łȂ��Ȃ猳�ɖ߂��j
'''
    

class S51_013(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�{�X�o�g���ɒ���A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́u�_�炩�ȕ\�� �L���g�v���ׂĂɁA�p���[���{1000���A�\�E�����{1�B
'''
    

class S51_014(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��؂ȏK��������"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z �L�� ���Ȃ��̎v���o�u��Ɂu�����̖� �A�X�i�v������Ȃ�A���̃J�[�h�̃p���[���{1000���A�\�E�����{1�B
�y���z �A���R�[�� �m��D�̃L������1���T�����ɒu���n �i���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�������g�Ƀ��X�g���Ēu���j
'''
    

class S51_016(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�퓬�����A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 1000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��̃L�������ׂĂ��s�A�o�^�[�t���s�l�b�g�t�Ȃ�A���Ȃ��͎����̎R�D�̏ォ��1�����A�X�g�b�N�u��ɒu���Ă悢�B
�y�N�z�� ������2000 ���x��1 �m�@ ��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{2000�j
'''
    

class S51_017(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�V�˃Q�[���f�U�C�i�[�h����"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 2
        self.cost = 3
        self.soul = 3
        self.feature = ('�s�l�b�g�t', '�s�Ȋw�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z �o�g�����̂��̃J�[�h�����o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�����A�N���b�N�u��ɒu���A���̃J�[�h�����X�g����B
'''
    
    
class S51_018(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�ӂ̙ꂫ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_019(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�}�U�[�Y�E���U���I�t(S51)"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_020(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ς��Ȃ��C����"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    

class S51_021(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Z�z���Ȗ����[�t�@"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 0
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ����y�N�z���g�������A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
�y���z�m�@�n ���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D���ォ��4���܂Ō��āA�s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A�c��̃J�[�h���T�����ɒu���B
'''
    

class S51_022(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�̕P�t���i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z�����̍T�����̃N���C�}�b�N�X��2���ȉ��Ȃ�A��D�̂��̃J�[�h�̃��x����-1�B
�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B
�y���z���̃J�[�h���A�^�b�N�������A���Ȃ��͑��̎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[��+X�BX�͑��̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
'''
    

class S51_023(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�������h���t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��̃L�������ׂĂɁA���̔\�͂�^����B�w�y�i�z ���̃J�[�h�̓T�C�h�A�^�b�N�ł��Ȃ��B�x
�y���z�m�@ ��D��1���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''


class S51_024(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̒��t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͑���̑O��̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ����y�N�z���g�������A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
'''
    

class S51_025(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�gAR�A�C�h���h���i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̐��ʂ̃L�����̃��x�������̃J�[�h�̃��x����荂���Ȃ�A���̃J�[�h�̓t�����g�A�^�b�N�ł��Ȃ��B
�y���zCX�R���{ ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���������啑��v������Ȃ�A���Ȃ��͎����̃X�g�b�N�̏ォ��1�����A��D�ɖ߂��Ă悢�B
'''
    

class S51_026(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Ӗ��[�Ȍ������i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z �L�� ���Ȃ��̎v���o�u��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2���ȏ�Ȃ�A���̃J�[�h�̃p���[���{4000�B
�y���z �A���R�[�� �m��D�́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���T�����ɒu���n �i���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�������g�Ƀ��X�g���Ēu���j
'''
    

class S51_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�U���̒����G�C�W"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���zCX�R���{�m���Ȃ��̃N���C�}�b�N�X�u��́u�I�[�f�B�i���E�i���o�[2�v��1���N���b�N�u��ɒu���n ���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������4���܂őI�сA�X�g�b�N�u��ɍD���ȏ��ԂŒu���A���̃^�[�����A���̃J�[�h�̃\�E�����{1�B
�y���z �o�g�����̂��̃J�[�h�����o�[�X�������A���̃J�[�h���v���o�ɂ���B
'''
    

class S51_028(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�݂̎����䂳���[�t�@"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h���A�^�b�N�������A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͑��̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~1000�ɓ������B
�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���̃J�[�h����D���畑��ɒu���ꂽ�^�[�����A���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�����A�T�����ɒu���B���̃J�[�h�̃g���K�[�A�C�R���Ƀ\�E���}�[�N������Ȃ�A���̃J�[�h���X�^���h����B
'''
    

class S51_029(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�u���̐g���Ȃ��G�C�W"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͑���̃X�g�b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B����������A���Ȃ��͑���̍T�����̃J�[�h��1���I�сA�X�g�b�N�u��ɒu���B
�y���z�m�@�n ����̃^�[�����A�o�g�����̂��̃J�[�h�����o�[�X�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�����X�g���A���̂��Ȃ��̃A���R�[���X�e�b�v�̎n�߂ɁA���̃J�[�h���T�����ɒu���B
'''
    

class S51_030(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�L���̌��Ѓ��i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��͎����̃N���b�N�́u��肽�������Ί� ���i�v��1���I�сA�X�g�b�N�u��ɒu���Ă悢�B
�y�N�z��������1000 ���x��1 �m��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{1000�j
'''
    

class S51_031(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���M�ɖ���������G�C�W"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͑���̎v���o�u��̕\�����̃J�[�h��1���I�сA�������ɂ��Ă悢�B����������A���Ȃ��̃^�[���̏I���ɁA���̃J�[�h��\�����ɂ���B
�y���z�m�A�n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���̃L������1���I�сA����̕���̃L�����̂��Ȃ����̘g�ɓ������B
'''
    

class S51_032(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�����R�m�c�t�m�[�`���X"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̓C�x���g�Ɓw�������x����D����v���C�ł��Ȃ��B
'''
    

class S51_033(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�I�[�O�}�[�t�J���ҏd��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�Ȋw�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{�w�B�w�͂��̃L�����̃��x���~500�ɓ������B
�y�N�z�m���̃J�[�h�����X�g����n ���Ȃ��͎����̍T�����́u�劽���̒� ���i�v��1���I�сA�v���o�ɂ���B
�y�N�z�m�A ���Ȃ��̕���́u���M�ɖ��������� �G�C�W�v��1���v���o�ɂ���n ���Ȃ��͎����̎R�D�����ă��x���w�ȉ��̃J�[�h���Ɂu���i�v���܂ރL������2���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B�w�͂��Ȃ��̎v���o�u��́u�劽���̒� ���i�v�̖����ɓ������B
'''
    

class S51_034(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�X�y�V�����X�e�[�W���i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{1000�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A���̔\�͂�^����B�w�y���z�m�@�n ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B�x
'''
    

class S51_035(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�sAnIncarnateoftheRadius�t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�G�l�~�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ���2���܂ň����A�����̎�D��1���I�сA�T�����ɒu���B
�y���zCX�R���{�m�A ��D��4���T�����ɒu���A���Ȃ��̃N���C�}�b�N�X�u��́u���̐�����v��1�����̃J�[�h�̉��Ƀ}�[�J�[�Ƃ��ė������ɒu���n ���Ȃ��̃A���R�[���X�e�b�v�̎n�߂ɁA�O��ɂ��̃J�[�h������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃N���b�N���ׂĂ��A�T�����ɒu���B
�y���zCX�R���{�m�E ��D��3���T�����ɒu���A���̃J�[�h�̉��̃}�[�J�[��1���T�����ɒu���n ����̃A���R�[���X�e�b�v�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̍s����2��s���B�w�����3�_���[�W��^����B�x�i�_���[�W�L�����Z���͔�������j
'''
    

class S51_036(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��̐N���m�G�C�W"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̂��Ȃ��̃J�[�h���Ɂu���i�v���܂ރL����������Ȃ�A���̃J�[�h�̃p���[��+3000�B
�y���z�m���̃J�[�h���T�����ɒu���n���̂��Ȃ��̃J�[�h���Ɂu���i�v���܂ރL�������t�����g�A�^�b�N���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃o�g�����̃L������1���I�сA���̃^�[�����A�p���[+1000�B
'''
    

class S51_037(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��l�̊��t�s��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A����̑O��̃L������1���ȉ��Ȃ�A���Ȃ��͑���̑O��̃L������1���I�сA���̃^�[�����A�p���[���|3000�B
'''
    

class S51_038(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�̂���D�����i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�N�z�m���̃J�[�h�����X�g����n ���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{1500�B
'''
    

class S51_039(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�劽���̒����i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m���Ȃ��̃X�g�b�N�̏ォ��1�����N���b�N�u��ɒu���n ���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃N���b�N��1���I�сA��D�ɖ߂��A�����̎R�D�̏ォ��1�����A�N���b�N�u��ɒu���B
'''
    

class S51_040(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���s�H�Ƒ�w�����d��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�Ȋw�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m��D��1���N���b�N�u��ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ăJ�[�h���Ɂu���i�v���u�G�C�W�v���܂ރL������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    

class S51_041(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��肽�������Ί烆�i"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s���y�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_042(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���@�U�����[�t�@"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���zCX�R���{ ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��̃N���C�}�b�N�X�u��Ɂu�d�������̉���v������Ȃ�A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI�сA�X�g�b�N�u��ɒu���A�����̎R�D�̏ォ��1�������J����B���̃J�[�h�̃��x����1�ȏ�Ȃ��D�ɉ�����B�i�N���C�}�b�N�X�̃��x����0�Ƃ��Ĉ����B�����łȂ��Ȃ猳�ɖ߂��j
'''
    

class S51_043(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��������҂̖����[�t�@"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��̃L�������ׂĂɁA���̔\�͂�^����B�w�y�i�z ���̃J�[�h�̓T�C�h�A�^�b�N�ł��Ȃ��B�x
�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ����y�N�z���g�������A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͑��̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
'''
    
    
class S51_044(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ɂ��΍R"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 3
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_045(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�I�[�f�B�i���E�X�P�[��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_046(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "SAO�����L�^�S�W"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_047(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���������啑��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_048(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�I�[�f�B�i���E�i���o�[2"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_049(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���̐����"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('��',)
        self.useCardLimit = None
    ''''''
    
    
class S51_050(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�d�������̉���"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('��',)
        self.useCardLimit = None
    ''''''
    

class S51_051(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�܂�Ȃ��ӎv���Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̌��̃L������1���ȉ��Ȃ�A���̃J�[�h�̓A�^�b�N�ł��Ȃ��B
�y���zCX�R���{�m�@�n ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�N�G����̃p�[�e�B�v���C�v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑��̎����̃L������1���ƁA���̃J�[�h��I�сA���̃^�[�����A���̔\�͂�^����B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̍T�����̃L������1���I�сA��D�ɖ߂��Ă悢�B�x
'''
    

class S51_052(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h�V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃L�������ׂĂ��s�A�o�^�[�t���s�l�b�g�t�Ȃ�A���̃J�[�h�̃p���[���{1500���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y�i�z ���̃J�[�h�̃o�g�����A����́w�������x����D����v���C�ł��Ȃ��B�x
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ�����u�g�A�g�U���h�L���g�v�́y���z�̌��ʂŕ���ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B
'''
    

class S51_053(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�I���E�X�e�[�W�V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y�N�z�m�@ ���̃J�[�h�����X�g����n ���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A���̔\�͂�^����B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̍T�����̃L������1���I�сA��D�ɖ߂��Ă悢�B�x
'''
    

class S51_054(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����ς�Ƃ������i���Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̂��Ȃ��̃o�g�����̃L���������o�[�X�������A���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{1500�B
�y���z�m�@�n ���Ȃ��̃L�����̃g���K�[�`�F�b�N�ŃN���C�}�b�N�X���ł����A���̃J�[�h�̃g���K�[�A�C�R�����\�E���}�[�N�~2�Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����̃L������1���I�сA��D�ɖ߂��A�����̎�D��1���I�сA�T�����ɒu���B
'''
    

class S51_055(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ɂ��₩�ȕ��ی㗢��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��2�����A�T�����ɒu���A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂����̃J�[�h�́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~1000�ɓ������B
'''
    

class S51_056(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�\����V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2���ȏ�Ȃ�A���̃J�[�h�̃p���[���{1500���A���̃J�[�h�́w�y���z �A���R�[�� �m��D�̃L������1���T�����ɒu���n�x�𓾂�B
'''
    

class S51_057(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h���Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ�����u�g�A�g�U���h�L���g�v�́y���z�̌��ʂŕ���ɒu���ꂽ���A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA��D�ɖ߂��Ă悢�B
�y���z�m��D��2���T�����ɒu���n ���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A�����1�_���[�W��^����B�i�_���[�W�L�����Z���͔�������j
'''
    

class S51_058(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��@�ꔯ�V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������āA�R�D�̏ォ�T�����ɒu���B
�y���zCX�R���{�m���̃J�[�h����D�ɖ߂��n���Ȃ��̃N���C�}�b�N�X�u��Ɂu�񓹂�㩁v���u���ꂽ���A�R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ��D�ɉ�����B�i�����łȂ��Ȃ猳�ɖ߂��j
'''
    

class S51_0(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̘T�����Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h���A�^�b�N�������A���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2���ȏ�Ȃ�A���̃^�[�����A���̃J�[�h�̃p���[���{2000�B
�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B�o�g�����̂��̃J�[�h�����o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h�̃��x����2�ȏ�Ȃ�A���Ȃ��͂��̃J�[�h�����X�g���Ă悢�B�i�N���C�}�b�N�X�̃��x����0�Ƃ��Ĉ����B���J�����J�[�h�͌��ɖ߂��j
'''
    

class S51_060(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�e�ސ؍��݃V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��̑O��̒����̘g�̃L�����ɁA�w�y���z �A���R�[�� �m��D�̃L������1���T�����ɒu���n�x��^����B
�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{1000�B
'''
    

class S51_061(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�{�X�o�g���ɒ��탊�Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃^�[�����A���̂��Ȃ��́u�{�X�o�g���ɒ��� �V���J�v���ׂĂɁA�p���[���{2000�B
�y���z �J�^�u�{�X�o�g���ɒ��� �V���J�v �m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n �i���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�{�X�o�g���ɒ��� �V���J�v��1���I�сA��D�ɖ߂��j
'''
    

class S51_062(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�������̌]�q"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z �o�g�����̂��̃J�[�h�����o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h�����x��0�ȉ��̃L�����Ȃ��D�ɉ�����B�i�����łȂ��Ȃ猳�ɖ߂��j
'''
    

class S51_063(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����C�Ȏd���V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃X�g�b�N��3���ȉ��Ȃ�A���̃J�[�h�̃p���[���{1500�B
�y�i�z ���̃J�[�h�̐��ʂ̃L�����ɁA�w�y���z �A���R�[�� �m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n�x��^����B
'''
    

class S51_064(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�{�X�o�g���ɒ���V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_065(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�������̗���"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�N�z�� ������3000 ���x��2 �m�@ ��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{3000�j
'''
    

class S51_066(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���C�ȃ��Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{1000�B
�y���z�m�@�n �A���R�[���X�e�b�v�̎n�߂ɁA���̂��Ȃ��̑O��̃��X�g���Ă���L���������Ȃ��Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�����X�g����B
'''
    
    
class S51_067(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�̂��Ă��@��"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_068(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Ă̋��G"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 3
        self.cost = 3
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_069(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�N�G����̃p�[�e�B�v���C"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE, util.TriggerType.GATE)
        self.useCardLimit = None
    ''''''

    def permanentEffect(self, player):
        for i in range(5):
            if len(player.MYFIELD["Stage"][i]) != 0:
                player.MYFIELD["Stage"][i][0].power += 1000
                player.MYFIELD["Stage"][i][0].soul += 1
                print("{} �Ɍ��ʂ��g���܂���".format(player.MYFIELD["Stage"][i][0].name))
                print("�p���[ : {}".format(player.MYFIELD["Stage"][i][0].power))
                print("�\�E�� : {}".format(player.MYFIELD["Stage"][i][0].soul))
        return [[1000, 1000, 1000, 1000, 1000], [1, 1, 1, 1, 1]]

    
class S51_070(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�񓹂��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE, util.TriggerType.STANDBY)
        self.useCardLimit = None
    ''''''

    def permanentEffect(self, player): # TODO �d��
        pass


class S51_071(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�{�C�ɂȂ鎞�h�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͑��̎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���X�g���A���̃L�����̂��Ȃ��g�ɓ������B
'''
    

class S51_072(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������4���ȏ�Ȃ�A���Ȃ��̎�D�̂��̃J�[�h�̃��x�����|1�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ�����u�g�A�g�U���h�L���g�v�́y���z�̌��ʂŕ���ɒu���ꂽ���A���Ȃ���1���܂ň����A���̃^�[�����A���̃J�[�h�̃p���[���{2000�B
�y���z�m�@ ��D��2���T�����ɒu���n ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ��̑O��̒����̘g�̃L�������A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�̏ォ��3�����A�T�����ɒu���B�����̃J�[�h�ɃN���C�}�b�N�X������Ȃ�A���̃J�[�h���X�^���h����B
'''
    

class S51_073(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��w���܂Ō��āA�J�[�h��1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����ɓ������B
�y���zCX�R���{�m�B ��D��2���T�����ɒu���A���̃J�[�h���T�����ɒu���n ���̂��Ȃ��̃L�������A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�s���̌��m�t�Ăсv������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��́u�g�A�g�U���h�L���g�v�ȊO�̎����̍T�����̃J�[�h���Ɂu�A�g�U���v���܂ރL������1���I�сA���̃J�[�h�������g�ɒu���B
'''
    

class S51_074(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���M���^�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̃X�g�b�N��2���ȉ��Ȃ�A���̃J�[�h�̃p���[���{1500�B
�y���z �A���R�[�� �m���Ȃ��̕���́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���N���b�N�u��ɒu���n �i���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�������g�Ƀ��X�g���Ēu���j
'''
    

class S51_075(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�sSAO���Ҏҁt�����ށ��a�l"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̃^�[�����A���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{1000�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��2���܂Ō��āA�J�[�h��1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���A�����̎�D��1���I�сA�T�����ɒu���B
'''
    

class S51_076(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����鏕���l�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
�y���zCX�R���{ ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�M���̎ˌ��v������Ȃ�A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ��D�ɉ�����B�i�����łȂ��Ȃ猳�ɖ߂��j
'''
    

class S51_077(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "AR�ł̐킢�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h���A�^�b�N�������A���Ȃ��͑��̎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{�w�B�w�͑��̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
'''
    

class S51_078(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����Ă��Ȃ����샆�C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̐��ʂ̃L�����̃��x�������̃J�[�h�̃��x����荂���Ȃ�A���̃J�[�h�̓t�����g�A�^�b�N�ł��Ȃ��B
�y���zCX�R���{�m��D��1���X�g�b�N�u��ɒu���n ���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃N���C�}�b�N�X�u��́u���҂������܂����I�v��1���I�сA��D�ɖ߂��B
'''
    

class S51_079(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���C�����ς����C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
�y���z�m��D��2���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���̃X�g�b�N���ׂĂ��A�T�����ɒu���A����͎����̎R�D�̏ォ�瓯���������X�g�b�N�u��ɒu���B
�y���z ����̃^�[�����A���Ȃ��̎󂯂��_���[�W���L�����Z������Ȃ��������A�O��ɂ��̃J�[�h������Ȃ�A���Ȃ��͎����̎R�D���ォ��1�����āA�R�D�̏ォ�T�����ɒu���B
'''
    

class S51_080(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�A�X�i�̗��l�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃��x��0�ȉ��̃L�������ׂĂɁA�p���[���{1000�B
�y���zCX�R���{�m�A�n ���Ȃ��̃A�^�b�N�t�F�C�Y�̎n�߂ɁA���Ȃ��̃N���C�}�b�N�X�u��ɃN���C�}�b�N�X���Ȃ��Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����āu�񑩂̑����v��1���܂őI�сA�N���C�}�b�N�X�u��ɒu���A���̎R�D���V���b�t������B
'''
    

class S51_081(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�`�q�ɓ���߂Ȃ��a�l"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z �J�^�u�g��U�� �A�X�i�v �m��D��1���T�����ɒu���n �i���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�g��U�� �A�X�i�v��1���I�сA��D�ɖ߂��j
�y�N�z�m�@ ���̃J�[�h���T�����ɒu���n ���Ȃ��͎����̎R�D���ォ��4���܂Ō��āA�s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A�c��̃J�[�h���T�����ɒu���B
'''
    

class S51_082(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�f���f���ȃN���C��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���̃^�[�����A���̃J�[�h�̃p���[���{2000�B�i���J�����J�[�h�͌��ɖ߂��j
�y���z ���̃J�[�h���A�^�b�N�������A���̂��Ȃ��̃L������1���ȉ��Ȃ�A���Ȃ��͎����̎R�D�̏ォ��1�����A�T�����ɒu���Ă悢�B���̃J�[�h�����x��0�ȉ��̃L�����Ȃ�A���̃L���������̍D���Șg�ɒu���B
'''
    

class S51_083(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����^�C�����C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
�y���z�m��D��1���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�����̕񍐁v��1���I�сA��D�ɖ߂��B
'''
    

class S51_084(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g�A�g�U���h�G�M��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͑���̑O��̃L������1���I�сA���̃^�[�����A�p���[���{3000�B
�y���z�m���Ȃ��̍T�����̃L������2���R�D�ɖ߂��A���̎R�D���V���b�t������n ���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃\�E�����{1�B
'''
    

class S51_085(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�f�[�^���W���C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��̃��x��3�ȏ�̃L�������ׂĂɁA�p���[���{2000�B
�y���z�m�@ ��D��2���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ăJ�[�h���Ɂu�A�g�U���v���܂ރL������2���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    

class S51_086(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Y����l�a�l��������"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̃^�[�����A���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{1500�B
'''
    

class S51_087(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ɟ��ފ��G�M��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̃^�[�����A���̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y���z�m���̃J�[�h���T�����ɒu���n ���̂��Ȃ��̃L���������䂩��T�����ɒu���ꂽ���A���ɂ��̃J�[�h������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃L���������̃L�����������g�Ƀ��X�g���Ēu���B
'''
    

class S51_088(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�{��̑ΖʃL���g"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́u�����̎h�� �A�X�i�v���ׂĂɁA�p���[���{2000�B
'''
    

class S51_089(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�S�_�̋C���L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̉��̃}�[�J�[1���ɂ��A���̃J�[�h�̃��x�����{1���A�p���[���{1500�B
�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̎R�D���ォ��1�����Ă悢�B����������A���Ȃ��͂��̃J�[�h�����̃J�[�h�̉��Ƀ}�[�J�[�Ƃ��ė������ɒu���B
'''
    

class S51_090(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��|��������߂�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��̎�D��5���ȏ�Ȃ�A���̃J�[�h�̃p���[���{2500���A���̃J�[�h�́w�y���z �A���R�[�� �m��D�̃L������1���T�����ɒu���n�x�𓾂�B
'''
    

class S51_091(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�_�炩�ȕ\��L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_092(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�N�[���ɘ_���V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����������Ȃ�A���Ȃ��͎����̃o�g�����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
�y�N�z�� ������2500 ���x��2 �m�@ ��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{2500�j
'''
    

class S51_093(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ً}�Q��N���C��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������4���ȏ�Ȃ�A���Ȃ��̎�D�̂��̃J�[�h�̃��x�����|1�B
�y�i�z ���̂��Ȃ��̃��x��0�ȉ��̃L����1���ɂ��A���̃J�[�h�̃p���[���{1000�B
'''
    

class S51_094(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ǂ����₵���a�l"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̂��̃J�[�h�̃��x�����|2�B
�y���z ���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
'''
    
    
class S51_096(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�I�[�f�B�i���E�i���o�[1"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_097(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s���̌��m�t�Ă�"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None
    ''''''
    
    
class S51_099(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���҂������܂����I"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_100(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�񑩂̑���"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�{',)
        self.useCardLimit = None
    ''''''
