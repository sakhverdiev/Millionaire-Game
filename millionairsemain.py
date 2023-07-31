import millionairesual
import random
import time
import sys

balance = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
level = 0
correct_answer = ""
q = []
acceptable_answers = ["a", "b", "c", "d", "50", "help", "audience", "friend", "finish"]
help_50 = "\"50:50\" Jokeri ucun '50' yazin"
help_50_avail = True
help_friend = "\"Dosta zeng\" Jokeri ucun 'friend' yazin"
help_friend_avail = True
help_audience = "\"Kutle\" Jokeri ucun 'audience' yazin"
help_audience_avail = True

print (" *************************************************")
time.sleep(0.5)
print (" *             ||   MILYONCU  ||            *")
time.sleep(1)
print (" *             ||   OYUNUNA   ||            *")
time.sleep(1)
print (" *             ||XOSGELMISINIZ||            *")
time.sleep(0.5)
print (" *************************************************\n")

player = input("Adiniz nedir? ")

print (f"\n{player}, evvelce size oyun haqqda melumat verecem!\n\
 15 sual olacaq ve bu suallar cetinlik seviyyelerine gore ayrilacaq.\n\
 Evvelce sadeden baslayib cetine dogru gedilecek. Eger butun suallari\n\
 dogru bilseniz $1,000,000 qazanacaqsiniz. *****UGURLAR*****\n\
      {help_50}\n\
      {help_friend}\n\
      {help_audience}\n\n\
 Jokerlerden istifade etmek ucun 'help' yazin.\n\n\
 Hazirsinizsa baslayaq!\n")
time.sleep(2)


def wait(phrase, t):
  print(f"\n\n {phrase}")
  sys.stdout.flush()
  for i in range(t):
    print("."),
    time.sleep(1)
    sys.stdout.flush()


def info(lvl):
  lvl += 1
  money = balance[lvl]
  v = [0 for i in range(3)]
  v[0] = f"#{lvl}. sual ${money} deyerindedir."
  v[1] = f"#{lvl}. suali bilseniz ${money} qazanacaqsiniz."
  v[2] = f"#{lvl}. sual ucun ${money} qazana bilersiniz."
  n = int (random.random() * 3)
  return v[n]
  

def ask_question(lvl):
  to_return = "\n " + info(lvl) + "\n "
  to_return += "=" * (len(to_return) - 3) + "\n "
  rndm = int (random.random() * 3)
  
  global q
  q = millionairesual.question(lvl, rndm)
  to_return += q[0]
  to_return += "\n A. " + q[1] + "\t\t B. " + q[2]
  to_return += "\n C. " + q[3] + "\t\t D. " + q[4]

  global correct_answer
  correct_answer = q[5]
  return to_return
  

def check_answer(lvl):
  answer = input("\n Sen: ")
  answer = answer.lower()
  global correct_answer, q, help_friend_avail, help_50_avail, help_audience_avail

  if not (answer in acceptable_answers):
    print ("\n Ne demek istediyiniz basa dusulmedi. Variantlardan birini secin. 'help' ve ya 'finish' - de sece bilersiniz. ")
    check_answer(lvl)
  
  elif (answer == "help"):
    print ("")
    if (help_50_avail):
      print (" "*5 + help_50)
    if (help_friend_avail): 
      print (" "*5 + help_friend)
    if (help_audience_avail): 
      print (" "*5 + help_audience)
    if not (help_50_avail or help_friend_avail or help_audience_avail):
      print ("\n" + " "*5 + "Islede bileceyiniz Joker qalmadi..." )
    check_answer(lvl)

  elif (answer == "friend"):
    if (help_friend_avail == True):
      help_friend_avail = False
      if (random.random() < 0.7): # Dost %70 faiz ehtimalla duz deyecek
        wait("Dosta zeng edilir", 4)
        print (f"\n Sizin dostunuz bu cavabin duz olacagini fikirlesir -> {correct_answer}.")
        check_answer(lvl)
      else:
        while True:
          i = int (random.random()*4 + 1)
          if (q[i] != "" and q[i] != correct_answer):
            wait("Dosta zeng edilir", 4)
            print (f"\n Sizin dostunuz bu cavabin duz olacagini fikirlesir -> {correct_answer}.")
            check_answer(lvl)
    else:
      print ("\n Bu jokeri isletmisiniz. Basqa hansi jokerin qaldigini gormek ucun 'help' yazin.")
      check_answer(lvl)
        
  elif (answer == "50"):
    if (help_50_avail == True):
      help_50_avail = False
      w = 0
      while True:
        if w == 2:
          break
        i = int (random.random()*4 + 1)
        if (correct_answer != q[i] and q[i] != ""):

          w += 1
          q[i] = ""

      print ("\n Iki sehv cavab silindi. Geriye ikisi qaldi:")
      temp = [" A. ", " B. ", " C. ", " D. "]
      for i in range(1,5):
        if (q[i] != ""):
          print (temp[i-1] + q[i] + "\t\t"),
      print ("")
      check_answer(lvl)
      
    else:
      print ("\n Bu jokeri isletmisiniz. Basqa hansi jokerin qaldigini gormek ucun 'help' yazin.")
      check_answer(lvl)

  elif (answer == "audience"):
    if (help_audience_avail == True):
      help_audience_avail = False
      while True:
        w = random.random()
        if (w > 0.45): 
          w = int (w*100)
          break

      if (random.random() < 0.8):
        audience_answer = correct_answer
      else:
        while True:
          i = int (random.random()*4 + 1)
          if (q[i] != ""):
            audience_answer = q[i]
            break

      wait("Kutlenin ses vermesi", 4)
      print (f"\n Kutlenin %{w} bu cavabin duzgun olacagini fikirlesir -> {audience_answer}.")
      check_answer(lvl)
      
    else:
      print ("\n Bu jokeri isletmisiniz. Basqa hansi jokerin qaldigini gormek ucun 'help' yazin.")
      check_answer(lvl)

  elif (answer == "finish"):
    print (f"\n {player}, siz oyunu bitirmeyi sectiniz. ${balance[lvl]} qazandiniz. Tebrikler!")
    quit()

  elif (answer == "a" or answer == "b" or answer == "c" or answer == "d"):
    if (correct_answer == q[ord(answer)-96]):
      if (lvl == 14):
        time.sleep(1)
        print(f"******** TEBRIKLER, {player.upper()}! *************")
        time.sleep(1)
        print(" ********* SIZ $1,000,000! QAZANDINIZ *************")
      else:
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print(f"\n Duzgun cavabi bildiniz, {player}!\n Sizin helelik ${balance[lvl+1]} pulunuz var.\n Sonraki suala kecek #{lvl+2}!")
        time.sleep(2)
        print (ask_question(lvl+1))
        check_answer(lvl+1)
        time.sleep(2)
      
    else:
      print(".")
      time.sleep(1)
      print("..")
      time.sleep(1)
      print("...")
      time.sleep(2)
      print(f"Cavab duzgun deyil.\n Duzgun cavab budur -> {correct_answer}.")
      time.sleep(2)
      print("Oyun bitdi!")

      user_choice = input("\n\n Yeniden cehd etmek isteyirsiniz? (y/n)  ")
      if (user_choice.lower() == "y"):
        help_audience_avail = True
        help_50_avail = True
        help_friend_avail = True
        print (ask_question(0))
        check_answer(0)
    

print (ask_question(0))
check_answer(0)