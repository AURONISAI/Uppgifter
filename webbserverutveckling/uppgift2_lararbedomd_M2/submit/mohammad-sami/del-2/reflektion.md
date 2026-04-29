# Reflektion - Del 2

Mohammad Sami Alsharef

## Vad jag larde mig av att fixa filerna

Det mest larorika med uppgiften var att felen i de tre filerna handlade om
helt olika saker, men alla skadade upplevelsen. I HTML-filen var det mest
tillganglighet och struktur som var fel - bilden hade ingen alt-text,
inputfaltet hade ingen label, och titeln sa inget om sidan. Sant ar latt
att gora ratt fran borjan om man bara kommer ihag det, men slarvar man
sa missar man det.

I CSS-filen var det fargkontraster och storlekar. Jag visste sen tidigare
att `lightgray` text pa en ljus bakgrund inte fungerar, men det ar en bra
paminnelse om att alltid kolla att texten gar att lasa. Och 9px font-size
ar nastan hanfull mot anvandaren - inget jag skulle valja sjalv men det
visar hur sma detaljer i CSS gor stor skillnad.

I JavaScript var felet allvarligast: en saknad `}` gjorde att hela scriptet
kraschade med syntax error. Sant ser man direkt i webblasarens konsol om
man tittar dar, och det ar nagot jag har lart mig att alltid oppna nar nat
inte funkar. Att funktionen dessutom hade ett meningslost namn (`test`)
och aldrig anropades visar att skriva kod inte bara handlar om att
syntaxen ska bli ratt - den ska ocksa kallas och betyda nagot.

## Hur jag tankte nar jag fixade

Jag bestamde mig for att skriva en kort kommentar pa svenska bredvid
varje andring, sa att det ar latt att se vad som var fel och vad jag
gjorde at det. Det gor det enklare for nan annan (eller mig sjalv om en
manad) att forsta vad som hander.

## Vad jag tar med mig

- Oppna alltid console-fliken nar nat inte funkar i JS.
- Lagg `alt` pa bilder och `<label>` pa inputfalt - alltid.
- Kolla fargkontraster, sarskilt om man valjer "ljus pa ljus" eller "mork pa mork".
- `var` ar gammalt, anvand `let` eller `const`.
- Funktioner ska ha namn som beskriver vad de gor, och de maste anropas for att gora nat.

Sammanfattningsvis: en sida kan se ut att fungera men anda vara trasig pa
manga satt - tillgangligheten, lasbarheten och javascriptet kan alla vara
kraschade utan att det syns direkt vid forsta blicken.
