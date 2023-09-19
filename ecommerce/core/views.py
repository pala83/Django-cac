from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    logos = [
        '01-kolsch.png',
        '02-irish-stout.png',
        '03-altbier.png',
        '04-stolichno.png',
        '05-pilsener.png',
        '06-guinnes.png',
        '07-camdem-pale-ale.png',
        '08-ipa-green.png',
        '09-smithwicks.png',
        '10-dunkel.png',
        '11-pillus.png',
        '12-old-vienna.png',
        '13-barley.png',
        '14-black-scottish-stout.png',
        '15-kostriber.png',
        '16-london-porter.png',
    ]

    context = {
        'logos': logos
    }
    return render(request, "core/index.html", context)

def cervezas(request):
    cervezas=[
        {
            'nombre': "Black Horse Ale - Carling O'Keefe",
            'cualidades': "DORADA / SUAVE / FRESCA / FRUTADA",
            'descripcion': "Existen muchas cervezas doradas y refrescantes. Pero frutadas y con destellos finales de lúpulo, sólo hay un estilo: la legendaria Black Horse Ale. En Brewery rescatamos la antigua receta de la cerveza favorita de los bebedores en Toronto, Canada, y la honramos desde 1983. En nuestra cocina, su legado sigue intacto.",
            'alcohol': "5%",
            'ibu': "22",
            'tapa': "tapa-black-horse.png",
            'botella': "botella-black-horde.jpg",
            'tipo': "rubia"
        },
        {
            'nombre': "Branding Ale - Carling O'Keefe",
            'cualidades': "LUPULADA / TURBIA / SEDOSA",
            'descripcion': "Este tipo de cervezas artesanales se fermentan a temperaturas superiores a las de las Lager (hasta los 25ºC). Son muy aromáticas, dulces, con cuerpo y generalmente con sabor muy marcado.",
            'alcohol': "4.5%",
            'ibu': "25",
            'tapa': "tapa-branding-ale.png",
            'botella': "botella-branding-ale.jpg",
            'tipo': "rubia"
        }, 
        {
            'nombre': "Light Beer - Blacksmith Beverages Ltd",
            'cualidades': "BRILLLANTE / SIMPLE / SUAVE",
            'descripcion': "Es una cerveza demasiado simple, a veces indistinguible del agua, es para aquellas personas que se ponen en pedo con exagerada facilidad. Su nombre describe su principal facultad, es Light en todo sentido y forma.",
            'alcohol': "3%",
            'ibu': "12",
            'tapa': "tapa-ligth-beer.png",
            'botella': "botella-ligth-beer.jpg",
            'tipo': "rubia"
        },
        {
            'nombre': "Labbatt Legere Light - Labatt Brewery",
            'cualidades': "DULCE / CLARA / AMARGA",
            'descripcion': "Una cerveza francesa que fue el experimento fallido de alguien que intento hacer vino con malta, creo una cerbeza absurdamente amarga y con el dulzor que le proporciona el delicado proceso de fermentacion del vino",
            'alcohol': "4%",
            'ibu': "85",
            'tapa': "tapa-labbat.png",
            'botella': "botella-labbat.jpg",
            'tipo': "rubia"
        },
        {
            'nombre': "Heidelberg - Carling Breweries",
            'cualidades': "BRONCE / COMPLEJA / FUERTE / CORPULENTA",
            'descripcion': "Nuestra cerveza de mayor graduación alcohólica. Una hermandad de malta y licor, con rasgos de nuez, caramelo y dulce de leche. Heidelberg fue creada en 1976 en Vancouver, Canada y la producimos segun la receta original.",
            'alcohol': "19%",
            'ibu': "53",
            'tapa': "tapa-heidelberg.png",
            'botella': "botella-helderberg.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Extra Old Stock - Brewery",
            'cualidades': "BRONCE / AROMA FRUTADO / LICOROSA",
            'descripcion': "Antiguamente los procesos de elaboracion de cerbeza eran muy rudimentarios, no existian las recetas de elaboracion de cerbeza que utilizamos actualmente. Esta cerbeza sigue la misma elaboracion de la vieja escuela, su elaboracion tan \"a ojo\" hace que sea tan especial para nosotros, ya que su elaboracion sigue el mismo proceso que utilizaba el fundador de Brewery, en los años 1735.",
            'alcohol': "6.2%",
            'ibu': "87",
            'tapa': "tapa-extra-old-stock.png",
            'botella': "botella-extra-old-stock.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Molson Bock - Molson Breweries",
            'cualidades': "AMBAR OSCURO / ESPESA / FIRME ",
            'descripcion': "Como el caracter de un carnero montañes, la cerveza Molson te va a meter un cabesazo que te va a dejar sentado un buen rato, para que puedas seguir degustando de esta extravagante cerveza traida de los Aples Suizos.",
            'alcohol': "5%",
            'ibu': "27",
            'tapa': "tapa-molson-bock.png",
            'botella': "botella-molson-bock.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Super Bock - Labatt Brewery",
            'cualidades': "DULCE / MUY ESPESA / CHOCOLATOSA",
            'descripcion': "Durante más de setecientos años, la llegada de la primavera se ha celebrado en una gran tradición europea, la elaboración de la cerveza Bock. Super Bock de Labatt se ha elaborado para reconocer esta feliz tradición. Es suave y delicioso... un producto de primera calidad elaborado especialmente para celebrar la llegada de la primavera. Super Bock Elaborado para celebrar la llegada de la primavera.",
            'alcohol': "14%",
            'ibu': "15",
            'tapa': "tapa-super-bock.png",
            'botella': "botella-super-bock.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Spar 6 Malt Liquor - North Island Brewing",
            'cualidades': "AMBAR OSCURO / TURBIA / RARA ",
            'descripcion': "Una cerveza creada por una tribu al norte de una isla de centroamerica, tiene un sabor extraño y dulce, algunos criticos afirman que es elaborada con agua de rio sin pasteurizar y desde Brewery confirmamos que es totalmente cierto.",
            'alcohol': "6%",
            'ibu': "8",
            'tapa': "tapa-spar6.png",
            'botella': "botella-spar6.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Labbat's IPA - Labbat Limited",
            'cualidades': "AMBAR / AMARGA / LUPULADA / CITRICA",
            'descripcion': "De Inglaterra a India hay un largo recorrido. En 1780, Mr. Hodgson descubrió que elevando el lúpulo y la graduación alcohólica, la cerveza llegaba a destino intacta. Bautizó a su fórmula India Pale Ale. En Brewery, le sumamos lúpulos americanos con presencia de flores y cítricos. Nuestra cerveza viajera.",
            'alcohol': "6.6%",
            'ibu': "58",
            'tapa': "tapa-labbat-ipa.png",
            'botella': "botella-labbat-ipa.jpg",
            'tipo': "roja"
        },
        {
            'nombre': "Dow Cream Porter - Carling O'Keefe Breweries",
            'cualidades': "NEGRA / CON NITROGENO / CREMOSA",
            'descripcion': "Es una cerveza negra de origen irlandés. En ella se descubren sabores de chocolate y nueces en el paladar, con un licoroso y placentero post-gusto. Muy corpulenta, de espuma cremosa e increíblemente fácil de tomar debido a que posee menos gas carbónico que las cervezas tradicionales.",
            'alcohol': "4.9%",
            'ibu': "35",
            'tapa': "tapa-porter.png",
            'botella': "botella-porter.jpg",
            'tipo': "negra"
        },
        {
            'nombre': "Duffy's Stout - Columbia Brewing",
            'cualidades': "PETROLEO / CAFE / SECA",
            'descripcion': "Elaborada con maltas tostadas y matices de cafe y nuez, te deja la lengua seca como pechuga de pavo al horno, la cerveza es tan negra que vuelve el cristal de la botella totalmente opaco, su receta fue creada por una petrolera que utilizaba uno de sus destiladores de petroleo para destilar alcohol.",
            'alcohol': "12%",
            'ibu': "52",
            'tapa': "tapa-duffy-stout.png",
            'botella': "botella-duffy-stout.jpg",
            'tipo': "negra"
        },
        {
            'nombre': "Guinness Extra Stout - Labatt Breweries",
            'cualidades': "NEGRA / FUERTE / INTENSA / LICOROSA ",
            'descripcion': "Catalina la Grande amaba las emociones fuertes. Por eso, la Guinness Stout, negra y tostada, empapada de alcohol y pasas, amarga y ahumada, era su cerveza favorita. Esencia inglesa de exportación. Tímidos, abstenerse.",
            'alcohol': "8.5%",
            'ibu': "49",
            'tapa': "tapa-guiness.png",
            'botella': "botella-guiness.jpg",
            'tipo': "negra"
        },
        {
            'nombre': "Silver Spring Extra Stout - Labatt Brewery",
            'cualidades': "OPACA / SUAVE / CITRICA / MISTERIOSA",
            'descripcion': "Esta receta sigue la misma tradicion de Labatt con sus cervezas frutadas y aromaticas, pero con la diferencia de que esta cerveza es negra y tiene olor a bodega y a humedad, se deduce que es un lote de cervezas que Labatt se olvido de exportar y por alguna razon se puso negra, su misterio y escacez la hace tan deliciosa.",
            'alcohol': "10%",
            'ibu': "55",
            'tapa': "tapa-silver-spring.png",
            'botella': "botella-silver-spring.jpg",
            'tipo': "negra"
        },
        {
            'nombre': "Moosehead London Stout - Moosehead Breweries",
            'cualidades': "OPACA / SIMPLE / MALTOSA ",
            'descripcion': "Una edicion especial de cerveza Inglesa, en su simpleza se esconde su elegancia y minimalismo, basicamente es una cerveza elaborada con malta tostada y nada mas, se suelen detectar aromas con tonalidad a cafe y nuez, ligeros maticez de cascara de naranja y corteza de roble, pero no tiene nada mas que malta tostada y agua de la canilla en su elaboracion.",
            'alcohol': "5%",
            'ibu': "12",
            'tapa': "tapa-london-stout.png",
            'botella': "botella-london-stout.jpg",
            'tipo': "negra"
        },
        {
            'nombre': "Champlain Porter - O'Keefe Brewery",
            'cualidades': "NEGRA / PERFUMADA / POTENTE",
            'descripcion': "En la profunda tristeza que oculta tu sombra marchándose, el sonido seco de un portazo y ciegas palabras que confirman el adiós de tu mirada. Se hace pequeña y se va, tu sombra, tu figura... Esa sensación de vacío, de terror, cesa el efecto hasta del más fuerte alcohol para gritarte... Perdón.",
            'alcohol': "17%" ,
            'ibu': "58",
            'tapa': "tapa-champlain.png",
            'botella': "botella-champlain.jpg",
            'tipo': "negra"
        }
    ]
    context = {
        'cervezas': cervezas,
        'tipos': ['rubia', 'roja', 'negra']
        }
    return render(request, "core/cervezas.html", context)

def contacto(request):
    return render(request, "core/contacto.html")

#def contacto(request, nombre):
#    return HttpResponse(f"<h1>Hola {nombre}</h1>")


# Create your views here.
