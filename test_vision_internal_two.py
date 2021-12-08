import os
import time
p_dir=os.getcwd()
os.chdir(p_dir+"/result")
def function_t(var):
    Module_list=["firmware_upgrade", "ethernet", "system_general"]
    filename='result_of_Autotest_.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module1_TC1(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module1_tc1.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"


def Module1_TC2(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module1_tc2.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module1_TC3(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module1_tc3.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module1_TC4(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module1_tc4.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module1_TC5(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module1_tc5.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"


def Module2_TC1(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module2_tc1.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module2_TC2(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module2_tc2.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module2_TC3(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module2_tc3.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module2_TC4(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module2_tc4.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module2_TC5(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module2_tc5.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module3_TC1(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module3_tc1.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module3_TC2(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module3_tc2.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module3_TC3(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module3_tc3.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module3_TC4(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module3_tc4.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"

def Module3_TC5(var):
    import os
    #p_dir=os.getcwd()
    #os.chdir(p_dir+"/result")
    filename='result_sampletest_module3_tc5.log'
    wo_rd = str(var)
    with open(filename, 'r') as f:
        cnt=f.read()
        if wo_rd in cnt:
            return "PASS"
        else:
            return "FAIL"




