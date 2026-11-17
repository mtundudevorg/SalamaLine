import { GraduationCap, HeartHandshake, ShieldCheck, HandHeart, Heart, Smartphone } from 'lucide-react'

export const regions = {
  'Arusha':['Arusha City','Arusha District','Karatu','Longido','Meru','Monduli','Ngorongoro'],
  'Dar es Salaam':['Ilala','Kinondoni','Temeke','Ubungo','Kigamboni'],
  'Dodoma':['Dodoma City','Bahi','Chamwino','Chemba','Kondoa','Kongwa','Mpwapwa'],
  'Geita':['Geita Town','Bukombe','Chato','Mbogwe','Nyang’hwale'],
  'Iringa':['Iringa Municipal','Iringa District','Kilolo','Mafinga Town','Mufindi'],
  'Kagera':['Bukoba Municipal','Bukoba District','Biharamulo','Karagwe','Kyerwa','Missenyi','Muleba','Ngara'],
  'Katavi':['Mpanda Municipal','Mpanda District','Mlele','Nsimbo','Tanganyika'],
  'Kigoma':['Kigoma-Ujiji','Buhigwe','Kakonko','Kasulu','Kibondo','Uvinza'],
  'Kilimanjaro':['Moshi Municipal','Moshi District','Hai','Mwanga','Rombo','Same','Siha'],
  'Lindi':['Lindi Municipal','Kilwa','Liwale','Nachingwea','Ruangwa'],
  'Manyara':['Babati Town','Babati District','Hanang','Kiteto','Mbulu','Simanjiro'],
  'Mara':['Musoma Municipal','Bunda','Butiama','Rorya','Serengeti','Tarime'],
  'Mbeya':['Mbeya City','Mbeya District','Busokelo','Chunya','Kyela','Mbarali','Rungwe'],
  'Morogoro':['Morogoro Municipal','Morogoro District','Gairo','Kilombero','Kilosa','Malinyi','Mlimba','Mvomero','Ulanga'],
  'Mtwara':['Mtwara Municipal','Mtwara District','Masasi','Nanyamba','Newala','Tandahimba'],
  'Mwanza':['Ilemela','Nyamagana','Buchosa','Kwimba','Magu','Misungwi','Sengerema','Ukerewe'],
  'Njombe':['Njombe Town','Njombe District','Ludewa','Makambako','Makete','Wanging’ombe'],
  'Pwani':['Kibaha Town','Kibaha District','Bagamoyo','Chalinze','Kisarawe','Mafia','Mkuranga','Rufiji'],
  'Rukwa':['Sumbawanga Municipal','Sumbawanga District','Kalambo','Nkasi'],
  'Ruvuma':['Songea Municipal','Songea District','Mbinga','Namtumbo','Nyasa','Tunduru'],
  'Shinyanga':['Shinyanga Municipal','Shinyanga District','Kahama Town','Kishapu','Msalala','Ushetu'],
  'Simiyu':['Bariadi Town','Bariadi District','Busega','Itilima','Maswa','Meatu'],
  'Singida':['Singida Municipal','Singida District','Ikungi','Iramba','Manyoni','Mkalama'],
  'Songwe':['Tunduma','Mbozi','Ileje','Momba','Songwe'],
  'Tabora':['Tabora Municipal','Igunga','Kaliua','Nzega','Sikonge','Urambo','Uyui'],
  'Tanga':['Tanga City','Handeni','Kilindi','Korogwe','Lushoto','Mkinga','Muheza','Pangani'],
  'Kaskazini Pemba':['Micheweni','Wete'],
  'Kusini Pemba':['Chake Chake','Mkoani'],
  'Kaskazini Unguja':['Kaskazini A','Kaskazini B'],
  'Kusini Unguja':['Kusini','Kati'],
  'Mjini Magharibi':['Mjini','Magharibi A','Magharibi B']
}
export const topics = [
  {id:'education', icon:GraduationCap, title:'Haki ya elimu', en:'Right to education', desc:'Taarifa na hatua za kutafuta msaada ikiwa msichana anazuiwa kwenda shule, analazimishwa kuacha masomo au anahitaji kurudi shuleni.'},
  {id:'marriage', icon:HeartHandshake, title:'Ndoa ya utotoni / ya kulazimishwa', en:'Child or forced marriage', desc:'Mwongozo wa usalama na namna ya kuomba msaada wa mtu aliyefundishwa.'},
  {id:'fgm', icon:ShieldCheck, title:'Ukeketaji (FGM)', en:'Female genital mutilation', desc:'Taarifa zilizoandaliwa kwa usalama na njia ya kuomba huduma ya afya au ulinzi.'},
  {id:'violence', icon:HandHeart, title:'Ukatili na unyanyasaji', en:'Violence and abuse', desc:'Msaada kuhusu ukatili wa kimwili, kihisia, kingono au nyumbani.'},
  {id:'mental', icon:Heart, title:'Afya ya akili na ustawi', en:'Mental health and wellbeing', desc:'Hatua ndogo za kujitunza na njia za kupata mshauri aliyefundishwa.'},
  {id:'digital', icon:Smartphone, title:'Usalama wa mtandaoni', en:'Digital safety', desc:'Ushauri kuhusu vitisho, udhalilishaji, kusambazwa kwa picha na unyanyasaji mtandaoni.'},
]
export const articles = [
  {id:'school', category:'Elimu', title:'Ukizuiwa kwenda shule, unaweza kuomba msaada', text:'Kila msichana anastahili kujifunza na kuwa na nafasi ya kupanga maisha yake. Ikiwa unazuiwa kuhudhuria shule, unaweza kuzungumza na mtu mzima unayemwamini au kuomba kuunganishwa na mtoa huduma aliyethibitishwa. Usijiweke kwenye hatari ili kupata msaada.', tags:['elimu','shule','haki']},
  {id:'marriage', category:'Ulinzi', title:'Ikiwa unaogopa ndoa ya kulazimishwa', text:'Usalama wako ni muhimu. Ikiwa ni salama, tafuta mtu unayemwamini na eleza unachohofia. Unaweza kuomba kuzungumza na mshauri aliyefundishwa bila kutoa maelezo usiyotaka kushiriki. Hatua za msaada zinapaswa kuzingatia ridhaa na usalama wako.', tags:['ndoa','utotoni','kulazimishwa']},
  {id:'online', category:'Usalama wa kidijitali', title:'Vitisho au unyanyasaji mtandaoni', text:'Usijibu vitisho ikiwa kufanya hivyo kunaweza kuongeza hatari. Ikiwa ni salama, hifadhi ushahidi mahali salama, kagua mipangilio ya faragha na tafuta msaada kutoka kwa mtu unayemwamini au huduma inayofaa. Usitume picha au taarifa zaidi kwa mtu anayekutishia.', tags:['mtandaoni','picha','vitisho','digital']},
  {id:'wellbeing', category:'Ustawi', title:'Unapohisi umelemewa', text:'Jaribu kwenda sehemu salama, pumua taratibu na wasiliana na mtu unayemwamini ikiwa unaweza. Haya siyo utambuzi wa kitabibu. Ikiwa unahisi unaweza kujiumiza au uko kwenye hatari ya haraka, tafuta msaada wa mtu aliye karibu nawe au huduma za dharura za eneo lako.', tags:['akili','msongo','ustawi']},
  {id:'fgm', category:'Afya na ulinzi', title:'Maswali kuhusu ukeketaji (FGM)', text:'Ukeketaji unaweza kuathiri afya na ustawi. Una haki ya kuuliza maswali kwa faragha na kupata huduma ya afya yenye heshima. Ikiwa unaogopa kuwa uko kwenye hatari, unaweza kuomba kuunganishwa na mtoa huduma aliyefundishwa. SalamaLine haichukui hatua kwa niaba yako bila ridhaa yako.', tags:['fgm','ukeketaji','afya']},
  {id:'violence', category:'Ulinzi', title:'Ukatili si kosa lako', text:'Ikiwa mtu anakutisha, anakudhibiti au anakudhuru, hustahili kulaumiwa kwa hilo. Fikiria usalama wako kabla ya kuchukua hatua. Unaweza kuomba kuzungumza na mshauri na kuchagua ni taarifa zipi uko tayari kushiriki.', tags:['ukatili','unyanyasaji','usalama']},
]
export const translations = {
  sw:{home:'Mwanzo', services:'Tafuta huduma', request:'Omba msaada', learn:'Taarifa salama', guide:'Mwelekezi', partner:'Eneo la mshauri', heroEyebrow:'USALAMA • FARAGHA • CHAGUO LAKO', heroTitle:'Hauko peke yako.', heroSub:'Taarifa salama na njia za kupata msaada wa kibinadamu — kwa heshima, bila lawama, na kwa hatua unazochagua mwenyewe.', start:'Pata msaada', read:'Soma taarifa salama', privacy:'Faragha yako ni muhimu', privacyText:'Unaamua unachoshiriki. Ridhaa yako inahitajika kabla ya ombi kupelekwa kwa mshauri.', topics:'Tunaweza kukusaidia kuhusu nini?', topicsSub:'Chagua mada inayokuhusu. Unaweza kusoma kwanza bila kuomba msaada.', how:'Msaada kwa namna inayokufaa', howSub:'Tumia tovuti, tafuta huduma kwa mkoa na wilaya, au tumia menyu ya simu za kawaida pale itakapounganishwa.', footer:'Njia salama ya kupata taarifa na msaada.', search:'Tafuta mada au huduma…', region:'Chagua mkoa', district:'Chagua wilaya', allRegions:'Mikoa yote', allDistricts:'Wilaya zote', find:'Tafuta', noResults:'Hakuna huduma iliyothibitishwa inayoonyeshwa kwa eneo hili kwa sasa.', noResultsSub:'Taarifa za watoa huduma huonekana baada ya kuthibitishwa na mshirika husika.', back:'Rudi', next:'Endelea', send:'Tuma ombi', consent:'Ninakubali kushirikisha taarifa nilizochagua na mshauri aliyethibitishwa ili anisaidie.', anonymous:'Nataka kuuliza bila kuacha mawasiliano kwa sasa', urgent:'Uko kwenye hatari ya haraka?', urgentText:'Ikiwa unaweza, nenda sehemu salama na wasiliana na mtu unayemwamini au huduma ya dharura ya eneo lako. Usisubiri tovuti hii ikiwa uko kwenye hatari ya sasa.', privacyTitle:'Faragha na usalama', privacyDesc:'Taarifa zako binafsi hazipaswi kuonekana kwa watumiaji wengine. Ufikiaji wa mshauri unapaswa kuwa kwa kesi alizopangiwa tu, kulingana na ruhusa na ukaguzi wa mfumo.', language:'Lugha', light:'Mwanga', dark:'Giza', system:'Mfumo', allTopics:'Mada zote', submitSuccess:'Ombi lako limepokelewa.', submitInfo:'Mshauri aliyethibitishwa atalipitia ombi lako kwa kuzingatia ridhaa uliyotoa.'},
  en:{home:'Home', services:'Find services', request:'Ask for support', learn:'Safe information', guide:'Guided help', partner:'Responder workspace', heroEyebrow:'SAFETY • PRIVACY • YOUR CHOICE', heroTitle:'You are not alone.', heroSub:'Safe information and pathways to human support — with dignity, without blame, and at a pace you choose.', start:'Get support', read:'Read safe information', privacy:'Your privacy matters', privacyText:'You choose what to share. Your consent is required before a request is routed to a responder.', topics:'What would you like support with?', topicsSub:'Choose a topic. You can read first without requesting help.', how:'Support that works for you', howSub:'Use the website, search by region and district, or use a basic-phone menu when connected.', footer:'A safer path to information and support.', search:'Search topics or services…', region:'Select region', district:'Select district', allRegions:'All regions', allDistricts:'All districts', find:'Search', noResults:'No verified service is currently listed for this location.', noResultsSub:'Provider information appears after verification by the relevant partner.', back:'Back', next:'Continue', send:'Submit request', consent:'I agree to share the information I selected with a verified responder so they can help me.', anonymous:'I want to ask without sharing contact details for now', urgent:'Are you in immediate danger?', urgentText:'If possible, move to a safer place and contact someone you trust or a local emergency service. Do not wait for this website if you are in immediate danger.', privacyTitle:'Privacy and security', privacyDesc:'Your personal information should not be visible to other users. Responders should access only cases assigned to them, subject to system permissions and audit controls.', language:'Language', light:'Light', dark:'Dark', system:'System', allTopics:'All topics', submitSuccess:'Your request has been received.', submitInfo:'A verified responder will review your request in line with the consent you gave.'}
}

