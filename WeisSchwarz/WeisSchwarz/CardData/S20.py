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


class S20_002(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�M���t�̃A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y�i�z���Ȃ��̃^�[�����A���̃J�[�h�̐��ʂ̃L�����̃��x����3�ȏ�Ȃ�A���̃J�[�h�̃p���[���{4000���A�\�E�����{1�B 
�y���z���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͂��̃L�������X�g�b�N�u��ɒu���B 
'''
    

class S20_003(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�\�t�@�ɉ������A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D����1�������J����B���̃J�[�h���s�A�o�^�[�t�̃L�����łȂ��Ȃ�N���b�N�u��ɒu���B(�����łȂ��Ȃ猳�ɖ߂�)
'''
    

class S20_004(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̏��� �A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y�i�z���̂��Ȃ��̃J�[�h���Ɂu�L���g�v���܂ރL����������Ȃ�A���̃J�[�h�̃p���[���{1000���A���̃J�[�h�́w�y���z�A���R�[���m��D�̃L������1���T�����ɒu���n�x�𓾂�B
'''
    

class S20_005(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ւ����̃A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y���z���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������A�^�b�N�������A���̃^�[�����A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_007(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�z�Ƃ������� �A�X�i"
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
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ�����u�O���ւ̕��A�v�̌��ʂŕ���ɒu���ꂽ���A���Ȃ��͎����̃N���b�N�̏ォ��1�����A�T�����ɒu���Ă悢�B 
�y���z�m�@ ��D��1���T�����ɒu���n���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��́s�A�o�^�[�t�̃L�������ׂĂɁA���̃^�[�����A�p���[���{500���A�\�E�����{1�B 
'''
    

class S20_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�V������ �A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y���z���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
'''
    

class S20_010(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���c�� �A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z���Ȃ������̃J�[�h�́w�������x���g�������A���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2���ȏ�Ȃ�A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
�y�N�z��������1000 ���x��1�m��D�̂��̃J�[�h���T�����ɒu���n(���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{1000)
'''
    

class S20_011(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�J�h�� �A�X�i"
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
    '''�y�i�z���̃J�[�h�̉��̃}�[�J�[1���ɂ��A���̃J�[�h�̃��x�����{1���A�p���[���{1500�B
�y���z���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�����A���̃J�[�h�̉��Ƀ}�[�J�[�Ƃ��Ēu���Ă悢�B
'''
    

class S20_T04(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�v���|�[�Y�̕Ԏ� �A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{1000�B
�y���z ���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�\�E�����{1�B(���J�����J�[�h�͌��ɖ߂�)
'''
    

class S20_013(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�c�� �q�[�X�N���t"
        self.color = util.Color.YELLOW
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
    '''�y���z���̃J�[�h���A�^�b�N�����Ƃ��A�N���C�}�b�N�X�u��Ɂu���Z��ł̃f���G���v������Ȃ�A���Ȃ��͑���̃R�X�g1�ȉ��̃L������1���I�сA��D�ɖ߂��A���̃^�[�����A���̃J�[�h�̓��o�[�X���Ȃ��B
'''
    

class S20_014(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����J �A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y���z�J�^�u�����R�m�c�ւ̓��c �L���g�v�m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n(���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�����R�m�c�ւ̓��c �L���g�v��1���I�сA��D�ɖ߂�)
�y�N�z�m�@�n���Ȃ��͎����́s�A�o�^�[�t�̃L������1���I�сA���̃^�[�����A�p���[���{500�B
'''
    

class S20_T01(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Ƃ��� �A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y�i�z���Ȃ��̃^�[�����A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_016(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Ď��� �N���f�B�[��"
        self.color = util.Color.YELLOW
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
    '''�y�N�z�m�@�n���Ȃ��͑���̑O��̃��x��0�ȉ��̃L������1���I�сA�X�g�b�N�u��ɒu���B
'''
    

class S20_T02(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�킢�̂͂��܂� �A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T03(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�B���ꂽ���� �q�[�X�N���t"
        self.color = util.Color.YELLOW
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
    

class S20_T05(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�n���̗����X�L�� �A�X�i"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���Ȃ��̃^�[�����A���̂��Ȃ��́s�A�o�^�[�t�̃L������2���ȏ�Ȃ�A���̃J�[�h�̃��x�����{1���A�p���[���{1500�B
'''
    

class S20_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�V������ �A�X�i"
        self.color = util.Color.YELLOW
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
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y���z���Ȃ��̃N���C�}�b�N�X���N���C�}�b�N�X�u��ɒu���ꂽ���A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B
'''
    
    
class S20_021(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�O���ւ̕��A"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_022(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g����"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_021(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�O���ւ̕��A"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_022(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g����"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_023(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "������������"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_T06(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�X�^�[�E�X�v���b�V���t"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_025(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���Z��ł̃f���G��"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    

class S20_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���@���m ���[�t�@"
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
    '''�y���z�m�@�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�X�y���r���v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃p���[���{1000���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y���z���̃J�[�h�̃o�g������Ń��x��2�ȏ�̃L���������o�[�X�������A���Ȃ��͂��̃L�������N���b�N�u��ɒu���Ă悢�B�x
'''
    

class S20_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����Ȋ肢 ���[�t�@"
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
    '''�y�i�z���Ȃ��̎R�D��5���ȉ��Ȃ�A���Ȃ��̎�D�̂��̃J�[�h�̃��x�����|1�B
�y�i�z���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L�������ׂĂɁA�p���[���{1500�B
�y�N�z�m�@ ��D�́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���T�����ɒu���n���̑���̃^�[���̏I���܂ŁA���̃J�[�h�̃p���[���{3000���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y�i�z���̃J�[�h�͑���̌��ʂɑI�΂�Ȃ��B�x
'''
    

class S20_028(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����ɂȂ�ē��� ���[�t�@"
        self.color = util.Color.GREEN
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
    '''�y���z���̃J�[�h���A�^�b�N�������A���Ȃ��͑��̎����̃L������1���I�сA���̃^�[�����A���x�����{1���A�p���[���{1000�B 
'''
    

class S20_029(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�h���C���� ���t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y���z�m�@�n���Ȃ��̃N���C�}�b�N�X�u��Ɂu�B���������z���v���u���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��̃L�������ׂĂɁA���̃^�[�����A�p���[���{1500�B
'''
    

class S20_030(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�V���t�t�̏��� ���[�t�@"
        self.color = util.Color.GREEN
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
    '''�y���z�A���R�[���m��D�̃L������1���T�����ɒu���n(���̃J�[�h�����䂩��T�����ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h�������g�Ƀ��X�g���Ēu��)
�y�N�z�m���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������2�����X�g����n���̃^�[�����A���̃J�[�h�̃p���[���{2500�B
'''
    

class S20_031(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̒��t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L������3���ȏ�Ȃ�A���̃J�[�h�́w�y���z�A���R�[���m��D�̃L������1���T�����ɒu���n�x�𓾂�B
�y���z�m�@�n���̃J�[�h���A�^�b�N�������A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃p���[���{2500�B
'''
    

class S20_032(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����Ɍ����������钼�t"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t', '�s�X�|�[�c�t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͑��̎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̃^�[�����A�p���[���{500�B
�y���z�J�^�u��؂Ȑl�̂��߂� �L���g�v�m�@�n(���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u��؂Ȑl�̂��߂� �L���g�v��1���I�сA��D�ɖ߂�)
'''
    

class S20_037(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s���w�E ���[�t�@"
        self.color = util.Color.GREEN
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
    '''�y�i�z���Ȃ��̃X�g�b�N��3���ȏ�Ȃ�A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_038(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����C���̒��t"
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
    ''''''
    

class S20_039(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�Q�Ă郊�[�t�@"
        self.color = util.Color.GREEN
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
    
    
class S20_045(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�B���������z��"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    

class S20_046(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�T������������ ���Y�x�b�g"
        self.color = util.Color.RED
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
    '''�y���z�m�@�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���߂Ă���������v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����̃L������2���܂őI�сA��D�ɖ߂��A�����̎�D��1���I�сA�T�����ɒu���A���̃^�[�����A���̃J�[�h�̃p���[���{1000�B 
'''
    

class S20_048(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�e�F���j�����郊�Y�x�b�g"
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
    '''�y���z���̃J�[�h���A�^�b�N�������A���̂��Ȃ��̃J�[�h���Ɂu�A�X�i�v���܂ރL�������ׂĂɁA���̃^�[�����A�p���[���{500�B
�y���z�J�^�u�p�[�e�B�[�̗U�� �A�X�i�v�m�@�n(���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�p�[�e�B�[�̗U�� �A�X�i�v��1���I�сA��D�ɖ߂�)
'''
    

class S20_049(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�t�����[�K�[�f���t�̃V���J"
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
    '''�y���z�m�@�n���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�s�v�l�E�}�̉ԁt�v��1���I�сA��D�ɖ߂��B
'''
    

class S20_050(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�E�l������ ���Y�x�b�g"
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
    '''�y���z���̃J�[�h�����o�[�X�������A���̃J�[�h�̃o�g������̃��x����0�ȉ��Ȃ�A���Ȃ��͂��̃L���������o�[�X���Ă悢�B
�y���z�����m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͑��̎����́s����t�̃L������1���I�сA���̃^�[�����A�p���[���{2500�B
'''
    

class S20_051(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�܂������ȐM�� �V���J"
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
    '''�y�N�z�W�� �m�@ ���Ȃ��̃L������2�����X�g����n���Ȃ��͎����̎R�D�̏ォ��4�����߂���A�T�����ɒu���B�����̃J�[�h�̃N���C�}�b�N�X1���ɂ��A���Ȃ��͎����̍T�����́A�s�A�o�^�[�t���s�l�b�g�t���s�g�����t�̃L������1���܂őI�сA��D�ɖ߂��B
'''
    

class S20_052(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ւ����̃��Y�x�b�g"
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
    '''�y�i�z���̂��Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t�̃L����1���ɂ��A���̃J�[�h�̃p���[���{500�B
'''
    

class S20_053(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ӂ̍��� ���Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���� ���̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{�w�B�w�͂��̃L�����̃��x���~500�ɓ������B
�y���z�m�A�n���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����̃L������1���I�сA��D�ɖ߂��B
'''
    

class S20_054(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�g���� �s�i"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�g�����t', '�s���t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̂��Ȃ��̃J�[�h���Ɂu�V���J�v���܂ރL�������ׂĂɁA�p���[���{500�B
�y���z�m���̃J�[�h���T�����ɒu���n���̂��Ȃ��̃J�[�h���Ɂu�V���J�v���܂ރL���������䂩��T�����ɒu���ꂽ���A���ɂ��̃J�[�h������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃L���������̃L�����������g�Ƀ��X�g���Ēu���B
'''
    

class S20_055(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�f�[�g�C�� �V���J"
        self.color = util.Color.RED
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
    '''�y���z���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��͎����̎R�D����1�������J����B���̃J�[�h���N���C�}�b�N�X�Ȃ�A���̃J�[�h�����X�g����B(���J�����J�[�h�͌��ɖ߂�)
'''
    

class S20_056(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���C�X�̎g���� ���Y�x�b�g"
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
    '''�y���z�m�@�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�C�Â����{���̋C�����v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��́s����t�̃L�������ׂĂɁA���̃^�[�����A�p���[���{2500�B
'''
    

class S20_057(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�`���̂͂��܂� �V���J"
        self.color = util.Color.RED
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
    '''�y���z�m�@�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���߂Ă̖`���v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�A����������A���Ȃ��͎����̍T�����́u�g���� �s�i�v��1���I�сA����̍D���Șg�Ƀ��X�g���Ēu���A���̃^�[�����A���̃J�[�h�̃p���[���{3500�B
'''
    

class S20_058(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�_�K�[�g�� �V���J"
        self.color = util.Color.RED
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
    

class S20_59(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���킢�����Y �V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���N���C�}�b�N�X�Ȃ�A���Ȃ��͑��̎����̃L������1���I�сA�T�����ɒu���B(���J�����J�[�h�͌��ɖ߂�)
'''
    

class S20_060(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�O�����ȏΊ� ���Y�x�b�g"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���N���C�}�b�N�X�Ȃ�A���̃J�[�h�����X�g����B(���J�����J�[�h�͌��ɖ߂�)
'''
    

class S20_061(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�b�艮�̃��Y�x�b�g"
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
    '''�y�i�z�������̃J�[�h�̑O�̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
�y���z�m���̃J�[�h�����X�g����n���Ȃ����w�����x���g�������A���̃J�[�h���X�^���h���Ă���Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1500�B
'''
    

class S20_062(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�r�[�X�g�e�C�}�[�t�V���J"
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
    '''�y���z�J�^�u�g���� �s�i�v�m�@�n(���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u�g���� �s�i�v��1���I�сA��D�ɖ߂�)
'''
    

class S20_063(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�A�C�h���I���� �V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_064(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�p�[�e�B�[�̒E�� �V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�N�z��������1500 ���x��1�m��D�̂��̃J�[�h���T�����ɒu���n(���Ȃ��̓t�����g�A�^�b�N����Ă��鎩���̃L������1���I�сA���̃^�[�����A�p���[���{1500)
'''
    

class S20_066(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���n�̃V���J"
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
    '''�y�i�z�O��̒����̘g�ɂ��̃J�[�h������Ȃ�A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_067(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�w�����������Y�x�b�g"
        self.color = util.Color.RED
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
    '''�y���z�`�F���W�m�A ��D��1���T�����ɒu���A���̃J�[�h���T�����ɒu���n���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T������ �u�O�����ȏΊ� ���Y�x�b�g�v��1���I�сA���̃J�[�h�������g�ɒu���B
'''
    

class S20_068(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�n�v�j���O �V���J"
        self.color = util.Color.RED
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
    ''''''
    

class S20_069(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ӂ̋C���� �V���J"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�N�z�m���Ȃ��́A�s�A�o�^�[�t���s�l�b�g�t���s�g�����t�̃L������2�����X�g����n���̃^�[�����A���̃J�[�h�̃p���[���{2500�B
'''
    
    
class S20_070(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�v�l�E�}�̉ԁt"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_071(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����̓��A"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_072(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���߂Ă���������"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_073(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���߂Ă̖`��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_074(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�i�̑h��"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_075(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�C�Â����{���̋C����"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    

class S20_077(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s���̌��m�t�L���g"
        self.color = util.Color.BLUE
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
    '''�y���z�m�B ��D��1���N���b�N�u��ɒu���n���Ȃ��̃N���C�}�b�N�X�u��Ɂu�s�񓁗��t�̎g����v���u���ꂽ���A�O��ɂ��̃J�[�h������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃^�[�����A���̃J�[�h�̃p���[���{3500���A���̃J�[�h�͎��̔\�͂𓾂�B�w�y���z���̔\�͂�1�^�[���ɂ�1��܂Ŕ�������B���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͂��̃J�[�h���X�^���h���Ă悢�B�x
�y���z���̃J�[�h���A�^�b�N�������A���Ȃ��͎����̎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A��D�ɉ�����B(�����łȂ��Ȃ猳�ɖ߂�)
'''
    

class S20_78(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���g�� �N���C��"
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
    '''�y���z���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��͎R�D�̏ォ��1�������J����B���̃J�[�h���s�A�o�^�[�t���s�l�b�g�t�̃L�����Ȃ�A���Ȃ��͎����̃L������1���I�сA���̃^�[�����A�p���[���{1000�B���J�����J�[�h�͌��ɖ߂�
�y�N�z�W���m�@�n���Ȃ��͎����̎R�D����4�����߂���A�T�����ɒu���B�����̃J�[�h�̃N���C�}�b�N�X1���ɂ��A���Ȃ��͎����́A�s�A�o�^�[�t���s�l�b�g�t�̃L������1���I�сA���̑���^�[���̏I���܂ŁA�p���[���{1000�B
'''
    

class S20_079(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���ɐg��u���L���g"
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
    '''�y���z�m�@ ��D��1���T�����ɒu���n���̃J�[�h����D���畑��ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̎R�D�����ās�A�o�^�[�t�̃L������1���܂őI��ő���Ɍ����A��D�ɉ�����B���̎R�D���V���b�t������B
'''
    

class S20_080(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "��؂Ȑl�̂��߂� �L���g"
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
    '''�y���z�m�@�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu���E�̏I���v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ���1�������B
�y���z�����m���Ȃ��̎R�D�̏ォ��1�����N���b�N�u��ɒu���n���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̑���̃^�[���̏I���܂ŁA���̃J�[�h�̃p���[���{2500�B
'''
    

class S20_081(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�l�H�m�\ ���C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y���z�m�A�n���̃J�[�h���A�^�b�N�������A�N���C�}�b�N�X�u��Ɂu�ˑR�̕ʂ�v������Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ���2���܂ň����B
'''
    

class S20_082(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���j�[�N�X�L���̔��� �L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̃J�[�h�̉��̃}�[�J�[1���ɂ��A���̃J�[�h�̃��x�����{1���A�p���[���{1500�B
�y���z���̃J�[�h�̃o�g�����肪���o�[�X�������A���Ȃ��͎����̎R�D�̏ォ��1�����A���̃J�[�h�̉��Ƀ}�[�J�[�Ƃ��Ēu���Ă悢�B
�y���z�m���̃J�[�h�̉��̃}�[�J�[���ׂĂ��T�����ɒu���n���̂��Ȃ��̃L�������A�^�b�N�������A���̃J�[�h�̉��̃}�[�J�[��5���ȏ�Ȃ�A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���̃J�[�h���X�^���h���A���̃^�[�����A���̃J�[�h�̃p���[���{6000�B
'''
    

class S20_083(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�\���v���C���[ �L���g"
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
    '''�y�i�z���̂��Ȃ��̃L���������Ȃ��Ȃ�A���̃J�[�h�̃��x�����{1���A�p���[���{1500�B
'''
    

class S20_084(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����̍��L�c �T�`"
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
    '''�y�i�z����̃^�[�����A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_085(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����J �L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''�y�i�z���̂��Ȃ��̃J�[�h���Ɂu�A�X�i�v���܂ރL�������ׂĂɁA�p���[���{500�B
�y�i�z����̃^�[�����A���̂��Ȃ��̃L�������ׂĂɁA�p���[���{500�B
'''
    

class S20_086(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�i��߂���L���g"
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
    '''�y�i�z���̂��Ȃ��̃J�[�h���Ɂu�A�X�i�v���܂ރL����������Ȃ�A���̃J�[�h�̃p���[���{1000���A���̃J�[�h�́w�y���z�A���R�[���m��D�̃L������1���T�����ɒu���n�x�𓾂�B
'''
    

class S20_087(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���肰�Ȃ��D���� �L���g"
        self.color = util.Color.BLUE
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
    '''�y���z�`�F���W�m�A ��D��1���T�����ɒu���A���̃J�[�h���T�����ɒu���n���Ȃ��̃N���C�}�b�N�X�t�F�C�Y�̎n�߂ɁA���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T������ �u���j�[�N�X�L���̔��� �L���g�v��1���I�сA���̃J�[�h�������g�ɒu���B
'''
    

class S20_089(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���₩�ȓ��� �L���g"
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
    '''�y���z�J�^�u���ւ����̃A�X�i�v�m�@�n(���̃J�[�h���v���C����ĕ���ɒu���ꂽ���A���Ȃ��̓R�X�g�𕥂��Ă悢�B����������A���Ȃ��͎����̍T�����́u���ւ����̃A�X�i�v��1���I�сA��D�ɖ߂�)
'''
    

class S20_T07(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�킢�̂͂��܂� �L���g"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T09(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���炵������ ���C"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('�s�l�b�g�t',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T12(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�܏\�ܑw�̐�R �L���g"
        self.color = util.Color.BLUE
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
    '''�y�N�z��������3000 ���x��2�m�@ ��D�̂��̃J�[�h���T�����ɒu���n(���Ȃ��͎����̃t�����g�A�^�b�N����Ă���L������1���I�сA���̃^�[�����A�p���[���{3000)
'''
    

class S20_T10(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�����R�m�c�ւ̓��c �L���g"
        self.color = util.Color.BLUE
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
    '''�y�i�z����̃^�[�����A���̃J�[�h�̃p���[���{1000�B
'''
    

class S20_T11(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "����m �G�M��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('�s�A�o�^�[�t', '�s����t')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    
    
class S20_096(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�v���|�[�Y"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 2
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_097(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���肪�Ƃ��A����Ȃ�"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_T14(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�s�񓁗��t�̎g����"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_T13(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "���E�̏I��"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
    
    
class S20_100(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "�ˑR�̕ʂ�"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('�F',)
        self.useCardLimit = None
    ''''''
