

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


class SE23_01(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���₩�Ȏ��A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z �m��D��1���T�����ɒu���n ���Ȃ��̃N���C�}�b�N�X�u��Ɂu�s���E���t�̏�Łv���u���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����āu��]�̌� �A�X�i�v��1���ƁA�s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    

class SE23_02(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ꂢ�L���A�X�i"
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
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{500�B
�y�N�z �m���̃J�[�h�����X�g����n ���Ȃ��͎����̃J�[�h���Ɂu�L���g�v���܂ރL������1���I�сA���̃^�[�����A�p���[���{500�B
'''
    

class SE23_03(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�sALO�t�̓���A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{500�B
�y�N�z �W�� �m�@�n ���Ȃ��͎����̎R�D�̏ォ��4�����߂���A�T�����ɒu���B�����̃J�[�h�̃N���C�}�b�N�X1���ɂ��A���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{2000�B
'''
    

class SE23_04(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�H�̎U��������"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̂��Ȃ��́A�s�l�b�g�t���s�A�o�^�[�t�̃L�������A�^�b�N�������A���̃^�[�����A���̃J�[�h�̃p���[���{1000�B
'''
    

class SE23_05(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Z���̂ЂƎ����t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{X�BX�͂��̃L�����̃��x���~500�ɓ������B
�y���z�m�A ��D��1���T�����ɒu���n ���Ȃ��̃N���C�}�b�N�X�u��Ɂu�t�F�A���B�E�_���X�v���u���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎�D�́u���z�ƌ��� ���[�t�@�����t�v��1���I�сA����̍D���Șg�ɒu���B
'''
    

class SE23_06(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�f�ލ̏W���[�t�@"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ��D�ɉ����A���Ȃ��͎����̎�D��1���I�сA�T�����ɒu���B(�����łȂ��Ȃ猳�ɖ߂�)
�y�N�z ��������2500 ���x��2�m�@ ��D�̂��̃J�[�h���T�����ɒu���n(���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{2500)
'''
    

class SE23_07(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�f�ލ̏W�V���J"
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ��D�ɉ����A���Ȃ��͎����̎�D��1���I�сA�T�����ɒu���B(�����łȂ��Ȃ猳�ɖ߂�)
�y���z ���̃J�[�h�����o�[�X�������A���̃J�[�h�̃o�g������̃��x����0�ȉ��Ȃ�A���Ȃ��͂��̃L���������o�[�X���Ă悢�B
'''
    

class SE23_08(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�V�쏹��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́s����t�̃L�������ׂĂɁA�p���[���{500�B
�y�i�z ����̑O��̃L�������ׂĂɁA�s�W�I�t��^����B
'''
    

class SE23_09(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "<ruby><rb>Sterben</rb><rp>(</rp><rt>�X�e���x��</rt><rp>)</rp></ruby><ruby><rb>�s���e�t</rb><rp>(</rp><rt>�f�X�E�K��</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h���A�^�b�N�������A����̃L�������ׂĂ��s�W�I�t�Ȃ�A���Ȃ��͑����1�_���[�W��^���Ă悢�B�i�_���[�W�L�����Z���͔�������j
�y���z ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�����̎h���g���v������Ȃ�A���̑���̃^�[���̏I���܂ŁA���̃J�[�h�̃p���[���{2500���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͂��̃L�������R�D�̏�ɒu���Ă悢�B�x
'''
    

class SE23_10(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŊϐ탊�Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̃X�g�b�N��3���ȉ��Ȃ�A���̃J�[�h�̃p���[���{1000�B
'''
    

class SE23_11(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���b�h�v���C���[<ruby><rb>�s���e�t</rb><rp>(</rp><rt>�f�X�E�K��</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ��̃h���[�t�F�C�Y�̎n�߂ɁA���Ȃ���1�_���[�W��^����B(�_���[�W�L�����Z���͔�������)
'''
    

class SE23_12(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ꂽ���_<ruby><rb>�s���e�t</rb><rp>(</rp><rt>�f�X�E�K��</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
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
    '''�y���z �m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���̑O��̃R�X�g1�ȉ��̃L������1���I�ԁB���̃L�����͎��̑���̃X�^���h�t�F�C�Y�ɃX�^���h���Ȃ��B
'''
    

class SE23_13(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ߏ�Ȏ�������"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 4000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́s����t�̃L�������ׂĂɁA�p���[���{1000�B
�y�i�z ����̌��̃L�������ׂĂɁA�s�W�I�t��^����B
'''
    

class SE23_14(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�Ȃ�Mob��胊�Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
�y���z �m�@�n ���̃J�[�h���t�����g�A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���̃L������1���I�сA���̃^�[�����A���x�����|1�B
'''
    

class SE23_15(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Ɏ���e��<ruby><rb>�s���e�t</rb><rp>(</rp><rt>�f�X�E�K��</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ����̃L�������ׂĂ��s�W�I�t�Ȃ�A���̃J�[�h�̃p���[���{2000�B
�y���z �m�@ ���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���̑O��̃��x��2�ȉ��́s�W�I�t�̃L������1���I�сA�T�����ɒu���B
'''
    

class SE23_16(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̃V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y�i�z ���Ȃ��̃X�g�b�N��6���ȏ�Ȃ�A���̃J�[�h�̃p���[���{500���A�\�E�����{1�B
'''
    
    
class SE23_17(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "������<ruby><rb>�h��</rb><rp>(</rp><rt>�G�X�g�b�N</rt><rp>)</rp></ruby>�g��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    

class SE23_18(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���z�̎����V�m��"
        self.color = util.Color.BLUE
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
    '''�y���z �m�@ ���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ă��x��2�ȏ�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
'''
    

class SE23_19(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ؘR����̒��V�m��"
        self.color = util.Color.BLUE
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
    '''�y�i�z ����̃^�[�����A���̂��Ȃ��̑O��̒����̘g�̃L�����ɁA�p���[���{1000�B
�y�N�z �W�� �m�@�n ���Ȃ��͎����̎R�D�̏ォ��4�����߂���A�T�����ɒu���B���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L�������w���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B���Ȃ��͎����̎�D���w���I�сA�T�����ɒu���B�w�͂����̃J�[�h�̃N���C�}�b�N�X�̖����ɓ������B
'''
    

class SE23_20(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ꎞ�I�ȋ����L���g"
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
    '''�y���z ���̃J�[�h���A�^�b�N�������A���Ȃ��͑��̎����̃J�[�h���Ɂu�V�m���v���܂ރL������1���I�сA���̃^�[�����A�p���[���{1000�B
�y���z ����̃A�^�b�N�t�F�C�Y�̎n�߂ɁA���Ȃ��͎����̎R�D�̏ォ��1�����T�����ɒu���Ă悢�B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���Ȃ��͂��̃J�[�h��O��̃L�����̂��Ȃ��g�ɓ������Ă悢�B
'''
    

class SE23_21(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ꎞ�I�ȋ����V�m��"
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
�y���z �A���R�[�� �m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n�i���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�������g�Ƀ��X�g���Ēu���j
'''
    

class SE23_22(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��������ׂ����݃V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{1000�B
�y���z �`�F���W �m�A ��D��1���T�����ɒu���A���̃J�[�h���T�����ɒu���n ���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�Ō�̈ꌂ �V�m���v��1���I�сA���̃J�[�h�������g�ɒu���B
'''
    

class SE23_23(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̉ʂăL���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��1�����āA�R�D�̏ォ���ɒu���B
�y���z ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���Ă̖��O�v������Ȃ�A���Ȃ��͎����̃N���b�N�̏ォ��1���܂ł��A�T�����ɒu���A���̃^�[�����A���̃J�[�h�̃p���[���{3000�B
�y���z �m�@�n ���̃J�[�h���t�����g�A�^�b�N���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
'''
    

class SE23_24(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Ō�̈ꌂ�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ�����w�`�F���W�x�ŕ���ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�u��̏ォ��1�����A�T�����ɒu���Ă悢�B
�y���z �m�A ��D��1���T�����ɒu���n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���e�̈�e�v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A�����4�_���[�W��^����B���̃_���[�W���L�����Z�����ꂽ���A���̑���̃^�[���̏I���܂ŁA���̃J�[�h�̃p���[���{3500�B
�y���z �o�g�����̂��̃J�[�h�����o�[�X�������A���̃J�[�h���v���o�ɂ���B
'''
    

class SE23_25(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�e�̊�b�m���V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��̑O��̃L���������Ȃ��Ȃ�A���̃J�[�h�̃p���[���{1000���A���̃J�[�h�́w�y���z�A���R�[���m��D�̃L������1���T�����ɒu���n�x�𓾂�B
'''
    

class SE23_26(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���s�̃L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̓T�C�h�A�^�b�N�ł��Ȃ��B
'''
    

class SE23_27(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�H�̎U���a�l"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ���1�������A�����̎�D��1���I�сA�T�����ɒu���B
�y���z �m���̃J�[�h���T�����ɒu���n ���̂��Ȃ��̃L���������䂩��T�����ɒu���ꂽ���A���ɂ��̃J�[�h������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃L���������̃L�����������g�Ƀ��X�g���Ēu���B
'''
    

class SE23_28(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����Ȃ肽�����T"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s���K�l�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{500�B
�y���z �m�@�n ���Ȃ��̃N���C�}�b�N�X�u��Ɂu�����Ȉ���v���u���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑��̎����̃J�[�h���Ɂu�V�m���v���܂ރL������1���I�сA���̃^�[�����A�p���[���{2000���A���̔\�͂�^����B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ���1�������Ă悢�B�x
'''
    

class SE23_29(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�키�I���L���g"
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~500�ɓ������B
'''
    

class SE23_30(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�킵�̃A�o�^�[�L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{�w�B�w�͂��Ȃ��́w�����x�����L�����̖����~500�ɓ������B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ���1�������A�����̎�D��1���I�сA�T�����ɒu���B
'''
    

class SE23_31(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���{��V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��͎����̎R�D�̏ォ��3�����A�T�����ɒu���B
�y�N�z ��������2000 ���x��1�m�@ ��D�̂��̃J�[�h���T�����ɒu���n(���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{2000)
'''
    

class SE23_32(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g���ɒ��Ӂh(�`�F�b�N�E�V�b�N�X)�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̐��ʂ̃L�����̃��x����3�ȏ�Ȃ�A���̃J�[�h�̃p���[���{3000�B
�y�N�z �m���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2�����X�g����n ���̃^�[�����A���̃J�[�h�̃p���[���{2500�B
'''
    

class SE23_33(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s���e�t(�f�X�E�K��)�Ƃ̑Λ��L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''�y���z �m�@�n ���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���Ă̖��O�v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ���1�������A���̃^�[�����A���̃J�[�h�̃p���[���{3000�B���Ȃ��̃A���R�[���X�e�b�v�̎n�߂ɁA���̃J�[�h�����X�g���Ă���Ȃ�A���Ȃ��͂��̃J�[�h���T�����ɒu���A���Ȃ��͎����̎�D�́u�����̉ʂ� �L���g�v��1���܂őI�сA���̃J�[�h�������g�ɒu���B
'''
    
    
class SE23_34(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Ă̖��O"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class SE23_35(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���e�̈�e(�t�@���g���E�o���b�g)"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class SE23_36(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����Ȉ��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
