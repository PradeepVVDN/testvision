*** Settings ***
Library        test_vision_internal_two.py
Library        DateTime
Library        BuiltIn

*** Test Cases ***


Module1_TC1

        [Tags]    Module1_TC1
	${value}=           test_vision_internal_two.Module1_TC1    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}
        
Module1_TC2

        [Tags]    Module1_TC2
	${value}=           test_vision_internal_two.Module1_TC2    FAIL
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module1_TC3

        [Tags]    Module1_TC3
	${value}=           test_vision_internal_two.Module1_TC3    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}   

Module1_TC4

        [Tags]    Module1_TC4
	${value}=           test_vision_internal_two.Module1_TC4    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module1_TC5

        [Tags]    Module1_TC5
	${value}=           test_vision_internal_two.Module1_TC5    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}


Module2_TC1

        [Tags]    Module2_TC1
	${value}=           test_vision_internal_two.Module2_TC1    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module2_TC2

        [Tags]    Module2_TC2
	${value}=           test_vision_internal_two.Module2_TC2    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module2_TC3

        [Tags]    Module2_TC3
	${value}=           test_vision_internal_two.Module2_TC3    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module2_TC4

        [Tags]    Module2_TC4
	${value}=           test_vision_internal_two.Module2_TC4    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module2_TC5

        [Tags]    Module2_TC5
	${value}=           test_vision_internal_two.Module2_TC5    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}


Module3_TC1

        [Tags]    Module3_TC1
	${value}=           test_vision_internal_two.Module3_TC1    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module3_TC2

        [Tags]    Module2_TC2
	${value}=           test_vision_internal_two.Module2_TC2    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module3_TC3

        [Tags]    Module3_TC3
	${value}=           test_vision_internal_two.Module3_TC3    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module3_TC4

        [Tags]    Module3_TC4
	${value}=           test_vision_internal_two.Module3_TC4    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}

Module3_TC5

        [Tags]    Module3_TC5
	${value}=           test_vision_internal_two.Module3_TC5    PASS
	SHOULD BE EQUAL     ${value}                                PASS
        ${d1}=    get time
        Log To Console   ${d1}
        ${d1}=    get time
        Log To Console   ${d1}



