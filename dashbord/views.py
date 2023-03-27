from django.shortcuts import render,redirect,HttpResponse
from .models import *
#from django.template import 
from django.contrib.auth import login,authenticate,logout,decorators
from django.shortcuts import render,redirect,HttpResponse

#from django.utils.timezone import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import Template,Context
from datetime import date 
from datetime import *

# Create your views here.
# def dashbord(request): 
#   return render(request, 'index.html'); 

def Login(request):
    if( request.method =='POST'):
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        print('user loged')
        if user is not None:
            login(request,user)
            return redirect("/dashboard")
        print("FAILED")
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('/login')

@decorators.login_required(login_url='/login')
def dashbord(request): 
  return render(request, 'index.html'); 
 

@decorators.login_required(login_url='/login')
def enregistrer_client(request):
	#return HttpResponse("hello")
	if request.method == "POST":
		
		client = Client(nom=request.POST['nom'], prenom=request.POST['prenom'], 
			tel=request.POST['tel'], adresse=request.POST['adresse'])
		client.save()
		messages.info(request,'Client enregistree')
		return render(request,'enregistrer_client.html',{'client':client})

	return render(request,'enregistrer_client.html')



# Ajout du  14-03-2023 11h12


@decorators.login_required(login_url='/login')
def dashboard(request):
	commande_recente = Commande.objects.all().order_by('-created')[:2]
	client_recent = Client.objects.all().order_by('-created')[:2]
	commande_nbr = Commande.objects.all().filter(created__year=date.today().year).count()
	client_nbr = Client.objects.all().filter(created__year=date.today().year).count()
	commandes = Commande.objects.all().filter(created__year=date.today().year)
	livraison_recente = Livraison.objects.all().order_by('-created')[:2]
	total = sum([ x.prix for  x in commandes if x.prix is not None ])



	# total_mois = {}
	# produits = Produit.objects.all()
	# arr = []
	# for p in produits:
	# 	s = sum([c.quantite for c in  p.commande_set.all().filter(created__year=date.today().year) ])
	# 	arr.append({'p':p,'s':s})





	for i in range(1,date.today().month+1):
		cmds = Commande.objects.all().filter(created__year=date.today().year).filter(created__month=i)
		# t = sum([x.produit.prix_unitaire * x.produit.nombre_lot * x.produit.quantite for x in cmds])
		c = Client.objects.all().filter(created__year=date.today().year).filter(created__month=i).count()
		cc = Commande.objects.all().filter(created__month=i).filter(created__year=date.today().year).count()
		# total_mois[i] = [i,cc,c,t]

	return render(request,'dashboard.html',{'commande_nbr':commande_nbr,
		'client_nbr':client_nbr,'commandes':commande_recente,
		'clients':client_recent,
		'livraisons':livraison_recente,
		'total':total,
		#
		# 'total_mois':total_mois,'arr':produits[:2]
		})


	
@decorators.login_required(login_url='/login')
def liste_client(request):
	clients = Client.objects.all()
	return render(request,'liste_client.html',{'clients':clients})
	pass


@decorators.login_required(login_url='/login')
def modifier_client(request,pk):
	client = Client.objects.get(pk=pk)
	if request.method == 'POST':
		client.nom = request.POST['nom']
		client.prenom = request.POST['prenom']
		client.tel = request.POST['tel']
		client.email = request.POST['email']
		client.adresse = request.POST['adresse']
		client.save()
		return render(request,'modifier_client.html',{'client':client,'save':True})
	return render(request,'modifier_client.html',{'client':client})
	pass


@decorators.login_required(login_url='/login')
def enregistrer_commande(request):
	clients = Client.objects.all()
	if request.method == "POST":
		#print(request.POST['livre'])
		client=Client.objects.get(id=request.POST['client'])
		commande = Commande(client_commande=client,
		    designation = request.POST['designation'],  
			nombreSachet=int(request.POST['nombreSachet']),
			date=request.POST['date'] ,
            poids =request.POST['poids'],
            prix =request.POST['prix'] )

		commande.save()
		messages.info(request,"Commande Enregistree avec succes")
		return render(request,'enregistrer_commande.html',{'commande':commande,'clients':clients})
	return render(request,'enregistrer_commande.html',{'clients':clients})
	pass


