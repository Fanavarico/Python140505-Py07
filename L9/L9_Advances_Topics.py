'''
In The Name of GOD


Ali Pilehvar Meibody



L9 advanced Topics





Inja ma bad az L9 , Yekseri ketabkhaneye dige yad midim ke zaroori nistand

ama besiar mohem hastando afradi ke alaghe mand hastand mitoonan yad begirand
'''



'''
aval 4 ta Python standard library yad migirim

ma 4 ta module darim 
		subprocess -> ejraye barname ha o dastoorate system amel az dakhele python
		sys --> ertebat ba mohite ejraye khode python
		pathlib --> modiriate masire file ha va pooshe ha
		argparse --> daryaft o etebar sanjie vorodii haye khate farman



'''

#========================================================
#========================================================
'''     	Subprocess			'''
#========================================================
#========================================================
'''
In subprocess vaghean karesh ine ke

fekr kon shoma tooye terminal (CMD) minevisi
git status

khob shoma hamchin dastoorati ro baya biay va dar yek
safeye meshkie 'bash' bezani , ama age bekhay hamin dastoorat
ro dakhele khode python bezani bayad az package subprocess estefade koni


niazi be nasbe in ketabkhone nist choon standard library hast
'''

import subprocess

#subprocess yek tabe dare bename run ke toosh list migire
#yani dastoori ke mikhay ro bayad be soorate ozv haye yek list benevisi

#masalan agar bekhay versone git ro begiri dar terminal
#bayad bezani --> git --version
#khob in dastoor az do bakhsh sakhte shdoe 1-git 2- --version
#kafie shabihe yek listesh koni ['git','--version'] 
#va bezarish dakhele tabeye .run az subprocess



subprocess.run(['git','--version'])

#in khat miad yek process jadid misaze va vaymise payan miabe va
#natijaro mesle yek khoroji mide --> shoma mitonid natije ro berizid
#tooye yek zarf

result = subprocess.run(['git','--version'] , capture_output=True, text=True)

#parameter capture_output --> yani khoroji ro zakhire kon
#parametere text --> yani khoroji besoorate str bashe

#hamchnin yek parametr darim bename cwd = ke mitoni jolosh masiri ke mikhahi
#in dastoor ejra beshe ro bezari



print(result.stdout)
print(result.returncode)




#masalan  bekhay yek file e python az yeja dige ro dakhelesh run koni

import subprocess
import sys

subprocess.run(
    [sys.executable, "worker.py"],
    check=True
)




#gahan shoma nemikhay montazer bemoni ta oon dastoor ejrsa beshe

#yani .run() montazer mishe ta process payan yabad
#agar bekhay yek process rah andazi koni va badan contorlesh koni 
#mitoni az tabeye Popen() estefade koni


import subprocess
import sys

process = subprocess.Popen(
    [sys.executable, "worker.py"]
)

print("Worker started")
print(process.pid)

# karaye dige

process.wait()
print("Worker finished")












#========================================================
#========================================================
'''     	sys			'''
#========================================================
#========================================================

#yek ketabkhone darim bename sys be manaye system hast
#bar khalafe subprocess ke ba farayandaye dige kar mikone
#sys omdatan darbareye processe felie python hast

#mohemtarin ghavbliat -->
import sys

print(sys.argv)

#agar shoma bejaye python main.py benevisi
#python main.py Ali 25

#sys.arg miad behet yek list mide 
#["main.py", "Ali", "25"]

#yani harchizi bade python omde ro behet mide

#ama baraye barnameye vaghei ketabkhoneye 'argparse' onaseb tare




#----Payan dadan be yek barname
#yek tabe darim bename sys.exit() yani age in etefagh oftad miad b barname payan mide

import sys

age = -5

if age < 0:
    print("Invalid age")
    sys.exit(1)

print("Continue")



#----masire mofasere python

import sys

print(sys.executable)

#masalan mide
#/home/user/project/.venv/bin/python

#yani pythonet dare inja ejra mishe



#---masire jostojoye module ha
import sys

for path in sys.path:
    print(path)


#---gereftane etelaat
import sys

print(sys.version) #noskheye python
print(sys.platform) #shenase platforme system amel



