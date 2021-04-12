# -*- coding:utf-8 -*-

class BaseballGame():
    game_started = False
    player_won = False

    def __init__(cls):
        print('** 숫자야구게임! **')
        commnad_input = str(input('게임을 시작하시겠습니까? (Y/n)'))
        if commnad_input in ['', 'y', 'Y', 'yes', 'Yes', 'YES']:
            cls.game_started = True
            cls.game_init()
            print('랜덤으로 {}자리 숫자를 생성하였습니다.'.format(cls.level))
            while cls.game_started and not cls.player_won and cls.life:
                cls.attemp_to_solve()
            
            if cls.player_won:
                print('축하합니다! 게임에서 승리하셨습니다')
            else:
                print('게임에서 패배하셨습니다, 다시 도전해보세요! 정답: [{}]'.format(', '.join(list(cls.question))))
        else:
            print('다음에 뵙겠습니다.')


    def game_init(cls, level = 3):
        cls.level = level
        cls.life = 9
        cls.question = cls.question_generator()
    

    def question_generator(cls):
        from random import randrange
        question_nums = []
        num_range = list(range(9))
        while len(question_nums) != cls.level:
            random_index = randrange(0, len(num_range))
            target = num_range.pop(random_index)
            question_nums.append(str(target))
        
        return ''.join(question_nums)


    def attemp_to_solve(cls):
        user_input = input('{}번의 기회가 남았습니다. 정답은 무엇일까요? :'.format(cls.life))
        user_input = user_input.strip().replace(' ', '').replace(',', '')
        valid_input = cls.input_validator(user_input)
        if valid_input.get('is_valid'):
            result = cls.check_answer(user_input)

            if result.get('is_won'):
                cls.player_won = True
                cls.game_started = False
            else:
                cls.life = cls.life - 1
                print('틀렸습니다. 결과는 ' + result.get('message'))
        else:
            print('입력값이 올바르지 않습니다. ' + valid_input.get('message'))
                

    def check_answer(cls, user_answer):
        result_strike = 0
        result_ball = 0
        correct_answer = cls.question
        for index, input_num in enumerate(user_answer):
            if correct_answer[index] == input_num:
                result_strike = result_strike + 1
            elif input_num in correct_answer:
                result_ball = result_ball + 1

        if result_strike == 3:
            return {'is_won': True}
        
        if result_strike or result_ball:
            result = ''
            if result_strike:
                result = result + '{} strike!'.format(result_strike)
            if result_ball:
                result = result + ' {} ball!'.format(result_ball)
            
            return {'is_won': False, 'message': result}
        else:
            return {'is_won': False, 'message': 'OUT'}


    def input_validator(cls, user_input):
        if len(user_input) != cls.level:
            return {'is_valid': False, 'message': '{}의 자릿수를 입력하여야 합니다.'.format(cls.level)}

        for index, input_num in enumerate(user_input):
            try:
                int(input_num)
            except:
                return {'is_valid': False, 'message': '숫자가 아닌 값이 포함되어있습니다.'}

            listed_user_inputs = list(user_input)
            listed_user_inputs.pop(index)
            if input_num in listed_user_inputs:
                return {'is_valid': False, 'message': '같은 값의 숫자가 포함되어 있습니다.'}

        return {'is_valid': True, 'message': ''}

BaseballGame()
