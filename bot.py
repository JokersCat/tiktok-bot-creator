import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from time import sleep

print("""
STILL UNDER DEVELOPPEMENT 
CREDITS TO: https://github.com/xtekky
""")

def login():

    driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 20)
    driver.get('https://temp-mail.org/en/')

    global validation
    global code

    sleep(10)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button'))).click()
    temp_mail = pyperclip.paste()

    # send verify email
    driver.switch_to.new_window()
    driver.get('https://www.tiktok.com/signup/phone-or-email/email')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[1]/div'))).click()  # month
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[1]/ul/li[11]'))).click()  # 11
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[2]/div'))).click()  # day
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[2]/ul/li[4]'))).click()  # 4
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[3]/div'))).click()  # year
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[3]/ul/li[19]'))).click()  # 2003
    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(temp_mail)  # email
    wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('Jeliie@4565')  # password
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[4]/div[5]/button'))).click()

    # get_verification_code
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    sleep(3)
    try:
        def getcode():
            global code
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a'))).click()
            code = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a'))).text()
    except:
        driver.refresh()
        getcode()

    sleep(999)

    # input code
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[4]/div[5]/div/input'))).send_keys(code) #paste code
    # click submit

    #finish login
    import random

    # generating name functions
    def genName():
        boyNames = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", 
                    "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", 
                    "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", 
                    "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", 
                    "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", 
                    "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", 
                    "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", 
                    "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", 
                    "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", 
                    "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", 
                    "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", 
                    "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar",
                    "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", 
                    "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", 
                    "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", 
                    "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir",
                    "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni",
                    "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", 
                    "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin",
                    "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", 
                    "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", 
                    "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", 
                    "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley", "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam",
                    "Asrar", "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay",
                    "Aun", "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan", "Ayan", 
                    "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub", "Azaan", "Azedine", 
                    "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", 
                    "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej",
                    "Bartosz", "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict",
                    "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel", 
                    "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", 
                    "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie",
                    "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan",
                    "Branden", "Brandon", "Brandonlee", "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme",
                    "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody", "Brogan", 
                    "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan", "Bryce", "Bryden", "Brydon", 
                    "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan",
                    "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum",
                    "Cai", "Caidan"]

        girlNames = ["Alice", "Hana", "Clare", "Janet", "Daisy"]
        print(''.join(random.choice(boyNames) + '_' + random.choice(girlNames) + '_' + str(random.randrange(101, 999, 1))))

    genName()

    # sub to account
    # script to sup to specific account


start = int(input('type 1 to start: '))
if start == 1:
    account = ('Account you want to bot: ')
    login()
else:
    print('See you next time')
    exit()


