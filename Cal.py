from psutil import sensors_battery
from sympy import symbols,solve,Eq
import os
import random
from functools import reduce
import math
import pyttsx3
import threading
from Thread import sub_thread

__all__ = ['swamtech','main','coreFunc']
__main_f_ = ['sin','cos','tan','log','Dist','prime','factor','angleSlope','slope','root','ptriplet','!factorial','deg','rad','ln','gcd','lineq','+','-','/','^^','*','quad_eq','sqsum','cusum','sumof','sumlog','sublog','multlog','divlog','powlg','cosec','sec','cot']
voice_engine = pyttsx3.init()
speech_engine_rate = voice_engine.setProperty('rate', 175)
man = voice_engine.getProperty('voices')
voice = voice_engine.setProperty('voice',man[2].id)
intro = "SWAMTECH CONSOLE CALCULATOR version 1.1"
def swamtech():
    p = sensors_battery()
    print("\n(x+-=/) \tSWAMTECH_CONSOLE_CALCULATOR \t(x+-=/)",sep=None)
    print("""
                                                                                            Battery :- {} %
                                                                                            Plugged In :- {}
         __________________________________________________________________________________________
        |                                                                                          |
        |   //////   //  //  //     */\*     ||\    /|| ||||||||||  //////    ////////  ||    ||   |
        |   ||       //  //  //    */  \*    || \  / ||     ||      //        //        ||    ||   |
        |   //////   //  //  //   */====\*   ||  \/  ||     ||      //////    //        ||====||   |
        |       ||   //  //  //   ||    ||   ||      ||     ||      //        //        ||    ||   |
        |   //////   ////////     ||    ||   ||      ||     ||      //////    ////////  ||    ||   |
        |                                                                                          |
        |____________________________________________________________________SYSTEMS_______________|
        |__________________________________________________________________________________________|
            """.format(p.percent,p.power_plugged))
def coreFunc():
    for i in __main_f_:
        print(i)
