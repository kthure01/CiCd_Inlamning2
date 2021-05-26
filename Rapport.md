# Rapport på inlämningsuppgift 2 i Ci/Cd

Jag börjar med att skapa upp ett nytt publikt repo på GitHub som jag döper till
[**CiCd_Inlamning2**](https://github.com/kthure01/CiCd_Inlamning2.git).

Repot klonar jag sedan ner på min Linux-maskin med:

>git clone [https://github.com/kthure01/CiCd_Inlamning2.git](https://github.com/kthure01/CiCd_Inlamning2.git)

Jag skapar även en ny branch som jag kallar dev. I denna branch kommer all
utveckling av appen att ske.

>git checkout dev

Nu börjar jag med att skapa lite filer. En **_.gitignore_** som innehåller information
vad som **inte** ska ”pushas” upp mot GitHub och en **_requirements.txt_** som kommer
innehålla information om de extra moduler som appen kommer att behöva för att
kunna köras och testas på ett korrekt sätt.

Nu gör en första synkning mot GitHub med:
>git add --all\
>git commit -m “SOME_DESCRIPTION_MESSAGE”\
>git push --set-upstream origin dev

I denna inlämningsuppgift har jag byggt in ett enkelt gränssnitt som frågar efter
2 nummer och vilken operator man vill använda. Har även byggt in lite felhantering.
Appen finns i **_calculator.py_** och testarna ligger i **_test_calculator.py_**. Även dessa
filer ”pushas” också till GitHub.

För att kolla om appen följer en vedertagen kodstandard så installerar jag en
modul till Python som heter **_flake8_**. Jag installerar även modulen **_pytest_** som kör
de tester jag skapat för appen.
Kommandot för att installera modulerna är: `pip install -r requirements.txt`
Kommandot för att testa kodstandarden är: `flake8 <app_file_name>`

Tester fungerar så att man skapar testfunktioner som i sin tur anropar den testade funktionen
i huvudprogrammet med olika värden. Att funktionen returnerar det förväntade kollar man via
ett **_assert_**-uttryck. 
Kommandot för att köra testerna är: `pytest -v <test_file_name>`


För att bygga applikationen och köra tester på den så använder jag mig av verktyget
[CircleCi](https://circleci.com/). Jag har kopplat ihop mina konton på GitHub och CircleCi.
Detta gör att jag då enkelt kan välja mitt GitHub-repo och sedan skapa en konfigurationsfil
**_config.yml_** som jag sedan lägger in i mitt repo (.circleci/config.yml).
I denna fil så skapar jag olika jobb som jag sedan kör i sektionen "workflows".
Jag har valt att skapa ett jobb som jag kallar **_build_** och ett som jag kallar **_test_**.
För att detta ska triggas igång så måste man ha gjort en manuell pull request från branchen dev till main.
Vidare så för att testerna ska köras så måste build-jobbet ha gått igenom felfritt annars så kommer
inte testerna att köras.
Testerna som körs är en kontroll av kodstandarden och en test där 2 funktioner i appen kontrolleras.

Det man ibland kan råka ut för är att man glömt kolla koden med flake8 eller missat att köra
någon test.

Det som saknas för att uppnå CD skulle väl vara att ha automatiskt skapa pull requests och att få 
ett automatiskt godkännande av dessa så att koden automatiskt mergas in till main branchen. 
