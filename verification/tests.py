init_code = """
if not "Microwave1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave1'?")

Microwave1 = USER_GLOBAL['Microwave1']

if not "Microwave2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave2'?")

Microwave2 = USER_GLOBAL['Microwave2']

if not "Microwave3" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave3'?")

Microwave3 = USER_GLOBAL['Microwave3']

if not "Microwave4" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave4'?")

Microwave4 = USER_GLOBAL['Microwave4']

if not "Microwave5" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave5'?")

Microwave5 = USER_GLOBAL['Microwave5']

if not "RemoteControl" in USER_GLOBAL:
    raise NotImplementedError("Where is 'RemoteControl'?")

RemoteControl = USER_GLOBAL['RemoteControl']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First": [
        prepare_test(middle_code='''rc_1 = RemoteControl("microwave_1")
rc_1.set_time("05:33")
rc_1.del_time("-30s")
rc_1.del_time("-2m")''',
                     test="rc_1.show_time()",
                     answer="_3:03")
    ],
    "2. Second": [
        prepare_test(middle_code='''rc_2 = RemoteControl("microwave_2")
rc_2.add_time("89:00")
rc_2.add_time("+90s")
rc_2.add_time("+20m")''',
                     test="rc_2.show_time()",
                     answer="9_:00")
    ],
    "3. Third": [
        prepare_test(middle_code='''rc_3 = RemoteControl("microwave_3")
rc_3.del_time("-90s")
rc_3.del_time("-6m")
rc_3.add_time("+2m")''',
                     test="rc_3.show_time()",
                     answer="02:_0")
    ],
    "4. Fourth": [
        prepare_test(middle_code='''rc_4 = RemoteControl("microwave_4")
rc_4.add_time("+60s")
rc_4.add_time("+12m")
rc_4.add_time("+2m")
rc_4.set_time("06:12")''',
                     test="rc_4.show_time()",
                     answer="06:1_")
    ],
    "5. Fifth": [
        prepare_test(middle_code='''rc_5 = RemoteControl("microwave_5")
rc_5.add_time("+90s")
rc_5.add_time("+180s")
rc_5.add_time("+2m")''',
                     test="rc_5.show_time()",
                     answer="06:30")
    ],
    "6. First_2": [
        prepare_test(middle_code='''rc_6 = RemoteControl("microwave_1")
rc_6.set_time("02:20")
rc_6.del_time("-0s")
rc_6.add_time("+40s")''',
                     test="rc_6.show_time()",
                     answer="_3:00")
    ],
    "7. Second_2": [
        prepare_test(middle_code='''rc_7 = RemoteControlM2("microwave_2")
rc_7.add_time("15:00")
rc_7.add_time("+90s")
rc_7.add_time("+12m")''',
                     test="rc_7.show_time()",
                     answer="2_:30")
    ],
    "8. Third_2": [
        prepare_test(middle_code='''rc_8 = RemoteControl("microwave_3")
rc_8.add_time("+10s")
rc_8.add_time("+15s")
rc_8.add_time("+12m")''',
                     test="rc_8.show_time()",
                     answer="12:_5")
    ],
    "9. Fourth_2": [
        prepare_test(middle_code='''rc_9 = RemoteControl("microwave_4")
rc_9.add_time("+0s")
rc_9.add_time("+1m")
rc_9.add_time("+2m")
rc_9.set_time("42:42")''',
                     test="rc_9.show_time()",
                     answer="42:4_")
    ],
    "10. Fifth_2": [
        prepare_test(middle_code='''rc_10 = RemoteControl("microwave_5")
rc_10.add_time("+10s")
rc_10.add_time("+180s")
rc_10.add_time("+6m")''',
                     test="rc_10.show_time()",
                     answer="09:10")
    ]

}
