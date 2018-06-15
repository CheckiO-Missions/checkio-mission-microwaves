init_code = """
if not "MicrowaveBase" in USER_GLOBAL:
    raise NotImplementedError("Where is 'MicrowaveBase'?")
MicrowaveBase = USER_GLOBAL['MicrowaveBase']

if not "Microwave1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave1'?")
Microwave1 = USER_GLOBAL['Microwave1']

if not "Microwave2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave2'?")
Microwave2 = USER_GLOBAL['Microwave2']

if not "Microwave3" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Microwave3'?")
Microwave3 = USER_GLOBAL['Microwave3']

if not "RemoteControl" in USER_GLOBAL:
    raise NotImplementedError("Where is 'RemoteControl'?")
RemoteControl = USER_GLOBAL['RemoteControl']

if not issubclass(Microwave1, MicrowaveBase):
    raise Warning('Microwave1 should be the subclass of MicrowaveBase')

if not issubclass(Microwave2, MicrowaveBase):
    raise Warning('Microwave2 should be the subclass of MicrowaveBase')

if not issubclass(Microwave3, MicrowaveBase):
    raise Warning('Microwave3 should be the subclass of MicrowaveBase')
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
        prepare_test(middle_code='''microwave_1 = Microwave1()
rc_1 = RemoteControl(microwave_1)
rc_1.set_time("05:33")
rc_1.del_time("30s")
rc_1.del_time("2m")''',
                     test="rc_1.show_time()",
                     answer="_3:03")
    ],
    "2. Second": [
        prepare_test(middle_code='''microwave_2 = Microwave2()
rc_2 = RemoteControl(microwave_2)
rc_2.set_time("89:00")
rc_2.add_time("90s")
rc_2.add_time("20m")''',
                     test="rc_2.show_time()",
                     answer="90:0_")
    ],
    "3. Third": [
        prepare_test(middle_code='''microwave_3 = Microwave3()
rc_3 = RemoteControl(microwave_3)
rc_3.del_time("90s")
rc_3.del_time("6m")
rc_3.add_time("2m")''',
                     test="rc_3.show_time()",
                     answer="02:00")
    ],
    "4. First_2": [
        prepare_test(middle_code='''microwave_1 = Microwave1()
rc_6 = RemoteControl(microwave_1)
rc_6.set_time("02:20")
rc_6.del_time("0s")
rc_6.add_time("40s")''',
                     test="rc_6.show_time()",
                     answer="_3:00")
    ],
    "5. Second_2": [
        prepare_test(middle_code='''microwave_2 = Microwave2()
rc_7 = RemoteControl(microwave_2)
rc_7.set_time("15:00")
rc_7.add_time("90s")
rc_7.add_time("12m")''',
                     test="rc_7.show_time()",
                     answer="28:3_")
    ],
    "6. Third_2": [
        prepare_test(middle_code='''microwave_3 = Microwave3()
rc_8 = RemoteControl(microwave_3)
rc_8.add_time("10s")
rc_8.add_time("15s")
rc_8.add_time("12m")''',
                     test="rc_8.show_time()",
                     answer="12:25")
    ]

}