#========================================================
#========================================================
'''     		Pathlib		'''
#========================================================
#========================================================
#shoma vaght ba folder ha file ha kar mikoni mitoni az ketabkhoneye
#OS estefade koni , dar l9 yad dadim.

#ama hamchnin pathlib ham darim

'''
fek kon hamchin porozhey dari
project/
├── main.py
├── data/
│   ├── file1.csv
│   └── file2.csv
└── results/



ghadim az os.path estefade mikardi, ama yek raveshe moder tar
estefade az pathlib.Path hast


'''

#masalan dar main.py mikhay adrss bdi be file1
from pathlib import Path

file = Path("data/file1.csv")



#yeki az khafan tarin karaeish ine ke mitoni masir ro ba amalgare / besazi

from pathlib import Path

folder = Path("data")

file = folder / "file1.csv"

print(file) #data/file1.csv


#----vizhegie moheme Path
#vaghty shoma yek PATH misazi , khorojisho mirizi dar yek file
#in file dar asl yek object hast
#in object yekseri method dare


file = Path("data/file1.csv")

print(file.exists()) #vojode masir ro barresi mikone (true,false)
print(file.is_file()) #barresi mikone masir yek file hast ya na (true,false)
print(file.is_dir()) #barresi mikone masir yek pooshe hast ya na (true,false)


#baraye skahte pooshe (folder)
folder = Path("outputs/reports")

folder.mkdir(
    parents=True, #afar pooshete valed vojod ndshte bashe
    exist_ok=True #age vojod dahste bashe khata nmide
)



#haat dige mitonid beaye open o .write mostaghim bekhonido benevisid

file = Path("notes.txt")

file.write_text(
    "Hello Python!",
    encoding="utf-8"
)

content = file.read_text(
    encoding="utf-8"
)

print(content)

#behamin sadegi



#Hamchenin mitoni etealaate yek file ro injori begirid

file = Path("data/report.pdf")

print(file.name) #esme file -> report.pdf
print(file.stem) #esme file bedone format -> report
print(file.suffix) #esme format --> .pdf
print(file.parent) #masire madar --> data



#-----peyda kardane file ha ba glob()
#farz kon yek poshe dari shamele koli file ke 100 ta aozna pdfe
#age bekhay fght file haye pdf onn ro peyda koni :



folder = Path("pdfs") #yani too foldere pdfs/

for file in folder.glob("*.pdf"):
    print(file.name)


#in *.pdf yani harchi k tahesh ba .pdf tamom shod


#agar hata file haye zir pooshe ham bekhay begarde bejaye glob() az rglob() estefade kon
for file in folder.rglob("*.pdf"):
    print(file)



#---taghire nam va hazfo jabejaei

#taghire name

file = Path("old.txt")

file.rename("new.txt")






#--hazf
file = Path("new.txt")

file.unlink()



#gereftane masire kamel
file = Path("data/file.csv")

print(file.resolve()) #/home/ali/project/data/file.csv





#create folder
Path("data").mkdir()

#nested folders
Path("data/users/images").mkdir(
    parents=True
)






#age bekhay masire poshe ei ke file e pythone feli dkaheelsh hast 
#az vzihegie __file__ estefade mikoni
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

data_dir = BASE_DIR / "data"





#========================================================
#========================================================
'''     argparse				'''
#========================================================
#========================================================
'''
shoma baraye ejraye barname haye python kafie benevsiid

python main.py 

vaghty yek script minevisi , hamishe codet yeksan nist mikhay
ejaze bedi dar halat haye mokhtalef ejra she
bedone inke varede khode code beshio taghir bedi


masalan yek barname dari ke pdf ro b yek excell tabdil mikone
esme file hast convert.py ya main.py ya harchizi

shoma mikhahi ke user betone , poshe vorodi , poshe khorji va kheyi chizaro
betone moshakhas kone bedone inke bere too code taghir bede

yani bejaye

python convert.py 


benevisde

python convert.py --input ./pdfs --outputs ./results


yani code convert.py ro run kon be soorati ke input = .(haminja) /foldere pdfs begard pdf haro

--output --> khoroji ro zakhire kon dar .(haminja) /results


khob ketabkhobne argparse vase hamin oomd


Yek clas darim bename ArgumentParser ke bayad az too dele argparse dar bairi


'''

