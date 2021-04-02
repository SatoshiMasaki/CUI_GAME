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


class S47_101(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�p����錕�Z�A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
�y���z ���̃J�[�h�̃o�g�����肪�y���o�[�X�z�������A���Ȃ��̃N���C�}�b�N�X�u��Ɂu�s�⌕�t�̍Ŋ��v������A���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������3���ȏ�Ȃ�A���Ȃ��͎����̎R�D���ォ��3���܂Ō��āA�J�[�h��1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���B
'''
    

class S47_102(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g��U���A�X�i	"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���� ���̃J�[�h�̑O�̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{2000���A���̔\�͂�^����B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͂��̃L�������v���o�ɂ��Ă悢�B�x
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A���̎R�D���V���b�t������B
�y���z�m�A ��D��1���T�����ɒu���n ���̂��Ȃ��̃L�������A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�s�G�N�X�L�����o�[�t�l���N�G�X�g�v������A���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������4���ȏ�Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����́u�g��U�� �L���g�v��1���Ƃ��̃J�[�h��I�сA����ւ���B�i�J�[�h�̌����͕ς��Ȃ��j
'''
    

class S47_103(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���炬�̂ЂƎ��A�X�i"
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
    '''�y���z�m���Ȃ��̍T�����̃L������2���R�D�ɖ߂��A���̎R�D���V���b�t������n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃\�E�����{1�B
�y���z �o�g�����̂��̃J�[�h���y���o�[�X�z�������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h�̃��x����1�ȏ�Ȃ�A���Ȃ��͂��̃J�[�h���X�g�b�N�u��ɒu���Ă悢�B�i�N���C�}�b�N�X�̃��x����0�Ƃ��Ĉ����B���J�����J�[�h�͌��ɖ߂��j
'''
    def cipEffect(self, player1, _, __):
        flag = util.effectConfirm()
        if flag == 1:
            player1.MYFIELD["Waiting_Room"].showWaitingRoom()
            for _ in range(2):
                pass

    def loseBattle(self, player1, player2, selfPosition, oppositePosition):
        pass
    

class S47_104(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�r�q�Ȏn���A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 8000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z ���̃J�[�h�̐��ʂ̃L�����̃��x�������̃J�[�h�̃��x����荂���Ȃ�A���̃J�[�h�̓t�����g�A�^�b�N�ł��Ȃ��B
'''
    

class S47_106(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�čՂ蒼�t	"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�\�E�����{1�B�i���J�����J�[�h�͌��ɖ߂��j
�y���z ���肪���x���A�b�v�������A���Ȃ��̃N���C�}�b�N�X�u��Ɂu�t�F�A���B�E�_���X�v������Ȃ�A���Ȃ��͎����̎R�D���ォ��4���܂Ō��āA�s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ����A�c��̃J�[�h���T�����ɒu���B
�y�N�z�m���̃J�[�h���y���X�g�z����n ���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
'''
    

class S47_107(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŖ`�����[�t�@	"
        self.color = util.Color.GREEN
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
    '''�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��w���܂Ō��āA�J�[�h��1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����ɓ������B
�y���z�m��D�̃L������2���T�����ɒu���n ���̃J�[�h�̃o�g�����肪�y���o�[�X�z�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͂��̃o�g��������N���b�N�u��ɒu���B
'''
    

class S47_108(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŖ`�����Y�x�b�g"
        self.color = util.Color.RED
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
    '''�y�i�z ���Ȃ��̍T�����̃N���C�}�b�N�X��2���ȉ��Ȃ�A���Ȃ��̎�D�̂��̃J�[�h�̃��x�����|1�B
�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
�y���z�m��D��1���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�X�g�b�N�u��ɒu���B
'''
    

class S47_109(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŖ`���V���J"
        self.color = util.Color.RED
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��1�����āA�R�D�̏ォ�T�����ɒu���B
�y���z ���̃J�[�h���A�^�b�N�������A���̂��Ȃ��̃L������1���ȉ��Ȃ�A���Ȃ��͎����̎R�D�̏ォ��1�����A�T�����ɒu���Ă悢�B���̃J�[�h�����x��0�ȉ��̃L�����Ȃ�A���̃L���������̍D���Șg�ɒu���B
'''
    

class S47_110(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ł��グ�p�[�e�B�[�]�q"
        self.color = None
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m��D�̃N���C�}�b�N�X��1���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA��D�ɖ߂��B
�y���z ���̃J�[�h���y���o�[�X�z�������A���̃J�[�h�̃o�g������̃��x����1�ȉ��Ȃ�A���Ȃ��͂��̃L�������y���o�[�X�z���Ă悢�B
'''
    

class S47_111(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�o�����ԗ���"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 1500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����������Ȃ�A���Ȃ��͎����̃o�g�����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
�y�N�z��������1500 ���x��1�m(1) ��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{1500�j
'''
    

class S47_112(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g��U���L���g"
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
    '''�y�i�z ��D�̂��̃J�[�h���v���C����ɂ�����A���Ȃ��͎����́u�킢�̌� �L���g�v��1���I�сA�T�����ɒu���Ă悢�B����������A���̃J�[�h���R�X�g0�Ńv���C�ł���B
�y�i�z ���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������3���ȏ�Ȃ�A���̃J�[�h�̃p���[���{1500���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y���z ���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͑��̎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���X�g���A���̃L�����̂��Ȃ��g�ɓ������B�x
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B
'''
    

class S47_113(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�킢�̌�L���g"
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
    '''�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ����y�N�z���g�������A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{500�B
�y�N�z �W�� �m�@ ���Ȃ��̃L������2�����X�g����n ���Ȃ��͎����̎R�D�̏ォ��4�����߂���A�T�����ɒu���B�����̃J�[�h�̃N���C�}�b�N�X1���ɂ��A���̍s�����s���B�w���Ȃ���2���܂ň����A�����̎�D��1���I�сA�T�����ɒu���B�x
'''
    

class S47_114(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�������̖{�C�L���g	"
        self.color = util.Color.BLUE
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���̃^�[�����A���̃J�[�h�̃p���[���{2000�B�i���J�����J�[�h�͌��ɖ߂��j
�y���z ���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��3���܂ł��A���J���Ă悢�B1���ȏ���J�����Ȃ�A���Ȃ��͂����̃J�[�h�́s�A�o�^�[�t���s�l�b�g�t�̃L������1���܂őI�сA��D�ɉ����A�c��̃J�[�h���T�����ɒu���A�����̎�D��1���I�сA�T�����ɒu���B
'''
    

class S47_115(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŖ`�����C	"
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
    '''�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D���ォ��2���܂Ō��āA�R�D�̏�ɍD���ȏ��ԂŒu���B
�y���z�m(1) ���̃J�[�h����D�ɖ߂��n ���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃L������1���I�сA���̑���̃^�[���̏I���܂ŁA�p���[���{2500�B
'''
    

class S47_116(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����铵�V�m��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
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
    

class S47_117(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����ȋC���N���C��"
        self.color = util.Color.BLUE
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
    '''�y���z ���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���Ȃ����y�N�z���g�������A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
�y���z ���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���̃^�[�����A���̃J�[�h�̃p���[���{1500�B
'''
    

class S47_118(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�gDiceyCaf?�h�M���o�[�g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 0
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m(2) ��D�́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���T�����ɒu���n ���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑���́A���x��������̃��x����荂���L������1���I�сA�R�D�̉��ɒu���B
�y�N�z��������2500 ���x��1�m(1) ��D�̂��̃J�[�h���T�����ɒu���n �i���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{2500�j
'''
    

class S47_119(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�݂�ȂŖ`���V�m��	"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m(1) ��D�̃N���C�}�b�N�X��1���T�����ɒu���n ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����̃N���C�}�b�N�X��1���I�сA��D�ɖ߂��B
�y���z ���̃J�[�h���A�^�b�N�������A���̃J�[�h�̐��ʂ̃L�����̃��x����3�ȏ�Ȃ�A���̃^�[�����A���̃J�[�h�̃p���[���{�w�B�w�͂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�����̖����~1000�ɓ������B
'''