def main():
    while True:
            mainput = (input("Calci ::> "))
            if 'sin' in mainput:
                try:
                    s = mainput.replace('sin','')
                    raddeg = math.radians(float(s))
                    result = (math.sin(raddeg))
                    print((result))

                except ValueError:
                    pass

            if 'cos' in mainput:
                try:
                    s = mainput.replace('cos','')
                    raddeg = math.radians(float(s))
                    result = math.cos(raddeg)
                    print((result))

                except ValueError:
                    pass

            if 'tan' in mainput:
                try:
                    s = mainput.replace('tan','')
                    raddeg = math.radians(float(s))
                    result = math.tan(float(raddeg))
                    print(result)

                except ValueError:
                    pass
                except ZeroDivisionError:
                    print('Infinty ( oo )')

            if 'log' in mainput:
                try:
                    s = mainput.replace('log','')
                    result = (math.log10(float(s)))
                    print(math.fabs(result))
                except ValueError:
                    if '-' in mainput:
                        print("Log ::: Not for Negative numbers")
                    else:
                        pass

            if '!' in mainput:
                try:
                    s = mainput.replace('!','')
                    result = (math.factorial(float(s)))
                    print(result)
                except ValueError:
                    if '-' in mainput:
                        print("Factorial ::: Not for negative values ")
                    else:
                        pass
                except OverflowError:
                    pass

            if 'deg' in mainput:
                try:
                    s = mainput.replace('deg','')
                    result = (math.degrees(float(s)))
                    print(math.fabs(result),"rad")
                except ValueError:
                    pass

            if 'rad' in mainput:
                try:
                    s = mainput.replace('rad','')
                    result = math.radians(float(s))
                    print(math.fabs(result),"deg")
                except ValueError:
                    pass

            if 'ln' in mainput:
                try:
                    s = mainput.replace('ln','')
                    result = math.log(float(s))
                    print(math.fabs(result))
                except ValueError:
                    pass


            if 'gcd' in mainput:
                intlist = []
                try:
                    s = mainput.replace('gcd','').split(',')
                    for i in s:
                        d = int(i)
                        intlist.append(d)
                    no1,no2 = intlist
                    print(math.gcd(no1,no2))
                except ValueError:
                    pass

            if '+' in mainput:
                intlist = []
                try:
                    s = mainput.replace('+',' ').split(' ')
                    for i in s:
                        d = float(i)
                        intlist.append(d)
                    print(math.fsum(intlist))
                except ValueError:
                    pass

            if '-' in mainput:
                intlist = []
                try:
                    s = mainput.replace('-',' ').split(' ')
                    for i in s:
                        d = float(i)
                        intlist.append(d)
                    print(reduce(lambda x,y:x-y,intlist))
                except ValueError:
                    pass

            if '*' in mainput:
                intlist = []
                try:
                    s = mainput.replace('*',' ').split(' ')
                    for i in s:
                        d = float(i)
                        intlist.append(d)
                    print(reduce(lambda x,y:x*y,intlist))
                except ValueError:
                    print("Special Characters not Permitted")

            if '/' in mainput:
                intlist = []
                try:
                    s = mainput.replace('/',' ').split(' ')
                    for i in s:
                        d = float(i)
                        intlist.append(d)
                    print(reduce(lambda x,y:x/y,intlist))
                except ValueError:
                    pass
                except ZeroDivisionError:
                    print("Infinity ( oo )")

            if 'Dist'in mainput:
                xlist = []
                ylist = []
                s = mainput.replace('Dist','').split(':')
                x1x2 = s[0].replace(' ','').split(',')
                y1y2 = s[1].split(',')
                for i in x1x2:
                    xlist.append(int(i))
                for o in y1y2:
                    ylist.append(int(o))
                x1 = xlist[0]
                x2 = xlist[1]
                y1 = ylist[0]
                y2 = ylist[1]
                DISTANCE = math.sqrt((x2-x1)**2+(y2-y1)**2)
                print(DISTANCE)

            if 'slope' in mainput:
                xlist = []
                ylist = []
                s = mainput.replace('slope','').split(':')
                x1x2 = s[0].replace(' ','').split(',')
                y1y2 = s[1].split(',')
                for i in x1x2:
                    xlist.append(int(i))
                for o in y1y2:
                    ylist.append(int(o))
                x1 = xlist[0]
                x2 = xlist[1]
                y1 = ylist[0]
                y2 = ylist[1]
                SLOPE = y2-y1/x2-x1
                print(SLOPE)

            if 'angleSlope' in mainput:
                try:
                    s = mainput.replace('angleSlope','').split(':')
                    s1 = s[0].replace(' ','')
                    theta = int(s1)
                    rad = math.radians(theta)
                    slope = math.tan(rad)
                    print(slope)
                except:
                    pass

            if 'root' in mainput:
                try:
                    s = mainput.replace('root ','')
                    root_result = math.sqrt(float(s))
                    print(root_result)
                except:
                    pass

            if '^^' in mainput:
                intlist = []
                try:
                    s = mainput.replace('^^',' ').split(' ')
                    for i in s:
                        d = float(i)
                        intlist.append(d)
                    print(reduce(lambda x,y:x**y,intlist))
                except ValueError:
                    pass
                except OverflowError:
                    print("Size too big")

            if mainput == "exit":
               break

            if mainput == 'help':
                coreFunc()

            if 'lineq' in mainput:
                try:
                        s = mainput.replace('lineq','').split(' ')
                        x,y = symbols('x y')
                        eqsorted = s[1].split('=')
                        if 'x'in mainput:
                            eqmsorted = eqsorted[0].split('x')
                            if eqmsorted[0]=='':
                                expr = Eq((x)+int(eqmsorted[1]),int(eqsorted[1]))
                            if eqmsorted[0] is not '':
                                expr = Eq(x*int(eqmsorted[0])+int(eqmsorted[1]),int(eqsorted[1]))
                            sol = solve(expr)
                            if len(sol) ==1:
                                print('x = '+str(sol[0]))
                            else:
                                for i in sol:
                                    print('x = ',str(i))
                        if 'y'in mainput:
                            eqmsorted = eqsorted[0].split('y')
                            if eqmsorted[0]=='':
                                expr = Eq((y)+int(eqmsorted[1]),int(eqsorted[1]))
                            if eqmsorted[0] is not '':
                                expr = Eq(x*int(eqmsorted[0])+int(eqmsorted[1]),int(eqsorted[1]))
                            sol = solve(expr)
                            if len(sol) ==1:
                                print('y = '+str(sol[0]))
                            else:
                                for i in sol:
                                    print('y = ',str(i))
                except ValueError:
                    print("Enter in the form ::: \n +-ax +- b= +-c\na,b = coeffcient ,x = variable,c = value")
                except IndexError:
                    print("Enter in the form ::: \n +-ax +- b= +-c\na,b = coeffcient ,x = variable,c = value")

            if 'sumof' in mainput: # Sum of natural no. from 1 to n
                intlist = []
                s = mainput.replace('sumof','').split('-')
                for i in s:
                    intlist.append(int(i))
                result = intlist[1]*(intlist[1]+1)/2
                print(result)

            if 'quad_eq' in mainput:
                try:
                    s = mainput.replace('quad_eq','').split(' ')
                    eqsorted = s[1].split('x^2')
                    eqmsorted = eqsorted[1].split('x')
                    a = int(eqsorted[0])
                    ra = 2*(a)
                    b = int(eqmsorted[0])
                    c = int(eqmsorted[1])
                    discriminant = (b**2)-(4*a*c)
                    alpha = (-b +math.sqrt(discriminant))
                    beta  = (-b - math.sqrt(discriminant))
                    ralpha = alpha/ra
                    rbeta = beta/ra
                    print("x = {} OR x = {}".format(math.fabs(ralpha),math.fabs(rbeta)))
                except ValueError:
                    pass

            if 'sqsum' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('sqsum','').split('-')
                    for i in s:
                        intlist.append(int(i))
                    n = intlist[1]
                    result = n*(n+1)*((2*n)+1)/6
                    print(result)
                except ValueError:
                    pass
                except OverflowError:
                    print("Very Large No.")

            if 'prime' in mainput:
                try:
                    s = mainput.replace('prime','')
                    num = int(s[1])
                    for i in range(2,num):
                        if (num%i) ==0:
                            print("False")
                            break
                        else:
                            print("True")
                except ValueError:
                    pass
                except IndexError:
                    pass

            if 'factor' in mainput:
                factors = []
                s = mainput.replace('factor','').split(' ')
                num = int(s[1])
                for i in range(1,num+1):
                    if (num%i) == 0:
                        factors.append(i)
                print(factors)

            if 'cusum'in mainput:
                try:
                    intlist = []
                    s = mainput.replace('cusum','').split('-')
                    for i in s:
                        intlist.append(int(i))
                    n = intlist[1]
                    result = n**2*(n+1)**2/4
                    print(result)
                except ValueError:
                    pass
                except OverflowError:
                    print("Very Large No.")

            if 'sumlg' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('sumlg','').split(' ')
                    lisst = s[1].split('+')
                    for i in lisst:
                        intlist.append(float(i))
                    print(reduce(lambda x,y:math.log10(x)+math.log10(y),intlist))
                except ValueError:
                    pass

            if 'sublg' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('sublg','').split(' ')
                    lisst = s[1].split('-')
                    for i in lisst:
                        intlist.append(float(i))
                    print(reduce(lambda x,y:math.log10(x) - math.log10(y),intlist))
                except ValueError:
                    pass

            if 'multlg' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('multlg','').split(' ')
                    lisst = s[1].split('*')
                    for i in lisst:
                        intlist.append(float(i))
                    print(reduce(lambda x,y:math.log10(x)+math.log10(y),intlist))
                except ValueError:
                    pass

            if 'divlg' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('divlg','').split(' ')
                    lisst = s[1].split('/')
                    for i in lisst:
                        intlist.append(float(i))
                    print(reduce(lambda x,y:math.log10(x) - math.log10(y),intlist))
                except ValueError:
                    pass

            if 'powlg' in mainput:
                # try:
                    intlist = []
                    s = mainput.replace('powlg','').split(' ')
                    lisst = s[1].split('^')
                    for i in lisst:
                        intlist.append(int(i))
                    result = intlist[1]*math.log10(intlist[0])
                    print(result)

            if 'cosec' in mainput:
                try:
                    s =  mainput.replace('cosec','').split(' ')
                    cosec_int = float(s[1])
                    deg = math.radians(cosec_int)
                    sin = math.sin(deg)
                    cosec = 1/sin
                    print(cosec)
                except ValueError:
                    pass
                except ZeroDivisionError:
                    print("Infinity ( oo )")

            if 'sec' in mainput:
                try:
                    s =  mainput.replace('sec','').split(' ')
                    sec_int = float(s[1])
                    deg = math.radians(sec_int)
                    cos = math.cos(deg)
                    sec = 1/cos
                    print(sec)
                except ValueError:
                    pass
                except ZeroDivisionError:
                    print("Infinity ( oo )")

            if 'cot' in mainput:
                try:
                    s =  mainput.replace('cot','').split(' ')
                    cot_int = float(s[1])
                    deg = math.radians(cot_int)
                    sin = math.sin(deg)
                    cosec = 1/sin
                    cot = math.sqrt(cosec**2-1)
                    print(cot)
                except ValueError:
                    pass
                except ZeroDivisionError:
                    print("Infinity ( oo )")

            if '=' in mainput:
                intlist = []
                try:
                    s = mainput.replace('=',' ').split(' ')
                    for i in s:
                        intlist.append(float(i))
                    print(reduce(lambda x,y:x==y,intlist))
                except ValueError:
                    pass

            if 'sqrt' in mainput:
                try:
                    s = mainput.replace('sqrt','')
                    root = int(s)
                    result = math.sqrt(root)
                    print(result)
                except:
                    pass
            # if '' in mainput:

            if 'cube' in mainput:
                try:
                    s = mainput.replace('cube','')
                    ints = float(s)
                    result = ints**3
                    print(result)
                except ValueError:
                    pass
                except OverflowError:
                    print('Result too Large')

            if 'cubert' in mainput:
                try:
                    s = mainput.replace('cubert','')
                    ints = float(s)
                    result = (ints**(1./3.))
                    print(result)
                except ValueError:
                    pass

            if 'sq' in mainput:
                try:
                    s = mainput.replace('sq','')
                    ints = float(s)
                    result = ints**2
                    print(result)
                except ValueError:
                    pass

            if 'ptriplet' in mainput:
                try:
                    intlist = []
                    s = mainput.replace('ptriplet','').split(',')
                    if len(s) !=3:
                        print("Plz Enter 3 Numbers")
                    for i in s:
                        intlist.append(int(i))
                    print((intlist[1])**2==(intlist[0])**2+(intlist[2]**2))
                except:
                    pass

            if mainput =='cls':
                os.system("cls")
                swamtech()


swamtech()
SPEAKING_ENGINE = sub_thread(intro)
SPEAKING_ENGINE.setDaemon(True)
SPEAKING_ENGINE.start()
main()