@decorators.login_required(login_url='/login')
def enregistrer_attribution(request):
	commandes = Commande.objects.all()
	livreurs = Livreur.objects.all()
	if request.method == "POST":
		#print(request.POST['livre'])
		commande=Commande.objects.get(id=request.POST['commande'])
		livreur=Livreur.objects.get(id=request.POST['livreur'])
		attribution = Attribution(designation = request.POST['designation'],
			commande=commande,
		    livreur =livreur,
			date=request.POST['date'] ,
            commentaire =request.POST['commentaire'],
        )

		attribution.save()
		messages.info(request,"Attribution Enregistree avec succes")
		return render(request,'enregistrer_attribution.html',{'attribution':attribution  ,'commandes':commandes,'livreurs':livreurs})
	return render(request,'enregistrer_attribution.html',{ 'commandes':commandes ,'livreurs':livreurs})
	pass




@decorators.login_required(login_url='/login')
def modifier_commande(request,pk):
	clients = Client.objects.all()
	commande = Commande.objects.get(pk=pk)
	if request.method == "POST":
		
		commande = Commande(client=Client.objects.get(id=request.POST['client']),
		    designation = request.POST['designation']  ,
			nombreSachet=int(request.POST['nombreSachet']),
			date_commande=request.POST['date_commande'] ,
            poids =request.POST['poids'],
            prix =request.POST['prix']
			)
		commande.designation = request.POST['designation']
		commande.date_commande = request.POST['date_commande']
		commande.prix = request.POST['prix']
		commande.nombreSachet = request.POST['nombreSachet']

		commande.save()
		messages.info(request,"Commande Modifiee avec succes")
		return render(request,'modifier_commande.html',{'save':True,'commande':commande,'clients':clients})


	return render(request,'modifier_commande.html',{'commande':commande,'clients':clients})
	pass


@decorators.login_required(login_url='/login')
def modifier_livraison(request,pk):
	# clients = Client.objects.all()
	# commande = Commande.objects.get(pk=pk)
	# if request.method == "POST":
		
	# 	commande = Commande(client=Client.objects.get(id=request.POST['client']),
	# 	    designation = request.POST['designation']  ,
	# 		nombreSachet=int(request.POST['nombreSachet']),
	# 		date_commande=request.POST['date_commande'] ,
    #         poids =request.POST['poids'],
    #         prix =request.POST['prix']
	# 		)
	# 	commande.designation = request.POST['designation']
	# 	commande.date_commande = request.POST['date_commande']
	# 	commande.prix = request.POST['prix']
	# 	commande.nombreSachet = request.POST['nombreSachet']

	# 	commande.save()
	# 	messages.info(request,"Commande Modifiee avec succes")
	# 	return render(request,'modifier_commande.html',{'save':True,'commande':commande,'clients':clients})


	# return render(request,'modifier_livraison.html',{'livraison':livraison,'livreurs':livreurs})
	return render(request,'modifier_livraison.html')
	pass

@decorators.login_required(login_url='/login')
def liste_commande(request):
	commandes = Commande.objects.all()
	return render(request,'liste_commande.html',{'commandes':commandes})
	pass



@decorators.login_required(login_url='/login')
def liste_attribution(request):
	attributions = Attribution.objects.all()
	return render(request,'liste_attribution.html',{'attributions':attributions})
	pass

# @decorators.login_required(login_url='/login')
# def liste_livraison(request):
# 	livraisons = Livraison.objects.all()
# 	return render(request,'liste_livraison.html',{'livraisons':livraisons})
	
@decorators.login_required(login_url='/login')
def gestion_livraison_automatique(request):
	#commande = Commande.objects.filter(actif=True)
	#distributeur = Distributeur.objects.filter()
	livraisons = Livraison.objects.all()
	return render(request,'gestion_livraison_automatique.html',{'livraisons':livraisons})

