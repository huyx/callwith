# -*- coding: utf-8 -*-
from callwith import CallWith


def setup_module():
    global callwith
    callwith = CallWith(3.1415926, '.2f')

format
def test_callwith__constructor():
    assert callwith.args == (3.1415926, '.2f')
    assert callwith.kwargs == {}

def test_callwith_call():
    assert callwith(format) == format(3.1415926, '.2f')
