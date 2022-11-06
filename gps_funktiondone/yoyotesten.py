
class yoyo():
    def yoyotest():
        from time import sleep
        from machine import Pin, PWM
        import neopixel

        button = Pin(25, Pin.IN)
        buzzer = PWM = PWM(Pin(23,Pin.OUT))
        buzzer.freq(1)
        buzzer.duty(1)
        buzzertid = 10
        n = 12
        p = 14
        np = neopixel.NeoPixel(Pin(p), n)
        nårvidet = True
        bipfejl = False

        def pause():
            sleep(3)

        def buzzerbip():
            buzzer.freq(400)
            buzzer.duty(100)
            sleep(1)
            buzzer.freq(1)
            buzzer.duty(1)
            
        def buzzerbip1():
            buzzer.freq(200)
            buzzer.duty(100)
            sleep(1)
            buzzer.freq(1)
            buzzer.duty(1)

        def set_color(r, g, b):
            for i in range(n):
                np[i] = (r, g, b)
                np.write()
                
        def clear():
            for i in range(n):
                np[i] = (0, 0, 0)
                np.write()

            
        def nårdet():
            if nårvidet == True:
                set_color(0, 20, 0) #grøn
                print("Nåede det")
            elif nårvidet == False:
                set_color(20, 20, 0) #gul
                print("Nåede det ikke. Fejl")
                
        def nårdetikke():
            set_color(20, 0, 0) #rød
            print("Nåede det ikke. Slut")

                
        def bipnulstil():
            clear()
            bipfejl = 0
            buzzer.freq(1)
            buzzer.duty(1)
            buzzertid = 6
            
        print("YoYo-test")
            

        while True:
            if button.value() == 1:
                print(" ")
                sleep(0.2)
            else:
                sleep(0.5)
                if button.value() == 0: #Afbryder et niveau
                    print("Afbryd")
                    bipnulstil()
                    sleep(1)
                else:
                    #Niveau 1
                    set_color(0, 40, 0) # Grøn start
                    print("Niveau 1")
                    sleep(1)
                    buzzerbip()
                    print("Start")
                    print("Løb")
                    sleep(buzzertid) #Tiden
                    buzzertid = buzzertid - 1
                    buzzerbip1()
                    nårvidet = True
                    nårdet()
                    print("Stop")
                    pause()
                    
                    #Niveau 2
                    if button.value() == 0: #Afbryder et niveau
                        print("Afbryd")
                        bipnulstil()
                        sleep(1)
                    else:
                        print("Niveau 2")
                        sleep(1)
                        buzzerbip()
                        print("Start")
                        print("Løb")
                        sleep(buzzertid) #Tiden
                        buzzertid = buzzertid - 1
                        buzzerbip1()
                        nårvidet = False
                        nårdet()
                        print("Stop")
                        nårdet()
                        pause()
                        
                         #Niveau 3
                        if button.value() == 0: #Afbryder et niveau
                            print("Afbryd")
                            bipnulstil()
                            sleep(1)
                        else:
                            print("Niveau 3")
                            sleep(1)
                            buzzerbip()
                            print("Start")
                            print("Løb")
                            sleep(buzzertid) #Tiden
                            buzzertid = buzzertid - 1
                            buzzerbip1()
                            nårvidet = True
                            nårdet()
                            print("Stop")
                            pause()
                            
                             #Niveau 4
                            if button.value() == 0: #Afbryder et niveau
                                print("Afbryd")
                                bipnulstil()
                                sleep(1)
                            else:
                                print("Niveau 4")
                                sleep(1)
                                buzzerbip()
                                print("Start")
                                print("Løb")
                                sleep(buzzertid) #Tiden
                                buzzertid = buzzertid - 1
                                buzzerbip1()
                                nårvidet = False
                                print("Slut")
                                nårdet()
                                pause()
                                
                                 #Niveau 5
                                if button.value() == 0: #Afbryder et niveau
                                    print("Afbryd")
                                    bipnulstil()
                                    sleep(1)
                                else:
                                    print("Niveau 5")
                                    sleep(1)
                                    buzzerbip()
                                    print("Start")
                                    sleep(buzzertid) #Tiden
                                    buzzertid = buzzertid - 1
                                    buzzerbip1()
                                    nårvidet = False
                                    print("Slut")
                                    nårdetikke()
                                    pause()
                                    
                                    
                                    clear()
                                    bipnulstil()
                                    print("Test slut")
    yoyotest()