import argparse

parser = argparse.ArgumentParser(
    description="My first CLI program"
)

parser.add_argument("--name")

args = parser.parse_args()

print(args.name)


#aval yek parser misazi va yek description mizari

#.add_argument yani ch chizaei bade python file.py taraf mitone bezane

#.parse_args() mire mikhone chia dadi

#baraye run krde barname bejaye
#python main.py

#shoma bayad bezani
#python main.py --name Ali

#onmoghe args.name --> mishe ali

#yani taraf age bezane
#python main.py --name Reza

#onmoghe args.name mishe Reza


#yani engar shoma az rooye dastore ejraye python mitonid vorodibegirid



#-----Paramter haye add_argument

#shoma mitonid type e vorodi ro begid chie masalan

parser.add_argument(
    "--age",
    type=int
)


#onmoghe bayad
#python main.py --age 25
#rn beshe



#in argument ha k add mikonid optionalle , yani age taraf nazane
#None mishe va okeye

#ama age bekhayd yk chzii ro ejbari konid -->

parser.add_argument(
    "--input",
    required=True
)



#age bejaye None bekhahid pish farz dashte bashe -->

parser.add_argument(
    "--format",
    default="csv"
)



#ae bekahhid entekhab haro mahdod konid
parser.add_argument(
    "--format",
    choices=["csv", "json", "txt"]
)


#--yechizi darim bename action='store_true'
parser.add_argument(
    "--verbose",
    action="store_true"
)


#yani age user benvisde 
#python main.py --verbose

#args.verbose ro True dar nazar migire, age nanvise False
#pas niazi be neevshtne --verbose True nist



#-----Ma do no argument darim

#1---> positional argument
parser.add_argument("filename")

#dastoor -> python main.py report.pdf



#2---> keyword arguments
parser.add_argument("--filename")

#yani bayad injori run bshe
#python main.py --filename report.pdf




#yeki az mohemtarin vizhegi in hast ke rahnamaye khodkar bename --help misaze
#yani

parser = argparse.ArgumentParser(
    description="Process PDF documents"
)

parser.add_argument(
    "--input",
    required=True,
    help="Input PDF directory"
)

parser.add_argument(
    "--output",
    default="results",
    help="Output directory"
)

args = parser.parse_args()


#karbar age bezane python main.py --help 
#onmoghe hame argument haro ba tozihatesh o minevisde







#========================================================
#========================================================
'''     Yel proozhe  vaghei	'''
#========================================================
#========================================================

#yek abzare CLI baraye peyda kardan va processe PDF
#in barname --> masire vorodi ro az terminal migire
#file e pdf ro peyda kone, pooshe khoroji besaze
#baraye har pdf yek file e gozarsh matni ijad kone

#dar soorate darkhast, etelaate git ro begire


#hamiishe aval bayad import ha anjam beshe
import argparse
import subprocess
import sys
from pathlib import Path


