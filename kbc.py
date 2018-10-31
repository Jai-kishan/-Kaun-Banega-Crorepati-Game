#git remote add origin https://github.com/Jai-kishan/-Kaun-Banega-Crorepati-Game.git git push -u origin master
import pyglet


all_padav = 0
questions = ["Who is the first Indian woman wrestler to win a gold medal at the Asian Games?      ","Identify the film from this video clip (shows the video clip of the original Golmaal","Which of these banks was founded in lahore in the 19th century?","Who is the only Vice President of India to have worked under three different Presidents?","Who wrote the Saraswati Vandana 'Var de Veenavaadini var de'?","Who became the first Indian to score a century before lunch in the opening session of a Test Match in June 2018?","In which of these sports would you normally see the referee running on the field?","Madhuri Dixit's 'Bucket List' is her film in which language?","What characteristics of a leopard is used by scientists to identify them individually?","Which of these national flags has the most number of stars on them?","Which of these food items has different varieties such as ‘Suji ka _______’. ‘Aate ka _______’, ‘Moong dal ka __________’ and ‘Gajar ka _______________’?","Which of these is the name of a type of women's clothing?","Which of these actresses became known as the 'Hawa-Hawai' girl?","Samukha, Vighnaharta and Ekadanta are other names for which Hindu god?","Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?"]
# ek question list banaya hai usme aur 15 question dale hain.
option1 = ["Sakshi Malik ",   "Chashme Baddour",  "Punjab and Sindh Bank",    "S Radhakrishnan        ",   "Jaishankar Prasad          ",    "Lokesh Rahul   ",   "Cricket.   ", "English",    "Pugmarks      ", "USA        ",  "Sharbat ",  "Padmini  ",  "Sridevi      ",  "Brahma    ",   "Dahi   "]
# ek option1_list banaya hain aur usme sare question ke pehle option dale hain. 
option2 = ["Babita Kumari",   "Golmaal        ",  "Punjab National Bank ",    "Bhairo Singh Shekhawat ",   "Sumitranandan Pant         ",    "Shikhar Dhawan ",   "Football   ", "Hindi  ",    "Spot patterns ", "Brazil     ",  "Halwa   ",  "Man Bai  ",  "Hema Malini  ",  "Krishna   ",   "Ghee   "]
# ek option2_list banaya hain aur usme sare question ke doosre option dale hain.
option3 = ["Vinesh Phogat",   "Padosan        ",  "UCO Banks            ",    "B D Jatti              ",   "Ramdhari Singh 'Dinkar'    ",    "Ajinkya Rahane ",   "Badminton  ", "Marathi",    "Tail          ", "Australia  ",  "Pakora  ",  "Jodha    ",  "Rekha        ",  "Rama      ",   "Paneer "]
# ek option3_list banaya hain aur usme sare question ke teesre option dale hain.
option4 = ["Kavita Devi  ",   "Angoor         ",  "Dena Bank            ",    "Hamid Ansari           ",   "Suryakant Tripathi 'Nirala'",    "Rohit Sharma   ",   "Tennis     ", "Telugu ",    "Whiskers      ", "New Zealand",  "Chaat   ",  "Anarkali ",  "Madhuri Dixit",  "Ganesha   ",   "Khoya  "]
# ek option4_list banaya hain aur usme sare question ke chautha option dale hain.
answer_list = ('C','B','B','D','D','B','B','C','B','A','B','D','A','D','C')
# ab hamne answer list banaya hain aur usme sare question ke sahi answer dale hain.
prize  = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1000000,2500000,5000000,10000000]
# ab hamne ek prize list banai hain usme hamne 1000 se lekar 1cr tak ki prize dali hain.
padav1=10000
padav2=320000
padav3=10000000
for i in range(0,15):
    
    print("\n\n\033[1;32;40m Aapka %d Question yeh hai :- \033[0m\n"%(i+1))
    print("\033[1;37;45m Question  %s  \033[0m"% questions[i])
    print ("\033[1;33;40mA- %s \033[0m"%option1[i])
    print ("\033[1;33;40mB- %s \033[0m"%option2[i])
    print ("\033[1;33;40mC- %s \033[0m"%option3[i])
    print ("\033[1;33;40mD- %s \033[0m"%option4[i]) 

    if i==0:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key1.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==1:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key2.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==2:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key3.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()    

    if i==3:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key4.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==4:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key5.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==5:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key6.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==6:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key7.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==7:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key8.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==8:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key9.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==9:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key10.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==10:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key11.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==11:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key12.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==12:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key13.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==13:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key14.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    if i==14:
        que_1 = pyglet.resource.media('Answers/KbcQuestion/Ans_key15.mp3')
        que_1.play()
        def exit_callback(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exit_callback , que_1.duration)
        pyglet.app.run()

    var1 =input("\n\n\033[1;37;45mEnter your answer:-             \033[0m")
    if var1 == answer_list[i]:
        print("\033[1;36;40mcongrats, sahi jawaab           \033[0m")
        if i==0:
            que_1 = pyglet.resource.media('Answers/write-Ans/Question-1.mp3')
            que_1.play()
            def exit_callback(dt):
            	pyglet.app.exit()
            pyglet.clock.schedule_once(exit_callback , que_1.duration)
            pyglet.app.run()

        if i==1:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-2.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==2:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-3.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==3:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-4.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==4:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-5.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==5:
            que_1 = pyglet.resource.media('Answers/write-Ans/Question-6.mp3')
            que_1.play()
            def exit_callback(dt):
            	pyglet.app.exit()
            pyglet.clock.schedule_once(exit_callback , que_1.duration)
            pyglet.app.run()

        if i==6:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-7.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==7:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-8.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==8:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-9.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==9:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-10.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==10:
            que_1 = pyglet.resource.media('Answers/write-Ans/Question-11.mp3')
            que_1.play()
            def exit_callback(dt):
            	pyglet.app.exit()
            pyglet.clock.schedule_once(exit_callback , que_1.duration)
            pyglet.app.run()

        if i==11:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-12.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==12:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-13.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==13:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-14.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()

        if i==14:
        	que_1 = pyglet.resource.media('Answers/write-Ans/Question-15.mp3')
        	que_1.play()
        	def exit_callback(dt):
        		pyglet.app.exit()
        	pyglet.clock.schedule_once(exit_callback , que_1.duration)
        	pyglet.app.run()
        print("\033[1;36;40maap %d jeet chuke hai     \033[0m"%prize[i])

        if prize[i]==10000:
            print ("\033[1;32;40mAapka pehla padav pura huaa \033[0m")
            all_padav = padav1
        if prize[i]==320000:
            print ("\033[1;32;40maapka dusra padav pura huaa \033[0m")
            all_padav = padav2
        if prize[i]==10000000:
            print ("\033[1;37;45mCongrats aap 1 crore jeet chuke \033[0m")        
    else:
        print("\033[1;31;40maapne galat chuna hai aur aap ye game haar gye hai \033[0m")
        if all_padav >=10000:
            print("\033[1;37;45mAap %d rupaye jeet gaye hai aur ghr le jaa sakte hai \033[0m" %all_padav)
        break