@decorators.login_required(login_url='/login')
def gestion_livraison_manuelle(request):
	return render(request,'gestion_livraison_manuelle.html')

@decorators.login_required(login_url='/login')
def liste_livraison(request):
	livraisons = Livraison.objects.all()
	return render(request,'liste_livraison.html',{'livraisons':livraisons})

@decorators.login_required(login_url='/login')
def enregistrer_livreur(request):
	if request.method == 'POST' or request.method == 'post':
		user1 = User.objects.create(username=request.POST['nom_utilisateur'],password=request.POST['password'])
		user1.save()
		livreur = Livreur.objects.create(nom=request.POST['nom'],prenom=request.POST['prenom'],tel=request.POST['tel'],user=user1 )
		livreur.save()
		return render(request,'enregistrer_livreur.html',{'livreur':livreur})
	return render(request,'enregistrer_livreur.html',{})

@decorators.login_required(login_url='/login')
def liste_livreur(request):
	livreurs = Livreur.objects.all()
	return render(request,'liste_livreur.html',{'livreurs':livreurs})


@decorators.login_required(login_url='/login')
def statistique(request):
	return render('statistique.html',{})
	pass

@decorators.login_required(login_url='/login')
def recapitulatif(request):
	try:
		datedebut = request.GET['datedebut']
		datefin = request.GET['datefin']
		f = open('./static/recapitulatif/recapitulatif_pdf.html')
		c = f.read()
		t = Template(c)
		datedebut = datetime.strptime(datedebut,'%Y-%m-%d')
		datefin = datetime.strptime(datefin,'%Y-%m-%d')
		arr = []
		produits = Produit.objects.all()
		for produit in produits:
			livraison_nbr = 0
			livraison_qte = 0
			commandes = produit.commande_set.all()
			for commande in commandes:
				for livraison in Livraison.objects.filter(date__gte=datedebut).filter(date__lte=datefin):
					if livraison.commande == commande:
						livraison_nbr  += 1
						livraison_qte += commande.quantite
			arr.append([produit,livraison_nbr,livraison_qte])
			livraison_nbr = 0
			livraison_qte = 0


		t = t.render(Context({'datedebut':datedebut,'datefin':datefin,'nom':'Boris','arr':arr}))
		HTML(string=t).write_pdf(f'recapitulatif_85.pdf')


		print('ok')
		f = open('recapitulatif_85.pdf','rb').read()
		#return f
		return HttpResponse(f, content_type='application/pdf')

	except Exception as e:
		print(e)
		print('SSSSSSSSSSSSSS')
		return render(request,'recapitulatif.html')
	pass


@decorators.login_required(login_url='/login')
def imprimer(request):
	pass    

# pour imprimer la liste des clients 27-03-2023

# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from .models import Client

# @decorators.login_required(login_url='/login')
# def client_list_pdf(request):
#     clients = Client.objects.all()
#     context = {
#         'clients': clients,
#     }
#     template_path = 'client_list_pdf.html'
#     # Créez un objet Template à partir du fichier template HTML
#     template = get_template(template_path)
#     # Rendre le contenu du template HTML avec le contexte des données
#     html = template.render(context)
#     # Créer un document PDF vide et un flux de sortie
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="client_list.pdf"'
#     # Convertir le template HTML en PDF
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # S'il y a une erreur, affichez-la en tant que texte brut dans le document PDF
#     if pisa_status.err:
#         return HttpResponse('Une erreur est survenue lors de la création du document PDF: %s' % escape(html))
#     return response


from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas
from .models import Client

def client_list_pdf(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    template = get_template('client_list.html')
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="client_list.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Liste des clients")
    p.drawString(100, 750, "Nom")
    p.drawString(300, 750, "Email")
    p.drawString(500, 750, "Téléphone")
    y = 700
    for client in clients:
        p.drawString(100, y, client.nom)
        p.drawString(300, y, client.email)
        p.drawString(500, y, client.tel)
        y -= 20
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