def main():

	#aval yek parser tarif mikonim
    parser = argparse.ArgumentParser(
        description="PDF processing CLI"
    )

    #ejaze midim bejaye python main.py 
    #jolosh 4 ta argument betone bezare
    #--input elzamie 
    #oon 3 taye dige elzami nist 
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results")
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--git-info", action="store_true")


    #user harchi bzne , oon chizi k benevise zakhire mishe tooye args
    args = parser.parse_args()

    #baraye dastresi b ooni k usr joloye --input gozaste 
    #kafie az dele args , inout ro beekshim biron
    input_dir = Path(args.input)
    output_dir = Path(args.output)

    #pas ag user bezane
    #python main.py --input /user/apm/desktop/files --output /user/apm/desktop/result

    #onmoghe input_dir = /user/apm/desktop/files 
    #va output_dir = /user/apm/desktop/result


    #aval check mikonim in directorie ya na ba ketabkhone Pathlib
    if not input_dir.is_dir():
        print("Input directory does not exist", file=sys.stderr)
        #age nabood -> barname ro stop mikonim
        sys.exit(1)


    #baraye output -> misazimesh
    output_dir.mkdir(parents=True, exist_ok=True)

    #bebinim --recursive true hast ya na
    #recursive yani hata foldrr haye dakheli ham begard

    #ba estefade az glob() mire harchi pdf has tooye directory input migrde
    #mirize too pdf_files
    if args.recursive:
        pdf_files = sorted(input_dir.rglob("*.pdf"))
    else:
        pdf_files = sorted(input_dir.glob("*.pdf"))

    #pdf files yek list hast az path haye .pdf 

    print(f"Found {len(pdf_files)} PDF files")

    for index, pdf in enumerate(pdf_files, start=1):
        print(f"{index}: {pdf.name}")

        #mirim az pdf kenare input directory yek path misazim
        relative_path = pdf.relative_to(input_dir)

        #dakheel outut mirim tahesh .txt mizanim
        report = output_dir / relative_path.with_suffix(".txt")
        
        #yek fodler report ro misazim baz
        report.parent.mkdir(parents=True, exist_ok=True)


        #dakhele report minevisim inro
        report.write_text(
            f"PDF: {relative_path}\n",
            encoding="utf-8"
        )

    #pas ta inja sakhte shod


    #hala age git_info true bood ba subprocess 
    #run mikonim git rev-parse --short HEAD ta bebinim
    #akharin gti commit ch boode

    if args.git_info:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
                timeout=10
            )
            print("Git commit:", result.stdout.strip())

        except (subprocess.CalledProcessError,
                FileNotFoundError,
                subprocess.TimeoutExpired) as error:
            print("Git information unavailable:", error)


if __name__ == "__main__":

	#in ham yani age file ro python file.py run krd
	#tabeye main() ejra she ke tozihatesh bala neveshtim
    main()






#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================

'''


Dar L9 ma yekseri file management yad dadim
khob ma ta alan file e txt ro midonestim ke az open() estefade mikrdim

hala baraye file e jpg/png, pdf, zip az chi estefade konim???

Part A - Binary Files

Part B - Json files

part c - CSV Files


'''
#------------------------------------------------
#------------------------------------------------
'''  Part A - Binary files 				'''
#------------------------------------------------
#------------------------------------------------
'''
hamontor gofte shdoe , compute dade haro be eshkel 0 o 1 negah midar

har 8 bit --> 1 byte hast 

Tasvir, video, pdf, file hame ina dade haye binary hastand

pas vaghty az open() estefade mikonim, 
age bekhayim reead konim az r va baraye write az w estefade mikrdim

in dar soorati bood ke filemoon .txt bashe , age filemomnn binary bashe

yani image, pdf, zip ,.. bashe --> badesh b mizarim




'''

with open("image.jpg", "rb") as file:
    data = file.read()


#onmoghe data dige str nist balke besoorate bytes hast

with open("image.jpg", "rb") as file:
    data = file.read()

print(type(data))
print(len(data))
print(data[:20])

'''
khorji -->
<class 'bytes'>
245760
b'\xff\xd8\xff\xe0\x00\x10JFIF...'

'''




#masalan copy kardan
with open("image.jpg", "rb") as file:
    data = file.read()

with open("copy.jpg", "wb") as file:
    file.write(data)





#------------------------------------------------
#------------------------------------------------
'''    Part B - Json 				'''
#------------------------------------------------
#------------------------------------------------

'''
JSON mokkhafafe JavaScript Object Notation hast ke yek
formate matni hast baraye zakhiro tabadole dade haye skahtar yafte (structured)

vaghty frontend o backend ertebat daran, dar besiari az API ha in shekle json hast

json shabihe dictionary hast va yekchizi mesle
{
  "name": "Ali",
  "age": 25,
  "city": "Tehran",
  "is_active": true,
  "skills": ["Python", "AI", "FastAPI"]
}


khob age ma yek dictionary dashte bashim , behtare bejaye inke ba open() tabdilesh
konim be yek file e .txt mostagim tabdil konim b file .json

ya inke age file .json darim ono bekhonim



'''

#----------------json.dump()

import json

user = {
    "name": "Ali",
    "age": 25,
    "city": "Tehran"
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)


