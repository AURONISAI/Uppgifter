# Reflektion

Det har var roligast hittils. Jag tog vara riktiga produktfoton
fran "inci shopify ready"-mappen och byggde en katalog som ser
ut som en riktig webshop.

Jag larde mig att lagga produkterna i en array istallet for att
skriva HTML for varje jacka. Da blir det mycket lattare att lagga
till en ny jacka senare, det blir bara en rad data.

Filter och sortering var lite knepigt forst. Jag forstod att jag
behovde anvanda Array.filter och Array.sort och sen rita om hela
katalogen igen. Det funkade bra till slut.

Modalen var ocksa ny for mig. Jag ville att man skulle kunna byta
farg pa jackan och se bilden andras direkt. Jag loste det med en
funktion som uppdaterar bilden nar man klickar pa en fargcirkel.

Det svaraste var nog att fa onskelistan att spara bade vilken
jacka och vilken farg, och sen ladda tillbaka allt nar man oppnar
sidan igen. Jag anvander JSON.stringify och JSON.parse for det.

Vader-API fick rekommendera en av vara jackor baserat pa
temperaturen. Det var kul att koppla en extern API till var
egen produktdata.

Nasta gang skulle jag vilja lagga till storlekar (S/M/L) och en
riktig kassa.
