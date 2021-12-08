import os
import subprocess
import time
#from test_vision_internal_one import runclient
#from test_vision_internal_two import XXXXXXX
#from program_2 import function_t 
while True:
        os.system("sudo clear")
        os.system("tput setaf 2")
        print("............welcome to testvision automation framework developed by VVDN.............")
        os.system("tput setaf 7")
        width = os.get_terminal_size().columns
        print("""
                                              Type "s"  ->  For Initial set up-----------
                                              Type "1"  ->  Module 1 ---->  Test_module_1
                                              Type "2"  ->  Module 2 ---->  Test_module_2
                                              Type "3"  ->  Module 3 ---->  Test_module_3
					      Type "4"  ->  Module 4 ---->  Test_module_4
                                              Type "5"  ->  Module 5 ---->  Test_module_5
                                              ....
                                              .... 
                                              ....
                                              .... Can be ADD more modules here
                                              ....
                                              ....
                                              ....
                                              Type "r"  ->  ~~~~To GENERATE RESULTS~~~~~~~~~~~~~~
                                              Type "e"  ->  ~~~~~~~~~~To EXIT ~~~~~~~~~~~~~~~~~~~\n\n""".center(width))			   
        a = input()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if a == "1":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print(".............Welcome to module 1 Test_module_1.............")
                module_name="Test_module_1"
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1  ---AUTO_TEST 1  -----: Testcase_1
Press 2  ---AUTO_TEST 2  -----: Testcase_2
Press 3  ---AUTO_TEST 3  -----: Testcase_3
Press 4  ---AUTO_TEST 4  -----: Testcase_4
Press 5  ---AUTO_TEST 5  -----: Testcase_5
...
...
...
can be ADD more testcases of Test_module_1 here
...
...
...
...
Press N  ---AUTO_TEST N  -----: Testcase_N
Press 0  ---FOR EXIT----------: Exit......
\n\n"""))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)

                if   b == 1:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module1_tc1.sh\n")
                     time.sleep(10)
                elif b == 2:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module1_tc2.sh\n")
                     time.sleep(10)
                elif b == 3:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module1_tc3.sh\n")
                     time.sleep(10)
                elif b == 4:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module1_tc4.sh\n")
                     time.sleep(10)
                elif b == 5:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module1_tc5.sh\n")
                     time.sleep(10)
                elif b == 0:
                    break
                input("Please Enter to continue....")
        

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "2":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print(".............Welcome to module2 Test_module_1.............")
                module_name="Test_module_2"
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1  ---AUTO_TEST 1  -----: Testcase_1
Press 2  ---AUTO_TEST 2  -----: Testcase_2
Press 3  ---AUTO_TEST 3  -----: Testcase_3
Press 4  ---AUTO_TEST 4  -----: Testcase_4
Press 5  ---AUTO_TEST 5  -----: Testcase_5
...
...
...
can be ADD more testcases of Test_module_2 here
...
...
...
...
Press N  ---AUTO_TEST N  -----: Testcase_N
Press 0  ---FOR EXIT----------: Exit......
\n\n"""))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)

                if   b == 1:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module2_tc1.sh\n")
                     time.sleep(10)
                elif b == 2:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module2_tc2.sh\n")
                     time.sleep(10)
                elif b == 3:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module2_tc3.sh\n")
                     time.sleep(10)
                elif b == 4:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module2_tc4.sh\n")
                     time.sleep(10)
                elif b == 5:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module2_tc5.sh\n")
                     time.sleep(10)
                elif b == 0:
                    break
                input("Please Enter to continue....")
        



# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "3":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print(".............Welcome to module3 Test_module_1.............")
                module_name="Test_module_3"
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1  ---AUTO_TEST 1  -----: Testcase_1
Press 2  ---AUTO_TEST 2  -----: Testcase_2
Press 3  ---AUTO_TEST 3  -----: Testcase_3
Press 4  ---AUTO_TEST 4  -----: Testcase_4
Press 5  ---AUTO_TEST 5  -----: Testcase_5
...
...
...
can be ADD more testcases of Test_module_3 here
...
...
...
...
Press N  ---AUTO_TEST N  -----: Testcase_N
Press 0  ---FOR EXIT----------: Exit......
\n\n"""))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)

                if   b == 1:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module3_tc1.sh\n")
                     time.sleep(10)
                elif b == 2:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module3_tc2.sh\n")
                     time.sleep(10)
                elif b == 3:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module3_tc3.sh\n")
                     time.sleep(10)
                elif b == 4:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module3_tc4.sh\n")
                     time.sleep(10)
                elif b == 5:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module3_tc5.sh\n")
                     time.sleep(10)
                elif b == 0:
                    break
                input("Please Enter to continue....")
        
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "4":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print(".............Welcome to module4 Test_module_1.............")
                module_name="Test_module_4"
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1  ---AUTO_TEST 1  -----: Testcase_1
Press 2  ---AUTO_TEST 2  -----: Testcase_2
Press 3  ---AUTO_TEST 3  -----: Testcase_3
Press 4  ---AUTO_TEST 4  -----: Testcase_4
Press 5  ---AUTO_TEST 5  -----: Testcase_5
...
...
...
can be ADD more testcases of Test_module_4 here
...
...
...
...
Press N  ---AUTO_TEST N  -----: Testcase_N
Press 0  ---FOR EXIT----------: Exit......
\n\n"""))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)

                if   b == 1:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module4_tc1.sh\n")
                     time.sleep(10)
                elif b == 2:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module4_tc2.sh\n")
                     time.sleep(10)
                elif b == 3:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module4_tc3.sh\n")
                     time.sleep(10)
                elif b == 4:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module4_tc4.sh\n")
                     time.sleep(10)
                elif b == 5:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module4_tc5.sh\n")
                     time.sleep(10)
                elif b == 0:
                    break
                input("Please Enter to continue....")
        
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "5":
            while True:
                os.system("clear")
                os.system("tput setaf 2")
                print(".............Welcome to module5 Test_module_1.............")
                module_name="Test_module_5"
                os.system("tput setaf 7")
                print()
                b = int(input("""
Press 1  ---AUTO_TEST 1  -----: Testcase_1
Press 2  ---AUTO_TEST 2  -----: Testcase_2
Press 3  ---AUTO_TEST 3  -----: Testcase_3
Press 4  ---AUTO_TEST 4  -----: Testcase_4
Press 5  ---AUTO_TEST 5  -----: Testcase_5
...
...
...
can be ADD more testcases of Test_module_5 here
...
...
...
...
Press N  ---AUTO_TEST N  -----: Testcase_N
Press 0  ---FOR EXIT----------: Exit......
\n\n"""))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)

                if   b == 1:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module5_tc1.sh\n")
                     time.sleep(10)
                elif b == 2:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module5_tc2.sh\n")
                     time.sleep(10)
                elif b == 3:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module5_tc3.sh\n")
                     time.sleep(10)
                elif b == 4:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module5_tc4.sh\n")
                     time.sleep(10)
                elif b == 5:
                     print ("AUTO_TEST",b,"in module",module_name,"is running")
                     runclient("sh sampletest_module5_tc5.sh\n")
                     time.sleep(10)
                elif b == 0:
                    break
                input("Please Enter to continue....")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "r":
            os.system("python generate_result.py")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

        elif a == "s":
            os.system("python init.py")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


        elif a == "e":
            os.system("clear")
            os.system("tput setaf 2")
            print("```````````````````````````````````````````````````````````'Thank You'```````````````````````````````````````````````````````````")
            os.system("tput setaf 7")
            print()
            exit()
        else:
            print("Not Supported any option....\n")
            input("Press Enter to Continue.....")