#bejaye inke file.write() bezanim az json.dump() 
#ham file ro dadim ham dictionary ro

#.dump() oon ro tabdil krde be user.json


#in pishrafte tare

#ensure_ascii --> ejaze mide character haye gheyre ASCII mesle farsi mostaghim neveshte she
#in 4 ta ident mizare fasele tooraftegi mizare ke khandanesh rahat tar she
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(
        user,
        file,
        ensure_ascii=False,
        indent=4
    )



#----------------json.load()

import json

with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)

print(user)
print(user["name"])

#in user --> yek dictionary hast
#yani yek file darim bename user.json va badesh dictionary



#----------------json.dumps()
#in tabe tahesh 's' dare be manaye string
#yani miad yek dictionary ro tabidl mikone be str

import json

user = {
    "name": "Ali",
    "age": 25
}

text = json.dumps(user)

print(text) #'{'name':'ali','age':25}'
print(type(text)) #<class 'str'>

#----------------json.loads()
#in tabe tahesh s dare be manaye str

#in miad va yek reshte JSON ro tabdil mikone be dictionary 

import json

text = '{"name": "Ali", "age": 25}'

data = json.loads(text)

print(data["name"]) #Ali
print(type(data)) #<class 'dict'>



#------------------------------------------------
#------------------------------------------------
'''    Part C : CSV	'''
#------------------------------------------------
#------------------------------------------------
'''

Ta alan file haye .txt , Binary (image,pdf,zip,..) , Json 
ro yad gereftim

jadval ha chetor? file haee mesle csv?

csv yani Comma-seperated Values yani etelaat dar file e matni besoorate
satro sotoon zakhire shode va soton ha joda has


masalan dar users.csv ma darim
name,age,city
Ali,25,Tehran
Sara,22,Shiraz
Reza,30,Tabriz

in file shabhe excel hast ama formate besiar sae tar



'''

import csv

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#bejaye file.read() omadim az reader() e csv estefae krdim
#reader dar asl yek listi az list ha hast

#Khoroji :
'''

['name', 'age', 'city']
['Ali', '25', 'Tehran']
['Sara', '22', 'Shiraz']
['Reza', '30', 'Tabriz']
'''


#hata mitonim bsorate dict bargardone

import csv

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

'''
{'name': 'Ali', 'age': '25', 'city': 'Tehran'}
{'name': 'Sara', 'age': '22', 'city': 'Shiraz'}
{'name': 'Reza', 'age': '30', 'city': 'Tabriz'}


'''


#neveshtane CSV
import csv

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Ali", 25])
    writer.writerow(["Sara", 22])


#yek file msiaze bename user.csv ke injorie
'''
name,age
Ali,25
Sara,22

'''


#writerow() yek radif minevise, age bekahim chand radif benevisim


rows = [
    ["Ali", 25],
    ["Sara", 22],
    ["Reza", 30]
]

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerows(rows)







#nevshtane ba dictwrite
import csv

users = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 22}
]

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age"]
    )

    writer.writeheader()
    writer.writerows(users)


'''
In nokte ro dar nazar begirid besoorate koli baraye kar kardan

ba datahaei mesle .csv ya excell ke .xlsx .xls

mian ba yek ketabkhone khareji bename 'pandas' estefade mikonan

ke khodesh kheyli advance hasto niaz b chandin jalase dare o dar

data analysis and data science estefade mishe

ama dar dele khode pandas, az hamin ketabkhone csv va json estefade shode




'''







#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
'''
Ma ta alan iterables haro khondim, vaghty chandin meghdar ro mikhahim
dakhele yek zarf beirizm az iterable esteafde mikonim

masaalan List --> ordered , chanagbel , allow duplciated
tuple --> orderrde, unchangable , alow duplicated
set --> non-order  , unchangable, no duplicated
Dictionary -> bejaye index value, key value darim


hala ma yekseri chizaye dige ham darim ke mitonim azashon estefade konim
dar bazi az karbord ha

yani ma hamishe az list estefade nemikonim , shayad az type haye dge stefade konim

majmoei eei az inha dakhele yek standard library hastan bename collection

harkodom azina omde yek naghsi ro bartarf kone




darsnameye naghesesho in paein gozashtan, dar chanroze dige takmil mikonam

'''




