# api_eindproject

Voor mijn eindproject heb ik gekozen om mijn database rond school te maken. Daarnaast hash ik ook de user zijn wachtwoorden. De inpiratie kwam van mijn vorig project hierbij had ik al iets gemaakt rond user's en website's. Maar nu heb ik het thema rond scholen gemaakt en de user's die erin zitten.

# Project inhoud

In mijn project heb ik 3 tabellen "Land tabel, School tabel en een User tabel". Hierbij is de logica dat je eerst een land moet aanmaken via de API. Daarna maak je een school aan via de land ID mee te geven. En als laatste kan je een user aanmaken door de school ID mee te geven.
En daarna kan je zoveel user toevoegen aan een school.

Voor mijn API ik alle 3 de parameters gebruikt "path, querie, body". mijn GET API's zijn meestal path/querie parameters. En mijn POST API's zijn met body parameters mee geleverd. Als laatste heb ik ook een PUT API die de user zijn R-nummer kan veranderen naar een andere. Doordat je de juiste user-ID mee geeft in het path. Daarnaast heb ik ook een DELETE API die een user zal deleten door de juiste user-ID mee te geven in het path.

Voor de Front-END heb ik gekozen om alleen mijn GET en POST API's op te zetten. Voor de PUT en DELETE api zal je postmen moeten gebruiken.
Ik heb ook gitlab gebruikt om mijn html-website te hosten. (Zie foto)

![Front-end page](./img/front-end-page.png)


# Python bibliotheken

Python-bibliotheken die ik voor dit project heb gebruikt, worden hieronder weergegeven.

1. Sqlalchemy
2. Passlib
3. Os
4. Fastapi
5. Pydantic

Ik heb "sqlalchemy" gebruikt om tabellen te creeren en informatie te inserten en verwijderen. Ik gebruik "passlib" om de user zijn passwoorden te encrypteren naar de database toe. "Os" wordt gebruikt om een directory op het systeem aan te maken als het nog niet bestond. "Fastapi" wordt gebruikt om een api te maken. Ik heb "pydantic" gebruikt om klassen te maken met het basismodel.


# Soorten API's

Voor dit project heb ik in totaal 11 API's waarvan je 9 API's via de front-end kan berijken. En de andere 3 API's zal je via postman moeten gebruiken. Van de 11 API's zijn er 6 GET API's en 3 POST API's en de laatste 2 zijn een PUT en DELETE API.

Nu zal ik alle API's laten zien via FastAPI/docs en Postman en ten slotte ook via de Front-END.

### FastAPI docs foto

Hier kan u al mijn API's zien via de FastAPI docs.

![FastAPI docs](./img/fastapi-docs.png)

### Postman foto's

API - Post Method - Land Creëren

![Postmen API foto - Land Creëren](./img/land-aanmaken.png)

API - Post Method - Land Dupliceren

![Postmen API foto - Land Creëren](./img/land-aanmaken-bestaat.png)



API - Post Method - School Creëren

![Postmen API foto - School Creëren](./img/school-aanmaken.png)

API - Post Method - School Dupliceren

![Postmen API foto - School Creëren](./img/school-aanmaken-bestaat.png)



API - Post Method - User Creëren

![Postmen API foto - User Creëren](./img/user-aanmaken.png)

API - Post Method - User Dupliceren

![Postmen API foto - User Creëren](./img/user-aanmaken-bestaat.png)



API - GET/PUT/DELETE Method - Check user, Change user, Delete user, Check user again

![Postmen API foto - Check user ](./img/aanmaken-veranderen-verwijderen-1.png)

![Postmen API foto - Change user ](./img/aanmaken-veranderen-verwijderen-2.png)

![Postmen API foto - Delete user ](./img/aanmaken-veranderen-verwijderen-3.png)

![Postmen API foto - Check user again ](./img/aanmaken-veranderen-verwijderen-4.png)



API - GET Methed - Check alle users

![Postmen API foto - Check alle user ](./img/alle-users.png)

API - GET Methed - Check specific users

![Postmen API foto - Check specific user ](./img/een-user.png)



API - GET Methed - Check alle landen

![Postmen API foto - Check alle landen ](./img/alle-landen.png)

API - GET Methed - Check specific users

![Postmen API foto - Check specific land ](./img/een-land.png)



API - GET Methed - Check all scholen

![Postmen API foto - Check all scholen ](./img/alle-scholen.png)

API - GET Methed - Check specific school

![Postmen API foto - Check specific school ](./img/een-school.png)



API - PUT/DELETE Method - User bestaat niet

![Postmen API foto - User bestaat niet om aan te passen ](./img/user-aanpassen-bestaat-niet.png)

![Postmen API foto - User bestaat niet om aan te verwijderen ](./img/user-deleten-bestaat-niet.png)


### Front-end foto's

Front-end - API calls gemaakt waarvan de post method niet inorde was

![Front-END API foto - POST API's niet inorde ](./img/front-end-niet-inorde.png)

Front-end - API calls gemaakt waarvan alles inorde is.

![Front-END API foto - Alles inorde ](./img/front-end-inorde.png)


# Punten

1. ❔ ALGEMENE EISEN & DOCUMENTATIE (alles samen +50%)
* Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
* Minstens 3 entiteiten in je API via een SQLite databank
* Minstens hashing en OAuth implementeren
* Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
* Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
* Volledige OpenAPI docs screenshot(s) op GitHub README.md
* Logisch gebruik van path parameters, query parameters en body
* Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
* Deployment van de API container(s) op Okteto Cloud via Docker Compose

3. 📳 AANVULLINGEN: FRONT-END
* 3.1 (+15%) Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat.
* 3.1.2 (+10%) Geef de front-end een leuke stijlgeving.


# URL Links

Github Repository: Hier zit u op <br />
Github Repository voor front-end: [GitHub Repo - Front-end Link](https://github.com/waelke553/api_eindproject_website) <br />
Hosted API: [Okteto - Hosted API Link](https://system-service-waelke553.cloud.okteto.net/) <br />
Hosted front-end: [Github - Hosted Front-end Link](https://waelke553.github.io/ api_basisproject_website/) <br />

Bijkomende commentaar, aanvullingen, enz:

Bij mijn front-end kan je zien dat als je de invoervelden invult. Dat je de link gewoon met het blote oog kunt zien. Ook als is je wachtwoord met bolletjes is dit niet bij de link.

Typ dus NIET uw gebruikte wachtwoorden!

Daarnaast als je de invoer velden van de GET API's leeg laat. Zal hij niet een specifieke user opvragen maar zal hij alles laten zien.