#-------------Collections
'''
yek ketabkhone ke karharo nesbat be listo dicte mamoli sade tar mikonad



Counter --> shomareshe tedade tekrare anaser

defaultdict --> dictionary ba meghdare psihfarz baraye kilidhy jadid

deque --> afoozadno hazfe sari az ebteda o entehaye yek donabel

namedtuple --> sakhte recordhae ba field haye namdar


'''






#------------------------------------------------
'''					 counters  		'''

counts = {}

for name in names:
    if name not in counts:
        counts[name] = 0

    counts[name] += 1

print(counts)
# {'Ali': 3, 'Sara': 2, 'Reza': 1}





from collections import Counter

words = ["python", "java", "python", "go", "python", "java"]

counts = Counter(words)

print(counts["python"])       # 3
print(counts.most_common(2))  # [('python', 3), ('java', 2)]


print(counts["Ali"])   # 3
print(counts["Sara"])  # 2
print(counts["Mina"])  # 0
#and also --> 

#hata str
letters = Counter("banana")

print(letters)
# Counter({'a': 3, 'n': 2, 'b': 1})



#shomarseh aklamat
text = "python is easy python is useful"

words = text.split()
counts = Counter(words)

print(counts)
# Counter({'python': 2, 'is': 2, 'easy': 1, 'useful': 1})












#------------------------------------------------
''' 			defaultdict  			'''
#mikhahim aftad ro bar asase hsahr gorohbandi konim

people = [
    ("Ali", "Tehran"),
    ("Sara", "Shiraz"),
    ("Reza", "Tehran"),
    ("Mina", "Shiraz"),
]

#nba dictioanry ammoli bayad ebteda vojode kalame ro barresi konim
groups = {}

for name, city in people:
    if city not in groups:
        groups[city] = []

    groups[city].append(name)

print(groups)
# {'Tehran': ['Ali', 'Reza'], 'Shiraz': ['Sara', 'Mina']}



#ama ba deafutl dirct
from collections import defaultdict

groups = defaultdict(list)

for name, city in people:
    groups[city].append(name)

print(dict(groups))
# {'Tehran': ['Ali', 'Reza'], 'Shiraz': ['Sara', 'Mina']}


#tafavite [] ba get()
scores = defaultdict(int)

print(scores.get("Ali"))  # None
print("Ali" in scores)    # False

print(scores["Ali"])     # 0
print("Ali" in scores)    # True







#------------------------------------------------
''' 				deque 				'''



from collections import deque

numbers = deque([10, 20, 30])

print(numbers)
# deque([10, 20, 30])



#4 amaliat
#append ->enteha
#appendleft ->ebteda

#hazdo bargardandane enteha --> pop()
#haazfo bargardanadnae ebtedaei --> popleft()

numbers = deque([10, 20, 30])

numbers.append(40)
numbers.appendleft(5)

print(numbers)
# deque([5, 10, 20, 30, 40])

last = numbers.pop()
first = numbers.popleft()

print(last)     # 40
print(first)    # 5
print(numbers)  # deque([10, 20, 30])






#bahe ebteda entah va saf
from collections import deque

queue = deque()

queue.append("Ali")
queue.append("Sara")
queue.append("Reza")

while queue:
    customer = queue.popleft()
    print("در حال خدمت‌رسانی به:", customer)








#max len
history = deque(maxlen=3)

history.append("page_1")
history.append("page_2")
history.append("page_3")

print(history)
# deque(['page_1', 'page_2', 'page_3'], maxlen=3)

history.append("page_4")

print(history)
# deque(['page_2', 'page_3', 'page_4'], maxlen=3)





#------------------------------------------------
'''   				namedtuple				'''


student = ("Ali", 22, 18.5)

print(student[0])  # Ali
print(student[2])  # 18.5





from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])

student = Student(name="Ali", age=22, grade=18.5)

print(student.name)   # Ali
print(student.age)    # 22
print(student.grade)  # 18.5


#shabihe tupel hanoz
print(students[0][0])  # Ali


student = Student("Ali", 22, 18.5)

student.grade = 20  # AttributeError











